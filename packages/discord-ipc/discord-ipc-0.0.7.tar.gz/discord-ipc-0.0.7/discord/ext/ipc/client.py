import asyncio
import logging

from websockets.client import WebSocketClientProtocol
from typing import Optional, Callable, Any, Coroutine
from .errors import ConnectionError, AsyncError
from .objects import ResponseObject
from inspect import iscoroutine
from websockets import connection
from discord import Client

try:
    from orjson import dumps, loads
except ImportError:
    from json import dumps, loads


logging = logging.getLogger(__name__)


class Client:
    
    def __init__(self, client: Client,
                secret_key: str, *,
                loop: Optional[asyncio.AbstractEventLoop] = None,
                log: Optional[bool] = False):
        self.client = client
        client.ipc = self
        self.secret_key = secret_key
        self.loop = loop
        self.log: bool = log
        self.ws: WebSocketClientProtocol = None
        self.events: list = []
        self.uri: str = None

    def print(self, content: str) -> None:
        if self.log:
            print("[ipc.Client]: {}".format(content))

    async def __aenter__(self) -> Client:
        if self.loop is None:
            self.loop = asyncio.get_running_loop()
        return self

    async def __aexit__(self, *args) -> None:
        try:
            await self.close()
        except Exception:
            pass

    async def connect(self, uri: str, *, reconnect: Optional[bool] = True) -> None:
        self.uri = uri
        if self.ws is not None:
            raise ConnectionError("Discord IPC: Server already connected or in-use..")
        self.ws = await self.connect(uri)
        logging.debug("Discord IPC: Connect to server.")
        self.print("Discord IPC: Successfully connected.")
        self.client.dispatch("ipc_connect")
        await self.login()
        while self.ws.open:
            await self.recv()
        if reconnect:
            await self.connect(uri, reconnect=reconnect)

    async def close(self, code: Optional[int] = 1000, message: Optional[str] = "Bye") -> None:
        if self.ws is not None:
            if not self.ws.closed:
                await self.ws.close(code=code, message=dumps({"type": "close", "message": message}))
                await self.ws.wait_closed()
                self.print("close")
                self.client.dispatch("ipc_close")
            self.ws = None
        else:
            raise ConnectionError("Already closed")

    async def reconnect(self) -> None:
        await self.close()
        await asyncio.sleep(0.5)
        await self.connect(self.uri)

    def login(self):
        return self.request("login", {"token": self.secret_key})

    async def request(self, eventtype: str, data: Optional[dict] = {}) -> None:
        payload = {
            "type": eventtype,
            "data": data
        }
        await self.ws.send(dumps(payload))

    def listen(self, eventtype: str):
        def decorator(func: Callable[[Any, Any], Coroutine[Any]]):
            if not iscoroutine(func):
                raise AsyncError("Function is not corotinue.")
            if eventtype in self.events:
                self.events[eventtype].append(func)
            else:
                self.events[eventtype] = [func]
            return func
        return decorator

    def dispatch(self, eventtype: str, response: ResponseObject) -> None:
        if eventtype in self.events:
            for coro in self.events[eventtype]:
                self.loop.create_task(coro())
        self.client.dispatch("ipc_{}".format(eventtype))

    async def recv(self) -> None:
        data = loads(await self.ws.recv())
        logging.debug("[Catch event]type: {}, data: {}".format(data["type"], data["data"]))

        if data["type"] == "close":
            self.client.dispatch("ipc_close")

        self.dispatch(data["type"], data["data"])