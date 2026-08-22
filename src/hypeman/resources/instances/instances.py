# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    instance_fork_params,
    instance_list_params,
    instance_logs_params,
    instance_stat_params,
    instance_wait_params,
    instance_start_params,
    instance_create_params,
    instance_update_params,
    instance_standby_params,
)
from .volumes import (
    VolumesResource,
    AsyncVolumesResource,
    VolumesResourceWithRawResponse,
    AsyncVolumesResourceWithRawResponse,
    VolumesResourceWithStreamingResponse,
    AsyncVolumesResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .snapshots import (
    SnapshotsResource,
    AsyncSnapshotsResource,
    SnapshotsResourceWithRawResponse,
    AsyncSnapshotsResourceWithRawResponse,
    SnapshotsResourceWithStreamingResponse,
    AsyncSnapshotsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from .auto_standby import (
    AutoStandbyResource,
    AsyncAutoStandbyResource,
    AutoStandbyResourceWithRawResponse,
    AsyncAutoStandbyResourceWithRawResponse,
    AutoStandbyResourceWithStreamingResponse,
    AsyncAutoStandbyResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.instance import Instance
from ...types.path_info import PathInfo
from .snapshot_schedule import (
    SnapshotScheduleResource,
    AsyncSnapshotScheduleResource,
    SnapshotScheduleResourceWithRawResponse,
    AsyncSnapshotScheduleResourceWithRawResponse,
    SnapshotScheduleResourceWithStreamingResponse,
    AsyncSnapshotScheduleResourceWithStreamingResponse,
)
from ...types.instance_stats import InstanceStats
from ...types.health_check_param import HealthCheckParam
from ...types.volume_mount_param import VolumeMountParam
from ...types.restart_policy_param import RestartPolicyParam
from ...types.snapshot_policy_param import SnapshotPolicyParam
from ...types.instance_list_response import InstanceListResponse
from ...types.instance_logs_response import InstanceLogsResponse
from ...types.wait_for_state_response import WaitForStateResponse
from ...types.auto_standby_policy_param import AutoStandbyPolicyParam
from ...types.shared_params.snapshot_compression_config import SnapshotCompressionConfig

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def auto_standby(self) -> AutoStandbyResource:
        return AutoStandbyResource(self._client)

    @cached_property
    def volumes(self) -> VolumesResource:
        return VolumesResource(self._client)

    @cached_property
    def snapshots(self) -> SnapshotsResource:
        return SnapshotsResource(self._client)

    @cached_property
    def snapshot_schedule(self) -> SnapshotScheduleResource:
        return SnapshotScheduleResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image: str,
        name: str,
        auto_standby: AutoStandbyPolicyParam | Omit = omit,
        cmd: SequenceNotStr[str] | Omit = omit,
        credentials: Dict[str, instance_create_params.Credentials] | Omit = omit,
        devices: SequenceNotStr[str] | Omit = omit,
        disk_io_bps: str | Omit = omit,
        entrypoint: SequenceNotStr[str] | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        gpu: instance_create_params.GPU | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        hotplug_size: str | Omit = omit,
        hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"] | Omit = omit,
        network: instance_create_params.Network | Omit = omit,
        overlay_size: str | Omit = omit,
        platform: str | Omit = omit,
        restart_policy: RestartPolicyParam | Omit = omit,
        size: str | Omit = omit,
        skip_guest_agent: bool | Omit = omit,
        skip_kernel_headers: bool | Omit = omit,
        snapshot_policy: SnapshotPolicyParam | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        ttl: str | Omit = omit,
        vcpus: int | Omit = omit,
        volumes: Iterable[VolumeMountParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Create and start instance

        Args:
          image: OCI image reference

          name: Human-readable name (lowercase letters, digits, and dashes only; cannot start or
              end with a dash)

          auto_standby: Linux-only automatic standby policy based on active inbound TCP connections
              observed from the host conntrack table.

          cmd: Override image CMD (like docker run <image> <command>). Omit to use image
              default.

          credentials: Host-managed credential brokering policies keyed by guest-visible env var name.
              Those guest env vars receive mock placeholder values, while the real values
              remain host-scoped in the request `env` map and are only materialized on the
              mediated egress path according to each credential's `source` and `inject` rules.

          devices: Device IDs or names to attach for GPU/PCI passthrough

          disk_io_bps: Disk I/O rate limit (e.g., "100MB/s", "500MB/s"). Defaults to proportional share
              based on CPU allocation if configured.

          entrypoint: Override image entrypoint (like docker run --entrypoint). Omit to use image
              default.

          env: Environment variables

          expires_at: Absolute expiration time. Must be in the future and is mutually exclusive with
              ttl.

          gpu: GPU configuration for the instance

          health_check: Workload health check policy. Health is reported separately from instance
              lifecycle state.

          hotplug_size: Additional memory for hotplug (human-readable format like "3GB", "1G"). Omit to
              disable hotplug memory.

          hypervisor: Hypervisor backend to use for this instance. qemu uses the architecture-native
              standard board; qemu-microvm uses QEMU's minimal Linux amd64 board and does not
              support PCI devices, hotplug memory, or more than eight virtio-mmio devices.
              Defaults to server configuration.

          network: Network configuration for the instance

          overlay_size: Writable overlay disk size (human-readable format like "10GB", "50G")

          platform: Target platform as os/arch[/variant] (e.g. "linux/amd64"), matching Docker
              --platform. Omit for the host platform. Not a fixed enum: the os/arch[/variant]
              grammar is validated server-side and invalid values return 400 invalid_platform.
              Only os "linux" with arch amd64 or arm64 is accepted today.

          restart_policy: Whole-instance restart supervision policy.

          size: Base memory size (human-readable format like "1GB", "512MB", "2G")

          skip_guest_agent: Skip guest-agent installation during boot. When true, the exec and stat APIs
              will not work for this instance. The instance will still run, but remote command
              execution will be unavailable.

          skip_kernel_headers: Skip kernel headers installation during boot for faster startup. When true, DKMS
              (Dynamic Kernel Module Support) will not work, preventing compilation of
              out-of-tree kernel modules (e.g., NVIDIA vGPU drivers). Recommended for
              workloads that don't need kernel module compilation.

          snapshot_policy: Snapshot policy for this instance. Controls compression settings applied when
              creating snapshots or entering standby, plus any default standby-only
              compression delay.

          tags: User-defined key-value tags.

          ttl: Relative lifetime from instance creation, in Go duration format. Use "0s" or
              omit both expiration fields to disable automatic expiration. Mutually exclusive
              with expires_at.

          vcpus: Number of virtual CPUs

          volumes: Volumes to attach to the instance at creation time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/instances",
            body=maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "auto_standby": auto_standby,
                    "cmd": cmd,
                    "credentials": credentials,
                    "devices": devices,
                    "disk_io_bps": disk_io_bps,
                    "entrypoint": entrypoint,
                    "env": env,
                    "expires_at": expires_at,
                    "gpu": gpu,
                    "health_check": health_check,
                    "hotplug_size": hotplug_size,
                    "hypervisor": hypervisor,
                    "network": network,
                    "overlay_size": overlay_size,
                    "platform": platform,
                    "restart_policy": restart_policy,
                    "size": size,
                    "skip_guest_agent": skip_guest_agent,
                    "skip_kernel_headers": skip_kernel_headers,
                    "snapshot_policy": snapshot_policy,
                    "tags": tags,
                    "ttl": ttl,
                    "vcpus": vcpus,
                    "volumes": volumes,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def update(
        self,
        id: str,
        *,
        auto_standby: AutoStandbyPolicyParam | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        restart_policy: RestartPolicyParam | Omit = omit,
        ttl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """Update mutable instance properties.

        TTL values are relative to when the update
        is committed. Expiration updates are rejected after the current deadline passes.

        Args:
          auto_standby: Linux-only automatic standby policy based on active inbound TCP connections
              observed from the host conntrack table.

          env: Environment variables to update (merged with existing). Only keys referenced by
              the instance's existing credential `source.env` bindings are accepted. Use this
              to rotate real credential values without restarting the VM.

          expires_at: Absolute expiration time. Must be in the future and is mutually exclusive with
              ttl.

          health_check: Workload health check policy. Health is reported separately from instance
              lifecycle state.

          restart_policy: Whole-instance restart supervision policy.

          ttl: Relative lifetime from when this update is committed, in Go duration format. Use
              "0s" to disable automatic expiration. Mutually exclusive with expires_at.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/instances/{id}", id=id),
            body=maybe_transform(
                {
                    "auto_standby": auto_standby,
                    "env": env,
                    "expires_at": expires_at,
                    "health_check": health_check,
                    "restart_policy": restart_policy,
                    "ttl": ttl,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def list(
        self,
        *,
        state: Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"]
        | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceListResponse:
        """
        List instances

        Args:
          state: Filter instances by state (e.g., Running, Stopped)

          tags:
              Filter instances by tag key-value pairs. Uses deepObject style:
              ?tags[team]=backend&tags[env]=staging Multiple entries are ANDed together. All
              specified key-value pairs must match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "state": state,
                        "tags": tags,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            cast_to=InstanceListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop and delete instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/instances/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def fork(
        self,
        id: str,
        *,
        name: str,
        from_running: bool | Omit = omit,
        target_state: Literal["Stopped", "Standby", "Running"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Fork an instance from stopped, standby, or running (with from_running=true)

        Args:
          name: Name for the forked instance (lowercase letters, digits, and dashes only; cannot
              start or end with a dash)

          from_running: Allow forking from a running source instance. When true and source is Running,
              the source is put into standby, forked, then restored back to Running.

          target_state: Optional final state for the forked instance. Default is the source instance
              state at fork time. For example, forking from Running defaults the fork result
              to Running.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/instances/{id}/fork", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "from_running": from_running,
                    "target_state": target_state,
                },
                instance_fork_params.InstanceForkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Get instance details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/instances/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def logs(
        self,
        id: str,
        *,
        follow: bool | Omit = omit,
        source: Literal["app", "vmm", "hypeman"] | Omit = omit,
        tail: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[InstanceLogsResponse]:
        """Streams instance logs as Server-Sent Events.

        Use the `source` parameter to
        select which log to stream:

        - `app` (default): Guest application logs (serial console)
        - `vmm`: Cloud Hypervisor VMM logs
        - `hypeman`: Hypeman operations log

        Returns the last N lines (controlled by `tail` parameter), then optionally
        continues streaming new lines if `follow=true`.

        Args:
          follow: Continue streaming new lines after initial output

          source:
              Log source to stream:

              - app: Guest application logs (serial console output)
              - vmm: Cloud Hypervisor VMM logs (hypervisor stdout+stderr)
              - hypeman: Hypeman operations log (actions taken on this instance)

          tail: Number of lines to return from end

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/instances/{id}/logs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "follow": follow,
                        "source": source,
                        "tail": tail,
                    },
                    instance_logs_params.InstanceLogsParams,
                ),
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[InstanceLogsResponse],
        )

    def restore(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Restore instance from standby

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/instances/{id}/restore", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def standby(
        self,
        id: str,
        *,
        compression: SnapshotCompressionConfig | Omit = omit,
        compression_delay: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Put instance in standby (pause, snapshot, delete VMM)

        Args:
          compression: Compression settings for standby snapshot memory. Overrides instance defaults.

          compression_delay: Delay before standby snapshot compression begins, expressed as a Go duration
              like "30s" or "5m". Overrides the instance default for this standby operation
              only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/instances/{id}/standby", id=id),
            body=maybe_transform(
                {
                    "compression": compression,
                    "compression_delay": compression_delay,
                },
                instance_standby_params.InstanceStandbyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def start(
        self,
        id: str,
        *,
        cmd: SequenceNotStr[str] | Omit = omit,
        entrypoint: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """Start a stopped instance

        Args:
          cmd: Override image CMD for this run.

        Omit to keep previous value.

          entrypoint: Override image entrypoint for this run. Omit to keep previous value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/instances/{id}/start", id=id),
            body=maybe_transform(
                {
                    "cmd": cmd,
                    "entrypoint": entrypoint,
                },
                instance_start_params.InstanceStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def stat(
        self,
        id: str,
        *,
        path: str,
        follow_links: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PathInfo:
        """Returns information about a path in the guest filesystem.

        Useful for checking if
        a path exists, its type, and permissions before performing file operations.

        Args:
          path: Path to stat in the guest filesystem

          follow_links: Follow symbolic links (like stat vs lstat)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/instances/{id}/stat", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "follow_links": follow_links,
                    },
                    instance_stat_params.InstanceStatParams,
                ),
            ),
            cast_to=PathInfo,
        )

    def stats(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceStats:
        """
        Returns real-time resource utilization statistics for a running VM instance.
        Metrics are collected from /proc/<pid>/stat and /proc/<pid>/statm for CPU and
        memory, and from TAP interface statistics for network I/O.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/instances/{id}/stats", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceStats,
        )

    def stop(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Stop instance (graceful shutdown)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/instances/{id}/stop", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def wait(
        self,
        id: str,
        *,
        state: Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"],
        api_timeout: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaitForStateResponse:
        """
        Blocks until the instance reaches the specified target state, the timeout
        expires, or the instance enters a terminal/error state. Useful for avoiding
        client-side polling when waiting for state transitions (e.g. waiting for an
        instance to become Running).

        Args:
          state: Target state to wait for

          api_timeout: Maximum duration to wait (Go duration format, e.g. "30s", "2m"). Capped at 5
              minutes. Defaults to 60 seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/instances/{id}/wait", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "state": state,
                        "api_timeout": api_timeout,
                    },
                    instance_wait_params.InstanceWaitParams,
                ),
            ),
            cast_to=WaitForStateResponse,
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def auto_standby(self) -> AsyncAutoStandbyResource:
        return AsyncAutoStandbyResource(self._client)

    @cached_property
    def volumes(self) -> AsyncVolumesResource:
        return AsyncVolumesResource(self._client)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResource:
        return AsyncSnapshotsResource(self._client)

    @cached_property
    def snapshot_schedule(self) -> AsyncSnapshotScheduleResource:
        return AsyncSnapshotScheduleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image: str,
        name: str,
        auto_standby: AutoStandbyPolicyParam | Omit = omit,
        cmd: SequenceNotStr[str] | Omit = omit,
        credentials: Dict[str, instance_create_params.Credentials] | Omit = omit,
        devices: SequenceNotStr[str] | Omit = omit,
        disk_io_bps: str | Omit = omit,
        entrypoint: SequenceNotStr[str] | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        gpu: instance_create_params.GPU | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        hotplug_size: str | Omit = omit,
        hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"] | Omit = omit,
        network: instance_create_params.Network | Omit = omit,
        overlay_size: str | Omit = omit,
        platform: str | Omit = omit,
        restart_policy: RestartPolicyParam | Omit = omit,
        size: str | Omit = omit,
        skip_guest_agent: bool | Omit = omit,
        skip_kernel_headers: bool | Omit = omit,
        snapshot_policy: SnapshotPolicyParam | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        ttl: str | Omit = omit,
        vcpus: int | Omit = omit,
        volumes: Iterable[VolumeMountParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Create and start instance

        Args:
          image: OCI image reference

          name: Human-readable name (lowercase letters, digits, and dashes only; cannot start or
              end with a dash)

          auto_standby: Linux-only automatic standby policy based on active inbound TCP connections
              observed from the host conntrack table.

          cmd: Override image CMD (like docker run <image> <command>). Omit to use image
              default.

          credentials: Host-managed credential brokering policies keyed by guest-visible env var name.
              Those guest env vars receive mock placeholder values, while the real values
              remain host-scoped in the request `env` map and are only materialized on the
              mediated egress path according to each credential's `source` and `inject` rules.

          devices: Device IDs or names to attach for GPU/PCI passthrough

          disk_io_bps: Disk I/O rate limit (e.g., "100MB/s", "500MB/s"). Defaults to proportional share
              based on CPU allocation if configured.

          entrypoint: Override image entrypoint (like docker run --entrypoint). Omit to use image
              default.

          env: Environment variables

          expires_at: Absolute expiration time. Must be in the future and is mutually exclusive with
              ttl.

          gpu: GPU configuration for the instance

          health_check: Workload health check policy. Health is reported separately from instance
              lifecycle state.

          hotplug_size: Additional memory for hotplug (human-readable format like "3GB", "1G"). Omit to
              disable hotplug memory.

          hypervisor: Hypervisor backend to use for this instance. qemu uses the architecture-native
              standard board; qemu-microvm uses QEMU's minimal Linux amd64 board and does not
              support PCI devices, hotplug memory, or more than eight virtio-mmio devices.
              Defaults to server configuration.

          network: Network configuration for the instance

          overlay_size: Writable overlay disk size (human-readable format like "10GB", "50G")

          platform: Target platform as os/arch[/variant] (e.g. "linux/amd64"), matching Docker
              --platform. Omit for the host platform. Not a fixed enum: the os/arch[/variant]
              grammar is validated server-side and invalid values return 400 invalid_platform.
              Only os "linux" with arch amd64 or arm64 is accepted today.

          restart_policy: Whole-instance restart supervision policy.

          size: Base memory size (human-readable format like "1GB", "512MB", "2G")

          skip_guest_agent: Skip guest-agent installation during boot. When true, the exec and stat APIs
              will not work for this instance. The instance will still run, but remote command
              execution will be unavailable.

          skip_kernel_headers: Skip kernel headers installation during boot for faster startup. When true, DKMS
              (Dynamic Kernel Module Support) will not work, preventing compilation of
              out-of-tree kernel modules (e.g., NVIDIA vGPU drivers). Recommended for
              workloads that don't need kernel module compilation.

          snapshot_policy: Snapshot policy for this instance. Controls compression settings applied when
              creating snapshots or entering standby, plus any default standby-only
              compression delay.

          tags: User-defined key-value tags.

          ttl: Relative lifetime from instance creation, in Go duration format. Use "0s" or
              omit both expiration fields to disable automatic expiration. Mutually exclusive
              with expires_at.

          vcpus: Number of virtual CPUs

          volumes: Volumes to attach to the instance at creation time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/instances",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "auto_standby": auto_standby,
                    "cmd": cmd,
                    "credentials": credentials,
                    "devices": devices,
                    "disk_io_bps": disk_io_bps,
                    "entrypoint": entrypoint,
                    "env": env,
                    "expires_at": expires_at,
                    "gpu": gpu,
                    "health_check": health_check,
                    "hotplug_size": hotplug_size,
                    "hypervisor": hypervisor,
                    "network": network,
                    "overlay_size": overlay_size,
                    "platform": platform,
                    "restart_policy": restart_policy,
                    "size": size,
                    "skip_guest_agent": skip_guest_agent,
                    "skip_kernel_headers": skip_kernel_headers,
                    "snapshot_policy": snapshot_policy,
                    "tags": tags,
                    "ttl": ttl,
                    "vcpus": vcpus,
                    "volumes": volumes,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def update(
        self,
        id: str,
        *,
        auto_standby: AutoStandbyPolicyParam | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        restart_policy: RestartPolicyParam | Omit = omit,
        ttl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """Update mutable instance properties.

        TTL values are relative to when the update
        is committed. Expiration updates are rejected after the current deadline passes.

        Args:
          auto_standby: Linux-only automatic standby policy based on active inbound TCP connections
              observed from the host conntrack table.

          env: Environment variables to update (merged with existing). Only keys referenced by
              the instance's existing credential `source.env` bindings are accepted. Use this
              to rotate real credential values without restarting the VM.

          expires_at: Absolute expiration time. Must be in the future and is mutually exclusive with
              ttl.

          health_check: Workload health check policy. Health is reported separately from instance
              lifecycle state.

          restart_policy: Whole-instance restart supervision policy.

          ttl: Relative lifetime from when this update is committed, in Go duration format. Use
              "0s" to disable automatic expiration. Mutually exclusive with expires_at.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/instances/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "auto_standby": auto_standby,
                    "env": env,
                    "expires_at": expires_at,
                    "health_check": health_check,
                    "restart_policy": restart_policy,
                    "ttl": ttl,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def list(
        self,
        *,
        state: Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"]
        | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceListResponse:
        """
        List instances

        Args:
          state: Filter instances by state (e.g., Running, Stopped)

          tags:
              Filter instances by tag key-value pairs. Uses deepObject style:
              ?tags[team]=backend&tags[env]=staging Multiple entries are ANDed together. All
              specified key-value pairs must match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "state": state,
                        "tags": tags,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            cast_to=InstanceListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop and delete instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/instances/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def fork(
        self,
        id: str,
        *,
        name: str,
        from_running: bool | Omit = omit,
        target_state: Literal["Stopped", "Standby", "Running"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Fork an instance from stopped, standby, or running (with from_running=true)

        Args:
          name: Name for the forked instance (lowercase letters, digits, and dashes only; cannot
              start or end with a dash)

          from_running: Allow forking from a running source instance. When true and source is Running,
              the source is put into standby, forked, then restored back to Running.

          target_state: Optional final state for the forked instance. Default is the source instance
              state at fork time. For example, forking from Running defaults the fork result
              to Running.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/instances/{id}/fork", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "from_running": from_running,
                    "target_state": target_state,
                },
                instance_fork_params.InstanceForkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Get instance details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/instances/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def logs(
        self,
        id: str,
        *,
        follow: bool | Omit = omit,
        source: Literal["app", "vmm", "hypeman"] | Omit = omit,
        tail: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[InstanceLogsResponse]:
        """Streams instance logs as Server-Sent Events.

        Use the `source` parameter to
        select which log to stream:

        - `app` (default): Guest application logs (serial console)
        - `vmm`: Cloud Hypervisor VMM logs
        - `hypeman`: Hypeman operations log

        Returns the last N lines (controlled by `tail` parameter), then optionally
        continues streaming new lines if `follow=true`.

        Args:
          follow: Continue streaming new lines after initial output

          source:
              Log source to stream:

              - app: Guest application logs (serial console output)
              - vmm: Cloud Hypervisor VMM logs (hypervisor stdout+stderr)
              - hypeman: Hypeman operations log (actions taken on this instance)

          tail: Number of lines to return from end

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/instances/{id}/logs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "follow": follow,
                        "source": source,
                        "tail": tail,
                    },
                    instance_logs_params.InstanceLogsParams,
                ),
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[InstanceLogsResponse],
        )

    async def restore(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Restore instance from standby

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/instances/{id}/restore", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def standby(
        self,
        id: str,
        *,
        compression: SnapshotCompressionConfig | Omit = omit,
        compression_delay: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Put instance in standby (pause, snapshot, delete VMM)

        Args:
          compression: Compression settings for standby snapshot memory. Overrides instance defaults.

          compression_delay: Delay before standby snapshot compression begins, expressed as a Go duration
              like "30s" or "5m". Overrides the instance default for this standby operation
              only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/instances/{id}/standby", id=id),
            body=await async_maybe_transform(
                {
                    "compression": compression,
                    "compression_delay": compression_delay,
                },
                instance_standby_params.InstanceStandbyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def start(
        self,
        id: str,
        *,
        cmd: SequenceNotStr[str] | Omit = omit,
        entrypoint: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """Start a stopped instance

        Args:
          cmd: Override image CMD for this run.

        Omit to keep previous value.

          entrypoint: Override image entrypoint for this run. Omit to keep previous value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/instances/{id}/start", id=id),
            body=await async_maybe_transform(
                {
                    "cmd": cmd,
                    "entrypoint": entrypoint,
                },
                instance_start_params.InstanceStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def stat(
        self,
        id: str,
        *,
        path: str,
        follow_links: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PathInfo:
        """Returns information about a path in the guest filesystem.

        Useful for checking if
        a path exists, its type, and permissions before performing file operations.

        Args:
          path: Path to stat in the guest filesystem

          follow_links: Follow symbolic links (like stat vs lstat)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/instances/{id}/stat", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "follow_links": follow_links,
                    },
                    instance_stat_params.InstanceStatParams,
                ),
            ),
            cast_to=PathInfo,
        )

    async def stats(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceStats:
        """
        Returns real-time resource utilization statistics for a running VM instance.
        Metrics are collected from /proc/<pid>/stat and /proc/<pid>/statm for CPU and
        memory, and from TAP interface statistics for network I/O.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/instances/{id}/stats", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceStats,
        )

    async def stop(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Stop instance (graceful shutdown)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/instances/{id}/stop", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def wait(
        self,
        id: str,
        *,
        state: Literal["Created", "Initializing", "Running", "Paused", "Shutdown", "Stopped", "Standby", "Unknown"],
        api_timeout: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaitForStateResponse:
        """
        Blocks until the instance reaches the specified target state, the timeout
        expires, or the instance enters a terminal/error state. Useful for avoiding
        client-side polling when waiting for state transitions (e.g. waiting for an
        instance to become Running).

        Args:
          state: Target state to wait for

          api_timeout: Maximum duration to wait (Go duration format, e.g. "30s", "2m"). Capped at 5
              minutes. Defaults to 60 seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/instances/{id}/wait", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "state": state,
                        "api_timeout": api_timeout,
                    },
                    instance_wait_params.InstanceWaitParams,
                ),
            ),
            cast_to=WaitForStateResponse,
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_raw_response_wrapper(
            instances.create,
        )
        self.update = to_raw_response_wrapper(
            instances.update,
        )
        self.list = to_raw_response_wrapper(
            instances.list,
        )
        self.delete = to_raw_response_wrapper(
            instances.delete,
        )
        self.fork = to_raw_response_wrapper(
            instances.fork,
        )
        self.get = to_raw_response_wrapper(
            instances.get,
        )
        self.logs = to_raw_response_wrapper(
            instances.logs,
        )
        self.restore = to_raw_response_wrapper(
            instances.restore,
        )
        self.standby = to_raw_response_wrapper(
            instances.standby,
        )
        self.start = to_raw_response_wrapper(
            instances.start,
        )
        self.stat = to_raw_response_wrapper(
            instances.stat,
        )
        self.stats = to_raw_response_wrapper(
            instances.stats,
        )
        self.stop = to_raw_response_wrapper(
            instances.stop,
        )
        self.wait = to_raw_response_wrapper(
            instances.wait,
        )

    @cached_property
    def auto_standby(self) -> AutoStandbyResourceWithRawResponse:
        return AutoStandbyResourceWithRawResponse(self._instances.auto_standby)

    @cached_property
    def volumes(self) -> VolumesResourceWithRawResponse:
        return VolumesResourceWithRawResponse(self._instances.volumes)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self._instances.snapshots)

    @cached_property
    def snapshot_schedule(self) -> SnapshotScheduleResourceWithRawResponse:
        return SnapshotScheduleResourceWithRawResponse(self._instances.snapshot_schedule)


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_raw_response_wrapper(
            instances.create,
        )
        self.update = async_to_raw_response_wrapper(
            instances.update,
        )
        self.list = async_to_raw_response_wrapper(
            instances.list,
        )
        self.delete = async_to_raw_response_wrapper(
            instances.delete,
        )
        self.fork = async_to_raw_response_wrapper(
            instances.fork,
        )
        self.get = async_to_raw_response_wrapper(
            instances.get,
        )
        self.logs = async_to_raw_response_wrapper(
            instances.logs,
        )
        self.restore = async_to_raw_response_wrapper(
            instances.restore,
        )
        self.standby = async_to_raw_response_wrapper(
            instances.standby,
        )
        self.start = async_to_raw_response_wrapper(
            instances.start,
        )
        self.stat = async_to_raw_response_wrapper(
            instances.stat,
        )
        self.stats = async_to_raw_response_wrapper(
            instances.stats,
        )
        self.stop = async_to_raw_response_wrapper(
            instances.stop,
        )
        self.wait = async_to_raw_response_wrapper(
            instances.wait,
        )

    @cached_property
    def auto_standby(self) -> AsyncAutoStandbyResourceWithRawResponse:
        return AsyncAutoStandbyResourceWithRawResponse(self._instances.auto_standby)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithRawResponse:
        return AsyncVolumesResourceWithRawResponse(self._instances.volumes)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self._instances.snapshots)

    @cached_property
    def snapshot_schedule(self) -> AsyncSnapshotScheduleResourceWithRawResponse:
        return AsyncSnapshotScheduleResourceWithRawResponse(self._instances.snapshot_schedule)


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_streamed_response_wrapper(
            instances.create,
        )
        self.update = to_streamed_response_wrapper(
            instances.update,
        )
        self.list = to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = to_streamed_response_wrapper(
            instances.delete,
        )
        self.fork = to_streamed_response_wrapper(
            instances.fork,
        )
        self.get = to_streamed_response_wrapper(
            instances.get,
        )
        self.logs = to_streamed_response_wrapper(
            instances.logs,
        )
        self.restore = to_streamed_response_wrapper(
            instances.restore,
        )
        self.standby = to_streamed_response_wrapper(
            instances.standby,
        )
        self.start = to_streamed_response_wrapper(
            instances.start,
        )
        self.stat = to_streamed_response_wrapper(
            instances.stat,
        )
        self.stats = to_streamed_response_wrapper(
            instances.stats,
        )
        self.stop = to_streamed_response_wrapper(
            instances.stop,
        )
        self.wait = to_streamed_response_wrapper(
            instances.wait,
        )

    @cached_property
    def auto_standby(self) -> AutoStandbyResourceWithStreamingResponse:
        return AutoStandbyResourceWithStreamingResponse(self._instances.auto_standby)

    @cached_property
    def volumes(self) -> VolumesResourceWithStreamingResponse:
        return VolumesResourceWithStreamingResponse(self._instances.volumes)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self._instances.snapshots)

    @cached_property
    def snapshot_schedule(self) -> SnapshotScheduleResourceWithStreamingResponse:
        return SnapshotScheduleResourceWithStreamingResponse(self._instances.snapshot_schedule)


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_streamed_response_wrapper(
            instances.create,
        )
        self.update = async_to_streamed_response_wrapper(
            instances.update,
        )
        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            instances.delete,
        )
        self.fork = async_to_streamed_response_wrapper(
            instances.fork,
        )
        self.get = async_to_streamed_response_wrapper(
            instances.get,
        )
        self.logs = async_to_streamed_response_wrapper(
            instances.logs,
        )
        self.restore = async_to_streamed_response_wrapper(
            instances.restore,
        )
        self.standby = async_to_streamed_response_wrapper(
            instances.standby,
        )
        self.start = async_to_streamed_response_wrapper(
            instances.start,
        )
        self.stat = async_to_streamed_response_wrapper(
            instances.stat,
        )
        self.stats = async_to_streamed_response_wrapper(
            instances.stats,
        )
        self.stop = async_to_streamed_response_wrapper(
            instances.stop,
        )
        self.wait = async_to_streamed_response_wrapper(
            instances.wait,
        )

    @cached_property
    def auto_standby(self) -> AsyncAutoStandbyResourceWithStreamingResponse:
        return AsyncAutoStandbyResourceWithStreamingResponse(self._instances.auto_standby)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithStreamingResponse:
        return AsyncVolumesResourceWithStreamingResponse(self._instances.volumes)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self._instances.snapshots)

    @cached_property
    def snapshot_schedule(self) -> AsyncSnapshotScheduleResourceWithStreamingResponse:
        return AsyncSnapshotScheduleResourceWithStreamingResponse(self._instances.snapshot_schedule)
