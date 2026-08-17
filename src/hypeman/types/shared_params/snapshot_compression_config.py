# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SnapshotCompressionConfig"]


class SnapshotCompressionConfig(TypedDict, total=False):
    enabled: Required[bool]
    """Enable snapshot memory compression"""

    algorithm: Literal["zstd", "lz4"]
    """Compression algorithm (defaults to zstd when enabled).

    Ignored when enabled is false.
    """

    level: int
    """Compression level.

    Allowed ranges are zstd=1-19 and lz4=0-9. When omitted, zstd defaults to 1 and
    lz4 defaults to 0. Ignored when enabled is false.
    """
