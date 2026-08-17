# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PushStatus"]

PushStatus: TypeAlias = Literal["queued", "pushing", "pushed", "failed"]
