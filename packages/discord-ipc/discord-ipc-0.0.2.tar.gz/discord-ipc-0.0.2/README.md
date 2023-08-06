# What is Discord IPC?
Discord IPC is a discord.py extension which allows the communication between a discord.py bot and an asynchronous web-framework. You can use the IPC extension to make a route, set some data, and have it update your command from your website - in turn updating the data of the command.

For example, updating your bot's prefix from the website.

# What is Discord IPC compatible with?
Discord IPC is currently compatible with either [Quart](https://github.com/pallets/quart) or [aiohttp.web](https://github.com/aio-libs/aiohttp)

# Installation
As with other extensions, instillation is through [git](https://git-scm.com/)
```py
python -m pip install -U git+https://github.com/ben-forster/discord-ipc
```

# Quick Example
```py
import discord
from discord.ext import commands, ipc


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self, secret_key="my_secret_key")  # create our IPC Server

    async def on_ready(self):
        """Called upon the READY event"""
        print("Bot is ready.")

    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("Ipc is ready.")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        print(endpoint, "raised", error)


intents = discord.Intents.default()
intents.message_content = True

client = Bot(command_prefix="!", intents=discord.Intents.default())

@client.ipc.route()
async def get_member_count(data):
    guild = client.get_guild(data.guild_id)  # get the guild object using parsed guild_id

    return guild.member_count  # return the member count to the client


if __name__ == "__main__":
    client.ipc.start()  # start the IPC Server
    client.run("TOKEN")
 ```   
You can find more examples in the [examples](https://github.com/ben-forster/discord-ipc/tree/main/examples) directory.

# Links
- [Documentation](https://discord-ipc.readthedocs.io/en/latest/)
- [Discord Server](https://discord.gg/Zcjg8AW4ga)
- [Discord API](https://discord.com/developers/docs/getting-started)
