# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .health_check import HealthCheck
from .volume_mount import VolumeMount
from .restart_policy import RestartPolicy
from .restart_status import RestartStatus
from .snapshot_policy import SnapshotPolicy
from .auto_standby_policy import AutoStandbyPolicy
from .instance_health_status import InstanceHealthStatus

__all__ = ["Instance", "GPU", "Network"]


class GPU(BaseModel):
    """GPU information attached to the instance"""

    device_path: Optional[str] = None
    """sysfs path of the assigned vGPU device"""

    mdev_uuid: Optional[str] = None
    """mdev device UUID (mdev hosts only)"""

    profile: Optional[str] = None
    """vGPU profile name"""


class Network(BaseModel):
    """Network configuration of the instance"""

    bandwidth_download: Optional[str] = None
    """Download bandwidth limit (human-readable, e.g., "1Gbps", "125MB/s")"""

    bandwidth_upload: Optional[str] = None
    """Upload bandwidth limit (human-readable, e.g., "1Gbps", "125MB/s")"""

    enabled: Optional[bool] = None
    """Whether instance is attached to the default network"""

    ip: Optional[str] = None
    """Assigned IP address (null if no network)"""

    mac: Optional[str] = None
    """Assigned MAC address (null if no network)"""

    name: Optional[str] = None
    """Network name (always "default" when enabled)"""


class Instance(BaseModel):
    id: str
    """Auto-generated unique identifier (CUID2 format)"""

    created_at: datetime
    """Creation timestamp (RFC3339)"""

    expires_at: Optional[datetime] = None
    """Absolute expiration time, or null when automatic expiration is disabled.

    Instance TTL is cleared on fork.
    """

    image: str
    """OCI image reference"""

    name: str
    """Human-readable name"""

    state: Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"]
    """Instance state:

    - Created: VMM created but not started (Cloud Hypervisor native)
    - Initializing: VM is running while guest init is still in progress
    - Running: Guest program has started and instance is ready
    - Paused: VM is paused (Cloud Hypervisor native)
    - Shutdown: VM shut down but VMM exists (Cloud Hypervisor native)
    - Stopped: No VMM running, no snapshot exists
    - Standby: No VMM running, snapshot exists (can be restored)
    - Unknown: Failed to determine state (see state_error for details)
    """

    auto_standby: Optional[AutoStandbyPolicy] = None
    """
    Linux-only automatic standby policy based on active inbound TCP connections
    observed from the host conntrack table.
    """

    current_phase: Optional[str] = None
    """The lifecycle phase the instance is currently in."""

    current_phase_since: Optional[datetime] = None
    """When the instance entered current_phase."""

    disk_io_bps: Optional[str] = None
    """Disk I/O rate limit (human-readable, e.g., "100MB/s")"""

    env: Optional[Dict[str, str]] = None
    """Environment variables"""

    exit_code: Optional[int] = None
    """App exit code (null if VM hasn't exited)"""

    exit_message: Optional[str] = None
    """
    Human-readable description of exit (e.g., "command not found", "killed by signal
    9 (SIGKILL) - OOM")
    """

    gpu: Optional[GPU] = None
    """GPU information attached to the instance"""

    has_snapshot: Optional[bool] = None
    """Whether a snapshot exists for this instance"""

    health_check: Optional[HealthCheck] = None
    """Workload health check policy.

    Health is reported separately from instance lifecycle state.
    """

    health_status: Optional[InstanceHealthStatus] = None

    hotplug_size: Optional[str] = None
    """Hotplug memory size (human-readable)"""

    hypervisor: Optional[Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"]] = None
    """Hypervisor backend running this instance"""

    network: Optional[Network] = None
    """Network configuration of the instance"""

    overlay_size: Optional[str] = None
    """Writable overlay disk size (human-readable)"""

    phase_durations_ms: Optional[Dict[str, int]] = None
    """
    Cumulative milliseconds the instance has spent in each lifecycle phase,
    including time accrued in the current phase up to the response time. Keys mirror
    instance states lowercased (running, standby, paused, stopped, created,
    initializing, shutdown). Consumers (e.g. billing) sum the phases they consider
    billable.
    """

    platform: Optional[str] = None
    """Resolved image platform as os/arch[/variant] (e.g.

    "linux/amd64"). amd64 images on an arm64 host run under Rosetta emulation.
    """

    restart_policy: Optional[RestartPolicy] = None
    """Whole-instance restart supervision policy."""

    restart_status: Optional[RestartStatus] = None
    """Runtime status for restart policy decisions."""

    size: Optional[str] = None
    """Base memory size (human-readable)"""

    snapshot_policy: Optional[SnapshotPolicy] = None

    started_at: Optional[datetime] = None
    """Start timestamp (RFC3339)"""

    state_error: Optional[str] = None
    """Error message if state couldn't be determined (only set when state is Unknown)"""

    stopped_at: Optional[datetime] = None
    """Stop timestamp (RFC3339)"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""

    vcpus: Optional[int] = None
    """Number of virtual CPUs"""

    volumes: Optional[List[VolumeMount]] = None
    """Volumes attached to the instance"""
