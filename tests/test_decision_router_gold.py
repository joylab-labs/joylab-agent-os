from __future__ import annotations

import json

import pytest

from joylab_agent_os.decision_router import (
    DecisionRequest,
    DecisionRouter,
    ModelDecision,
    assert_false_autonomy_zero,
    build_shadow_record,
)


class StubJev:
    def __init__(self, choice: str, confidence: float = 0.95):
        self.choice = choice
        self.confidence = confidence
        self.calls = 0

    def __call__(self, request: DecisionRequest) -> ModelDecision:
        self.calls += 1
        return ModelDecision(choice=self.choice, confidence=self.confidence)


def req(**kwargs) -> DecisionRequest:
    base = {
        "decision_id": "gold",
        "decision_type": "retry_action",
        "allowed_outputs": ("retry", "inspect", "escalate", "stop"),
        "state": {},
        "risk": frozenset(),
    }
    base.update(kwargs)
    return DecisionRequest(**base)


def test_gold_d001_deterministic_first_skips_jev():
    jev = StubJev("retry")
    result = DecisionRouter(jev).route(
        req(state={"deterministic_result": "CI_FAIL"})
    )
    assert result.actual_route == "CI_FAIL"
    assert result.authority == "CODE"
    assert jev.calls == 0


def test_gold_d002_bounded_decision_stays_inside_schema():
    jev = StubJev("inspect", 0.95)
    result = DecisionRouter(jev).route(req())
    assert result.shadow_route in {"retry", "inspect", "escalate", "stop"}
    assert result.shadow_route == "inspect"


def test_gold_d003_low_confidence_falls_back():
    result = DecisionRouter(StubJev("retry", 0.61)).route(req())
    assert result.actual_route == "SOL"
    assert result.shadow_route == "HIGHER_TIER_REVIEW"
    assert result.fallback_required is True


def test_gold_d004_safety_override_beats_model_confidence():
    jev = StubJev("retry", 0.99)
    result = DecisionRouter(jev).route(
        req(risk=frozenset({"database_migration"}))
    )
    assert result.actual_route == "S4"
    assert result.authority == "CODE"
    assert jev.calls == 0


def test_gold_d005_destructive_operation_requires_human():
    jev = StubJev("retry", 0.99)
    result = DecisionRouter(jev).route(
        req(risk=frozenset({"destructive_production"}))
    )
    assert result.actual_route == "HUMAN"
    assert result.authority == "HUMAN"
    assert jev.calls == 0


def test_gold_d006_identity_ambiguity_never_auto_merges():
    result = DecisionRouter(StubJev("retry")).route(
        req(state={"identity_ambiguous": True})
    )
    assert result.actual_route == "HUMAN"
    assert "no-auto-merge" in result.reason


def test_gold_d007_leaderdesk_release_hard_gate_overrides_jev():
    jev = StubJev("retry", 0.99)
    result = DecisionRouter(jev).route(
        req(state={"release_gate_failed": True})
    )
    assert result.actual_route == "HOLD"
    assert result.authority == "CODE"
    assert jev.calls == 0


def test_gold_d008_invalid_motion_schema_blocks_before_jev():
    jev = StubJev("retry")
    result = DecisionRouter(jev).route(
        req(state={"schema_valid": False})
    )
    assert result.actual_route == "HOLD"
    assert result.reason == "invalid-schema"
    assert jev.calls == 0


def test_gold_d009_repeated_failure_escalates_to_astra():
    jev = StubJev("retry")
    result = DecisionRouter(jev).route(
        req(state={"repeat_failures": 2, "repeat_failure_threshold": 2})
    )
    assert result.actual_route == "ASTRA"
    assert result.authority == "ASTRA"
    assert jev.calls == 0


def test_gold_d010_shadow_isolation_preserves_production_route():
    result = DecisionRouter(StubJev("inspect", 0.99)).route(
        req(), production_route="SOL", shadow=True
    )
    assert result.actual_route == "SOL"
    assert result.shadow_route == "inspect"
    assert result.false_autonomy == 0


def test_gold_d011_shadow_log_contains_required_fields():
    record = build_shadow_record(
        decision_id="d11",
        decision_type="retry_action",
        input_hash="sha256:abc",
        actual_route="SOL",
        shadow_route="inspect",
        confidence=0.94,
        outcome="PASS",
        timestamp="2026-10-03T14:33:00+09:00",
    )
    required = {
        "decision_id",
        "decision_type",
        "input_hash",
        "actual_route",
        "shadow_route",
        "confidence",
        "outcome",
        "timestamp",
        "false_autonomy",
    }
    assert required <= record.keys()


def test_gold_d012_same_fixture_and_policy_are_reproducible():
    request = req(decision_id="d12")
    router_a = DecisionRouter(StubJev("inspect", 0.92))
    router_b = DecisionRouter(StubJev("inspect", 0.92))
    assert router_a.route(request) == router_b.route(request)


def test_gold_d013_false_autonomy_is_absolute_release_gate():
    safe_records = [{"false_autonomy": 0}, {"false_autonomy": 0}]
    assert_false_autonomy_zero(safe_records)

    with pytest.raises(AssertionError, match="ROUTER RELEASE = HOLD"):
        assert_false_autonomy_zero(
            [{"false_autonomy": 0}, {"false_autonomy": 1}]
        )


def test_gold_d014_mandatory_escalation_overrides_low_effort_candidate():
    jev = StubJev("S1", 0.99)
    request = DecisionRequest(
        decision_id="d14",
        decision_type="effort",
        allowed_outputs=("S0", "S1", "S2", "S3", "S4"),
        state={},
        risk=frozenset({"identity_permission_model_change"}),
    )
    result = DecisionRouter(jev).route(request)
    assert result.actual_route == "S4"
    assert jev.calls == 0


def test_gold_d015_unknown_or_unbounded_state_falls_back():
    request = req(
        decision_id="d15",
        allowed_outputs=(),
    )
    result = DecisionRouter(StubJev("retry")).route(request)
    assert result.actual_route == "SOL"
    assert result.shadow_route == "UNKNOWN"
    assert result.fallback_required is True
    assert result.authority == "LUNA"
