# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ...types import SnapshotKind
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.instance import Instance
from ...types.snapshot import Snapshot
from ...types.instances import snapshot_create_params, snapshot_restore_params
from ...types.snapshot_kind import SnapshotKind
from ...types.shared_params.snapshot_compression_config import SnapshotCompressionConfig

__all__ = ["SnapshotsResource", "AsyncSnapshotsResource"]


class SnapshotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return SnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return SnapshotsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        kind: SnapshotKind,
        compression: SnapshotCompressionConfig | Omit = omit,
        name: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Create a snapshot for an instance

        Args:
          kind: Snapshot capture kind

          compression: Compression settings to use for this snapshot. Overrides instance and server
              defaults.

          name: Optional snapshot name (lowercase letters, digits, and dashes only; cannot start
              or end with a dash)

          tags: User-defined key-value tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/instances/{id}/snapshots", id=id),
            body=maybe_transform(
                {
                    "kind": kind,
                    "compression": compression,
                    "name": name,
                    "tags": tags,
                },
                snapshot_create_params.SnapshotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
        )

    def restore(
        self,
        snapshot_id: str,
        *,
        id: str,
        target_hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"] | Omit = omit,
        target_state: Literal["Stopped", "Standby", "Running"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Restore an instance from a snapshot in-place

        Args:
          target_hypervisor: Optional hypervisor override. Allowed only when restoring from a Stopped
              snapshot. Standby snapshots must restore with their original hypervisor.

          target_state:
              Optional final state after restore. Defaults by snapshot kind:

              - Standby snapshot defaults to Running
              - Stopped snapshot defaults to Stopped

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._post(
            path_template("/instances/{id}/snapshots/{snapshot_id}/restore", id=id, snapshot_id=snapshot_id),
            body=maybe_transform(
                {
                    "target_hypervisor": target_hypervisor,
                    "target_state": target_state,
                },
                snapshot_restore_params.SnapshotRestoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )


class AsyncSnapshotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncSnapshotsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        kind: SnapshotKind,
        compression: SnapshotCompressionConfig | Omit = omit,
        name: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Create a snapshot for an instance

        Args:
          kind: Snapshot capture kind

          compression: Compression settings to use for this snapshot. Overrides instance and server
              defaults.

          name: Optional snapshot name (lowercase letters, digits, and dashes only; cannot start
              or end with a dash)

          tags: User-defined key-value tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/instances/{id}/snapshots", id=id),
            body=await async_maybe_transform(
                {
                    "kind": kind,
                    "compression": compression,
                    "name": name,
                    "tags": tags,
                },
                snapshot_create_params.SnapshotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
        )

    async def restore(
        self,
        snapshot_id: str,
        *,
        id: str,
        target_hypervisor: Literal["cloud-hypervisor", "firecracker", "qemu", "qemu-microvm", "vz"] | Omit = omit,
        target_state: Literal["Stopped", "Standby", "Running"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Restore an instance from a snapshot in-place

        Args:
          target_hypervisor: Optional hypervisor override. Allowed only when restoring from a Stopped
              snapshot. Standby snapshots must restore with their original hypervisor.

          target_state:
              Optional final state after restore. Defaults by snapshot kind:

              - Standby snapshot defaults to Running
              - Stopped snapshot defaults to Stopped

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._post(
            path_template("/instances/{id}/snapshots/{snapshot_id}/restore", id=id, snapshot_id=snapshot_id),
            body=await async_maybe_transform(
                {
                    "target_hypervisor": target_hypervisor,
                    "target_state": target_state,
                },
                snapshot_restore_params.SnapshotRestoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )


class SnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.create = to_raw_response_wrapper(
            snapshots.create,
        )
        self.restore = to_raw_response_wrapper(
            snapshots.restore,
        )


class AsyncSnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.create = async_to_raw_response_wrapper(
            snapshots.create,
        )
        self.restore = async_to_raw_response_wrapper(
            snapshots.restore,
        )


class SnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.create = to_streamed_response_wrapper(
            snapshots.create,
        )
        self.restore = to_streamed_response_wrapper(
            snapshots.restore,
        )


class AsyncSnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.create = async_to_streamed_response_wrapper(
            snapshots.create,
        )
        self.restore = async_to_streamed_response_wrapper(
            snapshots.restore,
        )
