# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared_params.snapshot_compression_config import SnapshotCompressionConfig

__all__ = ["InstanceStandbyParams"]


class InstanceStandbyParams(TypedDict, total=False):
    compression: SnapshotCompressionConfig
    """Compression settings for standby snapshot memory. Overrides instance defaults."""

    compression_delay: str
    """
    Delay before standby snapshot compression begins, expressed as a Go duration
    like "30s" or "5m". Overrides the instance default for this standby operation
    only.
    """
