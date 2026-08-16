# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import SnapshotKind, snapshot_fork_params, snapshot_list_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.instance import Instance
from ..types.snapshot import Snapshot
from ..types.snapshot_kind import SnapshotKind
from ..types.snapshot_list_response import SnapshotListResponse

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

    def list(
        self,
        *,
        kind: SnapshotKind | Omit = omit,
        name: str | Omit = omit,
        source_instance_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        List snapshots

        Args:
          kind: Filter snapshots by kind

          name: Filter snapshots by snapshot name

          source_instance_id: Filter snapshots by source instance ID

          tags: Filter snapshots by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/snapshots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "kind": kind,
                        "name": name,
                        "source_instance_id": source_instance_id,
                        "tags": tags,
                    },
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    def delete(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a snapshot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/snapshots/{snapshot_id}", snapshot_id=snapshot_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def fork(
        self,
        snapshot_id: str,
        *,
        name: str,
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
        Fork a new instance from a snapshot

        Args:
          name: Name for the new instance (lowercase letters, digits, and dashes only; cannot
              start or end with a dash)

          target_hypervisor: Optional hypervisor override. Allowed only when forking from a Stopped snapshot.
              Standby snapshots must fork with their original hypervisor.

          target_state:
              Optional final state for the forked instance. Defaults by snapshot kind:

              - Standby snapshot defaults to Running
              - Stopped snapshot defaults to Stopped

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._post(
            path_template("/snapshots/{snapshot_id}/fork", snapshot_id=snapshot_id),
            body=maybe_transform(
                {
                    "name": name,
                    "target_hypervisor": target_hypervisor,
                    "target_state": target_state,
                },
                snapshot_fork_params.SnapshotForkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def get(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Get snapshot details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._get(
            path_template("/snapshots/{snapshot_id}", snapshot_id=snapshot_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
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

    async def list(
        self,
        *,
        kind: SnapshotKind | Omit = omit,
        name: str | Omit = omit,
        source_instance_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        List snapshots

        Args:
          kind: Filter snapshots by kind

          name: Filter snapshots by snapshot name

          source_instance_id: Filter snapshots by source instance ID

          tags: Filter snapshots by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/snapshots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "kind": kind,
                        "name": name,
                        "source_instance_id": source_instance_id,
                        "tags": tags,
                    },
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    async def delete(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a snapshot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/snapshots/{snapshot_id}", snapshot_id=snapshot_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def fork(
        self,
        snapshot_id: str,
        *,
        name: str,
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
        Fork a new instance from a snapshot

        Args:
          name: Name for the new instance (lowercase letters, digits, and dashes only; cannot
              start or end with a dash)

          target_hypervisor: Optional hypervisor override. Allowed only when forking from a Stopped snapshot.
              Standby snapshots must fork with their original hypervisor.

          target_state:
              Optional final state for the forked instance. Defaults by snapshot kind:

              - Standby snapshot defaults to Running
              - Stopped snapshot defaults to Stopped

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._post(
            path_template("/snapshots/{snapshot_id}/fork", snapshot_id=snapshot_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "target_hypervisor": target_hypervisor,
                    "target_state": target_state,
                },
                snapshot_fork_params.SnapshotForkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def get(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Get snapshot details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._get(
            path_template("/snapshots/{snapshot_id}", snapshot_id=snapshot_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
        )


class SnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = to_raw_response_wrapper(
            snapshots.list,
        )
        self.delete = to_raw_response_wrapper(
            snapshots.delete,
        )
        self.fork = to_raw_response_wrapper(
            snapshots.fork,
        )
        self.get = to_raw_response_wrapper(
            snapshots.get,
        )


class AsyncSnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = async_to_raw_response_wrapper(
            snapshots.list,
        )
        self.delete = async_to_raw_response_wrapper(
            snapshots.delete,
        )
        self.fork = async_to_raw_response_wrapper(
            snapshots.fork,
        )
        self.get = async_to_raw_response_wrapper(
            snapshots.get,
        )


class SnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = to_streamed_response_wrapper(
            snapshots.list,
        )
        self.delete = to_streamed_response_wrapper(
            snapshots.delete,
        )
        self.fork = to_streamed_response_wrapper(
            snapshots.fork,
        )
        self.get = to_streamed_response_wrapper(
            snapshots.get,
        )


class AsyncSnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = async_to_streamed_response_wrapper(
            snapshots.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            snapshots.delete,
        )
        self.fork = async_to_streamed_response_wrapper(
            snapshots.fork,
        )
        self.get = async_to_streamed_response_wrapper(
            snapshots.get,
        )
