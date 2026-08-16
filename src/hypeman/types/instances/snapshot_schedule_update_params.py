# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..snapshot_schedule_retention_param import SnapshotScheduleRetentionParam

__all__ = ["SnapshotScheduleUpdateParams"]


class SnapshotScheduleUpdateParams(TypedDict, total=False):
    interval: Required[str]
    """Snapshot interval (Go duration format, minimum 1m)."""

    retention: Required[SnapshotScheduleRetentionParam]
    """At least one of max_count or max_age must be provided."""

    metadata: Dict[str, str]
    """User-defined key-value tags."""

    name_prefix: Optional[str]
    """Optional prefix for auto-generated scheduled snapshot names (max 47 chars)."""
