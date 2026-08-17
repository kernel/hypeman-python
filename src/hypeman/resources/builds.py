# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, cast

import httpx

from ..types import build_list_params, build_create_params, build_events_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from ..types.build import Build
from .._base_client import make_request_options
from ..types.build_event import BuildEvent
from ..types.build_list_response import BuildListResponse

__all__ = ["BuildsResource", "AsyncBuildsResource"]


class BuildsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return BuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return BuildsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source: FileTypes,
        base_image_digest: str | Omit = omit,
        builder_id: str | Omit = omit,
        cache_scope: str | Omit = omit,
        cpus: int | Omit = omit,
        dockerfile: str | Omit = omit,
        global_cache_key: str | Omit = omit,
        image_name: str | Omit = omit,
        is_admin_build: str | Omit = omit,
        memory_mb: int | Omit = omit,
        secrets: str | Omit = omit,
        tags: str | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Build:
        """Creates a new build job.

        Source code should be uploaded as a tar.gz archive in
        the multipart form data.

        Args:
          source: Source tarball (tar.gz) containing application code and optionally a Dockerfile

          base_image_digest: Optional pinned base image digest

          builder_id: Optional Builder ID whose persistent cache disk backs this build. This is the
              only builder selector. One build at a time runs on a builder; builds for the
              same builder are serialized.

          cache_scope: Tenant-specific cache key prefix

          cpus: Number of vCPUs for builder VM (default 2)

          dockerfile: Dockerfile content. Required if not included in the source tarball.

          global_cache_key: Global cache identifier (e.g., "node", "python", "ubuntu", "browser"). When
              specified, the build will import from cache/global/{key}. Admin builds will also
              export to this location.

          image_name: Custom image name for the build output. When set, the image is pushed to
              {registry}/{image_name} instead of {registry}/builds/{id}.

          is_admin_build: Set to "true" to grant push access to global cache (operator-only). Admin builds
              can populate the shared global cache that all tenant builds read from.

          memory_mb: Memory limit for builder VM in MB (default 2048)

          secrets: JSON array of secret references to inject during build. Each object has "id"
              (required) for use with --mount=type=secret,id=... Example: [{"id":
              "npm_token"}, {"id": "github_token"}]

          tags: JSON object of tags. Example: {"team":"backend","env":"staging"}

          timeout_seconds: Build timeout (default 600)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "source": source,
                "base_image_digest": base_image_digest,
                "builder_id": builder_id,
                "cache_scope": cache_scope,
                "cpus": cpus,
                "dockerfile": dockerfile,
                "global_cache_key": global_cache_key,
                "image_name": image_name,
                "is_admin_build": is_admin_build,
                "memory_mb": memory_mb,
                "secrets": secrets,
                "tags": tags,
                "timeout_seconds": timeout_seconds,
            },
            [["source"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["source"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/builds",
            body=maybe_transform(body, build_create_params.BuildCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Build,
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
    ) -> BuildListResponse:
        """
        List builds

        Args:
          tags: Filter builds by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/builds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tags": tags}, build_list_params.BuildListParams),
            ),
            cast_to=BuildListResponse,
        )

    def cancel(
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
        Cancel build

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
            path_template("/builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def events(
        self,
        id: str,
        *,
        follow: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[BuildEvent]:
        """Streams build events as Server-Sent Events.

        Events include:

        - `log`: Build log lines with timestamp and content
        - `status`: Build status changes (queued→building→pushing→ready/failed)
        - `heartbeat`: Keep-alive events sent every 30s to prevent connection timeouts

        Returns existing logs as events, then continues streaming if follow=true.

        Args:
          follow: Continue streaming new events after initial output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/builds/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"follow": follow}, build_events_params.BuildEventsParams),
            ),
            cast_to=BuildEvent,
            stream=True,
            stream_cls=Stream[BuildEvent],
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
    ) -> Build:
        """
        Get build details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Build,
        )


class AsyncBuildsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/hypeman-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/hypeman-python#with_streaming_response
        """
        return AsyncBuildsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source: FileTypes,
        base_image_digest: str | Omit = omit,
        builder_id: str | Omit = omit,
        cache_scope: str | Omit = omit,
        cpus: int | Omit = omit,
        dockerfile: str | Omit = omit,
        global_cache_key: str | Omit = omit,
        image_name: str | Omit = omit,
        is_admin_build: str | Omit = omit,
        memory_mb: int | Omit = omit,
        secrets: str | Omit = omit,
        tags: str | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Build:
        """Creates a new build job.

        Source code should be uploaded as a tar.gz archive in
        the multipart form data.

        Args:
          source: Source tarball (tar.gz) containing application code and optionally a Dockerfile

          base_image_digest: Optional pinned base image digest

          builder_id: Optional Builder ID whose persistent cache disk backs this build. This is the
              only builder selector. One build at a time runs on a builder; builds for the
              same builder are serialized.

          cache_scope: Tenant-specific cache key prefix

          cpus: Number of vCPUs for builder VM (default 2)

          dockerfile: Dockerfile content. Required if not included in the source tarball.

          global_cache_key: Global cache identifier (e.g., "node", "python", "ubuntu", "browser"). When
              specified, the build will import from cache/global/{key}. Admin builds will also
              export to this location.

          image_name: Custom image name for the build output. When set, the image is pushed to
              {registry}/{image_name} instead of {registry}/builds/{id}.

          is_admin_build: Set to "true" to grant push access to global cache (operator-only). Admin builds
              can populate the shared global cache that all tenant builds read from.

          memory_mb: Memory limit for builder VM in MB (default 2048)

          secrets: JSON array of secret references to inject during build. Each object has "id"
              (required) for use with --mount=type=secret,id=... Example: [{"id":
              "npm_token"}, {"id": "github_token"}]

          tags: JSON object of tags. Example: {"team":"backend","env":"staging"}

          timeout_seconds: Build timeout (default 600)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "source": source,
                "base_image_digest": base_image_digest,
                "builder_id": builder_id,
                "cache_scope": cache_scope,
                "cpus": cpus,
                "dockerfile": dockerfile,
                "global_cache_key": global_cache_key,
                "image_name": image_name,
                "is_admin_build": is_admin_build,
                "memory_mb": memory_mb,
                "secrets": secrets,
                "tags": tags,
                "timeout_seconds": timeout_seconds,
            },
            [["source"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["source"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/builds",
            body=await async_maybe_transform(body, build_create_params.BuildCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Build,
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
    ) -> BuildListResponse:
        """
        List builds

        Args:
          tags: Filter builds by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/builds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tags": tags}, build_list_params.BuildListParams),
            ),
            cast_to=BuildListResponse,
        )

    async def cancel(
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
        Cancel build

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
            path_template("/builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def events(
        self,
        id: str,
        *,
        follow: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[BuildEvent]:
        """Streams build events as Server-Sent Events.

        Events include:

        - `log`: Build log lines with timestamp and content
        - `status`: Build status changes (queued→building→pushing→ready/failed)
        - `heartbeat`: Keep-alive events sent every 30s to prevent connection timeouts

        Returns existing logs as events, then continues streaming if follow=true.

        Args:
          follow: Continue streaming new events after initial output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/builds/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"follow": follow}, build_events_params.BuildEventsParams),
            ),
            cast_to=BuildEvent,
            stream=True,
            stream_cls=AsyncStream[BuildEvent],
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
    ) -> Build:
        """
        Get build details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Build,
        )


class BuildsResourceWithRawResponse:
    def __init__(self, builds: BuildsResource) -> None:
        self._builds = builds

        self.create = to_raw_response_wrapper(
            builds.create,
        )
        self.list = to_raw_response_wrapper(
            builds.list,
        )
        self.cancel = to_raw_response_wrapper(
            builds.cancel,
        )
        self.events = to_raw_response_wrapper(
            builds.events,
        )
        self.get = to_raw_response_wrapper(
            builds.get,
        )


class AsyncBuildsResourceWithRawResponse:
    def __init__(self, builds: AsyncBuildsResource) -> None:
        self._builds = builds

        self.create = async_to_raw_response_wrapper(
            builds.create,
        )
        self.list = async_to_raw_response_wrapper(
            builds.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            builds.cancel,
        )
        self.events = async_to_raw_response_wrapper(
            builds.events,
        )
        self.get = async_to_raw_response_wrapper(
            builds.get,
        )


class BuildsResourceWithStreamingResponse:
    def __init__(self, builds: BuildsResource) -> None:
        self._builds = builds

        self.create = to_streamed_response_wrapper(
            builds.create,
        )
        self.list = to_streamed_response_wrapper(
            builds.list,
        )
        self.cancel = to_streamed_response_wrapper(
            builds.cancel,
        )
        self.events = to_streamed_response_wrapper(
            builds.events,
        )
        self.get = to_streamed_response_wrapper(
            builds.get,
        )


class AsyncBuildsResourceWithStreamingResponse:
    def __init__(self, builds: AsyncBuildsResource) -> None:
        self._builds = builds

        self.create = async_to_streamed_response_wrapper(
            builds.create,
        )
        self.list = async_to_streamed_response_wrapper(
            builds.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            builds.cancel,
        )
        self.events = async_to_streamed_response_wrapper(
            builds.events,
        )
        self.get = async_to_streamed_response_wrapper(
            builds.get,
        )
