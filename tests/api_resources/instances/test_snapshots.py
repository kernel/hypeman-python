# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import Instance, Snapshot

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hypeman) -> None:
        snapshot = client.instances.snapshots.create(
            id="id",
            kind="Standby",
        )
        assert_matches_type(Snapshot, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hypeman) -> None:
        snapshot = client.instances.snapshots.create(
            id="id",
            kind="Standby",
            compression={
                "enabled": True,
                "algorithm": "zstd",
                "level": 1,
            },
            name="pre-upgrade",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Snapshot, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hypeman) -> None:
        response = client.instances.snapshots.with_raw_response.create(
            id="id",
            kind="Standby",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(Snapshot, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hypeman) -> None:
        with client.instances.snapshots.with_streaming_response.create(
            id="id",
            kind="Standby",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(Snapshot, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.snapshots.with_raw_response.create(
                id="",
                kind="Standby",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: Hypeman) -> None:
        snapshot = client.instances.snapshots.restore(
            snapshot_id="snapshotId",
            id="id",
        )
        assert_matches_type(Instance, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_with_all_params(self, client: Hypeman) -> None:
        snapshot = client.instances.snapshots.restore(
            snapshot_id="snapshotId",
            id="id",
            target_hypervisor="qemu",
            target_state="Running",
        )
        assert_matches_type(Instance, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Hypeman) -> None:
        response = client.instances.snapshots.with_raw_response.restore(
            snapshot_id="snapshotId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(Instance, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Hypeman) -> None:
        with client.instances.snapshots.with_streaming_response.restore(
            snapshot_id="snapshotId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(Instance, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.snapshots.with_raw_response.restore(
                snapshot_id="snapshotId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.instances.snapshots.with_raw_response.restore(
                snapshot_id="",
                id="id",
            )


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHypeman) -> None:
        snapshot = await async_client.instances.snapshots.create(
            id="id",
            kind="Standby",
        )
        assert_matches_type(Snapshot, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHypeman) -> None:
        snapshot = await async_client.instances.snapshots.create(
            id="id",
            kind="Standby",
            compression={
                "enabled": True,
                "algorithm": "zstd",
                "level": 1,
            },
            name="pre-upgrade",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(Snapshot, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.snapshots.with_raw_response.create(
            id="id",
            kind="Standby",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(Snapshot, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.snapshots.with_streaming_response.create(
            id="id",
            kind="Standby",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(Snapshot, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.snapshots.with_raw_response.create(
                id="",
                kind="Standby",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncHypeman) -> None:
        snapshot = await async_client.instances.snapshots.restore(
            snapshot_id="snapshotId",
            id="id",
        )
        assert_matches_type(Instance, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncHypeman) -> None:
        snapshot = await async_client.instances.snapshots.restore(
            snapshot_id="snapshotId",
            id="id",
            target_hypervisor="qemu",
            target_state="Running",
        )
        assert_matches_type(Instance, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.snapshots.with_raw_response.restore(
            snapshot_id="snapshotId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(Instance, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.snapshots.with_streaming_response.restore(
            snapshot_id="snapshotId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(Instance, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.snapshots.with_raw_response.restore(
                snapshot_id="snapshotId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.instances.snapshots.with_raw_response.restore(
                snapshot_id="",
                id="id",
            )
