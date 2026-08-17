# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .device_type import DeviceType

__all__ = ["Device"]


class Device(BaseModel):
    id: str
    """Auto-generated unique identifier (CUID2 format)"""

    bound_to_vfio: bool
    """
    Whether the device is currently bound to the vfio-pci driver, which is required
    for VM passthrough.

    - true: Device is bound to vfio-pci and ready for (or currently in use by) a VM.
      The device's native driver has been unloaded.
    - false: Device is using its native driver (e.g., nvidia) or no driver. Hypeman
      will automatically bind to vfio-pci when attaching to an instance.
    """

    created_at: datetime
    """Registration timestamp (RFC3339)"""

    device_id: str
    """PCI device ID (hex)"""

    iommu_group: int
    """IOMMU group number"""

    pci_address: str
    """PCI address"""

    type: DeviceType
    """Type of PCI device"""

    vendor_id: str
    """PCI vendor ID (hex)"""

    attached_to: Optional[str] = None
    """Instance ID if attached"""

    name: Optional[str] = None
    """Device name (user-provided or auto-generated from PCI address)"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""
