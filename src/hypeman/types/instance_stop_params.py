# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstanceStopParams"]


class InstanceStopParams(TypedDict, total=False):
    force: bool
    """Power the VM off without asking the guest to shut down.

    Use when the guest state will be discarded, for example before restoring a
    snapshot. A forced stop of a macOS guest is never graceful, so it cannot be used
    for a stopped snapshot or fork until the guest is booted and stopped gracefully
    again.
    """
