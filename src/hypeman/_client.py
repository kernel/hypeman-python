# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import HypemanError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        builds,
        health,
        images,
        pushes,
        devices,
        volumes,
        builders,
        ingresses,
        instances,
        resources,
        snapshots,
        capabilities,
    )
    from .resources.builds import BuildsResource, AsyncBuildsResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.images import ImagesResource, AsyncImagesResource
    from .resources.pushes import PushesResource, AsyncPushesResource
    from .resources.devices import DevicesResource, AsyncDevicesResource
    from .resources.volumes import VolumesResource, AsyncVolumesResource
    from .resources.builders import BuildersResource, AsyncBuildersResource
    from .resources.ingresses import IngressesResource, AsyncIngressesResource
    from .resources.resources import ResourcesResource, AsyncResourcesResource
    from .resources.snapshots import SnapshotsResource, AsyncSnapshotsResource
    from .resources.capabilities import CapabilitiesResource, AsyncCapabilitiesResource
    from .resources.instances.instances import InstancesResource, AsyncInstancesResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Hypeman", "AsyncHypeman", "Client", "AsyncClient"]


class Hypeman(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Hypeman client instance.

        This automatically infers the `api_key` argument from the `HYPEMAN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HYPEMAN_API_KEY")
        if api_key is None:
            raise HypemanError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPEMAN_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("HYPEMAN_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:4973"

        custom_headers_env = os.environ.get("HYPEMAN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def capabilities(self) -> CapabilitiesResource:
        from .resources.capabilities import CapabilitiesResource

        return CapabilitiesResource(self)

    @cached_property
    def images(self) -> ImagesResource:
        from .resources.images import ImagesResource

        return ImagesResource(self)

    @cached_property
    def instances(self) -> InstancesResource:
        from .resources.instances import InstancesResource

        return InstancesResource(self)

    @cached_property
    def snapshots(self) -> SnapshotsResource:
        from .resources.snapshots import SnapshotsResource

        return SnapshotsResource(self)

    @cached_property
    def volumes(self) -> VolumesResource:
        from .resources.volumes import VolumesResource

        return VolumesResource(self)

    @cached_property
    def devices(self) -> DevicesResource:
        from .resources.devices import DevicesResource

        return DevicesResource(self)

    @cached_property
    def ingresses(self) -> IngressesResource:
        from .resources.ingresses import IngressesResource

        return IngressesResource(self)

    @cached_property
    def resources(self) -> ResourcesResource:
        from .resources.resources import ResourcesResource

        return ResourcesResource(self)

    @cached_property
    def builders(self) -> BuildersResource:
        from .resources.builders import BuildersResource

        return BuildersResource(self)

    @cached_property
    def builds(self) -> BuildsResource:
        from .resources.builds import BuildsResource

        return BuildsResource(self)

    @cached_property
    def pushes(self) -> PushesResource:
        from .resources.pushes import PushesResource

        return PushesResource(self)

    @cached_property
    def with_raw_response(self) -> HypemanWithRawResponse:
        return HypemanWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HypemanWithStreamedResponse:
        return HypemanWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHypeman(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHypeman client instance.

        This automatically infers the `api_key` argument from the `HYPEMAN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HYPEMAN_API_KEY")
        if api_key is None:
            raise HypemanError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPEMAN_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("HYPEMAN_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:4973"

        custom_headers_env = os.environ.get("HYPEMAN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def capabilities(self) -> AsyncCapabilitiesResource:
        from .resources.capabilities import AsyncCapabilitiesResource

        return AsyncCapabilitiesResource(self)

    @cached_property
    def images(self) -> AsyncImagesResource:
        from .resources.images import AsyncImagesResource

        return AsyncImagesResource(self)

    @cached_property
    def instances(self) -> AsyncInstancesResource:
        from .resources.instances import AsyncInstancesResource

        return AsyncInstancesResource(self)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResource:
        from .resources.snapshots import AsyncSnapshotsResource

        return AsyncSnapshotsResource(self)

    @cached_property
    def volumes(self) -> AsyncVolumesResource:
        from .resources.volumes import AsyncVolumesResource

        return AsyncVolumesResource(self)

    @cached_property
    def devices(self) -> AsyncDevicesResource:
        from .resources.devices import AsyncDevicesResource

        return AsyncDevicesResource(self)

    @cached_property
    def ingresses(self) -> AsyncIngressesResource:
        from .resources.ingresses import AsyncIngressesResource

        return AsyncIngressesResource(self)

    @cached_property
    def resources(self) -> AsyncResourcesResource:
        from .resources.resources import AsyncResourcesResource

        return AsyncResourcesResource(self)

    @cached_property
    def builders(self) -> AsyncBuildersResource:
        from .resources.builders import AsyncBuildersResource

        return AsyncBuildersResource(self)

    @cached_property
    def builds(self) -> AsyncBuildsResource:
        from .resources.builds import AsyncBuildsResource

        return AsyncBuildsResource(self)

    @cached_property
    def pushes(self) -> AsyncPushesResource:
        from .resources.pushes import AsyncPushesResource

        return AsyncPushesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncHypemanWithRawResponse:
        return AsyncHypemanWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHypemanWithStreamedResponse:
        return AsyncHypemanWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HypemanWithRawResponse:
    _client: Hypeman

    def __init__(self, client: Hypeman) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def capabilities(self) -> capabilities.CapabilitiesResourceWithRawResponse:
        from .resources.capabilities import CapabilitiesResourceWithRawResponse

        return CapabilitiesResourceWithRawResponse(self._client.capabilities)

    @cached_property
    def images(self) -> images.ImagesResourceWithRawResponse:
        from .resources.images import ImagesResourceWithRawResponse

        return ImagesResourceWithRawResponse(self._client.images)

    @cached_property
    def instances(self) -> instances.InstancesResourceWithRawResponse:
        from .resources.instances import InstancesResourceWithRawResponse

        return InstancesResourceWithRawResponse(self._client.instances)

    @cached_property
    def snapshots(self) -> snapshots.SnapshotsResourceWithRawResponse:
        from .resources.snapshots import SnapshotsResourceWithRawResponse

        return SnapshotsResourceWithRawResponse(self._client.snapshots)

    @cached_property
    def volumes(self) -> volumes.VolumesResourceWithRawResponse:
        from .resources.volumes import VolumesResourceWithRawResponse

        return VolumesResourceWithRawResponse(self._client.volumes)

    @cached_property
    def devices(self) -> devices.DevicesResourceWithRawResponse:
        from .resources.devices import DevicesResourceWithRawResponse

        return DevicesResourceWithRawResponse(self._client.devices)

    @cached_property
    def ingresses(self) -> ingresses.IngressesResourceWithRawResponse:
        from .resources.ingresses import IngressesResourceWithRawResponse

        return IngressesResourceWithRawResponse(self._client.ingresses)

    @cached_property
    def resources(self) -> resources.ResourcesResourceWithRawResponse:
        from .resources.resources import ResourcesResourceWithRawResponse

        return ResourcesResourceWithRawResponse(self._client.resources)

    @cached_property
    def builders(self) -> builders.BuildersResourceWithRawResponse:
        from .resources.builders import BuildersResourceWithRawResponse

        return BuildersResourceWithRawResponse(self._client.builders)

    @cached_property
    def builds(self) -> builds.BuildsResourceWithRawResponse:
        from .resources.builds import BuildsResourceWithRawResponse

        return BuildsResourceWithRawResponse(self._client.builds)

    @cached_property
    def pushes(self) -> pushes.PushesResourceWithRawResponse:
        from .resources.pushes import PushesResourceWithRawResponse

        return PushesResourceWithRawResponse(self._client.pushes)


class AsyncHypemanWithRawResponse:
    _client: AsyncHypeman

    def __init__(self, client: AsyncHypeman) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def capabilities(self) -> capabilities.AsyncCapabilitiesResourceWithRawResponse:
        from .resources.capabilities import AsyncCapabilitiesResourceWithRawResponse

        return AsyncCapabilitiesResourceWithRawResponse(self._client.capabilities)

    @cached_property
    def images(self) -> images.AsyncImagesResourceWithRawResponse:
        from .resources.images import AsyncImagesResourceWithRawResponse

        return AsyncImagesResourceWithRawResponse(self._client.images)

    @cached_property
    def instances(self) -> instances.AsyncInstancesResourceWithRawResponse:
        from .resources.instances import AsyncInstancesResourceWithRawResponse

        return AsyncInstancesResourceWithRawResponse(self._client.instances)

    @cached_property
    def snapshots(self) -> snapshots.AsyncSnapshotsResourceWithRawResponse:
        from .resources.snapshots import AsyncSnapshotsResourceWithRawResponse

        return AsyncSnapshotsResourceWithRawResponse(self._client.snapshots)

    @cached_property
    def volumes(self) -> volumes.AsyncVolumesResourceWithRawResponse:
        from .resources.volumes import AsyncVolumesResourceWithRawResponse

        return AsyncVolumesResourceWithRawResponse(self._client.volumes)

    @cached_property
    def devices(self) -> devices.AsyncDevicesResourceWithRawResponse:
        from .resources.devices import AsyncDevicesResourceWithRawResponse

        return AsyncDevicesResourceWithRawResponse(self._client.devices)

    @cached_property
    def ingresses(self) -> ingresses.AsyncIngressesResourceWithRawResponse:
        from .resources.ingresses import AsyncIngressesResourceWithRawResponse

        return AsyncIngressesResourceWithRawResponse(self._client.ingresses)

    @cached_property
    def resources(self) -> resources.AsyncResourcesResourceWithRawResponse:
        from .resources.resources import AsyncResourcesResourceWithRawResponse

        return AsyncResourcesResourceWithRawResponse(self._client.resources)

    @cached_property
    def builders(self) -> builders.AsyncBuildersResourceWithRawResponse:
        from .resources.builders import AsyncBuildersResourceWithRawResponse

        return AsyncBuildersResourceWithRawResponse(self._client.builders)

    @cached_property
    def builds(self) -> builds.AsyncBuildsResourceWithRawResponse:
        from .resources.builds import AsyncBuildsResourceWithRawResponse

        return AsyncBuildsResourceWithRawResponse(self._client.builds)

    @cached_property
    def pushes(self) -> pushes.AsyncPushesResourceWithRawResponse:
        from .resources.pushes import AsyncPushesResourceWithRawResponse

        return AsyncPushesResourceWithRawResponse(self._client.pushes)


class HypemanWithStreamedResponse:
    _client: Hypeman

    def __init__(self, client: Hypeman) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def capabilities(self) -> capabilities.CapabilitiesResourceWithStreamingResponse:
        from .resources.capabilities import CapabilitiesResourceWithStreamingResponse

        return CapabilitiesResourceWithStreamingResponse(self._client.capabilities)

    @cached_property
    def images(self) -> images.ImagesResourceWithStreamingResponse:
        from .resources.images import ImagesResourceWithStreamingResponse

        return ImagesResourceWithStreamingResponse(self._client.images)

    @cached_property
    def instances(self) -> instances.InstancesResourceWithStreamingResponse:
        from .resources.instances import InstancesResourceWithStreamingResponse

        return InstancesResourceWithStreamingResponse(self._client.instances)

    @cached_property
    def snapshots(self) -> snapshots.SnapshotsResourceWithStreamingResponse:
        from .resources.snapshots import SnapshotsResourceWithStreamingResponse

        return SnapshotsResourceWithStreamingResponse(self._client.snapshots)

    @cached_property
    def volumes(self) -> volumes.VolumesResourceWithStreamingResponse:
        from .resources.volumes import VolumesResourceWithStreamingResponse

        return VolumesResourceWithStreamingResponse(self._client.volumes)

    @cached_property
    def devices(self) -> devices.DevicesResourceWithStreamingResponse:
        from .resources.devices import DevicesResourceWithStreamingResponse

        return DevicesResourceWithStreamingResponse(self._client.devices)

    @cached_property
    def ingresses(self) -> ingresses.IngressesResourceWithStreamingResponse:
        from .resources.ingresses import IngressesResourceWithStreamingResponse

        return IngressesResourceWithStreamingResponse(self._client.ingresses)

    @cached_property
    def resources(self) -> resources.ResourcesResourceWithStreamingResponse:
        from .resources.resources import ResourcesResourceWithStreamingResponse

        return ResourcesResourceWithStreamingResponse(self._client.resources)

    @cached_property
    def builders(self) -> builders.BuildersResourceWithStreamingResponse:
        from .resources.builders import BuildersResourceWithStreamingResponse

        return BuildersResourceWithStreamingResponse(self._client.builders)

    @cached_property
    def builds(self) -> builds.BuildsResourceWithStreamingResponse:
        from .resources.builds import BuildsResourceWithStreamingResponse

        return BuildsResourceWithStreamingResponse(self._client.builds)

    @cached_property
    def pushes(self) -> pushes.PushesResourceWithStreamingResponse:
        from .resources.pushes import PushesResourceWithStreamingResponse

        return PushesResourceWithStreamingResponse(self._client.pushes)


class AsyncHypemanWithStreamedResponse:
    _client: AsyncHypeman

    def __init__(self, client: AsyncHypeman) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def capabilities(self) -> capabilities.AsyncCapabilitiesResourceWithStreamingResponse:
        from .resources.capabilities import AsyncCapabilitiesResourceWithStreamingResponse

        return AsyncCapabilitiesResourceWithStreamingResponse(self._client.capabilities)

    @cached_property
    def images(self) -> images.AsyncImagesResourceWithStreamingResponse:
        from .resources.images import AsyncImagesResourceWithStreamingResponse

        return AsyncImagesResourceWithStreamingResponse(self._client.images)

    @cached_property
    def instances(self) -> instances.AsyncInstancesResourceWithStreamingResponse:
        from .resources.instances import AsyncInstancesResourceWithStreamingResponse

        return AsyncInstancesResourceWithStreamingResponse(self._client.instances)

    @cached_property
    def snapshots(self) -> snapshots.AsyncSnapshotsResourceWithStreamingResponse:
        from .resources.snapshots import AsyncSnapshotsResourceWithStreamingResponse

        return AsyncSnapshotsResourceWithStreamingResponse(self._client.snapshots)

    @cached_property
    def volumes(self) -> volumes.AsyncVolumesResourceWithStreamingResponse:
        from .resources.volumes import AsyncVolumesResourceWithStreamingResponse

        return AsyncVolumesResourceWithStreamingResponse(self._client.volumes)

    @cached_property
    def devices(self) -> devices.AsyncDevicesResourceWithStreamingResponse:
        from .resources.devices import AsyncDevicesResourceWithStreamingResponse

        return AsyncDevicesResourceWithStreamingResponse(self._client.devices)

    @cached_property
    def ingresses(self) -> ingresses.AsyncIngressesResourceWithStreamingResponse:
        from .resources.ingresses import AsyncIngressesResourceWithStreamingResponse

        return AsyncIngressesResourceWithStreamingResponse(self._client.ingresses)

    @cached_property
    def resources(self) -> resources.AsyncResourcesResourceWithStreamingResponse:
        from .resources.resources import AsyncResourcesResourceWithStreamingResponse

        return AsyncResourcesResourceWithStreamingResponse(self._client.resources)

    @cached_property
    def builders(self) -> builders.AsyncBuildersResourceWithStreamingResponse:
        from .resources.builders import AsyncBuildersResourceWithStreamingResponse

        return AsyncBuildersResourceWithStreamingResponse(self._client.builders)

    @cached_property
    def builds(self) -> builds.AsyncBuildsResourceWithStreamingResponse:
        from .resources.builds import AsyncBuildsResourceWithStreamingResponse

        return AsyncBuildsResourceWithStreamingResponse(self._client.builds)

    @cached_property
    def pushes(self) -> pushes.AsyncPushesResourceWithStreamingResponse:
        from .resources.pushes import AsyncPushesResourceWithStreamingResponse

        return AsyncPushesResourceWithStreamingResponse(self._client.pushes)


Client = Hypeman

AsyncClient = AsyncHypeman
