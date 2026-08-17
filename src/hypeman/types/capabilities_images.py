# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CapabilitiesImages"]


class CapabilitiesImages(BaseModel):
    default_platform: str
    """Image platform selected when a create request omits one"""

    platforms: List[str]
    """Image platforms (os/arch) this host can run.

    On Apple Silicon macOS this includes linux/amd64 only when Rosetta is currently
    installed — probed via the same Virtualization.framework availability check
    launches enforce — so a listed platform is launchable right now. Install Rosetta
    (softwareupdate --install-rosetta) to enable it.
    """
