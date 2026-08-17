# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InstanceStats"]


class InstanceStats(BaseModel):
    """Real-time resource utilization statistics for a VM instance"""

    allocated_memory_bytes: int
    """Total memory allocated to the VM (Size + HotplugSize) in bytes"""

    allocated_vcpus: int
    """Number of vCPUs allocated to the VM"""

    cpu_seconds: float
    """Total CPU time consumed by the VM hypervisor process in seconds"""

    instance_id: str
    """Instance identifier"""

    instance_name: str
    """Instance name"""

    memory_rss_bytes: int
    """Resident Set Size - actual physical memory used by the VM in bytes"""

    memory_vms_bytes: int
    """Virtual Memory Size - total virtual memory allocated in bytes"""

    network_rx_bytes: int
    """Total network bytes received by the VM (from TAP interface)"""

    network_tx_bytes: int
    """Total network bytes transmitted by the VM (from TAP interface)"""

    memory_utilization_ratio: Optional[float] = None
    """Memory utilization ratio (RSS / allocated memory).

    Only present when allocated_memory_bytes > 0.
    """
