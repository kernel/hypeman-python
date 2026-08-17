# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VolumeMount"]


class VolumeMount(BaseModel):
    mount_path: str
    """Path where volume is mounted in the guest"""

    volume_id: str
    """Volume identifier"""

    overlay: Optional[bool] = None
    """Create per-instance overlay for writes (requires readonly=true)"""

    overlay_size: Optional[str] = None
    """Max overlay size as human-readable string (e.g., "1GB").

    Required if overlay=true.
    """

    readonly: Optional[bool] = None
    """Whether volume is mounted read-only"""
