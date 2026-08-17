# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import ingress_list_params, ingress_create_params
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
from ..types.ingress import Ingress
from ..types.ingress_rule_param import IngressRuleParam
from ..types.ingress_list_response import IngressListResponse

__all__ = ["IngressesResource", "AsyncIngressesResource"]


class IngressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IngressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return IngressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return IngressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        rules: Iterable[IngressRuleParam],
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ingress:
        """
        Create ingress

        Args:
          name: Human-readable name (lowercase letters, digits, and dashes only; cannot start or
              end with a dash)

          rules: Routing rules for this ingress

          tags: User-defined key-value tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ingresses",
            body=maybe_transform(
                {
                    "name": name,
                    "rules": rules,
                    "tags": tags,
                },
                ingress_create_params.IngressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ingress,
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
    ) -> IngressListResponse:
        """
        List ingresses

        Args:
          tags: Filter ingresses by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ingresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tags": tags}, ingress_list_params.IngressListParams),
            ),
            cast_to=IngressListResponse,
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
        Delete ingress

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
            path_template("/ingresses/{id}", id=id),
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
    ) -> Ingress:
        """
        Get ingress details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/ingresses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ingress,
        )


class AsyncIngressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIngressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIngressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncIngressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        rules: Iterable[IngressRuleParam],
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ingress:
        """
        Create ingress

        Args:
          name: Human-readable name (lowercase letters, digits, and dashes only; cannot start or
              end with a dash)

          rules: Routing rules for this ingress

          tags: User-defined key-value tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ingresses",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rules": rules,
                    "tags": tags,
                },
                ingress_create_params.IngressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ingress,
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
    ) -> IngressListResponse:
        """
        List ingresses

        Args:
          tags: Filter ingresses by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ingresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tags": tags}, ingress_list_params.IngressListParams),
            ),
            cast_to=IngressListResponse,
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
        Delete ingress

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
            path_template("/ingresses/{id}", id=id),
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
    ) -> Ingress:
        """
        Get ingress details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/ingresses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ingress,
        )


class IngressesResourceWithRawResponse:
    def __init__(self, ingresses: IngressesResource) -> None:
        self._ingresses = ingresses

        self.create = to_raw_response_wrapper(
            ingresses.create,
        )
        self.list = to_raw_response_wrapper(
            ingresses.list,
        )
        self.delete = to_raw_response_wrapper(
            ingresses.delete,
        )
        self.get = to_raw_response_wrapper(
            ingresses.get,
        )


class AsyncIngressesResourceWithRawResponse:
    def __init__(self, ingresses: AsyncIngressesResource) -> None:
        self._ingresses = ingresses

        self.create = async_to_raw_response_wrapper(
            ingresses.create,
        )
        self.list = async_to_raw_response_wrapper(
            ingresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ingresses.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ingresses.get,
        )


class IngressesResourceWithStreamingResponse:
    def __init__(self, ingresses: IngressesResource) -> None:
        self._ingresses = ingresses

        self.create = to_streamed_response_wrapper(
            ingresses.create,
        )
        self.list = to_streamed_response_wrapper(
            ingresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            ingresses.delete,
        )
        self.get = to_streamed_response_wrapper(
            ingresses.get,
        )


class AsyncIngressesResourceWithStreamingResponse:
    def __init__(self, ingresses: AsyncIngressesResource) -> None:
        self._ingresses = ingresses

        self.create = async_to_streamed_response_wrapper(
            ingresses.create,
        )
        self.list = async_to_streamed_response_wrapper(
            ingresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ingresses.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ingresses.get,
        )
