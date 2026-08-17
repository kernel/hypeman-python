# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["InstanceStartParams"]


class InstanceStartParams(TypedDict, total=False):
    cmd: SequenceNotStr[str]
    """Override image CMD for this run. Omit to keep previous value."""

    entrypoint: SequenceNotStr[str]
    """Override image entrypoint for this run. Omit to keep previous value."""
