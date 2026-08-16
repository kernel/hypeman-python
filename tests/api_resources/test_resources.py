# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import Resources, MemoryReclaimResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hypeman) -> None:
        resource = client.resources.get()
        assert_matches_type(Resources, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hypeman) -> None:
        response = client.resources.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(Resources, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hypeman) -> None:
        with client.resources.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(Resources, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reclaim_memory(self, client: Hypeman) -> None:
        resource = client.resources.reclaim_memory(
            reclaim_bytes=536870912,
        )
        assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reclaim_memory_with_all_params(self, client: Hypeman) -> None:
        resource = client.resources.reclaim_memory(
            reclaim_bytes=536870912,
            dry_run=True,
            hold_for="5m",
            reason="prepare for another vm start",
        )
        assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reclaim_memory(self, client: Hypeman) -> None:
        response = client.resources.with_raw_response.reclaim_memory(
            reclaim_bytes=536870912,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reclaim_memory(self, client: Hypeman) -> None:
        with client.resources.with_streaming_response.reclaim_memory(
            reclaim_bytes=536870912,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHypeman) -> None:
        resource = await async_client.resources.get()
        assert_matches_type(Resources, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHypeman) -> None:
        response = await async_client.resources.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(Resources, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHypeman) -> None:
        async with async_client.resources.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(Resources, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reclaim_memory(self, async_client: AsyncHypeman) -> None:
        resource = await async_client.resources.reclaim_memory(
            reclaim_bytes=536870912,
        )
        assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reclaim_memory_with_all_params(self, async_client: AsyncHypeman) -> None:
        resource = await async_client.resources.reclaim_memory(
            reclaim_bytes=536870912,
            dry_run=True,
            hold_for="5m",
            reason="prepare for another vm start",
        )
        assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reclaim_memory(self, async_client: AsyncHypeman) -> None:
        response = await async_client.resources.with_raw_response.reclaim_memory(
            reclaim_bytes=536870912,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reclaim_memory(self, async_client: AsyncHypeman) -> None:
        async with async_client.resources.with_streaming_response.reclaim_memory(
            reclaim_bytes=536870912,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(MemoryReclaimResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True
