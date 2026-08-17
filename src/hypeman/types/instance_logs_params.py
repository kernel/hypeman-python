# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InstanceLogsParams"]


class InstanceLogsParams(TypedDict, total=False):
    follow: bool
    """Continue streaming new lines after initial output"""

    source: Literal["app", "vmm", "hypeman"]
    """Log source to stream:

    - app: Guest application logs (serial console output)
    - vmm: Cloud Hypervisor VMM logs (hypervisor stdout+stderr)
    - hypeman: Hypeman operations log (actions taken on this instance)
    """

    tail: int
    """Number of lines to return from end"""
