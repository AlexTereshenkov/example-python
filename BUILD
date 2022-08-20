# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(name="reqs")

python_sources(
    name="setup-py",
    sources=["setup.py"],
)

# to copy helloworld/greet/translations.json
resource(
    name="MANIFEST",
    source="MANIFEST.in",
)

python_distribution(
    name="say-hello",
    dependencies=[
        ":setup-py",
        ":MANIFEST",
        "helloworld:pex_binary"
# because we depend on helloworld:pex_binary,
# there is no need to provide all dependencies manually, e.g.
#        "helloworld:lib",
#        "helloworld/greet:lib",
#        "helloworld/greet:translations",
#        "helloworld/translator:lib",
        ],
    provides=python_artifact(
        name="say-hello",
    ),
    generate_setup=False,
    sdist=False,
)
