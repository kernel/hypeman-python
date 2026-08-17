# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AvailableDevice"]


class AvailableDevice(BaseModel):
    device_id: str
    """PCI device ID (hex)"""

    iommu_group: int
    """IOMMU group number"""

    pci_address: str
    """PCI address"""

    vendor_id: str
    """PCI vendor ID (hex)"""

    current_driver: Optional[str] = None
    """Currently bound driver (null if none)"""

    device_name: Optional[str] = None
    """Human-readable device name"""

    vendor_name: Optional[str] = None
    """Human-readable vendor name"""
