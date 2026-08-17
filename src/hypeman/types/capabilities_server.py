# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CapabilitiesServer"]


class CapabilitiesServer(BaseModel):
    api_version: str
    """API contract version (matches the OpenAPI document info version)"""

    version: str
    """
    Server build version (short git revision, with "-dirty" suffix for uncommitted
    builds, or "unknown")
    """
