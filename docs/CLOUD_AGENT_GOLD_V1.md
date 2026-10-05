# JoyLab Cloud Agent GOLD V1

Status: PILOT
Repository: `joylab-labs/joylab-agent-os`
Owner authority: Human
Execution target: Claude Code Cloud Session

## Mission

Prove that a bounded GitHub Issue can be completed remotely through:

```text
Issue
→ Cloud Session
→ Inspect
→ Feature Branch
→ Implement
→ Verify
→ Draft PR
→ Human Gate
```

The operator's MacBook may be offline or closed during cloud execution. This does not expand agent authority.

## GOLD-001 success criteria

A run is GOLD only when every gate below has inspectable evidence.

### G0 — Issue Gate
- Issue uses a bounded mission.
- In-scope and out-of-scope work are explicit.
- Acceptance criteria are testable.
- Required verification commands are listed or discoverable.

### G1 — Scope Gate
- `CLAUDE.md` and `AGENTS.md` were read.
- Work is performed on a feature branch.
- No direct commit to `main`.
- No unrelated dependency, permission, secret, schema, or production change.

### G2 — Verification Gate
Minimum repository verification:

```bash
python -m pip install -e ".[dev]"
pytest -q
```

Any project-specific GOLD or release gate triggered by the change must also pass.

PASS requires:
- relevant tests GREEN;
- no known blocking regression;
- False Autonomy remains 0;
- no required gate is bypassed.

### G3 — Draft PR Gate
The agent creates a Draft PR that includes:
- Issue reference;
- scope summary;
- files changed;
- verification commands and results;
- known risks;
- rollback note when relevant.

### G4 — Human Gate
The agent must stop at Draft PR.

Forbidden:
- self-approval;
- merge;
- branch-protection bypass;
- required-check bypass;
- production deployment when not explicitly approved.

## BLOCKED contract

If any gate cannot be satisfied, the run is BLOCKED rather than partially PASS.

Report:
1. failed gate;
2. failing check;
3. likely root cause;
4. files changed;
5. evidence available;
6. safest next action.

## GOLD-001 pilot task

The first pilot should be intentionally low-risk and repository-local.

Recommended task:

> Add a small repository contract test that verifies the Claude Cloud operating contract contains the non-negotiable controls: dedicated branch, verification, Draft PR, Human Gate, and never-merge rule.

Why this task:
- reversible;
- no production behavior change;
- exercises Issue → branch → code → pytest → Draft PR;
- provides machine-verifiable evidence;
- does not require secrets or external services.

## Certification record

Record the following after the pilot:

| Field | Required value |
|---|---|
| Issue | URL / number |
| Cloud session | completed |
| Feature branch | present |
| Direct main commit | false |
| Tests | PASS |
| Required gates | PASS |
| Draft PR | URL / number |
| Agent merge | false |
| Human Gate | preserved |
| GOLD result | PASS / BLOCKED |

Only a full PASS may be named `JOYLAB-CLOUD-AGENT-GOLD-001`.
