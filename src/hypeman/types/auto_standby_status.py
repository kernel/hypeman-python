# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutoStandbyStatus"]


class AutoStandbyStatus(BaseModel):
    active_inbound_connections: int
    """Number of currently tracked qualifying inbound TCP connections."""

    configured: bool
    """Whether the instance has any auto-standby policy configured."""

    eligible: bool
    """Whether the instance is currently eligible to enter standby."""

    enabled: bool
    """Whether the configured auto-standby policy is enabled."""

    reason: Literal[
        "unsupported_platform",
        "policy_missing",
        "policy_disabled",
        "instance_not_running",
        "network_disabled",
        "missing_ip",
        "has_vgpu",
        "active_inbound_connections",
        "idle_timeout_not_elapsed",
        "observer_error",
        "ready_for_standby",
    ]

    status: Literal[
        "unsupported",
        "disabled",
        "ineligible",
        "active",
        "idle_countdown",
        "ready_for_standby",
        "standby_requested",
        "error",
    ]

    supported: bool
    """Whether the current host platform supports auto-standby diagnostics."""

    tracking_mode: str
    """Diagnostic identifier for the runtime tracking mode in use."""

    countdown_remaining: Optional[str] = None
    """Remaining time before the controller attempts standby, when applicable."""

    hold_until: Optional[datetime] = None
    """Until when auto-standby is held off, if a hold is active."""

    idle_since: Optional[datetime] = None
    """When the controller most recently observed the instance become idle."""

    idle_timeout: Optional[str] = None
    """Configured idle timeout from the auto-standby policy."""

    last_inbound_activity_at: Optional[datetime] = None
    """
    Timestamp of the most recent qualifying inbound TCP activity the controller
    observed.
    """

    next_standby_at: Optional[datetime] = None
    """When the controller expects to attempt standby next, if a countdown is active."""
