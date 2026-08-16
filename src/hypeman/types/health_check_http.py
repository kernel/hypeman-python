# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HealthCheckHTTP"]


class HealthCheckHTTP(BaseModel):
    port: int
    """Port to probe on the instance network address."""

    expected_status: Optional[int] = None
    """Exact status code required for a successful probe."""

    path: Optional[str] = None
    """HTTP path to request."""

    scheme: Optional[Literal["http", "https"]] = None
    """HTTP scheme to use for the probe."""
