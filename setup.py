from setuptools import find_packages, setup

setup(
    name="say-hello",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "say-hello = helloworld.main:say_hello",
        ],
    },
    include_package_data=True,
    version="1.0",
    install_requires=["ansicolors"],
)
