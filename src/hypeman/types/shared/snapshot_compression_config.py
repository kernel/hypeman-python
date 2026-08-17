# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SnapshotCompressionConfig"]


class SnapshotCompressionConfig(BaseModel):
    enabled: bool
    """Enable snapshot memory compression"""

    algorithm: Optional[Literal["zstd", "lz4"]] = None
    """Compression algorithm (defaults to zstd when enabled).

    Ignored when enabled is false.
    """

    level: Optional[int] = None
    """Compression level.

    Allowed ranges are zstd=1-19 and lz4=0-9. When omitted, zstd defaults to 1 and
    lz4 defaults to 0. Ignored when enabled is false.
    """
