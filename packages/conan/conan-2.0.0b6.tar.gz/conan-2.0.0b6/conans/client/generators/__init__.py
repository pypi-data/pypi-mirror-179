import os
import traceback

from conans.client.subsystems import deduce_subsystem, subsystem_path
from conans.errors import ConanException, conanfile_exception_formatter
from conans.util.files import save, mkdir, chdir

_generators = ["CMakeToolchain", "CMakeDeps", "MSBuildToolchain",
               "MesonToolchain", "MesonDeps", "MSBuildDeps", "QbsToolchain",
               "VirtualRunEnv", "VirtualBuildEnv", "AutotoolsDeps",
               "AutotoolsToolchain", "BazelDeps", "BazelToolchain", "PkgConfigDeps",
               "VCVars", "IntelCC", "XcodeDeps", "PremakeDeps", "XcodeToolchain",
               "NMakeToolchain", "NMakeDeps"]


def _get_generator_class(generator_name):
    if generator_name not in _generators:
        raise ConanException("Invalid generator '%s'. Available types: %s" %
                             (generator_name, ", ".join(_generators)))
    if generator_name == "CMakeToolchain":
        from conan.tools.cmake import CMakeToolchain
        return CMakeToolchain
    elif generator_name == "CMakeDeps":
        from conan.tools.cmake import CMakeDeps
        return CMakeDeps
    elif generator_name == "AutotoolsDeps":
        from conan.tools.gnu import AutotoolsDeps
        return AutotoolsDeps
    elif generator_name == "AutotoolsToolchain":
        from conan.tools.gnu import AutotoolsToolchain
        return AutotoolsToolchain
    elif generator_name == "PkgConfigDeps":
        from conan.tools.gnu import PkgConfigDeps
        return PkgConfigDeps
    elif generator_name == "MSBuildToolchain":
        from conan.tools.microsoft import MSBuildToolchain
        return MSBuildToolchain
    elif generator_name == "MesonToolchain":
        from conan.tools.meson import MesonToolchain
        return MesonToolchain
    elif generator_name == "MesonDeps":
        from conan.tools.meson import MesonDeps
        return MesonDeps
    elif generator_name == "MSBuildDeps":
        from conan.tools.microsoft import MSBuildDeps
        return MSBuildDeps
    elif generator_name == "VCVars":
        from conan.tools.microsoft import VCVars
        return VCVars
    elif generator_name == "IntelCC":
        from conan.tools.intel import IntelCC
        return IntelCC
    elif generator_name == "QbsToolchain" or generator_name == "QbsProfile":
        from conan.tools.qbs.qbsprofile import QbsProfile
        return QbsProfile
    elif generator_name == "VirtualBuildEnv":
        from conan.tools.env.virtualbuildenv import VirtualBuildEnv
        return VirtualBuildEnv
    elif generator_name == "VirtualRunEnv":
        from conan.tools.env.virtualrunenv import VirtualRunEnv
        return VirtualRunEnv
    elif generator_name == "BazelDeps":
        from conan.tools.google import BazelDeps
        return BazelDeps
    elif generator_name == "BazelToolchain":
        from conan.tools.google import BazelToolchain
        return BazelToolchain
    elif generator_name == "XcodeDeps":
        from conan.tools.apple import XcodeDeps
        return XcodeDeps
    elif generator_name == "PremakeDeps":
        from conan.tools.premake import PremakeDeps
        return PremakeDeps
    elif generator_name == "XcodeToolchain":
        from conan.tools.apple import XcodeToolchain
        return XcodeToolchain
    elif generator_name == "NMakeToolchain":
        from conan.tools.microsoft import NMakeToolchain
        return NMakeToolchain
    elif generator_name == "NMakeDeps":
        from conan.tools.microsoft import NMakeDeps
        return NMakeDeps
    else:
        raise ConanException("Internal Conan error: Generator '{}' "
                             "not complete".format(generator_name))


def write_generators(conanfile, hook_manager):
    new_gen_folder = conanfile.generators_folder
    _receive_conf(conanfile)

    hook_manager.execute("pre_generate", conanfile=conanfile)

    if conanfile.generators:
        conanfile.output.info(f"Writing generators to {new_gen_folder}")
    for generator_name in set(conanfile.generators):
        generator_class = _get_generator_class(generator_name)
        if generator_class:
            try:
                generator = generator_class(conanfile)
                conanfile.output.highlight(f"Generator '{generator_name}' calling 'generate()'")
                mkdir(new_gen_folder)
                with chdir(new_gen_folder):
                    generator.generate()
                continue
            except Exception as e:
                # When a generator fails, it is very useful to have the whole stacktrace
                conanfile.output.error(traceback.format_exc())
                raise ConanException("Error in generator '{}': {}".format(generator_name, str(e)))

    if hasattr(conanfile, "generate"):
        conanfile.output.highlight("Calling generate()")
        mkdir(new_gen_folder)
        with chdir(new_gen_folder):
            with conanfile_exception_formatter(conanfile, "generate"):
                conanfile.generate()

    if conanfile.virtualbuildenv:
        mkdir(new_gen_folder)
        with chdir(new_gen_folder):
            from conan.tools.env.virtualbuildenv import VirtualBuildEnv
            env = VirtualBuildEnv(conanfile)
            env.generate()
    if conanfile.virtualrunenv:
        mkdir(new_gen_folder)
        with chdir(new_gen_folder):
            from conan.tools.env import VirtualRunEnv
            env = VirtualRunEnv(conanfile)
            env.generate()

    conanfile.output.highlight("Aggregating env generators")
    _generate_aggregated_env(conanfile)

    hook_manager.execute("post_generate", conanfile=conanfile)


def _receive_conf(conanfile):
    """  collect conf_info from the immediate build_requires, aggregate it and injects/update
    current conf
    """
    # TODO: Open question 1: Only build_requires can define config?
    # TODO: Only direct build_requires?
    # TODO: Is really the best mechanism to define this info? Better than env-vars?
    # Conf only for first level build_requires
    for build_require in conanfile.dependencies.direct_build.values():
        if build_require.conf_info:
            conanfile.conf.compose_conf(build_require.conf_info)


def _generate_aggregated_env(conanfile):

    def deactivates(filenames):
        # FIXME: Probably the order needs to be reversed
        result = []
        for s in filenames:
            folder, f = os.path.split(s)
            result.append(os.path.join(folder, "deactivate_{}".format(f)))
        return result

    for group, env_scripts in conanfile.env_scripts.items():
        subsystem = deduce_subsystem(conanfile, group)
        bats = []
        shs = []
        ps1s = []
        for env_script in env_scripts:
            path = os.path.join(conanfile.generators_folder, env_script)
            if env_script.endswith(".bat"):
                bats.append(path)
            elif env_script.endswith(".sh"):
                shs.append(subsystem_path(subsystem, path))
            elif env_script.endswith(".ps1"):
                ps1s.append(path)
        if shs:
            def sh_content(files):
                return ". " + " && . ".join('"{}"'.format(s) for s in files)
            filename = "conan{}.sh".format(group)
            save(os.path.join(conanfile.generators_folder, filename), sh_content(shs))
            save(os.path.join(conanfile.generators_folder, "deactivate_{}".format(filename)),
                 sh_content(deactivates(shs)))
        if bats:
            def bat_content(files):
                return "\r\n".join(["@echo off"] + ['call "{}"'.format(b) for b in files])
            filename = "conan{}.bat".format(group)
            save(os.path.join(conanfile.generators_folder, filename), bat_content(bats))
            save(os.path.join(conanfile.generators_folder, "deactivate_{}".format(filename)),
                 bat_content(deactivates(bats)))
        if ps1s:
            def ps1_content(files):
                return "\r\n".join(['& "{}"'.format(b) for b in files])
            filename = "conan{}.ps1".format(group)
            save(os.path.join(conanfile.generators_folder, filename), ps1_content(ps1s))
            save(os.path.join(conanfile.generators_folder, "deactivate_{}".format(filename)),
                 ps1_content(deactivates(ps1s)))
