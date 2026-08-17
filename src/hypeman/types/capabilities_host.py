# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CapabilitiesHost"]


class CapabilitiesHost(BaseModel):
    arch: str
    """Host CPU architecture"""

    os: str
    """Host operating system"""
