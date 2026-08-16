# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BuildEventsParams"]


class BuildEventsParams(TypedDict, total=False):
    follow: bool
    """Continue streaming new events after initial output"""
