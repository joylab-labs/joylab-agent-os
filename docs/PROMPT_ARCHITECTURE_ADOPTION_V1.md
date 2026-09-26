# JoyLab Prompt Architecture V1 — Adoption Dashboard

Updated: 2026-09-26

## Scope

This dashboard tracks JoyLab Prompt Architecture V1 adoption across completed rollout waves.

### Wave 1
1. joylab-agent-os
2. joylab-command-center
3. joylab-publishing-os
4. joylab-content-os
5. leaderdesk

### Wave 2
6. JoyLab_Vibe_Coding_OS_v1.0
7. joylab-core8-engine
8. joylab-portfolio-os

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
| joylab-publishing-os | YES | YES | YES | YES | YES | Contract Router V1 merged after full Build + contract checks passed. |
| joylab-content-os | YES | YES | YES | YES | YES | Local router + SPEC/source-of-truth cleanup merged; post-merge Tests passed. |
| leaderdesk | YES | YES | YES | YES | YES | Local router + migration-status cleanup merged. CI/release workflow later separated; main verification now passes without packaging artifacts. |

### Wave 2 status

| Repository | Audited | Router | Cleanup | Verification | Main status | Notes |
|---|---:|---:|---:|---:|---:|---|
| JoyLab_Vibe_Coding_OS_v1.0 | YES | YES | YES | YES | YES | Risk-adjusted S0-S4 routing merged; full SOP and 200-item Release Gate are now on-demand. |
| joylab-core8-engine | YES | YES | YES | YES | YES | CLAUDE bootstrap slimmed, Paperthin rituals made optional techniques, QUALITY_GATE scoped by effort; test/CI/release gates passed. |
| joylab-portfolio-os | YES | YES | YES | YES | YES | Local router + README/SSOT cleanup merged after Portfolio Engine and Database Tests passed. |

## Coverage

### Audit coverage
8 / 8 repositories = **100%**

All Wave 1 and Wave 2 repositories have been inspected and have a documented Prompt Debt assessment or canonical architecture review.

### Router merged to main
8 / 8 repositories = **100%**

Merged:
- joylab-agent-os
- joylab-command-center
- joylab-publishing-os
- joylab-content-os
- leaderdesk
- JoyLab_Vibe_Coding_OS_v1.0
- joylab-core8-engine
- joylab-portfolio-os

### Full cleanup + verification merged
8 / 8 repositories = **100%**

The current completion definition for “fully adopted” is:
- audit complete
- router present
- confirmed cleanup merged
- relevant CI/GOLD green
- main updated

## Wave 2 completion summary

### JoyLab Vibe Coding OS
Resolved:
- global precedence aligned with JoyLab Agent OS;
- full 15-step SOP made on-demand;
- 200-item Release Gate limited to actual release readiness;
- reversible low-risk work no longer requires blanket approval/process overhead.

### joylab-core8-engine
Resolved:
- AGENTS is canonical router;
- CLAUDE reduced to a thin bootstrap;
- /hate, /sip, /mandela, /factchk, /ssotize changed from mandatory stages to optional verification techniques;
- QUALITY_GATE is risk-adjusted by S0-S4;
- README no longer duplicates hard investment thresholds;
- historical Codex bootstrap prompt is explicitly non-current.

### joylab-portfolio-os
Resolved:
- local AGENTS router added;
- V1.3 parity oracle and V1.4 hard policy preserved;
- ETF/DB/engine contracts are loaded on demand;
- README status/SSOT ownership refreshed;
- Portfolio Engine Tests and Database Tests passed before merge.

## Highest-risk remaining debt

### joylab-publishing-os
Risk class: routing / authority

Main issue:
many valid specialized contracts exist, but agents need a local task-to-contract router.

Current action:
Contract Router V1 merged to main; monitor future contract-routing drift.

### joylab-content-os
Status: first-wave adoption complete.

Resolved:
- local AGENTS router added
- SPEC promoted to accessible repository-local execution source
- stale current-state marker removed
- verification policy scoped by effort without weakening HR-01~HR-05
- post-merge Tests passed.

### leaderdesk
Status: first-wave prompt architecture adoption complete.

Resolved:
- local AGENTS router added
- Mobile / PC / migration / release scopes separated
- dry-run migration implementation reflected in status docs
- blanket feature freeze narrowed without weakening data-integrity safeguards
- CI verification is separated from packaging/release
- ordinary main pushes no longer create installer artifacts or formal releases
- main verification now passes under the separated workflow

Operational follow-up:
- existing duplicate historical artifacts may still be cleaned up after preservation checks and explicit deletion approval.

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

1. Wave 1 adoption is complete across 5 / 5 repositories.
2. Wave 2 adoption is complete across 3 / 3 repositories.
3. Overall tracked adoption is 8 / 8 repositories = 100%.
4. Keep prompt-debt review as a maintenance check when new global rules, model-specific bootstraps, or major contracts are introduced.
5. Select Wave 3 only when there is a concrete routing/precedence problem to solve, rather than expanding mechanically.



## Verification notes

- Wave 1 and Wave 2 Prompt Architecture changes are present on main.
- Vibe Coding OS cleanup passed the JoyLab Release Gate before merge.
- Core8 cleanup passed test, ci-standard-v1, and JoyLab Release Gate before merge.
- Portfolio OS cleanup passed Portfolio Engine Tests and Database Tests before merge.
- LeaderDesk's later CI/release separation passed both PR verification and post-merge main verification; installer packaging is now limited to manual/tag release paths.
