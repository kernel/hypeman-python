# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RestartStatus"]


class RestartStatus(BaseModel):
    """Runtime status for restart policy decisions."""

    attempts: Optional[int] = None
    """Consecutive automatic restart attempts in the current failure window."""

    blocked_reason: Optional[Literal["manual_stop", "max_attempts_exceeded"]] = None
    """Reason automatic restarts are currently blocked."""

    last_attempt_at: Optional[datetime] = None
    """Last time Hypeman attempted an automatic restart."""

    last_reason: Optional[Literal["health_check_failed"]] = None
    """Most recent non-exit failure signal that entered restart policy."""

    next_attempt_at: Optional[datetime] = None
    """Next scheduled automatic restart attempt after backoff."""
