import discord
import collections

from discord.ext.ipc.client import Client
from discord.ext.ipc.server import Server
from discord.ext.ipc.errors import *

from discord .client import Client
from .server import Websocket, listen

if discord.version_info.major < 2:
    raise RuntimeError("You must have discord.py (v2.0 or greater) to use this library.")

_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "0.0.7"
version_info = _VersionInfo(0, 0, 7, "final", 0)

__all__ = (
    "Client",
    "Websocket",
    "Listen"
)
