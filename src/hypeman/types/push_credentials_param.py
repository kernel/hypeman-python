# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PushCredentialsParam"]


class PushCredentialsParam(TypedDict, total=False):
    """Docker-style registry credentials borrowed for one image pull or push request.

    They remain
    in memory and are never persisted or logged. When omitted or empty, the server's own registry
    credentials are used. An interrupted credentialed operation must be retried with fresh credentials.
    """

    password: str
    """Registry password or access token"""

    registry_token: str
    """Bearer token for an Authorization header"""

    username: str
    """Registry username"""
