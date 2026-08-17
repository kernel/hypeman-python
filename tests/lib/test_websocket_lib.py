from __future__ import annotations

import os
import json
from types import TracebackType
from pathlib import Path
from collections import deque
from dataclasses import field, dataclass
from collections.abc import AsyncIterator

import pytest

from hypeman.lib import (
    CopyCallbacks,
    CopyProtocolError,
    ExecProtocolError,
    exec,
    exec_async,
    cp_to_instance,
    cp_from_instance,
    cp_to_instance_async,
    cp_from_instance_async,
)


@dataclass
class FakeClient:
    base_url: str = "https://example.test/api/"
    api_key: str = "secret"


@dataclass
class FakeWebSocket:
    frames: deque[bytes | str | BaseException]
    sent: list[bytes | str] = field(default_factory=lambda: [])
    closed: bool = False

    def send(self, message: bytes | str) -> None:
        self.sent.append(message)

    def recv(self) -> bytes | str:
        frame = self.frames.popleft()
        if isinstance(frame, BaseException):
            raise frame
        return frame

    def close(self) -> None:
        self.closed = True

    def __enter__(self) -> FakeWebSocket:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


@dataclass
class FakeConnector:
    connections: deque[FakeWebSocket]
    calls: list[tuple[str, dict[str, str], int | None]] = field(default_factory=lambda: [])

    def __call__(self, url: str, *, additional_headers: dict[str, str], max_size: int | None) -> FakeWebSocket:
        self.calls.append((url, additional_headers, max_size))
        return self.connections.popleft()


@dataclass
class FakeAsyncWebSocket:
    frames: deque[bytes | str | BaseException]
    sent: list[bytes | str] = field(default_factory=lambda: [])
    closed: bool = False

    async def send(self, message: bytes | str) -> None:
        self.sent.append(message)

    async def recv(self) -> bytes | str:
        frame = self.frames.popleft()
        if isinstance(frame, BaseException):
            raise frame
        return frame

    async def close(self) -> None:
        self.closed = True

    async def __aenter__(self) -> FakeAsyncWebSocket:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()


@dataclass
class FakeAsyncConnector:
    connections: deque[FakeAsyncWebSocket]
    calls: list[tuple[str, dict[str, str], int | None]] = field(default_factory=lambda: [])

    def __call__(self, url: str, *, additional_headers: dict[str, str], max_size: int | None) -> FakeAsyncWebSocket:
        self.calls.append((url, additional_headers, max_size))
        return self.connections.popleft()


def text_frame(payload: dict[str, object]) -> str:
    return json.dumps(payload, separators=(",", ":"))


def upload_result(size: int = 0) -> str:
    return text_frame({"type": "result", "success": True, "bytes_written": size})


def file_header(path: str, *, size: int, mode: int = 0o640, mtime: int = 0) -> str:
    return text_frame(
        {
            "type": "header",
            "path": path,
            "mode": mode,
            "is_dir": False,
            "is_symlink": False,
            "link_target": "",
            "size": size,
            "mtime": mtime,
        }
    )


def test_exec_uses_client_auth_url_and_all_request_dimensions() -> None:
    websocket = FakeWebSocket(deque([b"out", b"err", '{"exitCode":0}']))
    connector = FakeConnector(deque([websocket]))

    result = exec(
        FakeClient(),
        "inst_123",
        ["sh", "-lc", "echo hi"],
        cwd="/app",
        env={"A": "b"},
        timeout=30,
        wait_for_agent=5,
        tty=True,
        rows=24,
        cols=80,
        stdin=[b"first", b"second"],
        resize=[(40, 120)],
        connector=connector,
    )

    assert result.output == b"outerr"
    assert result.exit_code == 0
    assert connector.calls == [
        ("wss://example.test/api/instances/inst_123/exec", {"Authorization": "Bearer secret"}, None)
    ]
    assert json.loads(str(websocket.sent[0])) == {
        "command": ["sh", "-lc", "echo hi"],
        "tty": True,
        "env": {"A": "b"},
        "cwd": "/app",
        "timeout": 30,
        "wait_for_agent": 5,
        "rows": 24,
        "cols": 80,
    }
    assert websocket.sent[1:3] == [b"first", b"second"]
    assert json.loads(str(websocket.sent[3])) == {"resize": {"rows": 40, "cols": 120}}
    assert websocket.closed


def test_exec_returns_nonzero_exit_without_losing_output() -> None:
    connector = FakeConnector(deque([FakeWebSocket(deque([b"failure\n", '{"exitCode":23}']))]))
    result = exec(FakeClient(base_url="http://localhost:4973"), "inst", ["false"], connector=connector)
    assert result.exit_code == 23
    assert result.output == b"failure\n"
    assert connector.calls[0][0] == "ws://localhost:4973/instances/inst/exec"


@pytest.mark.parametrize("frame", ["not-json", '{"error":"failed"}', '{"exitCode":"0"}', "[]"])
def test_exec_rejects_malformed_control_frames(frame: str) -> None:
    connector = FakeConnector(deque([FakeWebSocket(deque([frame]))]))
    with pytest.raises(ExecProtocolError):
        exec(FakeClient(), "inst", ["true"], connector=connector)


def test_exec_never_retries_after_dispatch() -> None:
    websocket = FakeWebSocket(deque([EOFError("closed")]))
    connector = FakeConnector(deque([websocket, FakeWebSocket(deque(['{"exitCode":0}']))]))
    with pytest.raises(ExecProtocolError, match="before an exitCode"):
        exec(FakeClient(), "inst", ["do-once"], connector=connector)
    assert len(connector.calls) == 1
    assert len(websocket.sent) == 1


@pytest.mark.asyncio
async def test_exec_async_supports_streaming_stdin() -> None:
    websocket = FakeAsyncWebSocket(deque([b"done", '{"exitCode":7}']))
    connector = FakeAsyncConnector(deque([websocket]))

    async def chunks() -> AsyncIterator[bytes]:
        yield b"one"
        yield b"two"

    result = await exec_async(FakeClient(), "inst", ["cat"], stdin=chunks(), connector=connector)
    assert result.output == b"done"
    assert result.exit_code == 7
    assert websocket.sent[1:] == [b"one", b"two"]


def test_cp_upload_file_preserves_mode_and_reports_progress(tmp_path: Path) -> None:
    source = tmp_path / "source.txt"
    source.write_bytes(b"payload")
    source.chmod(0o640)
    events: list[tuple[str, object]] = []
    callbacks = CopyCallbacks(
        on_file_start=lambda path, size: events.append(("start", (path, size))),
        on_progress=lambda copied: events.append(("progress", copied)),
        on_file_end=lambda path: events.append(("end", path)),
    )
    websocket = FakeWebSocket(deque([upload_result(7)]))
    connector = FakeConnector(deque([websocket]))

    cp_to_instance(
        FakeClient(),
        "inst",
        source,
        "/app/source.txt",
        archive=True,
        callbacks=callbacks,
        connector=connector,
    )

    request = json.loads(str(websocket.sent[0]))
    expected_request = {
        "direction": "to",
        "guest_path": "/app/source.txt",
        "is_dir": False,
        "mode": 0o640,
    }
    source_stat = source.stat()
    if source_stat.st_uid:
        expected_request["uid"] = source_stat.st_uid
    if source_stat.st_gid:
        expected_request["gid"] = source_stat.st_gid
    assert request == expected_request
    assert websocket.sent[1:] == [b"payload", '{"type":"end"}']
    assert events == [
        ("start", (str(source), 7)),
        ("progress", 7),
        ("end", str(source)),
    ]


def test_cp_upload_directory_uses_one_connection_per_entry(tmp_path: Path) -> None:
    source = tmp_path / "tree"
    source.mkdir()
    (source / "child.txt").write_bytes(b"x")
    first = FakeWebSocket(deque([upload_result()]))
    second = FakeWebSocket(deque([upload_result(1)]))
    connector = FakeConnector(deque([first, second]))

    cp_to_instance(FakeClient(), "inst", source, "/guest/tree", connector=connector)

    assert json.loads(str(first.sent[0]))["is_dir"] is True
    assert json.loads(str(second.sent[0]))["guest_path"] == "/guest/tree/child.txt"
    assert second.sent[1] == b"x"
    assert len(connector.calls) == 2


def test_cp_upload_file_symlink_follows_contents(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.write_bytes(b"contents")
    link = tmp_path / "link"
    link.symlink_to(target.name)
    websocket = FakeWebSocket(deque([upload_result(8)]))

    cp_to_instance(FakeClient(), "inst", link, "/guest/link", connector=FakeConnector(deque([websocket])))

    assert websocket.sent[1] == b"contents"


def test_cp_upload_rejects_partial_server_result(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.write_bytes(b"complete")
    connector = FakeConnector(deque([FakeWebSocket(deque([upload_result(3)]))]))
    with pytest.raises(CopyProtocolError, match="expected 8"):
        cp_to_instance(FakeClient(), "inst", source, "/guest/file", connector=connector)


def test_cp_download_file_is_atomic_and_preserves_metadata(tmp_path: Path) -> None:
    destination = tmp_path / "download"
    events: list[tuple[str, object]] = []
    callbacks = CopyCallbacks(
        on_file_start=lambda path, size: events.append(("start", (path, size))),
        on_progress=lambda copied: events.append(("progress", copied)),
        on_file_end=lambda path: events.append(("end", path)),
    )
    websocket = FakeWebSocket(
        deque(
            [
                file_header("sub/output.txt", size=5, mode=0o600, mtime=1_700_000_000),
                b"hello",
                text_frame({"type": "end", "final": True}),
            ]
        )
    )

    cp_from_instance(
        FakeClient(),
        "inst",
        "/guest/output.txt",
        destination,
        callbacks=callbacks,
        connector=FakeConnector(deque([websocket])),
    )

    output = destination / "sub" / "output.txt"
    assert output.read_bytes() == b"hello"
    assert stat_mode(output) == 0o600
    assert int(output.stat().st_mtime) == 1_700_000_000
    assert events == [("start", ("sub/output.txt", 5)), ("progress", 5), ("end", "sub/output.txt")]
    assert json.loads(str(websocket.sent[0])) == {
        "direction": "from",
        "guest_path": "/guest/output.txt",
        "follow_links": False,
    }


def stat_mode(path: Path) -> int:
    return path.stat().st_mode & 0o7777


@pytest.mark.parametrize("server_path", ["../escape", "/absolute", "sub/../../escape", "sub\\escape"])
def test_cp_download_rejects_traversal(tmp_path: Path, server_path: str) -> None:
    outside = tmp_path / "escape"
    connector = FakeConnector(deque([FakeWebSocket(deque([file_header(server_path, size=0)]))]))
    with pytest.raises(CopyProtocolError):
        cp_from_instance(FakeClient(), "inst", "/guest", tmp_path / "dest", connector=connector)
    assert not outside.exists()


def test_cp_download_rejects_existing_symlink_parent(tmp_path: Path) -> None:
    destination = tmp_path / "dest"
    destination.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    (destination / "linked").symlink_to(outside, target_is_directory=True)
    connector = FakeConnector(deque([FakeWebSocket(deque([file_header("linked/file", size=1), b"x"]))]))

    with pytest.raises(CopyProtocolError, match="local symlink"):
        cp_from_instance(FakeClient(), "inst", "/guest", destination, connector=connector)
    assert not (outside / "file").exists()


def test_cp_download_creates_safe_relative_symlink(tmp_path: Path) -> None:
    frame = text_frame(
        {
            "type": "header",
            "path": "links/current",
            "mode": 0o777,
            "is_dir": False,
            "is_symlink": True,
            "link_target": "../target",
            "size": 0,
            "mtime": 0,
        }
    )
    connector = FakeConnector(deque([FakeWebSocket(deque([frame, text_frame({"type": "end", "final": True})]))]))
    destination = tmp_path / "dest"

    cp_from_instance(FakeClient(), "inst", "/guest", destination, connector=connector)

    link = destination / "links" / "current"
    assert link.is_symlink()
    assert os.readlink(link) == "../target"


def test_cp_download_rejects_escaping_symlink(tmp_path: Path) -> None:
    frame = text_frame(
        {
            "type": "header",
            "path": "link",
            "mode": 0o777,
            "is_dir": False,
            "is_symlink": True,
            "link_target": "../../outside",
            "size": 0,
            "mtime": 0,
        }
    )
    connector = FakeConnector(deque([FakeWebSocket(deque([frame]))]))
    with pytest.raises(CopyProtocolError, match="escapes destination"):
        cp_from_instance(FakeClient(), "inst", "/guest", tmp_path / "dest", connector=connector)


def test_cp_download_removes_partial_file(tmp_path: Path) -> None:
    destination = tmp_path / "dest"
    connector = FakeConnector(
        deque([FakeWebSocket(deque([file_header("partial", size=5), b"ab", EOFError("closed")]))])
    )
    with pytest.raises(CopyProtocolError, match="final marker"):
        cp_from_instance(FakeClient(), "inst", "/guest", destination, connector=connector)
    assert not (destination / "partial").exists()
    assert not list(destination.glob(".hypeman-cp-*"))


def test_cp_download_surfaces_server_error(tmp_path: Path) -> None:
    error = text_frame({"type": "error", "message": "permission denied", "path": "/root/file"})
    connector = FakeConnector(deque([FakeWebSocket(deque([error]))]))
    with pytest.raises(CopyProtocolError, match="permission denied"):
        cp_from_instance(FakeClient(), "inst", "/root/file", tmp_path, connector=connector)


@pytest.mark.asyncio
async def test_cp_async_upload_and_download(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.write_bytes(b"async")
    upload_socket = FakeAsyncWebSocket(deque([upload_result(5)]))
    await cp_to_instance_async(
        FakeClient(),
        "inst",
        source,
        "/guest/source",
        connector=FakeAsyncConnector(deque([upload_socket])),
    )
    assert upload_socket.sent[1] == b"async"

    download_socket = FakeAsyncWebSocket(
        deque([file_header("result", size=5), b"async", text_frame({"type": "end", "final": True})])
    )
    destination = tmp_path / "dest"
    await cp_from_instance_async(
        FakeClient(),
        "inst",
        "/guest/result",
        destination,
        connector=FakeAsyncConnector(deque([download_socket])),
    )
    assert (destination / "result").read_bytes() == b"async"


def test_invalid_instance_id_is_rejected_before_connect() -> None:
    connector = FakeConnector(deque())
    with pytest.raises(ValueError, match="instance_id"):
        exec(FakeClient(), "../instance", ["true"], connector=connector)
    assert not connector.calls


def test_cp_upload_surfaces_error_and_close_frames(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.write_bytes(b"x")
    error_connector = FakeConnector(
        deque([FakeWebSocket(deque([text_frame({"type": "error", "message": "disk full"})]))])
    )
    with pytest.raises(CopyProtocolError, match="disk full"):
        cp_to_instance(FakeClient(), "inst", source, "/guest/file", connector=error_connector)

    close_connector = FakeConnector(deque([FakeWebSocket(deque([EOFError("closed")]))]))
    with pytest.raises(CopyProtocolError, match="before the result"):
        cp_to_instance(FakeClient(), "inst", source, "/guest/file", connector=close_connector)


def test_cp_download_rejects_malformed_control_frame(tmp_path: Path) -> None:
    connector = FakeConnector(deque([FakeWebSocket(deque(["not-json"]))]))
    with pytest.raises(CopyProtocolError, match="malformed JSON"):
        cp_from_instance(FakeClient(), "inst", "/guest", tmp_path, connector=connector)
