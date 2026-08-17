# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["VolumeAttachment"]


class VolumeAttachment(BaseModel):
    instance_id: str
    """ID of the instance this volume is attached to"""

    mount_path: str
    """Mount path in the guest"""

    readonly: bool
    """Whether the attachment is read-only"""
