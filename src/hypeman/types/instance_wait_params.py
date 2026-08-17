# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InstanceWaitParams"]


class InstanceWaitParams(TypedDict, total=False):
    state: Required[
        Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"]
    ]
    """Target state to wait for"""

    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """Maximum duration to wait (Go duration format, e.g.

    "30s", "2m"). Capped at 5 minutes. Defaults to 60 seconds.
    """
