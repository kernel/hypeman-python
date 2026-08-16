# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .build_status import BuildStatus

__all__ = ["BuildEvent"]


class BuildEvent(BaseModel):
    timestamp: datetime
    """Event timestamp"""

    type: Literal["log", "status", "heartbeat"]
    """Event type"""

    content: Optional[str] = None
    """Log line content (only for type=log)"""

    status: Optional[BuildStatus] = None
    """New build status (only for type=status)"""
