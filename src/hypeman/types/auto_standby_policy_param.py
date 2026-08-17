# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AutoStandbyPolicyParam"]


class AutoStandbyPolicyParam(TypedDict, total=False):
    """
    Linux-only automatic standby policy based on active inbound TCP connections
    observed from the host conntrack table.
    """

    enabled: bool
    """Whether automatic standby is enabled for this instance."""

    idle_timeout: str
    """
    How long the instance must have zero qualifying inbound TCP connections before
    Hypeman places it into standby.
    """

    ignore_destination_ports: Iterable[int]
    """Optional destination TCP ports that should not keep the instance awake."""

    ignore_source_cidrs: SequenceNotStr[str]
    """Optional client CIDRs that should not keep the instance awake."""
