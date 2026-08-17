# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceForkParams"]


class InstanceForkParams(TypedDict, total=False):
    name: Required[str]
    """
    Name for the forked instance (lowercase letters, digits, and dashes only; cannot
    start or end with a dash)
    """

    from_running: bool
    """
    Allow forking from a running source instance. When true and source is Running,
    the source is put into standby, forked, then restored back to Running.
    """

    target_state: Literal["Stopped", "Standby", "Running"]
    """
    Optional final state for the forked instance. Default is the source instance
    state at fork time. For example, forking from Running defaults the fork result
    to Running.
    """
