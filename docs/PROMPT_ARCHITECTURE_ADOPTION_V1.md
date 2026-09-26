# JoyLab Prompt Architecture V1 — Adoption Dashboard

Updated: 2026-09-26

## Scope

This dashboard tracks the first five repositories selected for JoyLab Prompt Architecture V1 adoption:

1. joylab-agent-os
2. joylab-command-center
3. joylab-publishing-os
4. joylab-content-os
5. leaderdesk

## Adoption stages

- AUDITED — repository rules and instruction-bearing files inspected.
- ROUTED — local or global AGENTS routing exists.
- CLEANED — confirmed prompt debt cleanup merged.
- VERIFIED — relevant CI/GOLD verification passed after cleanup.
- MAIN — architecture cleanup is present on main.

## Current status

| Repository | Audited | Router | Cleanup | Verification | Main status | Notes |
|---|---:|---:|---:|---:|---:|---|
| joylab-agent-os | YES | YES | YES | YES | YES | Global Agent OS V1 is canonical. |
| joylab-command-center | YES | YES | YES | YES | YES | Local router + implementation-status cleanup merged. |
| joylab-publishing-os | YES | PR OPEN | PR OPEN | PENDING | PARTIAL | Audit merged; Contract Router V1 is in PR #336. |
| joylab-content-os | YES | NO | AUDIT PR | PENDING | NO | Audit PR #1 open; cleanup not yet applied. |
| leaderdesk | YES | NO | AUDIT PR | PENDING | NO | Audit PR #1 open; cleanup not yet applied. |

## Coverage

### Audit coverage
5 / 5 repositories = **100%**

All first-wave repositories have been inspected and have a documented Prompt Debt assessment or canonical architecture review.

### Router merged to main
2 / 5 repositories = **40%**

Merged:
- joylab-agent-os
- joylab-command-center

Pending:
- joylab-publishing-os — PR #336
- joylab-content-os — cleanup not started
- leaderdesk — cleanup not started

### Full cleanup + verification merged
2 / 5 repositories = **40%**

The current completion definition for “fully adopted” is:
- audit complete
- router present
- confirmed cleanup merged
- relevant CI/GOLD green
- main updated

## Highest-risk remaining debt

### joylab-publishing-os
Risk class: routing / authority

Main issue:
many valid specialized contracts exist, but agents need a local task-to-contract router.

Current action:
Contract Router V1 PR #336.

### joylab-content-os
Risk class: source-of-truth accessibility / status drift

Main issues:
- declared implementation source of truth is absent from repository
- SPEC current-state marker conflicts with README
- universal Unit + Gold + Regression wording is over-broad for trivial/docs changes

Next action:
create local AGENTS router and repair SPEC status without weakening HR-01~HR-05.

### leaderdesk
Risk class: routing / migration-status drift

Main issues:
- no local router
- migration sequence appears partially implemented while freeze wording remains broad
- Mobile GOLD and PC GOLD need separate routing
- release automation behavior needs a separate operational-policy review

Next action:
create local AGENTS router, then update migration-status wording using repository evidence.

## Architecture target

The desired steady state is:

```text
Global JoyLab Agent OS
        ↓
Project AGENTS Router
        ↓
Relevant Contract / Runbook only
        ↓
Executable Gate
        ↓
Risk-adjusted GOLD
        ↓
Completion Contract
```

## Rules for adoption

A repository should not be marked fully adopted merely because it has an `AGENTS.md`.

It is fully adopted only when:
1. active rules have clear precedence,
2. project-specific rules are locally discoverable,
3. unrelated contracts are not always loaded,
4. executable gates remain authoritative,
5. stale status/process text is removed or re-scoped,
6. cleanup passes relevant CI/GOLD,
7. main contains the verified result.

## Next sequence

1. Finish and merge Publishing OS PR #336 after CI is green.
2. Merge Content OS audit PR, then open a cleanup PR.
3. Merge LeaderDesk audit PR, then open a cleanup PR.
4. Recalculate adoption coverage.
5. Expand the same scorecard to the next JoyLab repositories only after the first-wave pattern is stable.
