---
name: Cloud Agent Task
about: Bounded Issue for Claude Code Cloud execution
title: "[CLOUD] "
labels: ""
assignees: ""
---

## Mission

Describe one bounded outcome.

## Scope

### In
- 

### Out
- unrelated refactors
- dependency upgrades unless explicitly required
- secrets / permissions changes
- direct changes to `main`
- merge

## Acceptance Criteria

- [ ] Requested behavior exists.
- [ ] Relevant tests pass.
- [ ] Build / validation passes when applicable.
- [ ] No known blocking regression remains.
- [ ] Draft PR contains verification evidence.
- [ ] Human Gate remains required for merge.

## Verification Commands

```bash
python -m pip install -e ".[dev]"
pytest -q
```

Add narrower project-specific checks here when needed.

## Risk / Effort

Expected JoyLab effort level: S0 / S1 / S2 / S3 / S4

If the Issue touches a mandatory escalation category in `AGENTS.md`, use that higher level.

## Cloud Execution Instruction

Implement this Issue only.

Read `CLAUDE.md` and `AGENTS.md` first.
Inspect before editing.
Use a dedicated feature branch.
Do not modify unrelated files.
Run all relevant verification.
If verification passes, create a Draft PR.
If verification fails, report BLOCKED with evidence.
Never merge.
