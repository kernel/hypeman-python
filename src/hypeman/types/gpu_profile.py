# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GPUProfile"]


class GPUProfile(BaseModel):
    """Available vGPU profile"""

    available: int
    """Number of instances that can be created with this profile"""

    framebuffer_mb: int
    """Frame buffer size in MB"""

    name: str
    """Profile name (user-facing)"""
