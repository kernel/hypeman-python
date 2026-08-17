# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CapabilitiesRuntime"]


class CapabilitiesRuntime(BaseModel):
    available: bool
    """Whether this runtime's launch prerequisites are currently met on this host.

    Listed runtimes are supported by this server build on this platform;
    available=false means a host prerequisite is missing (for example qemu requires
    a runnable system-installed QEMU binary and the host vhost-vsock device) and
    launches naming this runtime will fail until it is installed.
    """

    features: List[str]
    """
    Stable feature IDs supported by this runtime on this host: "snapshots"
    (snapshot/restore), "standby" (pause + memory snapshot, with later restore),
    "fork" (clone an instance from a stopped source; forking a standby or running
    source restores/creates snapshots and additionally requires "standby"), "pause"
    (pause/resume), "hotplug-memory" (live memory resize), "balloon-control"
    (runtime balloon target changes), "vsock" (guest vsock communication),
    "gpu-passthrough" (GPU/PCI device passthrough), "disk-io-limit" (disk I/O rate
    limiting), "disk-resize" (live disk resize). Values are host- and
    configuration-truthful: vz omits snapshots and standby on macOS 13, which lacks
    Virtualization.framework VM save/restore, while still advertising fork
    (stopped-source clones need no save/restore there), and cloud-hypervisor reports
    "disk-resize" only when the configured default version supports it.
    """

    name: str
    """Runtime identifier"""
