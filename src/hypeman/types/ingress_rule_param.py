# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .ingress_match_param import IngressMatchParam
from .ingress_target_param import IngressTargetParam

__all__ = ["IngressRuleParam", "RequestHeaderAuth"]


class RequestHeaderAuth(TypedDict, total=False):
    header: Required[str]
    """Dedicated request header that must match before proxying.

    Reserved authentication, cookie, host, framing, proxy, and hop-by-hop headers
    are not allowed.
    """

    value: Required[str]
    """Exact header value required before proxying.

    This sensitive value is persisted and returned by the API like instance
    environment variables; clients should hide it by default.
    """


class IngressRuleParam(TypedDict, total=False):
    match: Required[IngressMatchParam]

    target: Required[IngressTargetParam]

    redirect_http: bool
    """
    Auto-create HTTP to HTTPS redirect for this hostname (only applies when tls is
    enabled)
    """

    request_header_auth: RequestHeaderAuth

    tls: bool
    """Enable TLS termination (certificate auto-issued via ACME)."""
