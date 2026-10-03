from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_wrapper(tmp_path: Path, command: list[str], artifact: Path | None = None):
    evidence = tmp_path / "evidence.json"
    failure = tmp_path / "failure.json"
    args = [
        sys.executable,
        str(ROOT / "scripts" / "run_with_evidence.py"),
        "--contract",
        str(ROOT / "examples" / "agent_contract.example.json"),
        "--evidence-out",
        str(evidence),
        "--failure-out",
        str(failure),
        "--stage",
        "test",
    ]
    if artifact is not None:
        args += ["--artifact", str(artifact)]
    args += ["--", *command]
    proc = subprocess.run(args, text=True)
    return proc, evidence, failure


def test_runtime_pass_writes_evidence(tmp_path):
    artifact = tmp_path / "artifact.txt"
    cmd = [sys.executable, "-c", f"from pathlib import Path; Path(r'{artifact}').write_text('ok')"]
    proc, evidence, failure = run_wrapper(tmp_path, cmd, artifact)
    assert proc.returncode == 0
    data = json.loads(evidence.read_text())
    assert data["outcome"] == "PASS"
    assert data["artifacts"][0]["exists"] is True
    assert not failure.exists()


def test_runtime_failure_writes_failure_packet(tmp_path):
    proc, evidence, failure = run_wrapper(tmp_path, [sys.executable, "-c", "raise SystemExit(7)"])
    assert proc.returncode == 7
    edata = json.loads(evidence.read_text())
    fdata = json.loads(failure.read_text())
    assert edata["outcome"] == "BLOCKED"
    assert fdata["error"]["code"] == "RUNTIME_COMMAND_FAILED"


def test_missing_required_artifact_blocks(tmp_path):
    missing = tmp_path / "missing.json"
    proc, evidence, failure = run_wrapper(tmp_path, [sys.executable, "-c", "print('ok')"], missing)
    assert proc.returncode == 3
    assert json.loads(evidence.read_text())["outcome"] == "BLOCKED"
    assert json.loads(failure.read_text())["error"]["code"] == "EVIDENCE_MISSING"
