from __future__ import annotations

import json
from typing import Union, Protocol, cast, runtime_checkable
from dataclasses import dataclass
from collections.abc import Mapping, Iterable, AsyncIterable
from typing_extensions import TypeAlias

from ._ws import (
    ClientConfig,
    SyncWebSocketConnector,
    AsyncWebSocketConnector,
    sync_connect,
    async_connect,
    connection_settings,
)

__all__ = ["ExecProtocolError", "ExecResult", "exec", "exec_async"]


@runtime_checkable
class _BinaryReader(Protocol):
    def read(self, size: int = -1) -> bytes: ...


Stdin: TypeAlias = Union[bytes, bytearray, memoryview, _BinaryReader, Iterable[bytes]]
AsyncStdin: TypeAlias = Union[Stdin, AsyncIterable[bytes]]


class ExecProtocolError(RuntimeError):
    """The exec WebSocket closed or sent an invalid control frame."""


@dataclass(frozen=True)
class ExecResult:
    """Result of an exec session.

    The server protocol combines stdout and stderr into ``output``; it doesn't carry
    channel metadata that would allow the SDK to split them.
    """

    output: bytes
    exit_code: int


@dataclass(frozen=True)
class _ExecRequest:
    command: list[str]
    tty: bool
    env: Mapping[str, str] | None
    cwd: str | None
    timeout: int | None
    wait_for_agent: int | None
    rows: int | None
    cols: int | None

    def encode(self) -> str:
        payload: dict[str, object] = {"command": self.command, "tty": self.tty}
        for key, value in (
            ("env", dict(self.env) if self.env is not None else None),
            ("cwd", self.cwd),
            ("timeout", self.timeout),
            ("wait_for_agent", self.wait_for_agent),
            ("rows", self.rows),
            ("cols", self.cols),
        ):
            if value is not None:
                payload[key] = value
        return json.dumps(payload, separators=(",", ":"))


def _request(
    command: Iterable[str],
    *,
    cwd: str | None,
    env: Mapping[str, str] | None,
    timeout: int | None,
    wait_for_agent: int | None,
    tty: bool,
    rows: int | None,
    cols: int | None,
) -> _ExecRequest:
    if isinstance(command, str):
        raise ValueError("command must be an argument sequence, not a string")
    argv = list(command)
    if not argv:
        raise ValueError("command must contain at least one string argument")
    for name, value in (("timeout", timeout), ("wait_for_agent", wait_for_agent)):
        if value is not None and (isinstance(value, bool) or value < 0):
            raise ValueError(f"{name} must be a non-negative number of seconds")
    for name, value in (("rows", rows), ("cols", cols)):
        if value is not None and (isinstance(value, bool) or value <= 0):
            raise ValueError(f"{name} must be positive")
    if (rows is not None or cols is not None) and not tty:
        raise ValueError("rows and cols require tty=True")
    return _ExecRequest(argv, tty, env, cwd, timeout, wait_for_agent, rows, cols)


def _stdin_chunks(stdin: Stdin | None) -> Iterable[bytes]:
    if stdin is None:
        return ()
    if isinstance(stdin, (bytes, bytearray, memoryview)):
        data = bytes(stdin)
        return (data,) if data else ()
    if isinstance(stdin, _BinaryReader):

        def read_chunks() -> Iterable[bytes]:
            while chunk := stdin.read(32 * 1024):
                yield chunk

        return read_chunks()
    return stdin


def _exit_code(frame: str) -> int:
    try:
        payload = cast(object, json.loads(frame))
    except json.JSONDecodeError as exc:
        raise ExecProtocolError("exec sent malformed JSON control frame") from exc
    if not isinstance(payload, dict):
        raise ExecProtocolError("exec sent an unexpected control frame")
    control = cast(dict[str, object], payload)
    if set(control) != {"exitCode"}:
        raise ExecProtocolError("exec sent an unexpected control frame")
    exit_code = control["exitCode"]
    if isinstance(exit_code, bool) or not isinstance(exit_code, int):
        raise ExecProtocolError("exec exitCode must be an integer")
    return exit_code


def exec(
    client: ClientConfig,
    instance_id: str,
    command: Iterable[str],
    *,
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
    timeout: int | None = None,
    wait_for_agent: int | None = None,
    tty: bool = False,
    rows: int | None = None,
    cols: int | None = None,
    stdin: Stdin | None = None,
    resize: Iterable[tuple[int, int]] = (),
    connector: SyncWebSocketConnector = sync_connect,
) -> ExecResult:
    """Execute a command and collect its merged stdout/stderr bytes.

    The request is dispatched once and is never retried. ``stdin`` is sent as binary
    WebSocket frames. The protocol has no stdin EOF frame, so commands must stop
    reading based on their input, another condition, or ``timeout``. TTY resize
    tuples are ``(rows, cols)``.
    """

    request = _request(
        command,
        cwd=cwd,
        env=env,
        timeout=timeout,
        wait_for_agent=wait_for_agent,
        tty=tty,
        rows=rows,
        cols=cols,
    )
    url, headers = connection_settings(client, instance_id, "exec")
    output = bytearray()
    with connector(url, additional_headers=headers, max_size=None) as websocket:
        websocket.send(request.encode())
        for chunk in _stdin_chunks(stdin):
            if chunk:
                websocket.send(chunk)
        for resize_rows, resize_cols in resize:
            if not tty or resize_rows <= 0 or resize_cols <= 0:
                raise ValueError("resize dimensions must be positive and require tty=True")
            websocket.send(json.dumps({"resize": {"rows": resize_rows, "cols": resize_cols}}, separators=(",", ":")))

        while True:
            try:
                frame = websocket.recv()
            except Exception as exc:
                raise ExecProtocolError("exec stream ended before an exitCode control frame") from exc
            if isinstance(frame, bytes):
                output.extend(frame)
                continue
            return ExecResult(output=bytes(output), exit_code=_exit_code(frame))


async def exec_async(
    client: ClientConfig,
    instance_id: str,
    command: Iterable[str],
    *,
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
    timeout: int | None = None,
    wait_for_agent: int | None = None,
    tty: bool = False,
    rows: int | None = None,
    cols: int | None = None,
    stdin: AsyncStdin | None = None,
    resize: Iterable[tuple[int, int]] = (),
    connector: AsyncWebSocketConnector = async_connect,
) -> ExecResult:
    """Asynchronous counterpart to :func:`exec`; requests are never retried."""

    request = _request(
        command,
        cwd=cwd,
        env=env,
        timeout=timeout,
        wait_for_agent=wait_for_agent,
        tty=tty,
        rows=rows,
        cols=cols,
    )
    url, headers = connection_settings(client, instance_id, "exec")
    output = bytearray()
    async with connector(url, additional_headers=headers, max_size=None) as websocket:
        await websocket.send(request.encode())
        if isinstance(stdin, AsyncIterable):
            async for chunk in stdin:
                if chunk:
                    await websocket.send(chunk)
        else:
            for chunk in _stdin_chunks(stdin):
                if chunk:
                    await websocket.send(chunk)
        for resize_rows, resize_cols in resize:
            if not tty or resize_rows <= 0 or resize_cols <= 0:
                raise ValueError("resize dimensions must be positive and require tty=True")
            await websocket.send(
                json.dumps({"resize": {"rows": resize_rows, "cols": resize_cols}}, separators=(",", ":"))
            )

        while True:
            try:
                frame = await websocket.recv()
            except Exception as exc:
                raise ExecProtocolError("exec stream ended before an exitCode control frame") from exc
            if isinstance(frame, bytes):
                output.extend(frame)
                continue
            return ExecResult(output=bytes(output), exit_code=_exit_code(frame))
