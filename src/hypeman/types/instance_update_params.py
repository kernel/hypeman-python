# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

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

    health_check: HealthCheckParam
    """Workload health check policy.

    Health is reported separately from instance lifecycle state.
    """

    restart_policy: RestartPolicyParam
    """Whole-instance restart supervision policy."""
