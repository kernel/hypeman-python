# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["IngressTarget"]


class IngressTarget(BaseModel):
    instance: str
    """Target instance name, ID, or capture reference.

    - For literal hostnames: Use the instance name or ID directly (e.g., "my-api")
    - For pattern hostnames: Reference a capture from the hostname (e.g.,
      "{instance}")

    When using pattern hostnames, the instance is resolved dynamically at request
    time.
    """

    port: int
    """Target port on the instance"""
