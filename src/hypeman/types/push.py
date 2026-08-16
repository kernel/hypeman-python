# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .push_status import PushStatus

__all__ = ["Push"]


class Push(BaseModel):
    id: str
    """Push job identifier"""

    created_at: datetime

    digest: str
    """Cached manifest digest being pushed"""

    image: str
    """Hypeman image name (normalized ref)"""

    status: PushStatus

    target: str
    """Remote reference the image is pushed to"""

    bytes: Optional[int] = None
    """Total compressed layer bytes pushed"""

    completed_at: Optional[datetime] = None

    error: Optional[str] = None
    """Error message"""

    layers: Optional[int] = None
    """Number of layers pushed"""

    queue_position: Optional[int] = None
    """Position in the push queue"""
