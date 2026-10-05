from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_claude_cloud_contract_keeps_human_gate():
    text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    required = [
        "dedicated feature branch",
        "Draft PR",
        "Never merge",
        "Human Gate",
        "Never weaken or bypass required checks",
    ]
    missing = [rule for rule in required if rule not in text]
    assert not missing, f"Claude Cloud contract missing controls: {missing}"


def test_cloud_gold_runbook_defines_core_gates():
    text = (ROOT / "docs" / "CLOUD_AGENT_GOLD_V1.md").read_text(encoding="utf-8")
    for gate in ["G0 — Issue Gate", "G1 — Scope Gate", "G2 — Verification Gate", "G3 — Draft PR Gate", "G4 — Human Gate"]:
        assert gate in text
    assert "Agent merge | false" in text
