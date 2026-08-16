# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ResourceAllocation"]


class ResourceAllocation(BaseModel):
    cpu: Optional[int] = None
    """vCPUs allocated"""

    disk_bytes: Optional[int] = None
    """Disk allocated in bytes (overlay + volumes)"""

    disk_io_bps: Optional[int] = None
    """Disk I/O bandwidth limit in bytes/sec"""

    instance_id: Optional[str] = None
    """Instance identifier"""

    instance_name: Optional[str] = None
    """Instance name"""

    memory_bytes: Optional[int] = None
    """Memory allocated in bytes"""

    network_download_bps: Optional[int] = None
    """Download bandwidth limit in bytes/sec (external→VM)"""

    network_upload_bps: Optional[int] = None
    """Upload bandwidth limit in bytes/sec (VM→external)"""
