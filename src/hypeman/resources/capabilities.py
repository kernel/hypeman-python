# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.capabilities import Capabilities

__all__ = ["CapabilitiesResource", "AsyncCapabilitiesResource"]


class CapabilitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return CapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return CapabilitiesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Capabilities:
        """
        Returns machine-readable host capabilities: server and API version, host
        OS/architecture, every runtime available on this host with its per-runtime
        feature IDs, the configured default runtime and whether it is available, guest
        networking model and host gateway, supported image platforms, and stable
        server-level feature IDs.

        Runtime-derived values reflect the actual host (for example, snapshot and
        standby support on macOS is gated on the host OS version), so clients can gate
        behavior on capabilities without hard-coding hypervisor knowledge.
        """
        return self._get(
            "/capabilities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Capabilities,
        )


class AsyncCapabilitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncCapabilitiesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Capabilities:
        """
        Returns machine-readable host capabilities: server and API version, host
        OS/architecture, every runtime available on this host with its per-runtime
        feature IDs, the configured default runtime and whether it is available, guest
        networking model and host gateway, supported image platforms, and stable
        server-level feature IDs.

        Runtime-derived values reflect the actual host (for example, snapshot and
        standby support on macOS is gated on the host OS version), so clients can gate
        behavior on capabilities without hard-coding hypervisor knowledge.
        """
        return await self._get(
            "/capabilities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Capabilities,
        )


class CapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.get = to_raw_response_wrapper(
            capabilities.get,
        )


class AsyncCapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.get = async_to_raw_response_wrapper(
            capabilities.get,
        )


class CapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.get = to_streamed_response_wrapper(
            capabilities.get,
        )


class AsyncCapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.get = async_to_streamed_response_wrapper(
            capabilities.get,
        )
