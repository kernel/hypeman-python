# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["BuildStatus"]

BuildStatus: TypeAlias = Literal["queued", "building", "pushing", "ready", "failed", "cancelled"]
