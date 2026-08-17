# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeCreateFromArchiveParams"]


class VolumeCreateFromArchiveParams(TypedDict, total=False):
    name: Required[str]
    """Volume name"""

    size_gb: Required[int]
    """Maximum size in GB (extraction fails if content exceeds this)"""

    id: str
    """Optional custom volume ID (auto-generated if not provided)"""

    tags: Dict[str, str]
    """Tags for the created volume."""
