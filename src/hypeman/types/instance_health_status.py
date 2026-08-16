# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InstanceHealthStatus"]


class InstanceHealthStatus(BaseModel):
    consecutive_failures: int
    """Consecutive failed checks in the current health window."""

    consecutive_successes: int
    """Consecutive successful checks in the current health window."""

    status: Literal["disabled", "starting", "healthy", "unhealthy", "unknown"]
    """Current workload health status."""

    last_checked_at: Optional[datetime] = None
    """Most recent check completion time."""

    last_error: Optional[str] = None
    """Truncated error from the most recent failed check."""

    last_failure_at: Optional[datetime] = None
    """Most recent failed check completion time."""

    last_success_at: Optional[datetime] = None
    """Most recent successful check completion time."""
