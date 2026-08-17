# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AutoStandbyPolicy"]


class AutoStandbyPolicy(BaseModel):
    """
    Linux-only automatic standby policy based on active inbound TCP connections
    observed from the host conntrack table.
    """

    enabled: Optional[bool] = None
    """Whether automatic standby is enabled for this instance."""

    idle_timeout: Optional[str] = None
    """
    How long the instance must have zero qualifying inbound TCP connections before
    Hypeman places it into standby.
    """

    ignore_destination_ports: Optional[List[int]] = None
    """Optional destination TCP ports that should not keep the instance awake."""

    ignore_source_cidrs: Optional[List[str]] = None
    """Optional client CIDRs that should not keep the instance awake."""
