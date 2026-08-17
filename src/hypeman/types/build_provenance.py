# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["BuildProvenance"]


class BuildProvenance(BaseModel):
    base_image_digest: Optional[str] = None
    """Pinned base image digest used"""

    buildkit_version: Optional[str] = None
    """BuildKit version used"""

    lockfile_hashes: Optional[Dict[str, str]] = None
    """Map of lockfile names to SHA256 hashes"""

    source_hash: Optional[str] = None
    """SHA256 hash of source tarball"""

    timestamp: Optional[datetime] = None
    """Build completion timestamp"""
