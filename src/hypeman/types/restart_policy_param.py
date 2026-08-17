# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RestartPolicyParam"]


class RestartPolicyParam(TypedDict, total=False):
    """Whole-instance restart supervision policy."""

    backoff: str
    """
    Delay before each restart attempt, expressed as a Go duration like "5s" or "1m".
    """

    max_attempts: int
    """Consecutive automatic restart attempts before blocking retries.

    0 means unlimited.
    """

    policy: Literal["never", "always", "on_failure"]
    """Restart behavior when the guest program exits:

    - never: do not automatically restart
    - always: restart after any guest exit
    - on_failure: restart only for nonzero, signaled, OOM, or unknown exits
    """

    stable_after: str
    """Running this long resets the consecutive restart attempt count."""
