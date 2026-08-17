# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["HealthCheckHTTPParam"]


class HealthCheckHTTPParam(TypedDict, total=False):
    port: Required[int]
    """Port to probe on the instance network address."""

    expected_status: int
    """Exact status code required for a successful probe."""

    path: str
    """HTTP path to request."""

    scheme: Literal["http", "https"]
    """HTTP scheme to use for the probe."""
