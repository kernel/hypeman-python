# Shared Types

```python
from hypeman.types import SnapshotCompressionConfig
```

# Health

Types:

```python
from hypeman.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/hypeman/resources/health.py">check</a>() -> <a href="./src/hypeman/types/health_check_response.py">HealthCheckResponse</a></code>

# Capabilities

Types:

```python
from hypeman.types import (
    Capabilities,
    CapabilitiesDefaultRuntime,
    CapabilitiesHost,
    CapabilitiesImages,
    CapabilitiesNetwork,
    CapabilitiesRuntime,
    CapabilitiesServer,
)
```

Methods:

- <code title="get /capabilities">client.capabilities.<a href="./src/hypeman/resources/capabilities.py">get</a>() -> <a href="./src/hypeman/types/capabilities.py">Capabilities</a></code>

# Images

Types:

```python
from hypeman.types import Image, ImageListResponse
```

Methods:

- <code title="post /images">client.images.<a href="./src/hypeman/resources/images.py">create</a>(\*\*<a href="src/hypeman/types/image_create_params.py">params</a>) -> <a href="./src/hypeman/types/image.py">Image</a></code>
- <code title="get /images">client.images.<a href="./src/hypeman/resources/images.py">list</a>(\*\*<a href="src/hypeman/types/image_list_params.py">params</a>) -> <a href="./src/hypeman/types/image_list_response.py">ImageListResponse</a></code>
- <code title="delete /images/{name}">client.images.<a href="./src/hypeman/resources/images.py">delete</a>(name) -> None</code>
- <code title="get /images/{name}">client.images.<a href="./src/hypeman/resources/images.py">get</a>(name) -> <a href="./src/hypeman/types/image.py">Image</a></code>

# Instances

Types:

```python
from hypeman.types import (
    AutoStandbyPolicy,
    AutoStandbyStatus,
    HealthCheck,
    HealthCheckExec,
    HealthCheckHTTP,
    HealthCheckTcp,
    Instance,
    InstanceHealthStatus,
    InstanceStats,
    PathInfo,
    PortMapping,
    RestartPolicy,
    RestartStatus,
    SetSnapshotScheduleRequest,
    SnapshotPolicy,
    SnapshotSchedule,
    SnapshotScheduleRetention,
    StandbyInstanceRequest,
    VolumeMount,
    WaitForStateResponse,
    InstanceListResponse,
    InstanceLogsResponse,
)
```

Methods:

- <code title="post /instances">client.instances.<a href="./src/hypeman/resources/instances/instances.py">create</a>(\*\*<a href="src/hypeman/types/instance_create_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="patch /instances/{id}">client.instances.<a href="./src/hypeman/resources/instances/instances.py">update</a>(id, \*\*<a href="src/hypeman/types/instance_update_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="get /instances">client.instances.<a href="./src/hypeman/resources/instances/instances.py">list</a>(\*\*<a href="src/hypeman/types/instance_list_params.py">params</a>) -> <a href="./src/hypeman/types/instance_list_response.py">InstanceListResponse</a></code>
- <code title="delete /instances/{id}">client.instances.<a href="./src/hypeman/resources/instances/instances.py">delete</a>(id) -> None</code>
- <code title="post /instances/{id}/fork">client.instances.<a href="./src/hypeman/resources/instances/instances.py">fork</a>(id, \*\*<a href="src/hypeman/types/instance_fork_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="get /instances/{id}">client.instances.<a href="./src/hypeman/resources/instances/instances.py">get</a>(id) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="get /instances/{id}/logs">client.instances.<a href="./src/hypeman/resources/instances/instances.py">logs</a>(id, \*\*<a href="src/hypeman/types/instance_logs_params.py">params</a>) -> str</code>
- <code title="post /instances/{id}/restore">client.instances.<a href="./src/hypeman/resources/instances/instances.py">restore</a>(id) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="post /instances/{id}/standby">client.instances.<a href="./src/hypeman/resources/instances/instances.py">standby</a>(id, \*\*<a href="src/hypeman/types/instance_standby_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="post /instances/{id}/start">client.instances.<a href="./src/hypeman/resources/instances/instances.py">start</a>(id, \*\*<a href="src/hypeman/types/instance_start_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="get /instances/{id}/stat">client.instances.<a href="./src/hypeman/resources/instances/instances.py">stat</a>(id, \*\*<a href="src/hypeman/types/instance_stat_params.py">params</a>) -> <a href="./src/hypeman/types/path_info.py">PathInfo</a></code>
- <code title="get /instances/{id}/stats">client.instances.<a href="./src/hypeman/resources/instances/instances.py">stats</a>(id) -> <a href="./src/hypeman/types/instance_stats.py">InstanceStats</a></code>
- <code title="post /instances/{id}/stop">client.instances.<a href="./src/hypeman/resources/instances/instances.py">stop</a>(id) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="get /instances/{id}/wait">client.instances.<a href="./src/hypeman/resources/instances/instances.py">wait</a>(id, \*\*<a href="src/hypeman/types/instance_wait_params.py">params</a>) -> <a href="./src/hypeman/types/wait_for_state_response.py">WaitForStateResponse</a></code>

## AutoStandby

Methods:

- <code title="post /instances/{id}/auto-standby/hold">client.instances.auto_standby.<a href="./src/hypeman/resources/instances/auto_standby.py">hold</a>(id) -> <a href="./src/hypeman/types/auto_standby_status.py">AutoStandbyStatus</a></code>
- <code title="get /instances/{id}/auto-standby/status">client.instances.auto_standby.<a href="./src/hypeman/resources/instances/auto_standby.py">status</a>(id) -> <a href="./src/hypeman/types/auto_standby_status.py">AutoStandbyStatus</a></code>

## Volumes

Methods:

- <code title="post /instances/{id}/volumes/{volumeId}">client.instances.volumes.<a href="./src/hypeman/resources/instances/volumes.py">attach</a>(volume_id, \*, id, \*\*<a href="src/hypeman/types/instances/volume_attach_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="delete /instances/{id}/volumes/{volumeId}">client.instances.volumes.<a href="./src/hypeman/resources/instances/volumes.py">detach</a>(volume_id, \*, id) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>

## Snapshots

Methods:

- <code title="post /instances/{id}/snapshots">client.instances.snapshots.<a href="./src/hypeman/resources/instances/snapshots.py">create</a>(id, \*\*<a href="src/hypeman/types/instances/snapshot_create_params.py">params</a>) -> <a href="./src/hypeman/types/snapshot.py">Snapshot</a></code>
- <code title="post /instances/{id}/snapshots/{snapshotId}/restore">client.instances.snapshots.<a href="./src/hypeman/resources/instances/snapshots.py">restore</a>(snapshot_id, \*, id, \*\*<a href="src/hypeman/types/instances/snapshot_restore_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>

## SnapshotSchedule

Methods:

- <code title="put /instances/{id}/snapshot-schedule">client.instances.snapshot_schedule.<a href="./src/hypeman/resources/instances/snapshot_schedule.py">update</a>(id, \*\*<a href="src/hypeman/types/instances/snapshot_schedule_update_params.py">params</a>) -> <a href="./src/hypeman/types/snapshot_schedule.py">SnapshotSchedule</a></code>
- <code title="delete /instances/{id}/snapshot-schedule">client.instances.snapshot_schedule.<a href="./src/hypeman/resources/instances/snapshot_schedule.py">delete</a>(id) -> None</code>
- <code title="get /instances/{id}/snapshot-schedule">client.instances.snapshot_schedule.<a href="./src/hypeman/resources/instances/snapshot_schedule.py">get</a>(id) -> <a href="./src/hypeman/types/snapshot_schedule.py">SnapshotSchedule</a></code>

# Snapshots

Types:

```python
from hypeman.types import Snapshot, SnapshotKind, SnapshotListResponse
```

Methods:

- <code title="get /snapshots">client.snapshots.<a href="./src/hypeman/resources/snapshots.py">list</a>(\*\*<a href="src/hypeman/types/snapshot_list_params.py">params</a>) -> <a href="./src/hypeman/types/snapshot_list_response.py">SnapshotListResponse</a></code>
- <code title="delete /snapshots/{snapshotId}">client.snapshots.<a href="./src/hypeman/resources/snapshots.py">delete</a>(snapshot_id) -> None</code>
- <code title="post /snapshots/{snapshotId}/fork">client.snapshots.<a href="./src/hypeman/resources/snapshots.py">fork</a>(snapshot_id, \*\*<a href="src/hypeman/types/snapshot_fork_params.py">params</a>) -> <a href="./src/hypeman/types/instance.py">Instance</a></code>
- <code title="get /snapshots/{snapshotId}">client.snapshots.<a href="./src/hypeman/resources/snapshots.py">get</a>(snapshot_id) -> <a href="./src/hypeman/types/snapshot.py">Snapshot</a></code>

# Volumes

Types:

```python
from hypeman.types import Volume, VolumeAttachment, VolumeListResponse
```

Methods:

- <code title="post /volumes">client.volumes.<a href="./src/hypeman/resources/volumes.py">create</a>(\*\*<a href="src/hypeman/types/volume_create_params.py">params</a>) -> <a href="./src/hypeman/types/volume.py">Volume</a></code>
- <code title="get /volumes">client.volumes.<a href="./src/hypeman/resources/volumes.py">list</a>(\*\*<a href="src/hypeman/types/volume_list_params.py">params</a>) -> <a href="./src/hypeman/types/volume_list_response.py">VolumeListResponse</a></code>
- <code title="delete /volumes/{id}">client.volumes.<a href="./src/hypeman/resources/volumes.py">delete</a>(id) -> None</code>
- <code title="post /volumes/from-archive">client.volumes.<a href="./src/hypeman/resources/volumes.py">create_from_archive</a>(body, \*\*<a href="src/hypeman/types/volume_create_from_archive_params.py">params</a>) -> <a href="./src/hypeman/types/volume.py">Volume</a></code>
- <code title="get /volumes/{id}">client.volumes.<a href="./src/hypeman/resources/volumes.py">get</a>(id) -> <a href="./src/hypeman/types/volume.py">Volume</a></code>

# Devices

Types:

```python
from hypeman.types import (
    AvailableDevice,
    Device,
    DeviceType,
    DeviceListResponse,
    DeviceListAvailableResponse,
)
```

Methods:

- <code title="post /devices">client.devices.<a href="./src/hypeman/resources/devices.py">create</a>(\*\*<a href="src/hypeman/types/device_create_params.py">params</a>) -> <a href="./src/hypeman/types/device.py">Device</a></code>
- <code title="get /devices/{id}">client.devices.<a href="./src/hypeman/resources/devices.py">retrieve</a>(id) -> <a href="./src/hypeman/types/device.py">Device</a></code>
- <code title="get /devices">client.devices.<a href="./src/hypeman/resources/devices.py">list</a>(\*\*<a href="src/hypeman/types/device_list_params.py">params</a>) -> <a href="./src/hypeman/types/device_list_response.py">DeviceListResponse</a></code>
- <code title="delete /devices/{id}">client.devices.<a href="./src/hypeman/resources/devices.py">delete</a>(id) -> None</code>
- <code title="get /devices/available">client.devices.<a href="./src/hypeman/resources/devices.py">list_available</a>() -> <a href="./src/hypeman/types/device_list_available_response.py">DeviceListAvailableResponse</a></code>

# Ingresses

Types:

```python
from hypeman.types import Ingress, IngressMatch, IngressRule, IngressTarget, IngressListResponse
```

Methods:

- <code title="post /ingresses">client.ingresses.<a href="./src/hypeman/resources/ingresses.py">create</a>(\*\*<a href="src/hypeman/types/ingress_create_params.py">params</a>) -> <a href="./src/hypeman/types/ingress.py">Ingress</a></code>
- <code title="get /ingresses">client.ingresses.<a href="./src/hypeman/resources/ingresses.py">list</a>(\*\*<a href="src/hypeman/types/ingress_list_params.py">params</a>) -> <a href="./src/hypeman/types/ingress_list_response.py">IngressListResponse</a></code>
- <code title="delete /ingresses/{id}">client.ingresses.<a href="./src/hypeman/resources/ingresses.py">delete</a>(id) -> None</code>
- <code title="get /ingresses/{id}">client.ingresses.<a href="./src/hypeman/resources/ingresses.py">get</a>(id) -> <a href="./src/hypeman/types/ingress.py">Ingress</a></code>

# Resources

Types:

```python
from hypeman.types import (
    DiskBreakdown,
    GPUProfile,
    GPUResourceStatus,
    MemoryReclaimAction,
    MemoryReclaimRequest,
    MemoryReclaimResponse,
    PassthroughDevice,
    ResourceAllocation,
    ResourceStatus,
    Resources,
)
```

Methods:

- <code title="get /resources">client.resources.<a href="./src/hypeman/resources/resources.py">get</a>() -> <a href="./src/hypeman/types/resources.py">Resources</a></code>
- <code title="post /resources/memory/reclaim">client.resources.<a href="./src/hypeman/resources/resources.py">reclaim_memory</a>(\*\*<a href="src/hypeman/types/resource_reclaim_memory_params.py">params</a>) -> <a href="./src/hypeman/types/memory_reclaim_response.py">MemoryReclaimResponse</a></code>

# Builders

Types:

```python
from hypeman.types import Builder, BuilderStatus, BuilderListResponse
```

Methods:

- <code title="post /builders">client.builders.<a href="./src/hypeman/resources/builders.py">create</a>(\*\*<a href="src/hypeman/types/builder_create_params.py">params</a>) -> <a href="./src/hypeman/types/builder.py">Builder</a></code>
- <code title="get /builders">client.builders.<a href="./src/hypeman/resources/builders.py">list</a>(\*\*<a href="src/hypeman/types/builder_list_params.py">params</a>) -> <a href="./src/hypeman/types/builder_list_response.py">BuilderListResponse</a></code>
- <code title="delete /builders/{id}">client.builders.<a href="./src/hypeman/resources/builders.py">delete</a>(id) -> None</code>
- <code title="get /builders/{id}">client.builders.<a href="./src/hypeman/resources/builders.py">get</a>(id) -> <a href="./src/hypeman/types/builder.py">Builder</a></code>
- <code title="post /builders/{id}/prune">client.builders.<a href="./src/hypeman/resources/builders.py">prune</a>(id) -> <a href="./src/hypeman/types/builder.py">Builder</a></code>

# Builds

Types:

```python
from hypeman.types import (
    Build,
    BuildEvent,
    BuildPolicy,
    BuildProvenance,
    BuildStatus,
    BuildListResponse,
)
```

Methods:

- <code title="post /builds">client.builds.<a href="./src/hypeman/resources/builds.py">create</a>(\*\*<a href="src/hypeman/types/build_create_params.py">params</a>) -> <a href="./src/hypeman/types/build.py">Build</a></code>
- <code title="get /builds">client.builds.<a href="./src/hypeman/resources/builds.py">list</a>(\*\*<a href="src/hypeman/types/build_list_params.py">params</a>) -> <a href="./src/hypeman/types/build_list_response.py">BuildListResponse</a></code>
- <code title="delete /builds/{id}">client.builds.<a href="./src/hypeman/resources/builds.py">cancel</a>(id) -> None</code>
- <code title="get /builds/{id}/events">client.builds.<a href="./src/hypeman/resources/builds.py">events</a>(id, \*\*<a href="src/hypeman/types/build_events_params.py">params</a>) -> <a href="./src/hypeman/types/build_event.py">BuildEvent</a></code>
- <code title="get /builds/{id}">client.builds.<a href="./src/hypeman/resources/builds.py">get</a>(id) -> <a href="./src/hypeman/types/build.py">Build</a></code>

# Pushes

Types:

```python
from hypeman.types import CreatePushRequest, Push, PushCredentials, PushStatus, PushListResponse
```

Methods:

- <code title="post /pushes">client.pushes.<a href="./src/hypeman/resources/pushes.py">create</a>(\*\*<a href="src/hypeman/types/push_create_params.py">params</a>) -> <a href="./src/hypeman/types/push.py">Push</a></code>
- <code title="get /pushes">client.pushes.<a href="./src/hypeman/resources/pushes.py">list</a>() -> <a href="./src/hypeman/types/push_list_response.py">PushListResponse</a></code>
- <code title="get /pushes/{id}">client.pushes.<a href="./src/hypeman/resources/pushes.py">get</a>(id) -> <a href="./src/hypeman/types/push.py">Push</a></code>
