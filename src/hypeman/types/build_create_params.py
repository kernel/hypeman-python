# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["BuildCreateParams"]


class BuildCreateParams(TypedDict, total=False):
    source: Required[FileTypes]
    """Source tarball (tar.gz) containing application code and optionally a Dockerfile"""

    base_image_digest: str
    """Optional pinned base image digest"""

    builder_id: str
    """
    Optional Builder ID whose persistent cache disk backs this build. This is the
    only builder selector. One build at a time runs on a builder; builds for the
    same builder are serialized.
    """

    cache_scope: str
    """Tenant-specific cache key prefix"""

    cpus: int
    """Number of vCPUs for builder VM (default 2)"""

    dockerfile: str
    """Dockerfile content. Required if not included in the source tarball."""

    global_cache_key: str
    """
    Global cache identifier (e.g., "node", "python", "ubuntu", "browser"). When
    specified, the build will import from cache/global/{key}. Admin builds will also
    export to this location.
    """

    image_name: str
    """Custom image name for the build output.

    When set, the image is pushed to {registry}/{image_name} instead of
    {registry}/builds/{id}.
    """

    is_admin_build: str
    """
    Set to "true" to grant push access to global cache (operator-only). Admin builds
    can populate the shared global cache that all tenant builds read from.
    """

    memory_mb: int
    """Memory limit for builder VM in MB (default 2048)"""

    secrets: str
    """
    JSON array of secret references to inject during build. Each object has "id"
    (required) for use with --mount=type=secret,id=... Example: [{"id":
    "npm_token"}, {"id": "github_token"}]
    """

    tags: str
    """JSON object of tags. Example: {"team":"backend","env":"staging"}"""

    timeout_seconds: int
    """Build timeout (default 600)"""
