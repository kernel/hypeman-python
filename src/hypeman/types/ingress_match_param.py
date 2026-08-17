# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IngressMatchParam"]


class IngressMatchParam(TypedDict, total=False):
    hostname: Required[str]
    """Hostname to match. Can be:

    - Literal: "api.example.com" (exact match on Host header)
    - Pattern: "{instance}.example.com" (dynamic routing based on subdomain)

    Pattern hostnames use named captures in curly braces (e.g., {instance}, {app})
    that extract parts of the hostname for routing. The extracted values can be
    referenced in the target.instance field.
    """

    port: int
    """Host port to listen on for this rule (default 80)"""
