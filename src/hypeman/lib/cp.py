from __future__ import annotations

import os
import json
import stat
import asyncio
import tempfile
from uuid import uuid4
from typing import BinaryIO, cast
from pathlib import Path, PurePosixPath
from dataclasses import dataclass
from collections.abc import Callable

from ._ws import (
    ClientConfig,
    SyncWebSocket,
    AsyncWebSocket,
    SyncWebSocketConnector,
    AsyncWebSocketConnector,
    sync_connect,
    async_connect,
    connection_settings,
)

__all__ = [
    "CopyCallbacks",
    "CopyProtocolError",
    "cp_from_instance",
    "cp_from_instance_async",
    "cp_to_instance",
    "cp_to_instance_async",
]

_CHUNK_SIZE = 32 * 1024


class CopyProtocolError(RuntimeError):
    """The cp WebSocket sent an invalid or incomplete transfer."""


@dataclass(frozen=True)
class CopyCallbacks:
    """Optional per-file transfer callbacks.

    ``on_progress`` receives the bytes copied for the current file, not the
    aggregate across a directory.
    """

    on_file_start: Callable[[str, int], None] | None = None
    on_progress: Callable[[int], None] | None = None
    on_file_end: Callable[[str], None] | None = None


@dataclass(frozen=True)
class _UploadEntry:
    source: Path
    guest_path: str
    is_dir: bool
    mode: int
    uid: int
    gid: int
    size: int


def _upload_entries(
    source: Path,
    guest_path: str,
    *,
    mode: int | None,
    archive: bool,
    follow_symlinks: bool,
) -> list[_UploadEntry]:
    if mode is not None and (isinstance(mode, bool) or mode < 0 or mode > 0o7777):
        raise ValueError("mode must be between 0 and 0o7777")

    entries: list[_UploadEntry] = []
    visited: set[tuple[int, int]] = set()

    def visit(local_path: Path, remote_path: str, root: bool = False) -> None:
        try:
            link_info = local_path.lstat()
        except OSError as exc:
            raise OSError(f"cannot stat upload source {local_path}") from exc

        is_link = stat.S_ISLNK(link_info.st_mode)
        try:
            info = local_path.stat() if is_link else link_info
        except OSError as exc:
            raise OSError(f"cannot follow upload symlink {local_path}") from exc

        is_dir = stat.S_ISDIR(info.st_mode)
        entry_mode = mode if root and mode is not None else stat.S_IMODE(info.st_mode)
        uid = int(getattr(info, "st_uid", 0)) if archive else 0
        gid = int(getattr(info, "st_gid", 0)) if archive else 0
        entries.append(
            _UploadEntry(
                source=local_path,
                guest_path=remote_path,
                is_dir=is_dir,
                mode=entry_mode,
                uid=uid,
                gid=gid,
                size=0 if is_dir else info.st_size,
            )
        )
        if not is_dir:
            return

        # The copy-to protocol has no symlink frame. Match the existing SDKs by
        # following file links. Directory links are represented as empty
        # directories unless callers explicitly opt into traversal.
        if is_link and not follow_symlinks:
            return
        identity = (info.st_dev, info.st_ino)
        if identity in visited:
            entries.pop()
            return
        visited.add(identity)
        for child in sorted(local_path.iterdir(), key=lambda item: item.name):
            visit(child, str(PurePosixPath(remote_path) / child.name))

    visit(source, guest_path, root=True)
    return entries


def _request(entry: _UploadEntry) -> str:
    payload = {
        "direction": "to",
        "guest_path": entry.guest_path,
        "is_dir": entry.is_dir,
        "mode": entry.mode,
    }
    if entry.uid:
        payload["uid"] = entry.uid
    if entry.gid:
        payload["gid"] = entry.gid
    return json.dumps(payload, separators=(",", ":"))


def _parse_message(frame: str) -> dict[str, object]:
    try:
        decoded = cast(object, json.loads(frame))
    except json.JSONDecodeError as exc:
        raise CopyProtocolError("cp sent malformed JSON") from exc
    if not isinstance(decoded, dict):
        raise CopyProtocolError("cp sent an invalid control frame")
    message = cast(dict[str, object], decoded)
    if not isinstance(message.get("type"), str):
        raise CopyProtocolError("cp sent an invalid control frame")
    return message


def _integer_field(
    message: dict[str, object], name: str, default: int | None = None, maximum: int | None = None
) -> int:
    value = message.get(name, default)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0 or (maximum is not None and value > maximum):
        raise CopyProtocolError(f"cp header {name} has an invalid integer value")
    return value


def _check_upload_result(frame: bytes | str, expected_size: int) -> None:
    if not isinstance(frame, str):
        raise CopyProtocolError("cp upload expected a result control frame")
    message = _parse_message(frame)
    message_type = message["type"]
    if message_type == "error":
        detail = message.get("message")
        raise CopyProtocolError(f"copy failed: {detail if isinstance(detail, str) else 'unknown server error'}")
    if message_type != "result" or not isinstance(message.get("success"), bool):
        raise CopyProtocolError("cp upload expected a result control frame")
    if not message["success"]:
        detail = message.get("error")
        raise CopyProtocolError(f"copy failed: {detail if isinstance(detail, str) else 'unknown server error'}")
    bytes_written = message.get("bytes_written", 0)
    if isinstance(bytes_written, bool) or not isinstance(bytes_written, int) or bytes_written != expected_size:
        raise CopyProtocolError(f"cp upload wrote {bytes_written!r} bytes; expected {expected_size}")


def _copy_file_sync(websocket: SyncWebSocket, entry: _UploadEntry, callbacks: CopyCallbacks | None) -> None:
    if callbacks and callbacks.on_file_start:
        callbacks.on_file_start(str(entry.source), entry.size)
    copied = 0
    with entry.source.open("rb") as source:
        while chunk := source.read(_CHUNK_SIZE):
            websocket.send(chunk)
            copied += len(chunk)
            if callbacks and callbacks.on_progress:
                callbacks.on_progress(copied)
    websocket.send('{"type":"end"}')
    try:
        result = websocket.recv()
    except Exception as exc:
        raise CopyProtocolError("cp upload ended before the result frame") from exc
    _check_upload_result(result, entry.size)
    if callbacks and callbacks.on_file_end:
        callbacks.on_file_end(str(entry.source))


def cp_to_instance(
    client: ClientConfig,
    instance_id: str,
    src_path: str | os.PathLike[str],
    dst_path: str,
    *,
    mode: int | None = None,
    archive: bool = False,
    follow_symlinks: bool = False,
    callbacks: CopyCallbacks | None = None,
    connector: SyncWebSocketConnector = sync_connect,
) -> None:
    """Copy a local file or directory into a running instance."""

    entries = _upload_entries(
        Path(src_path),
        dst_path,
        mode=mode,
        archive=archive,
        follow_symlinks=follow_symlinks,
    )
    url, headers = connection_settings(client, instance_id, "cp")
    for entry in entries:
        with connector(url, additional_headers=headers, max_size=None) as websocket:
            websocket.send(_request(entry))
            if entry.is_dir:
                websocket.send('{"type":"end"}')
                try:
                    result = websocket.recv()
                except Exception as exc:
                    raise CopyProtocolError("cp upload ended before the result frame") from exc
                _check_upload_result(result, 0)
            else:
                _copy_file_sync(websocket, entry, callbacks)


async def _copy_file_async(websocket: AsyncWebSocket, entry: _UploadEntry, callbacks: CopyCallbacks | None) -> None:
    if callbacks and callbacks.on_file_start:
        callbacks.on_file_start(str(entry.source), entry.size)
    copied = 0
    source = await asyncio.to_thread(entry.source.open, "rb")
    try:
        while chunk := await asyncio.to_thread(source.read, _CHUNK_SIZE):
            await websocket.send(chunk)
            copied += len(chunk)
            if callbacks and callbacks.on_progress:
                callbacks.on_progress(copied)
    finally:
        await asyncio.to_thread(source.close)
    await websocket.send('{"type":"end"}')
    try:
        result = await websocket.recv()
    except Exception as exc:
        raise CopyProtocolError("cp upload ended before the result frame") from exc
    _check_upload_result(result, entry.size)
    if callbacks and callbacks.on_file_end:
        callbacks.on_file_end(str(entry.source))


async def cp_to_instance_async(
    client: ClientConfig,
    instance_id: str,
    src_path: str | os.PathLike[str],
    dst_path: str,
    *,
    mode: int | None = None,
    archive: bool = False,
    follow_symlinks: bool = False,
    callbacks: CopyCallbacks | None = None,
    connector: AsyncWebSocketConnector = async_connect,
) -> None:
    """Asynchronous counterpart to :func:`cp_to_instance`."""

    entries = await asyncio.to_thread(
        _upload_entries,
        Path(src_path),
        dst_path,
        mode=mode,
        archive=archive,
        follow_symlinks=follow_symlinks,
    )
    url, headers = connection_settings(client, instance_id, "cp")
    for entry in entries:
        async with connector(url, additional_headers=headers, max_size=None) as websocket:
            await websocket.send(_request(entry))
            if entry.is_dir:
                await websocket.send('{"type":"end"}')
                try:
                    result = await websocket.recv()
                except Exception as exc:
                    raise CopyProtocolError("cp upload ended before the result frame") from exc
                _check_upload_result(result, 0)
            else:
                await _copy_file_async(websocket, entry, callbacks)


@dataclass
class _DownloadHeader:
    path: str
    target: Path
    mode: int
    is_dir: bool
    is_symlink: bool
    link_target: str
    size: int
    mtime: int
    uid: int
    gid: int


class _DownloadState:
    def __init__(self, destination: Path, archive: bool, callbacks: CopyCallbacks | None) -> None:
        destination.mkdir(parents=True, exist_ok=True)
        self.root = destination.resolve()
        self.archive = archive
        self.callbacks = callbacks
        self.header: _DownloadHeader | None = None
        self.file: BinaryIO | None = None
        self.temp_path: Path | None = None
        self.bytes_received = 0
        self.complete = False

    def abort(self) -> None:
        if self.file is not None:
            self.file.close()
            self.file = None
        if self.temp_path is not None:
            self.temp_path.unlink(missing_ok=True)
            self.temp_path = None

    def consume(self, frame: bytes | str) -> None:
        if isinstance(frame, bytes):
            self._data(frame)
            return
        message = _parse_message(frame)
        message_type = message["type"]
        if message_type == "header":
            self._start(message)
        elif message_type == "end":
            self._end(message)
        elif message_type == "error":
            detail = message.get("message")
            path = message.get("path")
            location = f" at {path}" if isinstance(path, str) and path else ""
            raise CopyProtocolError(
                f"copy failed{location}: {detail if isinstance(detail, str) else 'unknown server error'}"
            )
        else:
            raise CopyProtocolError(f"cp download sent unexpected {message_type!r} frame")

    def _safe_target(self, server_path: object) -> Path:
        if not isinstance(server_path, str) or not server_path or "\\" in server_path:
            raise CopyProtocolError("cp header path must be a non-empty relative POSIX path")
        relative = PurePosixPath(server_path)
        if relative.is_absolute() or any(part in ("", ".", "..") for part in relative.parts):
            raise CopyProtocolError(f"cp path escapes destination: {server_path}")
        target = self.root.joinpath(*relative.parts)
        self._safe_parents(target.parent)
        return target

    def _safe_parents(self, parent: Path) -> None:
        try:
            relative = parent.relative_to(self.root)
        except ValueError as exc:
            raise CopyProtocolError("cp path escapes destination") from exc
        current = self.root
        for part in relative.parts:
            current /= part
            if current.is_symlink():
                raise CopyProtocolError(f"cp path traverses local symlink: {current}")
        parent.mkdir(parents=True, exist_ok=True)

    def _start(self, message: dict[str, object]) -> None:
        if self.header is not None:
            raise CopyProtocolError("cp sent a new header before ending the previous entry")
        target = self._safe_target(message.get("path"))
        mode = _integer_field(message, "mode", maximum=0o777)
        size = _integer_field(message, "size")
        mtime = _integer_field(message, "mtime")
        uid = _integer_field(message, "uid", 0)
        gid = _integer_field(message, "gid", 0)
        is_dir = message.get("is_dir")
        is_symlink = message.get("is_symlink", False)
        if not isinstance(is_dir, bool) or not isinstance(is_symlink, bool) or (is_dir and is_symlink):
            raise CopyProtocolError("cp header has invalid entry type flags")
        link_target = message.get("link_target", "")
        if not isinstance(link_target, str):
            raise CopyProtocolError("cp header link_target must be a string")

        header = _DownloadHeader(
            path=str(message["path"]),
            target=target,
            mode=mode,
            is_dir=is_dir,
            is_symlink=is_symlink,
            link_target=link_target,
            size=size,
            mtime=mtime,
            uid=uid,
            gid=gid,
        )
        self.header = header
        self.bytes_received = 0
        if header.is_dir:
            if target.is_symlink() or (target.exists() and not target.is_dir()):
                raise CopyProtocolError(f"cp cannot replace local path with directory: {target}")
            target.mkdir(parents=True, exist_ok=True)
            target.chmod(header.mode)
            self._chown(target, header, follow_symlinks=True)
        elif header.is_symlink:
            self._create_symlink(header)
        else:
            if target.is_symlink() or (target.exists() and target.is_dir()):
                raise CopyProtocolError(f"cp refuses unsafe local file target: {target}")
            descriptor, temp_name = tempfile.mkstemp(prefix=".hypeman-cp-", dir=target.parent)
            self.temp_path = Path(temp_name)
            self.file = os.fdopen(descriptor, "wb")
            if self.callbacks and self.callbacks.on_file_start:
                self.callbacks.on_file_start(header.path, header.size)

    def _create_symlink(self, header: _DownloadHeader) -> None:
        target = PurePosixPath(header.link_target)
        if not header.link_target or "\\" in header.link_target or target.is_absolute():
            raise CopyProtocolError(f"cp sent unsafe symlink target: {header.link_target}")
        resolved = header.target.parent.joinpath(*target.parts).resolve(strict=False)
        try:
            resolved.relative_to(self.root)
        except ValueError as exc:
            raise CopyProtocolError(f"cp symlink target escapes destination: {header.link_target}") from exc
        temp = header.target.parent / f".hypeman-cp-link-{uuid4().hex}"
        try:
            temp.symlink_to(header.link_target)
            os.replace(temp, header.target)
        finally:
            temp.unlink(missing_ok=True)
        self._chown(header.target, header, follow_symlinks=False)

    def _data(self, data: bytes) -> None:
        if self.header is None or self.file is None or self.header.is_dir or self.header.is_symlink:
            raise CopyProtocolError("cp sent binary data without a regular file header")
        if self.bytes_received + len(data) > self.header.size:
            raise CopyProtocolError(f"cp sent more bytes than declared for {self.header.path}")
        written = self.file.write(data)
        if written != len(data):
            raise OSError(f"short local write for {self.header.path}")
        self.bytes_received += written
        if self.callbacks and self.callbacks.on_progress:
            self.callbacks.on_progress(self.bytes_received)

    def _end(self, message: dict[str, object]) -> None:
        if self.header is None:
            raise CopyProtocolError("cp sent an end frame without a header")
        final = message.get("final")
        if not isinstance(final, bool):
            raise CopyProtocolError("cp end final must be a boolean")
        header = self.header
        if not header.is_dir and not header.is_symlink:
            if self.file is None or self.temp_path is None:
                raise CopyProtocolError("cp regular file state is incomplete")
            if self.bytes_received != header.size:
                raise CopyProtocolError(
                    f"cp received {self.bytes_received} bytes for {header.path}; expected {header.size}"
                )
            self.file.close()
            self.file = None
            self.temp_path.chmod(header.mode)
            if header.mtime:
                os.utime(self.temp_path, (header.mtime, header.mtime))
            self._chown(self.temp_path, header, follow_symlinks=True)
            os.replace(self.temp_path, header.target)
            self.temp_path = None
            if self.callbacks and self.callbacks.on_file_end:
                self.callbacks.on_file_end(header.path)
        self.header = None
        self.bytes_received = 0
        if final:
            self.complete = True

    def _chown(self, path: Path, header: _DownloadHeader, *, follow_symlinks: bool) -> None:
        if not self.archive or not hasattr(os, "chown"):
            return
        try:
            os.chown(path, header.uid, header.gid, follow_symlinks=follow_symlinks)
        except OSError:
            pass


def _download_request(src_path: str, follow_symlinks: bool) -> str:
    return json.dumps(
        {"direction": "from", "guest_path": src_path, "follow_links": follow_symlinks},
        separators=(",", ":"),
    )


def cp_from_instance(
    client: ClientConfig,
    instance_id: str,
    src_path: str,
    dst_path: str | os.PathLike[str],
    *,
    follow_symlinks: bool = False,
    archive: bool = False,
    callbacks: CopyCallbacks | None = None,
    connector: SyncWebSocketConnector = sync_connect,
) -> None:
    """Copy a guest file or directory into a safely-contained local directory."""

    url, headers = connection_settings(client, instance_id, "cp")
    state = _DownloadState(Path(dst_path), archive, callbacks)
    try:
        with connector(url, additional_headers=headers, max_size=None) as websocket:
            websocket.send(_download_request(src_path, follow_symlinks))
            while not state.complete:
                try:
                    frame = websocket.recv()
                except Exception as exc:
                    raise CopyProtocolError("cp download ended before the final marker") from exc
                state.consume(frame)
    except BaseException:
        state.abort()
        raise


async def cp_from_instance_async(
    client: ClientConfig,
    instance_id: str,
    src_path: str,
    dst_path: str | os.PathLike[str],
    *,
    follow_symlinks: bool = False,
    archive: bool = False,
    callbacks: CopyCallbacks | None = None,
    connector: AsyncWebSocketConnector = async_connect,
) -> None:
    """Asynchronous counterpart to :func:`cp_from_instance`."""

    url, headers = connection_settings(client, instance_id, "cp")
    state = _DownloadState(Path(dst_path), archive, callbacks)
    try:
        async with connector(url, additional_headers=headers, max_size=None) as websocket:
            await websocket.send(_download_request(src_path, follow_symlinks))
            while not state.complete:
                try:
                    frame = await websocket.recv()
                except Exception as exc:
                    raise CopyProtocolError("cp download ended before the final marker") from exc
                state.consume(frame)
    except BaseException:
        state.abort()
        raise
