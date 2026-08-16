# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hypeman import Hypeman, AsyncHypeman
from tests.utils import assert_matches_type
from hypeman.types import (
    Instance,
    PathInfo,
    InstanceStats,
    InstanceListResponse,
    WaitForStateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hypeman) -> None:
        instance = client.instances.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
            auto_standby={
                "enabled": True,
                "idle_timeout": "5m",
                "ignore_destination_ports": [22, 9000],
                "ignore_source_cidrs": ["10.0.0.0/8", "192.168.0.0/16"],
            },
            cmd=["echo", "hello"],
            credentials={
                "OUTBOUND_OPENAI_KEY": {
                    "inject": [
                        {
                            "as": {
                                "format": "Bearer ${value}",
                                "header": "Authorization",
                            },
                            "hosts": ["api.openai.com", "*.openai.com"],
                        }
                    ],
                    "source": {"env": "OUTBOUND_OPENAI_KEY"},
                }
            },
            devices=["l4-gpu"],
            disk_io_bps="100MB/s",
            entrypoint=["/bin/sh", "-c"],
            env={
                "PORT": "3000",
                "NODE_ENV": "production",
            },
            gpu={"profile": "L40S-1Q"},
            health_check={
                "exec": {
                    "command": ["curl", "-f", "http://localhost:4318/"],
                    "working_dir": "/app",
                },
                "failure_threshold": 3,
                "http": {
                    "port": 8080,
                    "expected_status": 200,
                    "path": "/healthz",
                    "scheme": "http",
                },
                "interval": "10s",
                "start_period": "30s",
                "success_threshold": 1,
                "tcp": {"port": 5432},
                "timeout": "2s",
                "type": "none",
            },
            hotplug_size="2GB",
            hypervisor="cloud-hypervisor",
            network={
                "bandwidth_download": "1Gbps",
                "bandwidth_upload": "1Gbps",
                "egress": {
                    "enabled": True,
                    "enforcement": {"mode": "all"},
                },
                "enabled": True,
            },
            overlay_size="20GB",
            platform="linux/amd64",
            restart_policy={
                "backoff": "5s",
                "max_attempts": 10,
                "policy": "on_failure",
                "stable_after": "10m",
            },
            size="2GB",
            skip_guest_agent=False,
            skip_kernel_headers=True,
            snapshot_policy={
                "compression": {
                    "enabled": True,
                    "algorithm": "zstd",
                    "level": 1,
                },
                "standby_compression_delay": "2m",
            },
            tags={
                "team": "backend",
                "env": "staging",
            },
            vcpus=2,
            volumes=[
                {
                    "mount_path": "/mnt/data",
                    "volume_id": "vol-abc123",
                    "overlay": True,
                    "overlay_size": "1GB",
                    "readonly": True,
                }
            ],
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hypeman) -> None:
        instance = client.instances.update(
            id="id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.update(
            id="id",
            auto_standby={
                "enabled": True,
                "idle_timeout": "5m",
                "ignore_destination_ports": [22, 9000],
                "ignore_source_cidrs": ["10.0.0.0/8", "192.168.0.0/16"],
            },
            env={"OUTBOUND_OPENAI_KEY": "new-rotated-key-456"},
            health_check={
                "exec": {
                    "command": ["curl", "-f", "http://localhost:4318/"],
                    "working_dir": "/app",
                },
                "failure_threshold": 3,
                "http": {
                    "port": 8080,
                    "expected_status": 200,
                    "path": "/healthz",
                    "scheme": "http",
                },
                "interval": "10s",
                "start_period": "30s",
                "success_threshold": 1,
                "tcp": {"port": 5432},
                "timeout": "2s",
                "type": "none",
            },
            restart_policy={
                "backoff": "5s",
                "max_attempts": 10,
                "policy": "on_failure",
                "stable_after": "10m",
            },
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hypeman) -> None:
        instance = client.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.list(
            state="Created",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hypeman) -> None:
        instance = client.instances.delete(
            "id",
        )
        assert instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fork(self, client: Hypeman) -> None:
        instance = client.instances.fork(
            id="id",
            name="my-workload-1-fork",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fork_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.fork(
            id="id",
            name="my-workload-1-fork",
            from_running=False,
            target_state="Running",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fork(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.fork(
            id="id",
            name="my-workload-1-fork",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fork(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.fork(
            id="id",
            name="my-workload-1-fork",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fork(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.fork(
                id="",
                name="my-workload-1-fork",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hypeman) -> None:
        instance = client.instances.get(
            "id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_logs(self, client: Hypeman) -> None:
        instance_stream = client.instances.logs(
            id="id",
        )
        instance_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_logs_with_all_params(self, client: Hypeman) -> None:
        instance_stream = client.instances.logs(
            id="id",
            follow=True,
            source="app",
            tail=0,
        )
        instance_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_logs(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.logs(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_logs(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_logs(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: Hypeman) -> None:
        instance = client.instances.restore(
            "id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.restore(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.restore(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.restore(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_standby(self, client: Hypeman) -> None:
        instance = client.instances.standby(
            id="id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_standby_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.standby(
            id="id",
            compression={
                "enabled": True,
                "algorithm": "zstd",
                "level": 1,
            },
            compression_delay="45s",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_standby(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.standby(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_standby(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.standby(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_standby(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.standby(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Hypeman) -> None:
        instance = client.instances.start(
            id="id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.start(
            id="id",
            cmd=["string"],
            entrypoint=["string"],
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.start(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.start(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.start(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stat(self, client: Hypeman) -> None:
        instance = client.instances.stat(
            id="id",
            path="path",
        )
        assert_matches_type(PathInfo, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stat_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.stat(
            id="id",
            path="path",
            follow_links=True,
        )
        assert_matches_type(PathInfo, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stat(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.stat(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(PathInfo, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stat(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.stat(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(PathInfo, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stat(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.stat(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats(self, client: Hypeman) -> None:
        instance = client.instances.stats(
            "id",
        )
        assert_matches_type(InstanceStats, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stats(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.stats(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceStats, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stats(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.stats(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceStats, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stats(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.stats(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Hypeman) -> None:
        instance = client.instances.stop(
            "id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.stop(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.stop(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.stop(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_wait(self, client: Hypeman) -> None:
        instance = client.instances.wait(
            id="id",
            state="Created",
        )
        assert_matches_type(WaitForStateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_wait_with_all_params(self, client: Hypeman) -> None:
        instance = client.instances.wait(
            id="id",
            state="Created",
            api_timeout="timeout",
        )
        assert_matches_type(WaitForStateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_wait(self, client: Hypeman) -> None:
        response = client.instances.with_raw_response.wait(
            id="id",
            state="Created",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(WaitForStateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_wait(self, client: Hypeman) -> None:
        with client.instances.with_streaming_response.wait(
            id="id",
            state="Created",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(WaitForStateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_wait(self, client: Hypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.wait(
                id="",
                state="Created",
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
            auto_standby={
                "enabled": True,
                "idle_timeout": "5m",
                "ignore_destination_ports": [22, 9000],
                "ignore_source_cidrs": ["10.0.0.0/8", "192.168.0.0/16"],
            },
            cmd=["echo", "hello"],
            credentials={
                "OUTBOUND_OPENAI_KEY": {
                    "inject": [
                        {
                            "as": {
                                "format": "Bearer ${value}",
                                "header": "Authorization",
                            },
                            "hosts": ["api.openai.com", "*.openai.com"],
                        }
                    ],
                    "source": {"env": "OUTBOUND_OPENAI_KEY"},
                }
            },
            devices=["l4-gpu"],
            disk_io_bps="100MB/s",
            entrypoint=["/bin/sh", "-c"],
            env={
                "PORT": "3000",
                "NODE_ENV": "production",
            },
            gpu={"profile": "L40S-1Q"},
            health_check={
                "exec": {
                    "command": ["curl", "-f", "http://localhost:4318/"],
                    "working_dir": "/app",
                },
                "failure_threshold": 3,
                "http": {
                    "port": 8080,
                    "expected_status": 200,
                    "path": "/healthz",
                    "scheme": "http",
                },
                "interval": "10s",
                "start_period": "30s",
                "success_threshold": 1,
                "tcp": {"port": 5432},
                "timeout": "2s",
                "type": "none",
            },
            hotplug_size="2GB",
            hypervisor="cloud-hypervisor",
            network={
                "bandwidth_download": "1Gbps",
                "bandwidth_upload": "1Gbps",
                "egress": {
                    "enabled": True,
                    "enforcement": {"mode": "all"},
                },
                "enabled": True,
            },
            overlay_size="20GB",
            platform="linux/amd64",
            restart_policy={
                "backoff": "5s",
                "max_attempts": 10,
                "policy": "on_failure",
                "stable_after": "10m",
            },
            size="2GB",
            skip_guest_agent=False,
            skip_kernel_headers=True,
            snapshot_policy={
                "compression": {
                    "enabled": True,
                    "algorithm": "zstd",
                    "level": 1,
                },
                "standby_compression_delay": "2m",
            },
            tags={
                "team": "backend",
                "env": "staging",
            },
            vcpus=2,
            volumes=[
                {
                    "mount_path": "/mnt/data",
                    "volume_id": "vol-abc123",
                    "overlay": True,
                    "overlay_size": "1GB",
                    "readonly": True,
                }
            ],
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.create(
            image="docker.io/library/alpine:latest",
            name="my-workload-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.update(
            id="id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.update(
            id="id",
            auto_standby={
                "enabled": True,
                "idle_timeout": "5m",
                "ignore_destination_ports": [22, 9000],
                "ignore_source_cidrs": ["10.0.0.0/8", "192.168.0.0/16"],
            },
            env={"OUTBOUND_OPENAI_KEY": "new-rotated-key-456"},
            health_check={
                "exec": {
                    "command": ["curl", "-f", "http://localhost:4318/"],
                    "working_dir": "/app",
                },
                "failure_threshold": 3,
                "http": {
                    "port": 8080,
                    "expected_status": 200,
                    "path": "/healthz",
                    "scheme": "http",
                },
                "interval": "10s",
                "start_period": "30s",
                "success_threshold": 1,
                "tcp": {"port": 5432},
                "timeout": "2s",
                "type": "none",
            },
            restart_policy={
                "backoff": "5s",
                "max_attempts": 10,
                "policy": "on_failure",
                "stable_after": "10m",
            },
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.list(
            state="Created",
            tags={
                "team": "backend",
                "env": "staging",
            },
        )
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.delete(
            "id",
        )
        assert instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert instance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fork(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.fork(
            id="id",
            name="my-workload-1-fork",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fork_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.fork(
            id="id",
            name="my-workload-1-fork",
            from_running=False,
            target_state="Running",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fork(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.fork(
            id="id",
            name="my-workload-1-fork",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fork(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.fork(
            id="id",
            name="my-workload-1-fork",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fork(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.fork(
                id="",
                name="my-workload-1-fork",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.get(
            "id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_logs(self, async_client: AsyncHypeman) -> None:
        instance_stream = await async_client.instances.logs(
            id="id",
        )
        await instance_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_logs_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance_stream = await async_client.instances.logs(
            id="id",
            follow=True,
            source="app",
            tail=0,
        )
        await instance_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_logs(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.logs(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_logs(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_logs(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.restore(
            "id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.restore(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.restore(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.restore(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_standby(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.standby(
            id="id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_standby_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.standby(
            id="id",
            compression={
                "enabled": True,
                "algorithm": "zstd",
                "level": 1,
            },
            compression_delay="45s",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_standby(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.standby(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_standby(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.standby(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_standby(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.standby(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.start(
            id="id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.start(
            id="id",
            cmd=["string"],
            entrypoint=["string"],
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.start(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.start(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.start(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stat(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.stat(
            id="id",
            path="path",
        )
        assert_matches_type(PathInfo, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stat_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.stat(
            id="id",
            path="path",
            follow_links=True,
        )
        assert_matches_type(PathInfo, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stat(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.stat(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(PathInfo, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stat(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.stat(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(PathInfo, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stat(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.stat(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.stats(
            "id",
        )
        assert_matches_type(InstanceStats, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.stats(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceStats, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.stats(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceStats, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stats(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.stats(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.stop(
            "id",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.stop(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.stop(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.stop(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_wait(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.wait(
            id="id",
            state="Created",
        )
        assert_matches_type(WaitForStateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_wait_with_all_params(self, async_client: AsyncHypeman) -> None:
        instance = await async_client.instances.wait(
            id="id",
            state="Created",
            api_timeout="timeout",
        )
        assert_matches_type(WaitForStateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_wait(self, async_client: AsyncHypeman) -> None:
        response = await async_client.instances.with_raw_response.wait(
            id="id",
            state="Created",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(WaitForStateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_wait(self, async_client: AsyncHypeman) -> None:
        async with async_client.instances.with_streaming_response.wait(
            id="id",
            state="Created",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(WaitForStateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_wait(self, async_client: AsyncHypeman) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.wait(
                id="",
                state="Created",
            )
