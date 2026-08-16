# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeCreateParams"]


class VolumeCreateParams(TypedDict, total=False):
    name: Required[str]
    """Volume name"""

    size_gb: Required[int]
    """Size in gigabytes"""

    id: str
    """Optional custom identifier (auto-generated if not provided)"""

    tags: Dict[str, str]
    """User-defined key-value tags."""
