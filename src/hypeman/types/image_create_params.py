# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .push_credentials_param import PushCredentialsParam

__all__ = ["ImageCreateParams"]


class ImageCreateParams(TypedDict, total=False):
    name: Required[str]
    """OCI image reference (e.g., docker.io/library/nginx:latest)"""

    credentials: PushCredentialsParam
    """Docker-style registry credentials borrowed for one image pull or push request.

    They remain in memory and are never persisted or logged. When omitted or empty,
    the server's own registry credentials are used. An interrupted credentialed
    operation must be retried with fresh credentials.
    """

    platform: str
    """Target platform as os/arch[/variant] (e.g.

    "linux/amd64"), matching Docker --platform. Omit for the host platform. Not a
    fixed enum: the os/arch[/variant] grammar is validated server-side and invalid
    values return 400 invalid_platform. Only os "linux" with arch amd64 or arm64 is
    accepted today.
    """

    tags: Dict[str, str]
    """User-defined key-value tags."""
