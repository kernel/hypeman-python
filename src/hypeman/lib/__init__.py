"""Manually maintained APIs for Hypeman's WebSocket endpoints."""

from .cp import (
    CopyCallbacks,
    CopyProtocolError,
    cp_to_instance,
    cp_from_instance,
    cp_to_instance_async,
    cp_from_instance_async,
)
from .exec import ExecResult, ExecProtocolError, exec, exec_async

__all__ = [
    "CopyCallbacks",
    "CopyProtocolError",
    "ExecProtocolError",
    "ExecResult",
    "cp_from_instance",
    "cp_from_instance_async",
    "cp_to_instance",
    "cp_to_instance_async",
    "exec",
    "exec_async",
]
