import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def _get_version(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    version = None
    for line in lines:
        if "__version__" in line:
            version = line.split()[2]
            break
    return version.replace('"', '')

install_requires = [
    "websockets"
]

extras_require = {
    "speed": [
        "orjson"
    ]
}

packages = [
    "discord.ext.ipc"
]

setuptools.setup(
    name="discord-ipc",
    version=_get_version("discord/ext/ipc/__init__.py"),
    author="benforster",
    author_email="benfo1942@gmail.com",
    description="Discord IPC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benforster/discord-ext-ipc",
    install_requires=install_requires,
    extras_require=extras_require,
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
