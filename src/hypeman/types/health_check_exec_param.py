# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["HealthCheckExecParam"]


class HealthCheckExecParam(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """Command and arguments to run inside the guest after guest-agent readiness."""

    working_dir: str
    """Optional working directory for the command."""
