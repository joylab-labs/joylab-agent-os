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
| joylab-publishing-os | YES | YES | YES | YES | YES | Contract Router V1 merged after full Build + contract checks passed. |
| joylab-content-os | YES | YES | YES | YES | YES | Local router + SPEC/source-of-truth cleanup merged; post-merge Tests passed. |
| leaderdesk | YES | YES | YES | YES* | YES | Local router + migration-status cleanup merged. Tests and web/Windows build passed; artifact upload was blocked by GitHub Actions storage quota after build. |

## Coverage

### Audit coverage
5 / 5 repositories = **100%**

All first-wave repositories have been inspected and have a documented Prompt Debt assessment or canonical architecture review.

### Router merged to main
5 / 5 repositories = **100%**

Merged:
- joylab-agent-os
- joylab-command-center
- joylab-publishing-os
- joylab-content-os
- leaderdesk

### Full cleanup + verification merged
5 / 5 repositories = **100%***

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

Operational follow-up:
- main-push release automation still deserves a separate policy review
- the post-merge workflow reached passing tests, web build, and Windows installer build, then failed at artifact upload because GitHub Actions artifact storage quota was exhausted; this is tracked as infrastructure capacity, not a prompt-architecture regression.

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

1. First-wave Prompt Architecture V1 adoption is complete across all 5 repositories.
2. Resolve the separate LeaderDesk GitHub Actions artifact-storage quota issue.
3. Review LeaderDesk main-push release creation policy separately from prompt cleanup.
4. Expand the scorecard to the next JoyLab repositories only after this first-wave pattern remains stable.


## Verification note

`YES*` for LeaderDesk means the cleanup itself is verified by successful dependency install, audit, tests, web build, and Windows installer build on the post-merge main workflow. The workflow's final artifact-upload step failed because the repository/account GitHub Actions artifact storage quota was exhausted. That quota failure did not invalidate the documentation/router changes, but it remains an operational release-pipeline blocker that must be resolved separately.
