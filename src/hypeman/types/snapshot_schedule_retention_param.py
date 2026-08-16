# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SnapshotScheduleRetentionParam"]


class SnapshotScheduleRetentionParam(TypedDict, total=False):
    """Automatic cleanup policy for scheduled snapshots."""

    max_age: str
    """Delete scheduled snapshots older than this duration (Go duration format)."""

    max_count: int
    """
    Keep at most this many scheduled snapshots for the instance (0 disables
    count-based cleanup).
    """
