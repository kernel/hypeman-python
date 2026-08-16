# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IngressTargetParam"]


class IngressTargetParam(TypedDict, total=False):
    instance: Required[str]
    """Target instance name, ID, or capture reference.

    - For literal hostnames: Use the instance name or ID directly (e.g., "my-api")
    - For pattern hostnames: Reference a capture from the hostname (e.g.,
      "{instance}")

    When using pattern hostnames, the instance is resolved dynamically at request
    time.
    """

    port: Required[int]
    """Target port on the instance"""
