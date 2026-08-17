# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VolumeMountParam"]


class VolumeMountParam(TypedDict, total=False):
    mount_path: Required[str]
    """Path where volume is mounted in the guest"""

    volume_id: Required[str]
    """Volume identifier"""

    overlay: bool
    """Create per-instance overlay for writes (requires readonly=true)"""

    overlay_size: str
    """Max overlay size as human-readable string (e.g., "1GB").

    Required if overlay=true.
    """

    readonly: bool
    """Whether volume is mounted read-only"""
