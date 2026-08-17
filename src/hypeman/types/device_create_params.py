# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["DeviceCreateParams"]


class DeviceCreateParams(TypedDict, total=False):
    pci_address: Required[str]
    """PCI address of the device (required, e.g., "0000:a2:00.0")"""

    name: str
    """Optional globally unique device name.

    If not provided, a name is auto-generated from the PCI address (e.g.,
    "pci-0000-a2-00-0")
    """

    tags: Dict[str, str]
    """User-defined key-value tags."""
