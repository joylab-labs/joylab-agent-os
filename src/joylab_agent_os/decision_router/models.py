from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class DecisionRequest:
    decision_id: str
    decision_type: str
    allowed_outputs: Sequence[str]
    state: Mapping[str, Any] = field(default_factory=dict)
    risk: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class ModelDecision:
    choice: str
    confidence: float
    provider: str = "jev"


@dataclass(frozen=True)
class RouteDecision:
    decision_id: str
    actual_route: str
    shadow_route: str | None
    authority: str
    confidence: float | None
    fallback_required: bool
    false_autonomy: int = 0
    reason: str = ""
