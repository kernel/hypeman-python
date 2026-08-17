# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.snapshot_compression_config import SnapshotCompressionConfig

__all__ = ["SnapshotPolicy"]


class SnapshotPolicy(BaseModel):
    compression: Optional[SnapshotCompressionConfig] = None

    standby_compression_delay: Optional[str] = None
    """
    Delay before standby snapshot compression begins, expressed as a Go duration
    like "30s" or "5m". Applies only to standby compression and defaults to
    immediate start when omitted.
    """
