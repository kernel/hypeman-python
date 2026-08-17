# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IngressMatch"]


class IngressMatch(BaseModel):
    hostname: str
    """Hostname to match. Can be:

    - Literal: "api.example.com" (exact match on Host header)
    - Pattern: "{instance}.example.com" (dynamic routing based on subdomain)

    Pattern hostnames use named captures in curly braces (e.g., {instance}, {app})
    that extract parts of the hostname for routing. The extracted values can be
    referenced in the target.instance field.
    """

    port: Optional[int] = None
    """Host port to listen on for this rule (default 80)"""
