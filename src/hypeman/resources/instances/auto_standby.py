# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.auto_standby_status import AutoStandbyStatus

__all__ = ["AutoStandbyResource", "AsyncAutoStandbyResource"]


class AutoStandbyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoStandbyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AutoStandbyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoStandbyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AutoStandbyResourceWithStreamingResponse(self)

    def hold(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoStandbyStatus:
        """
        Places a hold that prevents the auto-standby controller from putting the
        instance into standby before `hold_until`, and cancels any queued auto-standby
        attempt.

        Each hold replaces the instance's previous hold, so `hold_until` always reflects
        the most recent call. Holding again after the policy's `idle_timeout` is
        shortened moves `hold_until` earlier.

        Callers may use this before opening a connection to a candidate-idle instance: a
        200 means it is safe to connect until `hold_until`; a 409 means the instance is
        in standby (or irrevocably entering it) and must be restored first.

        Instances where auto-standby is disabled, unconfigured, or unsupported return
        200 with their current status because no auto-standby will occur.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/instances/{id}/auto-standby/hold", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoStandbyStatus,
        )

    def status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoStandbyStatus:
        """
        Get auto-standby diagnostic status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/instances/{id}/auto-standby/status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoStandbyStatus,
        )


class AsyncAutoStandbyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoStandbyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoStandbyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoStandbyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncAutoStandbyResourceWithStreamingResponse(self)

    async def hold(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoStandbyStatus:
        """
        Places a hold that prevents the auto-standby controller from putting the
        instance into standby before `hold_until`, and cancels any queued auto-standby
        attempt.

        Each hold replaces the instance's previous hold, so `hold_until` always reflects
        the most recent call. Holding again after the policy's `idle_timeout` is
        shortened moves `hold_until` earlier.

        Callers may use this before opening a connection to a candidate-idle instance: a
        200 means it is safe to connect until `hold_until`; a 409 means the instance is
        in standby (or irrevocably entering it) and must be restored first.

        Instances where auto-standby is disabled, unconfigured, or unsupported return
        200 with their current status because no auto-standby will occur.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/instances/{id}/auto-standby/hold", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoStandbyStatus,
        )

    async def status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoStandbyStatus:
        """
        Get auto-standby diagnostic status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/instances/{id}/auto-standby/status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoStandbyStatus,
        )


class AutoStandbyResourceWithRawResponse:
    def __init__(self, auto_standby: AutoStandbyResource) -> None:
        self._auto_standby = auto_standby

        self.hold = to_raw_response_wrapper(
            auto_standby.hold,
        )
        self.status = to_raw_response_wrapper(
            auto_standby.status,
        )


class AsyncAutoStandbyResourceWithRawResponse:
    def __init__(self, auto_standby: AsyncAutoStandbyResource) -> None:
        self._auto_standby = auto_standby

        self.hold = async_to_raw_response_wrapper(
            auto_standby.hold,
        )
        self.status = async_to_raw_response_wrapper(
            auto_standby.status,
        )


class AutoStandbyResourceWithStreamingResponse:
    def __init__(self, auto_standby: AutoStandbyResource) -> None:
        self._auto_standby = auto_standby

        self.hold = to_streamed_response_wrapper(
            auto_standby.hold,
        )
        self.status = to_streamed_response_wrapper(
            auto_standby.status,
        )


class AsyncAutoStandbyResourceWithStreamingResponse:
    def __init__(self, auto_standby: AsyncAutoStandbyResource) -> None:
        self._auto_standby = auto_standby

        self.hold = async_to_streamed_response_wrapper(
            auto_standby.hold,
        )
        self.status = async_to_streamed_response_wrapper(
            auto_standby.status,
        )
