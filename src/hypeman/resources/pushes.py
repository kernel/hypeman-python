# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import push_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.push import Push
from .._base_client import make_request_options
from ..types.push_list_response import PushListResponse
from ..types.push_credentials_param import PushCredentialsParam

__all__ = ["PushesResource", "AsyncPushesResource"]


class PushesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PushesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return PushesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PushesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return PushesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image: str,
        target: str,
        credentials: PushCredentialsParam | Omit = omit,
        insecure: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Push:
        """
        Creates a push job that exports a hypeman image from the local OCI cache to a
        remote registry (e.g. AWS ECR, Docker Hub). Only images in the ready state can
        be pushed.

        Args:
          image: Hypeman image name to push (tag or digest form)

          target: Full remote reference to push to

          credentials: Docker-style registry credentials borrowed for one image pull or push request.
              They remain in memory and are never persisted or logged. When omitted or empty,
              the server's own registry credentials are used. An interrupted credentialed
              operation must be retried with fresh credentials.

          insecure: Allow pushing to plain-HTTP registries

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pushes",
            body=maybe_transform(
                {
                    "image": image,
                    "target": target,
                    "credentials": credentials,
                    "insecure": insecure,
                },
                push_create_params.PushCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Push,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PushListResponse:
        """Lists outbound image push jobs, newest first."""
        return self._get(
            "/pushes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PushListResponse,
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
    ) -> Push:
        """
        Get push details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/pushes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Push,
        )


class AsyncPushesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPushesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPushesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPushesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncPushesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image: str,
        target: str,
        credentials: PushCredentialsParam | Omit = omit,
        insecure: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Push:
        """
        Creates a push job that exports a hypeman image from the local OCI cache to a
        remote registry (e.g. AWS ECR, Docker Hub). Only images in the ready state can
        be pushed.

        Args:
          image: Hypeman image name to push (tag or digest form)

          target: Full remote reference to push to

          credentials: Docker-style registry credentials borrowed for one image pull or push request.
              They remain in memory and are never persisted or logged. When omitted or empty,
              the server's own registry credentials are used. An interrupted credentialed
              operation must be retried with fresh credentials.

          insecure: Allow pushing to plain-HTTP registries

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pushes",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "target": target,
                    "credentials": credentials,
                    "insecure": insecure,
                },
                push_create_params.PushCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Push,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PushListResponse:
        """Lists outbound image push jobs, newest first."""
        return await self._get(
            "/pushes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PushListResponse,
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
    ) -> Push:
        """
        Get push details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/pushes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Push,
        )


class PushesResourceWithRawResponse:
    def __init__(self, pushes: PushesResource) -> None:
        self._pushes = pushes

        self.create = to_raw_response_wrapper(
            pushes.create,
        )
        self.list = to_raw_response_wrapper(
            pushes.list,
        )
        self.get = to_raw_response_wrapper(
            pushes.get,
        )


class AsyncPushesResourceWithRawResponse:
    def __init__(self, pushes: AsyncPushesResource) -> None:
        self._pushes = pushes

        self.create = async_to_raw_response_wrapper(
            pushes.create,
        )
        self.list = async_to_raw_response_wrapper(
            pushes.list,
        )
        self.get = async_to_raw_response_wrapper(
            pushes.get,
        )


class PushesResourceWithStreamingResponse:
    def __init__(self, pushes: PushesResource) -> None:
        self._pushes = pushes

        self.create = to_streamed_response_wrapper(
            pushes.create,
        )
        self.list = to_streamed_response_wrapper(
            pushes.list,
        )
        self.get = to_streamed_response_wrapper(
            pushes.get,
        )


class AsyncPushesResourceWithStreamingResponse:
    def __init__(self, pushes: AsyncPushesResource) -> None:
        self._pushes = pushes

        self.create = async_to_streamed_response_wrapper(
            pushes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            pushes.list,
        )
        self.get = async_to_streamed_response_wrapper(
            pushes.get,
        )
