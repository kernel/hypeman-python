# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["HealthCheckTcp"]


class HealthCheckTcp(BaseModel):
    port: int
    """Port to open on the instance network address."""
