# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .snapshot_schedule_retention import SnapshotScheduleRetention

__all__ = ["SnapshotSchedule"]


class SnapshotSchedule(BaseModel):
    created_at: datetime
    """Schedule creation timestamp."""

    instance_id: str
    """Source instance ID."""

    interval: str
    """Snapshot interval (Go duration format)."""

    next_run_at: datetime
    """Next scheduled run time."""

    retention: SnapshotScheduleRetention
    """Automatic cleanup policy for scheduled snapshots."""

    updated_at: datetime
    """Schedule update timestamp."""

    last_error: Optional[str] = None
    """Last schedule run error, if any."""

    last_run_at: Optional[datetime] = None
    """Last schedule execution time."""

    last_snapshot_id: Optional[str] = None
    """Snapshot ID produced by the last successful run."""

    metadata: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""

    name_prefix: Optional[str] = None
    """Optional prefix used for generated scheduled snapshot names."""
