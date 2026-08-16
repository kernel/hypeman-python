# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import resource_reclaim_memory_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.resources import Resources
from ..types.memory_reclaim_response import MemoryReclaimResponse

__all__ = ["ResourcesResource", "AsyncResourcesResource"]


class ResourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return ResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return ResourcesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resources:
        """
        Returns current host resource capacity, allocation status, and per-instance
        breakdown. Resources include CPU, memory, disk, and network. Oversubscription
        ratios are applied to calculate effective limits.
        """
        return self._get(
            "/resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resources,
        )

    def reclaim_memory(
        self,
        *,
        reclaim_bytes: int,
        dry_run: bool | Omit = omit,
        hold_for: str | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryReclaimResponse:
        """Requests runtime balloon inflation across reclaim-eligible guests.

        The same
        planner used by host-pressure reclaim is applied, including protected floors and
        per-VM step limits.

        Args:
          reclaim_bytes: Total bytes of guest memory to reclaim across eligible VMs.

          dry_run: Calculate a reclaim plan without applying balloon changes or creating a hold.

          hold_for: How long to keep the reclaim hold active (Go duration string). Defaults to 5m
              when omitted.

          reason: Optional operator-provided reason attached to logs and traces.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/resources/memory/reclaim",
            body=maybe_transform(
                {
                    "reclaim_bytes": reclaim_bytes,
                    "dry_run": dry_run,
                    "hold_for": hold_for,
                    "reason": reason,
                },
                resource_reclaim_memory_params.ResourceReclaimMemoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryReclaimResponse,
        )


class AsyncResourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncResourcesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Resources:
        """
        Returns current host resource capacity, allocation status, and per-instance
        breakdown. Resources include CPU, memory, disk, and network. Oversubscription
        ratios are applied to calculate effective limits.
        """
        return await self._get(
            "/resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Resources,
        )

    async def reclaim_memory(
        self,
        *,
        reclaim_bytes: int,
        dry_run: bool | Omit = omit,
        hold_for: str | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryReclaimResponse:
        """Requests runtime balloon inflation across reclaim-eligible guests.

        The same
        planner used by host-pressure reclaim is applied, including protected floors and
        per-VM step limits.

        Args:
          reclaim_bytes: Total bytes of guest memory to reclaim across eligible VMs.

          dry_run: Calculate a reclaim plan without applying balloon changes or creating a hold.

          hold_for: How long to keep the reclaim hold active (Go duration string). Defaults to 5m
              when omitted.

          reason: Optional operator-provided reason attached to logs and traces.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/resources/memory/reclaim",
            body=await async_maybe_transform(
                {
                    "reclaim_bytes": reclaim_bytes,
                    "dry_run": dry_run,
                    "hold_for": hold_for,
                    "reason": reason,
                },
                resource_reclaim_memory_params.ResourceReclaimMemoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryReclaimResponse,
        )


class ResourcesResourceWithRawResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.get = to_raw_response_wrapper(
            resources.get,
        )
        self.reclaim_memory = to_raw_response_wrapper(
            resources.reclaim_memory,
        )


class AsyncResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.get = async_to_raw_response_wrapper(
            resources.get,
        )
        self.reclaim_memory = async_to_raw_response_wrapper(
            resources.reclaim_memory,
        )


class ResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.get = to_streamed_response_wrapper(
            resources.get,
        )
        self.reclaim_memory = to_streamed_response_wrapper(
            resources.reclaim_memory,
        )


class AsyncResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.get = async_to_streamed_response_wrapper(
            resources.get,
        )
        self.reclaim_memory = async_to_streamed_response_wrapper(
            resources.reclaim_memory,
        )
