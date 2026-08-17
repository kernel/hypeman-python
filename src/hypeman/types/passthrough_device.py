# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PassthroughDevice"]


class PassthroughDevice(BaseModel):
    """Physical GPU available for passthrough"""

    available: bool
    """Whether this GPU is available (not attached to an instance)"""

    name: str
    """GPU name"""
