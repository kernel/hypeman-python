# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import Ingress, IngressListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIngresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hypeman) -> None:
        ingress = client.ingresses.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {"hostname": "{instance}.example.com"},
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                }
            ],
        )
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hypeman) -> None:
        ingress = client.ingresses.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {
                        "hostname": "{instance}.example.com",
                        "port": 8080,
                    },
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                    "redirect_http": True,
                    "request_header_auth": {
                        "header": "X-Ingress-Verification",
                        "value": "0123456789abcdef0123456789abcdef",
                    },
                    "tls": True,
                }
            ],
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hypeman) -> None:
        response = client.ingresses.with_raw_response.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {"hostname": "{instance}.example.com"},
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hypeman) -> None:
        with client.ingresses.with_streaming_response.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {"hostname": "{instance}.example.com"},
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert_matches_type(Ingress, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hypeman) -> None:
        ingress = client.ingresses.list()
        assert_matches_type(IngressListResponse, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hypeman) -> None:
        ingress = client.ingresses.list(
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(IngressListResponse, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hypeman) -> None:
        response = client.ingresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert_matches_type(IngressListResponse, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hypeman) -> None:
        with client.ingresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert_matches_type(IngressListResponse, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hypeman) -> None:
        ingress = client.ingresses.delete(
            "id",
        )
        assert ingress is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hypeman) -> None:
        response = client.ingresses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert ingress is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hypeman) -> None:
        with client.ingresses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert ingress is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ingresses.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hypeman) -> None:
        ingress = client.ingresses.get(
            "id",
        )
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hypeman) -> None:
        response = client.ingresses.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hypeman) -> None:
        with client.ingresses.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert_matches_type(Ingress, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ingresses.with_raw_response.get(
                "",
            )


class TestAsyncIngresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHypeman) -> None:
        ingress = await async_client.ingresses.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {"hostname": "{instance}.example.com"},
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                }
            ],
        )
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHypeman) -> None:
        ingress = await async_client.ingresses.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {
                        "hostname": "{instance}.example.com",
                        "port": 8080,
                    },
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                    "redirect_http": True,
                    "request_header_auth": {
                        "header": "X-Ingress-Verification",
                        "value": "0123456789abcdef0123456789abcdef",
                    },
                    "tls": True,
                }
            ],
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHypeman) -> None:
        response = await async_client.ingresses.with_raw_response.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {"hostname": "{instance}.example.com"},
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHypeman) -> None:
        async with async_client.ingresses.with_streaming_response.create(
            name="my-api-ingress",
            rules=[
                {
                    "match": {"hostname": "{instance}.example.com"},
                    "target": {
                        "instance": "{instance}",
                        "port": 8080,
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert_matches_type(Ingress, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHypeman) -> None:
        ingress = await async_client.ingresses.list()
        assert_matches_type(IngressListResponse, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHypeman) -> None:
        ingress = await async_client.ingresses.list(
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(IngressListResponse, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHypeman) -> None:
        response = await async_client.ingresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert_matches_type(IngressListResponse, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHypeman) -> None:
        async with async_client.ingresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert_matches_type(IngressListResponse, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHypeman) -> None:
        ingress = await async_client.ingresses.delete(
            "id",
        )
        assert ingress is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHypeman) -> None:
        response = await async_client.ingresses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert ingress is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHypeman) -> None:
        async with async_client.ingresses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert ingress is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ingresses.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHypeman) -> None:
        ingress = await async_client.ingresses.get(
            "id",
        )
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHypeman) -> None:
        response = await async_client.ingresses.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert_matches_type(Ingress, ingress, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHypeman) -> None:
        async with async_client.ingresses.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert_matches_type(Ingress, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ingresses.with_raw_response.get(
                "",
            )
