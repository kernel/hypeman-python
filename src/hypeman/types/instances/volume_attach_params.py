# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VolumeAttachParams"]


class VolumeAttachParams(TypedDict, total=False):
    id: Required[str]

    mount_path: Required[str]
    """Path where volume should be mounted"""

    readonly: bool
    """Mount as read-only"""
