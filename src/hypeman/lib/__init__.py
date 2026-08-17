"""Manually maintained APIs for Hypeman's WebSocket endpoints."""

from .cp import (
    CopyCallbacks,
    CopyProtocolError,
    cp_to_instance,
    cp_from_instance,
    cp_to_instance_async,
    cp_from_instance_async,
)
from ._ws import (
    SyncWebSocket,
    AsyncWebSocket,
    SyncWebSocketConnector,
    AsyncWebSocketConnector,
)
from .exec import ExecResult, ExecProtocolError, exec, exec_async

__all__ = [
    "AsyncWebSocket",
    "AsyncWebSocketConnector",
    "CopyCallbacks",
    "CopyProtocolError",
    "ExecProtocolError",
    "ExecResult",
    "SyncWebSocket",
    "SyncWebSocketConnector",
    "cp_from_instance",
    "cp_from_instance_async",
    "cp_to_instance",
    "cp_to_instance_async",
    "exec",
    "exec_async",
]
