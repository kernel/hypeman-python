# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from ..snapshot_kind import SnapshotKind
from ..shared_params.snapshot_compression_config import SnapshotCompressionConfig

__all__ = ["SnapshotCreateParams"]


class SnapshotCreateParams(TypedDict, total=False):
    kind: Required[SnapshotKind]
    """Snapshot capture kind"""

    compression: SnapshotCompressionConfig
    """Compression settings to use for this snapshot.

    Overrides instance and server defaults.
    """

    name: str
    """
    Optional snapshot name (lowercase letters, digits, and dashes only; cannot start
    or end with a dash)
    """

    tags: Dict[str, str]
    """User-defined key-value tags."""
