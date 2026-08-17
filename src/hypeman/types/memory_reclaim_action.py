# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryReclaimAction"]


class MemoryReclaimAction(BaseModel):
    applied_reclaim_bytes: int

    assigned_memory_bytes: int

    hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"]

    instance_id: str

    instance_name: str

    planned_target_guest_memory_bytes: int

    previous_target_guest_memory_bytes: int

    protected_floor_bytes: int

    status: str
    """Result of this VM's reclaim step."""

    target_guest_memory_bytes: int

    error: Optional[str] = None
    """Error message when status is error or unsupported."""
