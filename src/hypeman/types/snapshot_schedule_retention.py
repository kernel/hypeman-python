# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SnapshotScheduleRetention"]


class SnapshotScheduleRetention(BaseModel):
    """Automatic cleanup policy for scheduled snapshots."""

    max_age: Optional[str] = None
    """Delete scheduled snapshots older than this duration (Go duration format)."""

    max_count: Optional[int] = None
    """
    Keep at most this many scheduled snapshots for the instance (0 disables
    count-based cleanup).
    """
