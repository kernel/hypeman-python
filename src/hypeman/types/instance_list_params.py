# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["InstanceListParams"]


class InstanceListParams(TypedDict, total=False):
    state: Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"]
    """Filter instances by state (e.g., Running, Stopped)"""

    tags: Dict[str, str]
    """Filter instances by tag key-value pairs.

    Uses deepObject style: ?tags[team]=backend&tags[env]=staging Multiple entries
    are ANDed together. All specified key-value pairs must match.
    """
