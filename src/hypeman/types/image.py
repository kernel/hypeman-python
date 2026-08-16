# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    created_at: datetime
    """Creation timestamp (RFC3339)"""

    digest: str
    """Resolved manifest digest"""

    name: str
    """Normalized OCI image reference (tag or digest)"""

    status: Literal["pending", "pulling", "converting", "ready", "failed"]
    """Build status"""

    cmd: Optional[List[str]] = None
    """CMD from container metadata"""

    entrypoint: Optional[List[str]] = None
    """Entrypoint from container metadata"""

    env: Optional[Dict[str, str]] = None
    """Environment variables from container metadata"""

    error: Optional[str] = None
    """Error message if status is failed"""

    platform: Optional[str] = None
    """Resolved image platform as os/arch[/variant] (e.g. "linux/amd64")"""

    queue_position: Optional[int] = None
    """Position in build queue (null if not queued)"""

    size_bytes: Optional[int] = None
    """Disk size in bytes (null until ready)"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""

    working_dir: Optional[str] = None
    """Working directory from container metadata"""
