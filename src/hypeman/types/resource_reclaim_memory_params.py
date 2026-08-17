# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ResourceReclaimMemoryParams"]


class ResourceReclaimMemoryParams(TypedDict, total=False):
    reclaim_bytes: Required[int]
    """Total bytes of guest memory to reclaim across eligible VMs."""

    dry_run: bool
    """Calculate a reclaim plan without applying balloon changes or creating a hold."""

    hold_for: str
    """How long to keep the reclaim hold active (Go duration string).

    Defaults to 5m when omitted.
    """

    reason: str
    """Optional operator-provided reason attached to logs and traces."""
