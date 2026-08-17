# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["BuilderCreateParams"]


class BuilderCreateParams(TypedDict, total=False):
    id: str
    """Optional caller-supplied identifier, auto-generated if not provided"""

    disk_size_gb: int
    """Cache disk size in gigabytes. Omit to use the server default."""

    name: str
    """Optional non-unique display name"""

    tags: Dict[str, str]
    """User-defined key-value tags."""
