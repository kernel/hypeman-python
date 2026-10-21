# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GPUProfile"]


class GPUProfile(BaseModel):
    """Available vGPU profile"""

    available: int
    """
    Number of additional instances of this profile the host can take if only this
    profile is added. Counts for different profiles are not additive: an instance of
    one profile can reduce availability of others on the same GPU.
    """

    framebuffer_mb: int
    """Frame buffer size in MB"""

    name: str
    """Profile name (user-facing)"""
