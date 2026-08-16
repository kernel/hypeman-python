# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import builder_list_params, builder_create_params
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
from ..types.builder import Builder
from ..types.builder_list_response import BuilderListResponse

__all__ = ["BuildersResource", "AsyncBuildersResource"]


class BuildersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BuildersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return BuildersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BuildersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return BuildersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str | Omit = omit,
        disk_size_gb: int | Omit = omit,
        name: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Builder:
        """Creates a builder and its cache disk.

        One build at a time runs per builder.

        Args:
          id: Optional caller-supplied identifier, auto-generated if not provided

          disk_size_gb: Cache disk size in gigabytes. Omit to use the server default.

          name: Optional non-unique display name

          tags: User-defined key-value tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/builders",
            body=maybe_transform(
                {
                    "id": id,
                    "disk_size_gb": disk_size_gb,
                    "name": name,
                    "tags": tags,
                },
                builder_create_params.BuilderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Builder,
        )

    def list(
        self,
        *,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuilderListResponse:
        """
        List builders

        Args:
          tags: Filter builders by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/builders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tags": tags}, builder_list_params.BuilderListParams),
            ),
            cast_to=BuilderListResponse,
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
        Permanently deletes a builder and its cache disk.

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
            path_template("/builders/{id}", id=id),
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
    ) -> Builder:
        """
        Get builder details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/builders/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Builder,
        )

    def prune(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Builder:
        """Resets the builder's cache disk.

        The builder transitions to pruning, then ready.
        Builder identity is preserved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/builders/{id}/prune", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Builder,
        )


class AsyncBuildersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBuildersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBuildersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBuildersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncBuildersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str | Omit = omit,
        disk_size_gb: int | Omit = omit,
        name: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Builder:
        """Creates a builder and its cache disk.

        One build at a time runs per builder.

        Args:
          id: Optional caller-supplied identifier, auto-generated if not provided

          disk_size_gb: Cache disk size in gigabytes. Omit to use the server default.

          name: Optional non-unique display name

          tags: User-defined key-value tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/builders",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "disk_size_gb": disk_size_gb,
                    "name": name,
                    "tags": tags,
                },
                builder_create_params.BuilderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Builder,
        )

    async def list(
        self,
        *,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuilderListResponse:
        """
        List builders

        Args:
          tags: Filter builders by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/builders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tags": tags}, builder_list_params.BuilderListParams),
            ),
            cast_to=BuilderListResponse,
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
        Permanently deletes a builder and its cache disk.

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
            path_template("/builders/{id}", id=id),
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
    ) -> Builder:
        """
        Get builder details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/builders/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Builder,
        )

    async def prune(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Builder:
        """Resets the builder's cache disk.

        The builder transitions to pruning, then ready.
        Builder identity is preserved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/builders/{id}/prune", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Builder,
        )


class BuildersResourceWithRawResponse:
    def __init__(self, builders: BuildersResource) -> None:
        self._builders = builders

        self.create = to_raw_response_wrapper(
            builders.create,
        )
        self.list = to_raw_response_wrapper(
            builders.list,
        )
        self.delete = to_raw_response_wrapper(
            builders.delete,
        )
        self.get = to_raw_response_wrapper(
            builders.get,
        )
        self.prune = to_raw_response_wrapper(
            builders.prune,
        )


class AsyncBuildersResourceWithRawResponse:
    def __init__(self, builders: AsyncBuildersResource) -> None:
        self._builders = builders

        self.create = async_to_raw_response_wrapper(
            builders.create,
        )
        self.list = async_to_raw_response_wrapper(
            builders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            builders.delete,
        )
        self.get = async_to_raw_response_wrapper(
            builders.get,
        )
        self.prune = async_to_raw_response_wrapper(
            builders.prune,
        )


class BuildersResourceWithStreamingResponse:
    def __init__(self, builders: BuildersResource) -> None:
        self._builders = builders

        self.create = to_streamed_response_wrapper(
            builders.create,
        )
        self.list = to_streamed_response_wrapper(
            builders.list,
        )
        self.delete = to_streamed_response_wrapper(
            builders.delete,
        )
        self.get = to_streamed_response_wrapper(
            builders.get,
        )
        self.prune = to_streamed_response_wrapper(
            builders.prune,
        )


class AsyncBuildersResourceWithStreamingResponse:
    def __init__(self, builders: AsyncBuildersResource) -> None:
        self._builders = builders

        self.create = async_to_streamed_response_wrapper(
            builders.create,
        )
        self.list = async_to_streamed_response_wrapper(
            builders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            builders.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            builders.get,
        )
        self.prune = async_to_streamed_response_wrapper(
            builders.prune,
        )
