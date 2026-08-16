# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SnapshotRestoreParams"]


class SnapshotRestoreParams(TypedDict, total=False):
    id: Required[str]

    target_hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"]
    """Optional hypervisor override.

    Allowed only when restoring from a Stopped snapshot. Standby snapshots must
    restore with their original hypervisor.
    """

    target_state: Literal["Stopped", "Standby", "Running"]
    """Optional final state after restore. Defaults by snapshot kind:

    - Standby snapshot defaults to Running
    - Stopped snapshot defaults to Stopped
    """
