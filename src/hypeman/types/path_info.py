# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PathInfo"]


class PathInfo(BaseModel):
    exists: bool
    """Whether the path exists"""

    error: Optional[str] = None
    """Error message if stat failed (e.g., permission denied).

    Only set when exists is false due to an error rather than the path not existing.
    """

    is_dir: Optional[bool] = None
    """True if this is a directory"""

    is_file: Optional[bool] = None
    """True if this is a regular file"""

    is_symlink: Optional[bool] = None
    """True if this is a symbolic link (only set when follow_links=false)"""

    link_target: Optional[str] = None
    """Symlink target path (only set when is_symlink=true)"""

    mode: Optional[int] = None
    """File mode (Unix permissions)"""

    size: Optional[int] = None
    """File size in bytes"""
