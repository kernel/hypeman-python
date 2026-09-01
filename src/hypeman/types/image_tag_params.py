# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ImageTagParams"]


class ImageTagParams(TypedDict, total=False):
    target: Required[str]
    """Target OCI image reference with a tag.

    The local tag points to the source image without pulling it again.
    """
