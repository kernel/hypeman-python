# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .builder_status import BuilderStatus

__all__ = ["Builder"]


class Builder(BaseModel):
    id: str
    """Builder identifier"""

    created_at: datetime
    """Creation timestamp (RFC3339)"""

    disk_size_gb: int
    """Persistent builder cache disk size in gigabytes.

    Cannot be changed after creation.
    """

    max_concurrency: int
    """Maximum concurrent builds on this builder. Currently fixed at 1."""

    queued_builds: List[str]
    """Point-in-time IDs of queued builds waiting for this builder, oldest first"""

    status: BuilderStatus
    """Builder lifecycle status"""

    active_build_id: Optional[str] = None
    """Point-in-time ID of the build currently running on this builder"""

    last_used_at: Optional[datetime] = None
    """When a build last ran on this builder"""

    name: Optional[str] = None
    """Optional non-unique display name"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""
