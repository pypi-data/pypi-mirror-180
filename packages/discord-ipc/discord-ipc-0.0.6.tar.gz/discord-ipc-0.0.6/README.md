# Discord IPC

<a href="https://pypi.org/project/discord-ipc/" target="_blank"><img src="https://img.shields.io/pypi/v/better-ipc"></a>
<img src="https://img.shields.io/pypi/pyversions/discord-ipc">
<img src="https://img.shields.io/github/last-commit/benforster/discord-ipc">
<img src="https://img.shields.io/github/license/benforster/ord-ipc">
<a href="https://discord.gg/Zcjg8AW4ga" target="_blank"><img src="https://img.shields.io/discord/875005644594372638?label=discord"></a>

## An IPC extension allowing for the communication between a discord.py bot and an asynchronous web-framework.

#### This project is a fork of the now unmaintained [discord-ext-ipct](https://github.com/Ext-Creators/discord-ext-ipc) project.

# What is Discord IPC?
Discord IPC is a discord.py extension which allows the communication between a discord.py bot and an asynchronous web-framework. You can use the IPC extension to make a route, set some data, and have it update your command from your website - in turn updating the data of the command.

For example, updating your bot's prefix from the website.

# What is Discord IPC compatible with?
Discord IPC is currently compatible with either [Quart](https://github.com/pallets/quart) or [aiohttp.web](https://github.com/aio-libs/aiohttp)

# Installation
As with other extensions, instillation is through [pip](https://pypi.org/project/pip/)

Python >=3.5.3 is required.

### Linux/macOS
```shell
python3 -m pip install -U discord-ipc
```
### Windows
```shell
py -m pip install -U discord-ipc
```

# Examples

### Client example
```py
import discord
from discord.ext import commands, ipc


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self, secret_key="my_secret_key")  # create our IPC Server

    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("IPC is ready.")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        print(endpoint, "raised", error)

    async def setup_hook(self) -> None:
        await self.ipc.start()
        print("Bot is online.")
        
 
my_bot = MyBot(command_prefix="!", intents=discord.Intents.all())


@my_bot.ipc.route()
async def get_member_count(data):
    guild = my_bot.get_guild(data.guild_id)  # get the guild object using parsed guild_id

    return guild.member_count  # return the member count to the client

await my_bot.ipc.start()
await my_bot.start('token')

 ```   
You can find more examples in the [examples](https://github.com/ben-forster/discord-ipc/tree/main/examples) directory.

# Support

- [Documentation](https://discord-ipc.readthedocs.io/en/latest/)

- [Discord Server](https://discord.gg/Zcjg8AW4ga)

- [Discord API](https://discord.com/developers/docs/getting-started)
