# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstanceDeleteParams"]


class InstanceDeleteParams(TypedDict, total=False):
    graceful_shutdown: bool
    """Whether to attempt graceful guest shutdown before deleting the instance"""
