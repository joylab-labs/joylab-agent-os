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
