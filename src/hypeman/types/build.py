# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .build_status import BuildStatus
from .build_provenance import BuildProvenance

__all__ = ["Build"]


class Build(BaseModel):
    id: str
    """Build job identifier"""

    created_at: datetime
    """Build creation timestamp"""

    status: BuildStatus
    """Build job status"""

    builder_id: Optional[str] = None
    """Persistent Builder resource whose cache backed this build"""

    builder_instance_id: Optional[str] = None
    """Disposable VM instance that executed this build; distinct from builder_id"""

    completed_at: Optional[datetime] = None
    """Build completion timestamp"""

    duration_ms: Optional[int] = None
    """Build duration in milliseconds"""

    error: Optional[str] = None
    """Error message (only when status is failed)"""

    image_digest: Optional[str] = None
    """Digest of built image (only when status is ready)"""

    image_ref: Optional[str] = None
    """Full image reference (only when status is ready)"""

    provenance: Optional[BuildProvenance] = None

    queue_position: Optional[int] = None
    """Position in build queue (only when status is queued)"""

    started_at: Optional[datetime] = None
    """Build start timestamp"""

    tags: Optional[Dict[str, str]] = None
    """User-defined key-value tags."""
