# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ResourceStatus"]


class ResourceStatus(BaseModel):
    allocated: int
    """Currently allocated resources"""

    available: int
    """Available for allocation (effective_limit - allocated)"""

    capacity: int
    """Raw host capacity"""

    effective_limit: int
    """Capacity after oversubscription (capacity \\** ratio)"""

    oversub_ratio: float
    """Oversubscription ratio applied"""

    type: str
    """Resource type"""

    source: Optional[str] = None
    """How capacity was determined (detected, configured)"""
