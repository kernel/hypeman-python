# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from .ingress_rule_param import IngressRuleParam

__all__ = ["IngressCreateParams"]


class IngressCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    Human-readable name (lowercase letters, digits, and dashes only; cannot start or
    end with a dash)
    """

    rules: Required[Iterable[IngressRuleParam]]
    """Routing rules for this ingress"""

    tags: Dict[str, str]
    """User-defined key-value tags."""
