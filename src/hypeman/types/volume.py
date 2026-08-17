# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .volume_attachment import VolumeAttachment

__all__ = ["Volume"]


class Volume(BaseModel):
    id: str
    """Unique identifier"""

    created_at: datetime
    """Creation timestamp (RFC3339)"""

    name: str
    """Volume name"""

    size_gb: int
    """Size in gigabytes"""

    attachments: Optional[List[VolumeAttachment]] = None
    """List of current attachments (empty if not attached)"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""
