# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .disk_breakdown import DiskBreakdown
from .resource_status import ResourceStatus
from .gpu_resource_status import GPUResourceStatus
from .resource_allocation import ResourceAllocation

__all__ = ["Resources"]


class Resources(BaseModel):
    allocations: List[ResourceAllocation]

    cpu: ResourceStatus

    disk: ResourceStatus

    memory: ResourceStatus

    network: ResourceStatus

    disk_breakdown: Optional[DiskBreakdown] = None

    disk_io: Optional[ResourceStatus] = None

    gpu: Optional[GPUResourceStatus] = None
    """GPU resource status. Null if no GPUs available."""
