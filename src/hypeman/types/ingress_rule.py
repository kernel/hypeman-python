# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .ingress_match import IngressMatch
from .ingress_target import IngressTarget

__all__ = ["IngressRule", "RequestHeaderAuth"]


class RequestHeaderAuth(BaseModel):
    header: str
    """Dedicated request header that must match before proxying.

    Reserved authentication, cookie, host, framing, proxy, and hop-by-hop headers
    are not allowed.
    """

    value: str
    """Exact header value required before proxying.

    This sensitive value is persisted and returned by the API like instance
    environment variables; clients should hide it by default.
    """


class IngressRule(BaseModel):
    match: IngressMatch

    target: IngressTarget

    redirect_http: Optional[bool] = None
    """
    Auto-create HTTP to HTTPS redirect for this hostname (only applies when tls is
    enabled)
    """

    request_header_auth: Optional[RequestHeaderAuth] = None

    tls: Optional[bool] = None
    """Enable TLS termination (certificate auto-issued via ACME)."""
