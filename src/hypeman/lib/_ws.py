from __future__ import annotations

from types import TracebackType
from typing import TypeVar, Protocol, cast
from urllib.parse import urlsplit, urlunsplit

from websockets.sync.client import connect as websocket_connect
from websockets.asyncio.client import connect as async_websocket_connect

__all__ = [
    "AsyncWebSocket",
    "AsyncWebSocketConnector",
    "ClientConfig",
    "SyncWebSocket",
    "SyncWebSocketConnector",
]


MAX_INBOUND_MESSAGE_SIZE = 2**20


class ClientConfig(Protocol):
    """The generated client settings used by the custom WebSocket APIs."""

    api_key: str

    @property
    def base_url(self) -> object: ...


class SyncWebSocket(Protocol):
    def send(self, message: bytes | str) -> None: ...

    def recv(self) -> bytes | str: ...

    def close(self) -> None: ...

    def __enter__(self: _SyncWebSocketT) -> _SyncWebSocketT: ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None: ...


_SyncWebSocketT = TypeVar("_SyncWebSocketT", bound=SyncWebSocket)


class SyncWebSocketConnector(Protocol):
    def __call__(self, url: str, *, additional_headers: dict[str, str], max_size: int) -> SyncWebSocket: ...


class AsyncWebSocket(Protocol):
    async def send(self, message: bytes | str) -> None: ...

    async def recv(self) -> bytes | str: ...

    async def close(self) -> None: ...

    async def __aenter__(self: _AsyncWebSocketT) -> _AsyncWebSocketT: ...

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None: ...


_AsyncWebSocketT = TypeVar("_AsyncWebSocketT", bound=AsyncWebSocket)


class AsyncWebSocketContext(Protocol):
    async def __aenter__(self) -> AsyncWebSocket: ...

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None: ...


class AsyncWebSocketConnector(Protocol):
    def __call__(self, url: str, *, additional_headers: dict[str, str], max_size: int) -> AsyncWebSocketContext: ...


def sync_connect(
    url: str,
    *,
    additional_headers: dict[str, str],
    max_size: int = MAX_INBOUND_MESSAGE_SIZE,
) -> SyncWebSocket:
    return cast(SyncWebSocket, websocket_connect(url, additional_headers=additional_headers, max_size=max_size))


def async_connect(
    url: str,
    *,
    additional_headers: dict[str, str],
    max_size: int = MAX_INBOUND_MESSAGE_SIZE,
) -> AsyncWebSocketContext:
    return cast(
        AsyncWebSocketContext,
        async_websocket_connect(url, additional_headers=additional_headers, max_size=max_size),
    )


def connection_settings(
    client: ClientConfig,
    instance_id: str,
    endpoint: str,
) -> tuple[str, dict[str, str]]:
    if not instance_id or "/" in instance_id or "\\" in instance_id or ".." in instance_id:
        raise ValueError("instance_id must not be empty or contain path traversal sequences")

    parsed = urlsplit(str(client.base_url))
    if parsed.scheme == "https":
        scheme = "wss"
    elif parsed.scheme == "http":
        scheme = "ws"
    else:
        raise ValueError("client.base_url must use http or https")
    if not parsed.netloc:
        raise ValueError("client.base_url must include a host")

    prefix = parsed.path.rstrip("/")
    path = f"{prefix}/instances/{instance_id}/{endpoint}"
    url = urlunsplit((scheme, parsed.netloc, path, parsed.query, ""))
    return url, {"Authorization": f"Bearer {client.api_key}"}
