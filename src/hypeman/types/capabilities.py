# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .capabilities_host import CapabilitiesHost
from .capabilities_images import CapabilitiesImages
from .capabilities_server import CapabilitiesServer
from .capabilities_network import CapabilitiesNetwork
from .capabilities_runtime import CapabilitiesRuntime
from .capabilities_default_runtime import CapabilitiesDefaultRuntime

__all__ = ["Capabilities"]


class Capabilities(BaseModel):
    default_runtime: CapabilitiesDefaultRuntime

    features: List[str]
    """
    Stable server-level feature IDs: API surfaces this server exposes regardless of
    which runtime backs an instance. Always present: "instances", "images",
    "builds", "volumes", "ingress", "exec", "logs". Host-conditional: "devices"
    (device passthrough management, Linux hosts only) and "rosetta-emulation" (Apple
    Silicon macOS hosts with Rosetta currently installed, per the same availability
    probe launches enforce). Per-runtime features are reported under each runtimes[]
    entry.
    """

    host: CapabilitiesHost

    images: CapabilitiesImages

    network: CapabilitiesNetwork

    runtimes: List[CapabilitiesRuntime]
    """
    Every runtime this server build supports on this host platform, each with its
    own availability flag and feature IDs. Hosts commonly support several runtimes
    at once (for example cloud-hypervisor, firecracker, qemu, and qemu-microvm on
    linux/amd64). A listed runtime is only launchable when its "available" flag is
    true. Entries are sorted by name.
    """

    server: CapabilitiesServer
