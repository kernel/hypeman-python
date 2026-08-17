# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared_params.snapshot_compression_config import SnapshotCompressionConfig

__all__ = ["SnapshotPolicyParam"]


class SnapshotPolicyParam(TypedDict, total=False):
    compression: SnapshotCompressionConfig

    standby_compression_delay: str
    """
    Delay before standby snapshot compression begins, expressed as a Go duration
    like "30s" or "5m". Applies only to standby compression and defaults to
    immediate start when omitted.
    """
