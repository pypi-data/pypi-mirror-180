import discord

if discord.version_info.major < 2:
    raise RuntimeError("You must have discord.py (v2.0 or greater) to use this library.")

__title__ = "discord-ipc"
__author__ = "benforster"
__license__ = "MIT License"
__copyright__ = "Copyright 2022, Ben Forster"
__version__ = "0.0.5"


from .errors import BaseException, NoEndpointFoundError, MulticastFailure, InvalidReturn, ServerAlreadyStarted
from .client import Client
from .server import Server
from .objects import ClientPayload, ServerResponse
