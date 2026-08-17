# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SnapshotForkParams"]


class SnapshotForkParams(TypedDict, total=False):
    name: Required[str]
    """
    Name for the new instance (lowercase letters, digits, and dashes only; cannot
    start or end with a dash)
    """

    target_hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"]
    """Optional hypervisor override.

    Allowed only when forking from a Stopped snapshot. Standby snapshots must fork
    with their original hypervisor.
    """

    target_state: Literal["Stopped", "Standby", "Running"]
    """Optional final state for the forked instance. Defaults by snapshot kind:

    - Standby snapshot defaults to Running
    - Stopped snapshot defaults to Stopped
    """
