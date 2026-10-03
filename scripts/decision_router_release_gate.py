from __future__ import annotations

import argparse
import json
from pathlib import Path

from joylab_agent_os.decision_router import assert_false_autonomy_zero


def main() -> int:
    parser = argparse.ArgumentParser(description="JoyLab Decision Router release gate")
    parser.add_argument(
        "--records",
        default="decision-router/gold/cases/shadow_records.json",
        help="JSON array containing shadow evaluation records",
    )
    args = parser.parse_args()

    path = Path(args.records)
    records = json.loads(path.read_text(encoding="utf-8"))
    assert_false_autonomy_zero(records)
    print(f"DECISION ROUTER GOLD: PASS | FALSE_AUTONOMY=0 | records={len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
