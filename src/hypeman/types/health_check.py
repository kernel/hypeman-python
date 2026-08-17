# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .health_check_tcp import HealthCheckTcp
from .health_check_exec import HealthCheckExec
from .health_check_http import HealthCheckHTTP

__all__ = ["HealthCheck"]


class HealthCheck(BaseModel):
    """Workload health check policy.

    Health is reported separately from instance lifecycle state.
    """

    exec: Optional[HealthCheckExec] = None

    failure_threshold: Optional[int] = None
    """Consecutive failed checks required to mark the workload unhealthy."""

    http: Optional[HealthCheckHTTP] = None

    interval: Optional[str] = None
    """Delay between checks as a Go duration."""

    start_period: Optional[str] = None
    """Startup grace period before failures can mark the workload unhealthy."""

    success_threshold: Optional[int] = None
    """Consecutive successful checks required to mark the workload healthy."""

    tcp: Optional[HealthCheckTcp] = None

    timeout: Optional[str] = None
    """Per-check timeout as a Go duration."""

    type: Optional[Literal["none", "http", "tcp", "exec"]] = None
    """Probe type. Omit health_check or set type=none to disable health checks."""
