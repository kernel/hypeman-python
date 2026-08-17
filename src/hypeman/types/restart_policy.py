# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RestartPolicy"]


class RestartPolicy(BaseModel):
    """Whole-instance restart supervision policy."""

    backoff: Optional[str] = None
    """
    Delay before each restart attempt, expressed as a Go duration like "5s" or "1m".
    """

    max_attempts: Optional[int] = None
    """Consecutive automatic restart attempts before blocking retries.

    0 means unlimited.
    """

    policy: Optional[Literal["never", "always", "on_failure"]] = None
    """Restart behavior when the guest program exits:

    - never: do not automatically restart
    - always: restart after any guest exit
    - on_failure: restart only for nonzero, signaled, OOM, or unknown exits
    """

    stable_after: Optional[str] = None
    """Running this long resets the consecutive restart attempt count."""
