# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .gpu_profile import GPUProfile
from .passthrough_device import PassthroughDevice

__all__ = ["GPUResourceStatus"]


class GPUResourceStatus(BaseModel):
    """GPU resource status. Null if no GPUs available."""

    allocatable_slots: int
    """
    Free slots eligible for placement, matching admission control (excludes
    quarantined VFs; 0 while VF health state is unavailable)
    """

    mode: Literal["vgpu", "passthrough"]
    """GPU mode (vgpu for SR-IOV/mdev, passthrough for whole GPU)"""

    quarantined_slots: int
    """VFs quarantined after guest driver init failures (vGPU mode only).

    May overlap used_slots until the affected instance releases its VF.
    """

    total_slots: int
    """Total slots (VFs for vGPU, physical GPUs for passthrough)"""

    used_slots: int
    """Slots currently in use.

    Includes quarantined VFs that are still assigned, so this can overlap
    quarantined_slots.
    """

    devices: Optional[List[PassthroughDevice]] = None
    """Physical GPUs (only in passthrough mode)"""

    placement_disabled_reason: Optional[str] = None
    """
    Present when allocatable_slots is 0 because the VF health state could not be
    read or written rather than because the host is full. vGPU placement is refused
    until the state file is repaired or the next write succeeds.
    """

    profiles: Optional[List[GPUProfile]] = None
    """Available vGPU profiles (only in vGPU mode)"""
