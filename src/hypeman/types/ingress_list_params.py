# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["IngressListParams"]


class IngressListParams(TypedDict, total=False):
    tags: Dict[str, str]
    """Filter ingresses by tag key-value pairs."""
