# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .snapshot_kind import SnapshotKind
from .shared.snapshot_compression_config import SnapshotCompressionConfig

__all__ = ["Snapshot"]


class Snapshot(BaseModel):
    id: str
    """Auto-generated unique snapshot identifier"""

    created_at: datetime
    """Snapshot creation timestamp"""

    kind: SnapshotKind
    """Snapshot capture kind"""

    size_bytes: int
    """Total payload size in bytes"""

    source_hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"]
    """Source instance hypervisor at snapshot creation time"""

    source_instance_id: str
    """Source instance ID at snapshot creation time"""

    source_instance_name: str
    """Source instance name at snapshot creation time"""

    compressed_size_bytes: Optional[int] = None
    """Compressed memory payload size in bytes"""

    compression: Optional[SnapshotCompressionConfig] = None

    compression_error: Optional[str] = None
    """Compression error message when compression_state is error"""

    compression_state: Optional[Literal["none", "compressing", "compressed", "error"]] = None
    """Compression status of the snapshot payload memory file"""

    name: Optional[str] = None
    """Optional human-readable snapshot name (unique per source instance)"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""

    uncompressed_size_bytes: Optional[int] = None
    """Uncompressed memory payload size in bytes"""
