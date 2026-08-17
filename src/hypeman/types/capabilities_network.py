# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CapabilitiesNetwork"]


class CapabilitiesNetwork(BaseModel):
    guest_to_guest: bool
    """Whether direct VM-to-VM traffic is permitted on the default network"""

    model: Literal["bridge", "nat"]
    """Guest networking model.

    "bridge" is a Linux bridge with per-VM TAP devices; "nat" is hypervisor-provided
    NAT (macOS).
    """

    gateway: Optional[str] = None
    """Guest-visible host gateway IP.

    Guests reach host services (including host ingress) through this address.
    Omitted when no default network has been resolved on this host yet.
    """

    subnet: Optional[str] = None
    """Guest subnet CIDR"""
