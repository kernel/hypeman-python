# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .snapshot_kind import SnapshotKind

__all__ = ["SnapshotListParams"]


class SnapshotListParams(TypedDict, total=False):
    kind: SnapshotKind
    """Filter snapshots by kind"""

    name: str
    """Filter snapshots by snapshot name"""

    source_instance_id: str
    """Filter snapshots by source instance ID"""

    tags: Dict[str, str]
    """Filter snapshots by tag key-value pairs."""
