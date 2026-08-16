# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .push_credentials_param import PushCredentialsParam

__all__ = ["PushCreateParams"]


class PushCreateParams(TypedDict, total=False):
    image: Required[str]
    """Hypeman image name to push (tag or digest form)"""

    target: Required[str]
    """Full remote reference to push to"""

    credentials: PushCredentialsParam
    """Docker-style registry credentials borrowed for one image pull or push request.

    They remain in memory and are never persisted or logged. When omitted or empty,
    the server's own registry credentials are used. An interrupted credentialed
    operation must be retried with fresh credentials.
    """

    insecure: bool
    """Allow pushing to plain-HTTP registries"""
