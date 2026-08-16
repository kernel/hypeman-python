# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .health_check_param import HealthCheckParam
from .volume_mount_param import VolumeMountParam
from .restart_policy_param import RestartPolicyParam
from .snapshot_policy_param import SnapshotPolicyParam
from .auto_standby_policy_param import AutoStandbyPolicyParam

__all__ = [
    "InstanceCreateParams",
    "Credentials",
    "CredentialsInject",
    "CredentialsInjectAs",
    "CredentialsSource",
    "GPU",
    "Network",
    "NetworkEgress",
    "NetworkEgressEnforcement",
]


class InstanceCreateParams(TypedDict, total=False):
    image: Required[str]
    """OCI image reference"""

    name: Required[str]
    """
    Human-readable name (lowercase letters, digits, and dashes only; cannot start or
    end with a dash)
    """

    auto_standby: AutoStandbyPolicyParam
    """
    Linux-only automatic standby policy based on active inbound TCP connections
    observed from the host conntrack table.
    """

    cmd: SequenceNotStr[str]
    """Override image CMD (like docker run <image> <command>).

    Omit to use image default.
    """

    credentials: Dict[str, Credentials]
    """
    Host-managed credential brokering policies keyed by guest-visible env var name.
    Those guest env vars receive mock placeholder values, while the real values
    remain host-scoped in the request `env` map and are only materialized on the
    mediated egress path according to each credential's `source` and `inject` rules.
    """

    devices: SequenceNotStr[str]
    """Device IDs or names to attach for GPU/PCI passthrough"""

    disk_io_bps: str
    """Disk I/O rate limit (e.g., "100MB/s", "500MB/s").

    Defaults to proportional share based on CPU allocation if configured.
    """

    entrypoint: SequenceNotStr[str]
    """Override image entrypoint (like docker run --entrypoint).

    Omit to use image default.
    """

    env: Dict[str, str]
    """Environment variables"""

    gpu: GPU
    """GPU configuration for the instance"""

    health_check: HealthCheckParam
    """Workload health check policy.

    Health is reported separately from instance lifecycle state.
    """

    hotplug_size: str
    """Additional memory for hotplug (human-readable format like "3GB", "1G").

    Omit to disable hotplug memory.
    """

    hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"]
    """Hypervisor backend to use for this instance.

    qemu uses the architecture-native standard board; qemu-microvm uses QEMU's
    minimal Linux amd64 board and does not support PCI devices, hotplug memory, or
    more than eight virtio-mmio devices. Defaults to server configuration.
    """

    network: Network
    """Network configuration for the instance"""

    overlay_size: str
    """Writable overlay disk size (human-readable format like "10GB", "50G")"""

    platform: str
    """Target platform as os/arch[/variant] (e.g.

    "linux/amd64"), matching Docker --platform. Omit for the host platform. Not a
    fixed enum: the os/arch[/variant] grammar is validated server-side and invalid
    values return 400 invalid_platform. Only os "linux" with arch amd64 or arm64 is
    accepted today.
    """

    restart_policy: RestartPolicyParam
    """Whole-instance restart supervision policy."""

    size: str
    """Base memory size (human-readable format like "1GB", "512MB", "2G")"""

    skip_guest_agent: bool
    """
    Skip guest-agent installation during boot. When true, the exec and stat APIs
    will not work for this instance. The instance will still run, but remote command
    execution will be unavailable.
    """

    skip_kernel_headers: bool
    """
    Skip kernel headers installation during boot for faster startup. When true, DKMS
    (Dynamic Kernel Module Support) will not work, preventing compilation of
    out-of-tree kernel modules (e.g., NVIDIA vGPU drivers). Recommended for
    workloads that don't need kernel module compilation.
    """

    snapshot_policy: SnapshotPolicyParam
    """Snapshot policy for this instance.

    Controls compression settings applied when creating snapshots or entering
    standby, plus any default standby-only compression delay.
    """

    tags: Dict[str, str]
    """User-defined key-value tags."""

    vcpus: int
    """Number of virtual CPUs"""

    volumes: Iterable[VolumeMountParam]
    """Volumes to attach to the instance at creation time"""


class CredentialsInjectAs(TypedDict, total=False):
    """Current v1 transform shape.

    Header templating is supported now; other transform
    types (for example request signing) can be added in future revisions.
    """

    format: Required[str]
    """Template that must include `${value}`."""

    header: Required[str]
    """Header name to set/mutate for matching outbound requests."""


_CredentialsInjectReservedKeywords = TypedDict(
    "_CredentialsInjectReservedKeywords",
    {
        "as": CredentialsInjectAs,
    },
    total=False,
)


class CredentialsInject(_CredentialsInjectReservedKeywords, total=False):
    hosts: SequenceNotStr[str]
    """
    Optional destination host patterns (`api.example.com`, `*.example.com`). Omit to
    allow injection on all destinations.
    """


class CredentialsSource(TypedDict, total=False):
    env: Required[str]
    """
    Name of the real credential in the request `env` map. The guest-visible env var
    key can receive a mock placeholder, while the mediated egress path resolves that
    placeholder back to this real value only on the host.
    """


class Credentials(TypedDict, total=False):
    inject: Required[Iterable[CredentialsInject]]

    source: Required[CredentialsSource]


class GPU(TypedDict, total=False):
    """GPU configuration for the instance"""

    profile: str
    """vGPU profile name (e.g., "L40S-1Q"). Only used in vGPU mode."""


class NetworkEgressEnforcement(TypedDict, total=False):
    """Egress enforcement policy applied when mediation is enabled."""

    mode: Literal["all", "http_https_only"]
    """
    `all` (default) rejects direct non-mediated TCP egress from the VM, while
    `http_https_only` rejects direct egress only on TCP ports 80 and 443.
    """


class NetworkEgress(TypedDict, total=False):
    """
    Host-mediated outbound network policy.
    Omit this object, or set `enabled: false`, to preserve normal direct outbound networking
    when `network.enabled` is true.
    """

    enabled: bool
    """
    Whether to enable the mediated egress path. When false or omitted, the instance
    keeps normal direct outbound networking and host-managed credential rewriting is
    disabled.
    """

    enforcement: NetworkEgressEnforcement
    """Egress enforcement policy applied when mediation is enabled."""


class Network(TypedDict, total=False):
    """Network configuration for the instance"""

    bandwidth_download: str
    """Download bandwidth limit (external→VM, e.g., "1Gbps", "125MB/s").

    Defaults to proportional share based on CPU allocation.
    """

    bandwidth_upload: str
    """Upload bandwidth limit (VM→external, e.g., "1Gbps", "125MB/s").

    Defaults to proportional share based on CPU allocation.
    """

    egress: NetworkEgress
    """
    Host-mediated outbound network policy. Omit this object, or set
    `enabled: false`, to preserve normal direct outbound networking when
    `network.enabled` is true.
    """

    enabled: bool
    """Whether to attach instance to the default network"""
