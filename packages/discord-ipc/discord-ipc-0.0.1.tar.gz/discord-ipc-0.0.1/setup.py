from setuptools import setup

with open("README.md", "r") as ld:
    long_description = ld.read()

setup(
    name="discord-ipc",
    author="ben-forster",
    url="https://github.com/ben-forster/discord-ipc",
    version="0.0.1",
    packages=["discord.ext.ipc"],
    license="MIT",
    description="An IPC extension allowing for the communication between a discord.py bot and an asynchronous web-framework.",
    install_requires=["discord.py>=1.4.1"],
    python_requires=">=3.6"
)