# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import Instance

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach(self, client: Hypeman) -> None:
        volume = client.instances.volumes.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
        )
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach_with_all_params(self, client: Hypeman) -> None:
        volume = client.instances.volumes.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
            readonly=True,
        )
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Hypeman) -> None:
        response = client.instances.volumes.with_raw_response.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Hypeman) -> None:
        with client.instances.volumes.with_streaming_response.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Instance, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.volumes.with_raw_response.attach(
                volume_id="volumeId",
                id="",
                mount_path="/mnt/data",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.instances.volumes.with_raw_response.attach(
                volume_id="",
                id="id",
                mount_path="/mnt/data",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_detach(self, client: Hypeman) -> None:
        volume = client.instances.volumes.detach(
            volume_id="volumeId",
            id="id",
        )
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Hypeman) -> None:
        response = client.instances.volumes.with_raw_response.detach(
            volume_id="volumeId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Hypeman) -> None:
        with client.instances.volumes.with_streaming_response.detach(
            volume_id="volumeId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Instance, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.volumes.with_raw_response.detach(
                volume_id="volumeId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.instances.volumes.with_raw_response.detach(
                volume_id="",
                id="id",
            )


class TestAsyncVolumes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.instances.volumes.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
        )
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach_with_all_params(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.instances.volumes.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
            readonly=True,
        )
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.volumes.with_raw_response.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.volumes.with_streaming_response.attach(
            volume_id="volumeId",
            id="id",
            mount_path="/mnt/data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Instance, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.volumes.with_raw_response.attach(
                volume_id="volumeId",
                id="",
                mount_path="/mnt/data",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.instances.volumes.with_raw_response.attach(
                volume_id="",
                id="id",
                mount_path="/mnt/data",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncHypeman) -> None:
        volume = await async_client.instances.volumes.detach(
            volume_id="volumeId",
            id="id",
        )
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.volumes.with_raw_response.detach(
            volume_id="volumeId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Instance, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.volumes.with_streaming_response.detach(
            volume_id="volumeId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Instance, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.volumes.with_raw_response.detach(
                volume_id="volumeId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.instances.volumes.with_raw_response.detach(
                volume_id="",
                id="id",
            )
