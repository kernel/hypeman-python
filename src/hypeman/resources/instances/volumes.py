# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.instances import volume_attach_params

__all__ = ["VolumesResource", "AsyncVolumesResource"]


class VolumesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return VolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return VolumesResourceWithStreamingResponse(self)

    def attach(
        self,
        volume_id: str,
        *,
        id: str,
        mount_path: str,
        readonly: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Attach volume to instance

        Args:
          mount_path: Path where volume should be mounted

          readonly: Mount as read-only

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._post(
            path_template("/instances/{id}/volumes/{volume_id}", id=id, volume_id=volume_id),
            body=maybe_transform(
                {
                    "mount_path": mount_path,
                    "readonly": readonly,
                },
                volume_attach_params.VolumeAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    def detach(
        self,
        volume_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Detach volume from instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._delete(
            path_template("/instances/{id}/volumes/{volume_id}", id=id, volume_id=volume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )


class AsyncVolumesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncVolumesResourceWithStreamingResponse(self)

    async def attach(
        self,
        volume_id: str,
        *,
        id: str,
        mount_path: str,
        readonly: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Attach volume to instance

        Args:
          mount_path: Path where volume should be mounted

          readonly: Mount as read-only

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._post(
            path_template("/instances/{id}/volumes/{volume_id}", id=id, volume_id=volume_id),
            body=await async_maybe_transform(
                {
                    "mount_path": mount_path,
                    "readonly": readonly,
                },
                volume_attach_params.VolumeAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )

    async def detach(
        self,
        volume_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Detach volume from instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._delete(
            path_template("/instances/{id}/volumes/{volume_id}", id=id, volume_id=volume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instance,
        )


class VolumesResourceWithRawResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.attach = to_raw_response_wrapper(
            volumes.attach,
        )
        self.detach = to_raw_response_wrapper(
            volumes.detach,
        )


class AsyncVolumesResourceWithRawResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.attach = async_to_raw_response_wrapper(
            volumes.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            volumes.detach,
        )


class VolumesResourceWithStreamingResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.attach = to_streamed_response_wrapper(
            volumes.attach,
        )
        self.detach = to_streamed_response_wrapper(
            volumes.detach,
        )


class AsyncVolumesResourceWithStreamingResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.attach = async_to_streamed_response_wrapper(
            volumes.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            volumes.detach,
        )
