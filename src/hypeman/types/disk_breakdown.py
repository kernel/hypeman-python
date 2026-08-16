# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DiskBreakdown"]


class DiskBreakdown(BaseModel):
    images_bytes: Optional[int] = None
    """Disk used by exported rootfs images"""

    oci_cache_bytes: Optional[int] = None
    """Disk used by OCI layer cache (shared blobs)"""

    overlays_bytes: Optional[int] = None
    """Disk used by instance overlays (rootfs + volume overlays)"""

    volumes_bytes: Optional[int] = None
    """Disk used by volumes"""
