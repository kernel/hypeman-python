# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import Push, PushListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPushes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hypeman) -> None:
        push = client.pushes.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
        )
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hypeman) -> None:
        push = client.pushes.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
            credentials={
                "password": "password",
                "registry_token": "registry_token",
                "username": "username",
            },
            insecure=True,
        )
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hypeman) -> None:
        response = client.pushes.with_raw_response.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = response.parse()
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hypeman) -> None:
        with client.pushes.with_streaming_response.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = response.parse()
            assert_matches_type(Push, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hypeman) -> None:
        push = client.pushes.list()
        assert_matches_type(PushListResponse, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hypeman) -> None:
        response = client.pushes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = response.parse()
        assert_matches_type(PushListResponse, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hypeman) -> None:
        with client.pushes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = response.parse()
            assert_matches_type(PushListResponse, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hypeman) -> None:
        push = client.pushes.get(
            "id",
        )
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hypeman) -> None:
        response = client.pushes.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = response.parse()
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hypeman) -> None:
        with client.pushes.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = response.parse()
            assert_matches_type(Push, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pushes.with_raw_response.get(
                "",
            )


class TestAsyncPushes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHypeman) -> None:
        push = await async_client.pushes.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
        )
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHypeman) -> None:
        push = await async_client.pushes.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
            credentials={
                "password": "password",
                "registry_token": "registry_token",
                "username": "username",
            },
            insecure=True,
        )
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHypeman) -> None:
        response = await async_client.pushes.with_raw_response.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = await response.parse()
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHypeman) -> None:
        async with async_client.pushes.with_streaming_response.create(
            image="docker.io/library/alpine:latest",
            target="123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = await response.parse()
            assert_matches_type(Push, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHypeman) -> None:
        push = await async_client.pushes.list()
        assert_matches_type(PushListResponse, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHypeman) -> None:
        response = await async_client.pushes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = await response.parse()
        assert_matches_type(PushListResponse, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHypeman) -> None:
        async with async_client.pushes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = await response.parse()
            assert_matches_type(PushListResponse, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHypeman) -> None:
        push = await async_client.pushes.get(
            "id",
        )
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHypeman) -> None:
        response = await async_client.pushes.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = await response.parse()
        assert_matches_type(Push, push, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHypeman) -> None:
        async with async_client.pushes.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = await response.parse()
            assert_matches_type(Push, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pushes.with_raw_response.get(
                "",
            )
