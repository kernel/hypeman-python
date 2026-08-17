# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .memory_reclaim_action import MemoryReclaimAction

__all__ = ["MemoryReclaimResponse"]


class MemoryReclaimResponse(BaseModel):
    actions: List[MemoryReclaimAction]

    applied_reclaim_bytes: int

    host_available_bytes: int

    host_pressure_state: Literal["healthy", "pressure"]

    planned_reclaim_bytes: int

    requested_reclaim_bytes: int

    hold_until: Optional[datetime] = None
    """When the current manual reclaim hold expires."""
