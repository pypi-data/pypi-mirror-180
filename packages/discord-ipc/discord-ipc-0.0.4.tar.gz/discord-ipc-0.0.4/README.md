# Discord IPC

<a href="https://pypi.org/project/discord-ipc/" target="_blank"><img src="https://img.shields.io/pypi/v/better-ipc"></a>
<img src="https://img.shields.io/pypi/pyversions/discord-ipc">
<img src="https://img.shields.io/github/last-commit/benforster/discord-ipc">
<img src="https://img.shields.io/github/license/MiroslavRosenov/discord-ipc">
<a href="https://discord.gg/Zcjg8AW4ga" target="_blank"><img src="https://img.shields.io/discord/875005644594372638?label=discord"></a>

## An IPC extension allowing for the communication between a discord.py bot and an asynchronous web-framework.

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
from discord.ext.ipc.server import Server
from discord.ext.ipc.objects import ClientPayload

class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.all()

        super().__init__(
            command_prefix="$",
            intents=intents,
        )

        self.ipc = ipc.Server(self, secret_key="my_secret_key")  # create our IPC Server

    async def setup_hook(self) -> None:
        await self.ipc.start()

    @Server.route()
    async def get_user_data(self, data: ClientPayload) -> Dict:
        user = self.get_user(data.user_id)
        return user._to_mimimal_user_json()

await self.start('token')

 ```   
You can find more examples in the [examples](https://github.com/ben-forster/discord-ipc/tree/main/examples) directory.

# Support

- [Documentation](https://discord-ipc.readthedocs.io/en/latest/)

- [Discord Server](https://discord.gg/Zcjg8AW4ga)

- [Discord API](https://discord.com/developers/docs/getting-started)
