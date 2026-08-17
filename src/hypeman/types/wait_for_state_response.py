# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WaitForStateResponse"]


class WaitForStateResponse(BaseModel):
    state: Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"]
    """Current instance state when the wait completed"""

    timed_out: bool
    """Whether the timeout expired before the target state was reached"""

    state_error: Optional[str] = None
    """Error message when derived state is Unknown"""
