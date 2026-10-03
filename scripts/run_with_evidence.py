#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00","Z")

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def digest(path: Path):
    if not path.is_file():
        return None
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def write_json(path, obj):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--contract", required=True)
    p.add_argument("--evidence-out", required=True)
    p.add_argument("--failure-out", required=True)
    p.add_argument("--stage", default=None)
    p.add_argument("--artifact", action="append", default=[])
    p.add_argument("command", nargs=argparse.REMAINDER)
    args=p.parse_args()
    cmd=args.command[1:] if args.command and args.command[0]=="--" else args.command
    if not cmd:
        raise SystemExit("command required after --")
    contract=load(args.contract)
    started=now()
    proc=subprocess.run(cmd, text=True)
    completed=now()

    artifacts=[]
    missing=[]
    for raw in args.artifact:
        path=Path(raw)
        exists=path.exists()
        if not exists: missing.append(raw)
        size=path.stat().st_size if exists and path.is_file() else None
        artifacts.append({"path":raw,"exists":exists,"size_bytes":size,"sha256":digest(path) if exists else None})

    checks=[
      {"id":"command_exit","required":True,"status":"PASS" if proc.returncode==0 else "FAIL","detail":f"exit_code={proc.returncode}"}
    ]
    for raw in args.artifact:
        exists=Path(raw).exists()
        checks.append({"id":f"artifact:{raw}","required":True,"status":"PASS" if exists else "MISSING","detail":"exists" if exists else "required artifact missing"})

    blocked = proc.returncode != 0 or bool(missing)
    failure_path = args.failure_out if blocked else None
    evidence={
      "contract_version":"1.0",
      "agent_id":contract["agent_id"],
      "run_id":os.getenv("GITHUB_RUN_ID") or f"local-{int(datetime.now().timestamp())}",
      "agent_contract_ref":args.contract,
      "started_at":started,
      "completed_at":completed,
      "stage":args.stage,
      "outcome":"BLOCKED" if blocked else "PASS",
      "command_exit_code":proc.returncode,
      "checks":checks,
      "artifacts":artifacts,
      "failure_packet":failure_path,
      "summary":"Runtime blocked; see failure packet." if blocked else "Runtime command and required evidence passed."
    }
    write_json(args.evidence_out,evidence)

    if blocked:
        existing=[x["path"] for x in artifacts if x["exists"]]
        prev=contract.get("state",{}).get("previous_state_source") or contract.get("state",{}).get("current_state_source") or "unknown"
        code="RUNTIME_COMMAND_FAILED" if proc.returncode != 0 else "EVIDENCE_MISSING"
        message=f"Command exited with {proc.returncode}." if proc.returncode !=0 else f"Required artifacts missing: {', '.join(missing)}"
        packet={
          "packet_version":"1.0",
          "agent_id":contract["agent_id"],
          "occurred_at":completed,
          "error":{"code":code,"message":message,"stage":args.stage},
          "last_success":{"state":f"Preserve last verified state from {prev}.","evidence":existing},
          "existing_artifacts":existing,
          "retry_possible":True,
          "retry_count":0,
          "alternative_path":contract.get("failure_policy",{}).get("fallback"),
          "required_user_action":None,
          "blocked_by":"runtime command" if proc.returncode != 0 else "missing evidence",
          "notes":contract.get("failure_policy",{}).get("escalation")
        }
        write_json(args.failure_out,packet)
        return proc.returncode if proc.returncode !=0 else 3
    return 0

if __name__=="__main__":
    raise SystemExit(main())
