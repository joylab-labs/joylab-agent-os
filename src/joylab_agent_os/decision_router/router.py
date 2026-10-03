from __future__ import annotations

from collections.abc import Callable
from typing import Final

from .models import DecisionRequest, ModelDecision, RouteDecision


HUMAN_REQUIRED_RISKS: Final[frozenset[str]] = frozenset(
    {
        "destructive_production",
        "permanent_deletion",
        "credential_escalation",
        "permission_escalation",
        "irreversible_migration",
        "financial_action",
        "ambiguous_identity_merge",
        "official_record_confirmation",
    }
)

S4_RISKS: Final[frozenset[str]] = frozenset(
    {
        "database_migration",
        "backup_restore",
        "identity_permission_model_change",
        "production_data_transformation",
    }
)


class DecisionRouter:
    """Shadow-first bounded-decision router.

    The router never lets a shadow model change the production route.
    Deterministic and authority-boundary checks run first.
    """

    def __init__(
        self,
        jev: Callable[[DecisionRequest], ModelDecision],
        *,
        auto_candidate_threshold: float = 0.90,
        fallback_threshold: float = 0.70,
    ) -> None:
        self._jev = jev
        self.auto_candidate_threshold = auto_candidate_threshold
        self.fallback_threshold = fallback_threshold

    def route(
        self,
        request: DecisionRequest,
        *,
        production_route: str = "SOL",
        shadow: bool = True,
    ) -> RouteDecision:
        state = request.state

        if "deterministic_result" in state:
            result = str(state["deterministic_result"])
            return RouteDecision(
                request.decision_id,
                actual_route=result,
                shadow_route=None,
                authority="CODE",
                confidence=None,
                fallback_required=False,
                reason="deterministic-first",
            )

        if state.get("schema_valid") is False:
            return RouteDecision(
                request.decision_id,
                actual_route="HOLD",
                shadow_route=None,
                authority="CODE",
                confidence=None,
                fallback_required=False,
                reason="invalid-schema",
            )

        if state.get("release_gate_failed"):
            return RouteDecision(
                request.decision_id,
                actual_route="HOLD",
                shadow_route=None,
                authority="CODE",
                confidence=None,
                fallback_required=False,
                reason="hard-release-gate",
            )

        if state.get("identity_ambiguous"):
            return RouteDecision(
                request.decision_id,
                actual_route="HUMAN",
                shadow_route=None,
                authority="HUMAN",
                confidence=None,
                fallback_required=False,
                reason="ambiguous-identity-no-auto-merge",
            )

        if request.risk & HUMAN_REQUIRED_RISKS:
            return RouteDecision(
                request.decision_id,
                actual_route="HUMAN",
                shadow_route=None,
                authority="HUMAN",
                confidence=None,
                fallback_required=False,
                reason="human-authority-boundary",
            )

        if request.risk & S4_RISKS:
            return RouteDecision(
                request.decision_id,
                actual_route="S4",
                shadow_route=None,
                authority="CODE",
                confidence=None,
                fallback_required=True,
                reason="mandatory-s4-override",
            )

        repeat_failures = int(state.get("repeat_failures", 0) or 0)
        repeat_threshold = int(state.get("repeat_failure_threshold", 2) or 2)
        if repeat_failures >= repeat_threshold:
            return RouteDecision(
                request.decision_id,
                actual_route="ASTRA",
                shadow_route=None,
                authority="ASTRA",
                confidence=None,
                fallback_required=True,
                reason="repeated-targeted-failure",
            )

        if not request.allowed_outputs:
            return RouteDecision(
                request.decision_id,
                actual_route=production_route,
                shadow_route="UNKNOWN",
                authority="LUNA",
                confidence=None,
                fallback_required=True,
                reason="unbounded-or-unknown",
            )

        decision = self._jev(request)

        if decision.choice not in request.allowed_outputs:
            return RouteDecision(
                request.decision_id,
                actual_route=production_route,
                shadow_route="UNKNOWN",
                authority="LUNA",
                confidence=decision.confidence,
                fallback_required=True,
                reason="out-of-schema-model-output",
            )

        if decision.confidence < self.fallback_threshold:
            shadow_route = "HIGHER_TIER_REVIEW"
            fallback = True
        elif decision.confidence < self.auto_candidate_threshold:
            shadow_route = "MODEL_FALLBACK"
            fallback = True
        else:
            shadow_route = decision.choice
            fallback = False

        if shadow:
            return RouteDecision(
                request.decision_id,
                actual_route=production_route,
                shadow_route=shadow_route,
                authority="JEV",
                confidence=decision.confidence,
                fallback_required=fallback,
                false_autonomy=0,
                reason="shadow-only-production-route-preserved",
            )

        # V1 intentionally refuses live autonomous authority.
        return RouteDecision(
            request.decision_id,
            actual_route=production_route,
            shadow_route=shadow_route,
            authority="JEV",
            confidence=decision.confidence,
            fallback_required=True,
            false_autonomy=0,
            reason="v1-live-control-disabled",
        )
