# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .health_check_tcp_param import HealthCheckTcpParam
from .health_check_exec_param import HealthCheckExecParam
from .health_check_http_param import HealthCheckHTTPParam

__all__ = ["HealthCheckParam"]


class HealthCheckParam(TypedDict, total=False):
    """Workload health check policy.

    Health is reported separately from instance lifecycle state.
    """

    exec: HealthCheckExecParam

    failure_threshold: int
    """Consecutive failed checks required to mark the workload unhealthy."""

    http: HealthCheckHTTPParam

    interval: str
    """Delay between checks as a Go duration."""

    start_period: str
    """Startup grace period before failures can mark the workload unhealthy."""

    success_threshold: int
    """Consecutive successful checks required to mark the workload healthy."""

    tcp: HealthCheckTcpParam

    timeout: str
    """Per-check timeout as a Go duration."""

    type: Literal["none", "http", "tcp", "exec"]
    """Probe type. Omit health_check or set type=none to disable health checks."""
