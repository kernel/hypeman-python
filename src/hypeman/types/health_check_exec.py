# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["HealthCheckExec"]


class HealthCheckExec(BaseModel):
    command: List[str]
    """Command and arguments to run inside the guest after guest-agent readiness."""

    working_dir: Optional[str] = None
    """Optional working directory for the command."""
