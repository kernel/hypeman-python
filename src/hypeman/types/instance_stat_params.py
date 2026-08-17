# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceStatParams"]


class InstanceStatParams(TypedDict, total=False):
    path: Required[str]
    """Path to stat in the guest filesystem"""

    follow_links: bool
    """Follow symbolic links (like stat vs lstat)"""
