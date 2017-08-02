from conan.packager import ConanMultiPackager
import platform
import os

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="zlib:shared", pure_c=True)
    builder.password = os.getenv("CONAN_PASSWORD")
    filtered_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            if settings["build_type"] == "Release" \
                and settings["arch"] == "x86_64" \
                and not options["zlib:shared"]:
                filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds
    builder.run()
