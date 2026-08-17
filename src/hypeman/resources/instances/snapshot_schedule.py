# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.instances import snapshot_schedule_update_params
from ...types.snapshot_schedule import SnapshotSchedule
from ...types.snapshot_schedule_retention_param import SnapshotScheduleRetentionParam

__all__ = ["SnapshotScheduleResource", "AsyncSnapshotScheduleResource"]


class SnapshotScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SnapshotScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return SnapshotScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapshotScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return SnapshotScheduleResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        interval: str,
        retention: SnapshotScheduleRetentionParam,
        metadata: Dict[str, str] | Omit = omit,
        name_prefix: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotSchedule:
        """
        Scheduled runs automatically choose snapshot behavior from current instance
        state:

        - `Running` or `Standby` source: create a `Standby` snapshot.
        - `Stopped` source: create a `Stopped` snapshot. For running instances, this
          includes a brief pause/resume cycle during each capture. The minimum supported
          interval is `1m`, but larger intervals are recommended for heavier or
          latency-sensitive workloads. Updating only retention, metadata, or
          `name_prefix` preserves the next scheduled run; changing `interval`
          establishes a new cadence.

        Args:
          interval: Snapshot interval (Go duration format, minimum 1m).

          retention: At least one of max_count or max_age must be provided.

          metadata: User-defined key-value tags.

          name_prefix: Optional prefix for auto-generated scheduled snapshot names (max 47 chars).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/instances/{id}/snapshot-schedule", id=id),
            body=maybe_transform(
                {
                    "interval": interval,
                    "retention": retention,
                    "metadata": metadata,
                    "name_prefix": name_prefix,
                },
                snapshot_schedule_update_params.SnapshotScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotSchedule,
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
        Delete snapshot schedule for an instance

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
            path_template("/instances/{id}/snapshot-schedule", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SnapshotSchedule:
        """
        Get snapshot schedule for an instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/instances/{id}/snapshot-schedule", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotSchedule,
        )


class AsyncSnapshotScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSnapshotScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSnapshotScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapshotScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncSnapshotScheduleResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        interval: str,
        retention: SnapshotScheduleRetentionParam,
        metadata: Dict[str, str] | Omit = omit,
        name_prefix: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotSchedule:
        """
        Scheduled runs automatically choose snapshot behavior from current instance
        state:

        - `Running` or `Standby` source: create a `Standby` snapshot.
        - `Stopped` source: create a `Stopped` snapshot. For running instances, this
          includes a brief pause/resume cycle during each capture. The minimum supported
          interval is `1m`, but larger intervals are recommended for heavier or
          latency-sensitive workloads. Updating only retention, metadata, or
          `name_prefix` preserves the next scheduled run; changing `interval`
          establishes a new cadence.

        Args:
          interval: Snapshot interval (Go duration format, minimum 1m).

          retention: At least one of max_count or max_age must be provided.

          metadata: User-defined key-value tags.

          name_prefix: Optional prefix for auto-generated scheduled snapshot names (max 47 chars).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/instances/{id}/snapshot-schedule", id=id),
            body=await async_maybe_transform(
                {
                    "interval": interval,
                    "retention": retention,
                    "metadata": metadata,
                    "name_prefix": name_prefix,
                },
                snapshot_schedule_update_params.SnapshotScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotSchedule,
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
        Delete snapshot schedule for an instance

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
            path_template("/instances/{id}/snapshot-schedule", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SnapshotSchedule:
        """
        Get snapshot schedule for an instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/instances/{id}/snapshot-schedule", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotSchedule,
        )


class SnapshotScheduleResourceWithRawResponse:
    def __init__(self, snapshot_schedule: SnapshotScheduleResource) -> None:
        self._snapshot_schedule = snapshot_schedule

        self.update = to_raw_response_wrapper(
            snapshot_schedule.update,
        )
        self.delete = to_raw_response_wrapper(
            snapshot_schedule.delete,
        )
        self.get = to_raw_response_wrapper(
            snapshot_schedule.get,
        )


class AsyncSnapshotScheduleResourceWithRawResponse:
    def __init__(self, snapshot_schedule: AsyncSnapshotScheduleResource) -> None:
        self._snapshot_schedule = snapshot_schedule

        self.update = async_to_raw_response_wrapper(
            snapshot_schedule.update,
        )
        self.delete = async_to_raw_response_wrapper(
            snapshot_schedule.delete,
        )
        self.get = async_to_raw_response_wrapper(
            snapshot_schedule.get,
        )


class SnapshotScheduleResourceWithStreamingResponse:
    def __init__(self, snapshot_schedule: SnapshotScheduleResource) -> None:
        self._snapshot_schedule = snapshot_schedule

        self.update = to_streamed_response_wrapper(
            snapshot_schedule.update,
        )
        self.delete = to_streamed_response_wrapper(
            snapshot_schedule.delete,
        )
        self.get = to_streamed_response_wrapper(
            snapshot_schedule.get,
        )


class AsyncSnapshotScheduleResourceWithStreamingResponse:
    def __init__(self, snapshot_schedule: AsyncSnapshotScheduleResource) -> None:
        self._snapshot_schedule = snapshot_schedule

        self.update = async_to_streamed_response_wrapper(
            snapshot_schedule.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            snapshot_schedule.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            snapshot_schedule.get,
        )
