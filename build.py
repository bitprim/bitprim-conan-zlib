from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86_64"])
    builder.add_common_builds(shared_option_name="zlib:shared")

    filtered_builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        if (settings["build_type"] == "Release" or settings["build_type"] == "Debug") \
               and not("zlib:shared" in options and options["zlib:shared"]):
            filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds
    builder.run()
