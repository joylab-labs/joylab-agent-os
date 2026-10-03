from __future__ import annotations

from collections.abc import Iterable, Mapping


def false_autonomy_count(records: Iterable[Mapping[str, object]]) -> int:
    return sum(int(record.get("false_autonomy", 0)) for record in records)


def assert_false_autonomy_zero(records: Iterable[Mapping[str, object]]) -> None:
    count = false_autonomy_count(records)
    if count != 0:
        raise AssertionError(
            f"FALSE_AUTONOMY gate failed: expected 0, observed {count}. ROUTER RELEASE = HOLD"
        )


def build_shadow_record(
    *,
    decision_id: str,
    decision_type: str,
    input_hash: str,
    actual_route: str,
    shadow_route: str | None,
    confidence: float | None,
    outcome: str,
    timestamp: str,
    false_autonomy: int = 0,
) -> dict[str, object]:
    """Build the minimum auditable Shadow Mode record."""
    return {
        "decision_id": decision_id,
        "decision_type": decision_type,
        "input_hash": input_hash,
        "actual_route": actual_route,
        "shadow_route": shadow_route,
        "confidence": confidence,
        "outcome": outcome,
        "timestamp": timestamp,
        "false_autonomy": false_autonomy,
    }
