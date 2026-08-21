# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .health_check_param import HealthCheckParam
from .restart_policy_param import RestartPolicyParam
from .auto_standby_policy_param import AutoStandbyPolicyParam

__all__ = ["InstanceUpdateParams"]


class InstanceUpdateParams(TypedDict, total=False):
    auto_standby: AutoStandbyPolicyParam
    """
    Linux-only automatic standby policy based on active inbound TCP connections
    observed from the host conntrack table.
    """

    env: Dict[str, str]
    """
    Environment variables to update (merged with existing). Only keys referenced by
    the instance's existing credential `source.env` bindings are accepted. Use this
    to rotate real credential values without restarting the VM.
    """

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Absolute expiration time.

    Must be in the future and is mutually exclusive with ttl.
    """

    health_check: HealthCheckParam
    """Workload health check policy.

    Health is reported separately from instance lifecycle state.
    """

    restart_policy: RestartPolicyParam
    """Whole-instance restart supervision policy."""

    ttl: str
    """Relative lifetime from when this update is committed, in Go duration format.

    Use "0s" to disable automatic expiration. Mutually exclusive with expires_at.
    """
