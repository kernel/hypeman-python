# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import (
    Volume,
    VolumeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hypeman) -> None:
        volume = client.volumes.create(
            name="my-data-volume",
            size_gb=10,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hypeman) -> None:
        volume = client.volumes.create(
            name="my-data-volume",
            size_gb=10,
            id="vol-data-1",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hypeman) -> None:
        response = client.volumes.with_raw_response.create(
            name="my-data-volume",
            size_gb=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hypeman) -> None:
        with client.volumes.with_streaming_response.create(
            name="my-data-volume",
            size_gb=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hypeman) -> None:
        volume = client.volumes.list()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hypeman) -> None:
        volume = client.volumes.list(
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hypeman) -> None:
        response = client.volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hypeman) -> None:
        with client.volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeListResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hypeman) -> None:
        volume = client.volumes.delete(
            "id",
        )
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hypeman) -> None:
        response = client.volumes.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hypeman) -> None:
        with client.volumes.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.volumes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_archive(self, client: Hypeman) -> None:
        volume = client.volumes.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_archive_with_all_params(self, client: Hypeman) -> None:
        volume = client.volumes.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
            id="id",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_from_archive(self, client: Hypeman) -> None:
        response = client.volumes.with_raw_response.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_from_archive(self, client: Hypeman) -> None:
        with client.volumes.with_streaming_response.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hypeman) -> None:
        volume = client.volumes.get(
            "id",
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hypeman) -> None:
        response = client.volumes.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hypeman) -> None:
        with client.volumes.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.volumes.with_raw_response.get(
                "",
            )


class TestAsyncVolumes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.create(
            name="my-data-volume",
            size_gb=10,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.create(
            name="my-data-volume",
            size_gb=10,
            id="vol-data-1",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHypeman) -> None:
        response = await async_client.volumes.with_raw_response.create(
            name="my-data-volume",
            size_gb=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHypeman) -> None:
        async with async_client.volumes.with_streaming_response.create(
            name="my-data-volume",
            size_gb=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.list()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.list(
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHypeman) -> None:
        response = await async_client.volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHypeman) -> None:
        async with async_client.volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeListResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.delete(
            "id",
        )
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHypeman) -> None:
        response = await async_client.volumes.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHypeman) -> None:
        async with async_client.volumes.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.volumes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_archive(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_archive_with_all_params(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
            id="id",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_from_archive(self, async_client: AsyncHypeman) -> None:
        response = await async_client.volumes.with_raw_response.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_from_archive(self, async_client: AsyncHypeman) -> None:
        async with async_client.volumes.with_streaming_response.create_from_archive(
            body=b"Example data",
            name="name",
            size_gb=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.volumes.get(
            "id",
        )
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHypeman) -> None:
        response = await async_client.volumes.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHypeman) -> None:
        async with async_client.volumes.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.volumes.with_raw_response.get(
                "",
            )
