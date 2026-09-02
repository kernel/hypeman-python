# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GPUProfile"]


class GPUProfile(BaseModel):
    """Available vGPU profile"""

    available: int
    """Number of virtual functions currently able to create this profile.

    Best-effort: creating an instance may reduce availability on sibling functions
    sharing GPU framebuffer.
    """

    framebuffer_mb: int
    """Frame buffer size in MB"""

    name: str
    """Profile name (user-facing)"""
