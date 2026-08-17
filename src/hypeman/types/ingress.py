# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .ingress_rule import IngressRule

__all__ = ["Ingress"]


class Ingress(BaseModel):
    id: str
    """Auto-generated unique identifier"""

    created_at: datetime
    """Creation timestamp (RFC3339)"""

    name: str
    """Human-readable name"""

    rules: List[IngressRule]
    """Routing rules for this ingress"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""
