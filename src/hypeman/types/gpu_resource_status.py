# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .gpu_profile import GPUProfile
from .passthrough_device import PassthroughDevice

__all__ = ["GPUResourceStatus"]


class GPUResourceStatus(BaseModel):
    """GPU resource status. Null if no GPUs available."""

    mode: Literal["vgpu", "passthrough"]
    """GPU mode (vgpu for SR-IOV/mdev, passthrough for whole GPU)"""

    total_slots: int
    """Total slots (VFs for vGPU, physical GPUs for passthrough)"""

    used_slots: int
    """Slots currently in use"""

    devices: Optional[List[PassthroughDevice]] = None
    """Physical GPUs (only in passthrough mode)"""

    profiles: Optional[List[GPUProfile]] = None
    """Available vGPU profiles (only in vGPU mode)"""
