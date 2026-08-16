# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import AutoStandbyStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutoStandby:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hold(self, client: Hypeman) -> None:
        auto_standby = client.instances.auto_standby.hold(
            "id",
        )
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_hold(self, client: Hypeman) -> None:
        response = client.instances.auto_standby.with_raw_response.hold(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_standby = response.parse()
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_hold(self, client: Hypeman) -> None:
        with client.instances.auto_standby.with_streaming_response.hold(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_standby = response.parse()
            assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_hold(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.auto_standby.with_raw_response.hold(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: Hypeman) -> None:
        auto_standby = client.instances.auto_standby.status(
            "id",
        )
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Hypeman) -> None:
        response = client.instances.auto_standby.with_raw_response.status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_standby = response.parse()
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Hypeman) -> None:
        with client.instances.auto_standby.with_streaming_response.status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_standby = response.parse()
            assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.auto_standby.with_raw_response.status(
                "",
            )


class TestAsyncAutoStandby:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hold(self, async_client: AsyncHypeman) -> None:
        auto_standby = await async_client.instances.auto_standby.hold(
            "id",
        )
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_hold(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.auto_standby.with_raw_response.hold(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_standby = await response.parse()
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_hold(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.auto_standby.with_streaming_response.hold(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_standby = await response.parse()
            assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_hold(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.auto_standby.with_raw_response.hold(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncHypeman) -> None:
        auto_standby = await async_client.instances.auto_standby.status(
            "id",
        )
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.auto_standby.with_raw_response.status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_standby = await response.parse()
        assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.auto_standby.with_streaming_response.status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_standby = await response.parse()
            assert_matches_type(AutoStandbyStatus, auto_standby, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.auto_standby.with_raw_response.status(
                "",
            )
