# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    tags: Dict[str, str]
    """Filter devices by tag key-value pairs."""
