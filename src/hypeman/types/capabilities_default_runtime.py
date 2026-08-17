# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CapabilitiesDefaultRuntime"]


class CapabilitiesDefaultRuntime(BaseModel):
    available: bool
    """
    Whether the default runtime can launch on this host: it appears in runtimes and
    its launch prerequisites are met (matches that entry's "available"). When false,
    launches that rely on the default will fail until the server is reconfigured
    with an available runtime or the missing prerequisite (for example the QEMU
    system binary) is installed.
    """

    name: str
    """Runtime used for launches that do not name one"""
