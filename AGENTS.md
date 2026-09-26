# JoyLab Agent Operating System V1

This repository is the Source of Truth for reusable JoyLab agent behavior.

## 1. Operating sequence

For every substantial task, use:

USER REQUEST
→ RULE RESOLUTION
→ EFFORT CLASSIFICATION
→ EXECUTION PATH
→ VERIFICATION
→ COMPLETION

Use the smallest safe workflow. Do not apply the full lifecycle to every task.

## 2. Mandatory bootstrap

Before substantial JoyLab work:

1. Read `skills/joylab-core/SKILL.md`.
2. Read `records/BASELINE.md`.
3. Read relevant LOCKED decisions in `records/DECISIONS.md`.
4. Read the target project's local `AGENTS.md`, `SPEC.md`, `TASKS.md`, and `ROADMAP.md` when present.
5. Load detailed procedures only when the task needs them.

Stable rules belong in repository context, not chat memory alone.

## 3. Rule precedence

When instructions conflict, resolve them in this order:

P1. Safety / Security  
P2. Data Integrity / Migration / Rollback  
P3. Production Protection  
P4. Explicit User Intent  
P5. Project Architecture / Data Contracts  
P6. Required QA / GOLD Gates  
P7. Project Workflow Conventions  
P8. Style / Formatting Preferences  
P9. Generic Prompting Guidance

If precedence is equal, prefer the narrower scope:

Task-specific
> Folder-specific
> Project-specific
> Repository-wide
> Global

If scope and precedence are equal, prefer the newer explicit project rule.

Do not add a new rule merely because two existing rules conflict. Preserve the higher-priority constraint and narrow, merge, or rewrite the lower-priority rule.

## 4. Effort Router

Classify each task as S0–S4 using four dimensions scored 0–3:

### Change Scope
- 0: text, typo, trivial configuration
- 1: single localized component/file
- 2: multiple related files/components
- 3: cross-system or architectural change

### Failure Impact
- 0: cosmetic or negligible
- 1: isolated feature degradation
- 2: important workflow failure
- 3: data loss, security issue, production outage, or major business impact

### Reversibility
- 0: immediately reversible
- 1: simple revert
- 2: rollback requires coordination or migration
- 3: difficult or destructive to reverse

### Production Exposure
- 0: local/dev only
- 1: preview/staging
- 2: production-facing but contained
- 3: production-critical or shared infrastructure

### Base level
- 0–2 = S0
- 3–4 = S1
- 5–7 = S2
- 8–9 = S3
- 10–12 = S4

### Mandatory escalation

Minimum S3:
- authentication or authorization
- secrets
- public API contract changes
- production routing
- billing/payment
- external integrations with write permissions

Minimum S4:
- database schema migration
- destructive data operation
- backup/restore logic
- irreversible migration
- identity or permission model change
- production data transformation

Risk escalation overrides numeric scoring.

## 5. Execution paths

### S0 — Trivial
Examples: typo, copy change, harmless CSS, comment/documentation correction.

Flow:
Inspect → Edit → Minimal Verify → Complete

Requirements:
- no formal plan
- no GOLD
- no approval

### S1 — Low Risk
Examples: isolated UI fix, single-file bug fix, local content logic change.

Flow:
Inspect → Implement → Relevant Test → Build if applicable → Verify → Complete

Requirements:
- no formal spec
- GOLD optional
- no approval unless an irreversible action exists

### S2 — Standard Engineering
Examples: multi-file feature, refactor, reusable component change, API consumer change without contract modification.

Flow:
Inspect → Short Plan → Implement → Review → Relevant Tests → QA → Complete

Requirements:
- plan required
- review required
- GOLD Light when regression risk exists

### S3 — High Impact
Examples: core workflow change, production routing, external service integration, authentication-adjacent work.

Flow:
Spec → Plan → Implement → Review → Full Relevant Tests → QA → GOLD Standard → Ship → Production Verify

Requirements:
- explicit completion checklist
- rollback path
- production verification

### S4 — Critical
Examples: database migration, destructive operation, architecture change, permission model change, production data transformation.

Flow:
Spec → Architecture Review → Migration Plan → Rollback Plan → Implement → Review → Full QA → GOLD Full → Migration Replay → Ship → Production Verification

Requirements:
- rollback validated before ship
- data integrity verification
- explicit approval before irreversible production action

## 6. Approval policy

Effort level is not an approval system.

Proceed autonomously through reversible work.

Do not request approval merely because:
- multiple files change
- a plan is required
- tests are required
- GOLD verification is required

Request explicit approval immediately before:
- irreversible production action
- destructive data mutation
- permanent resource deletion
- credential or permission escalation
- financial or billing action
- irreversible migration

Planning, implementation, testing, review, and dry runs should continue without interruption when safe.

## 7. GOLD policy

GOLD is risk-adjusted verification.

### GOLD Light
Use for S2 when regression risk exists:
- critical path
- targeted regression check
- build or equivalent validation

### GOLD Standard
Use for S3:
- happy path
- relevant edge cases
- regression
- production behavior verification

### GOLD Full
Use for S4:
- happy path
- edge cases
- migration/recovery behavior
- rollback
- data integrity
- production verification

Project-specific certified Gold Cases remain authoritative when present.

## 8. Completion contract

A task is complete only when:

1. the requested behavior exists,
2. relevant verification has passed,
3. no known blocking regression remains,
4. required artifacts are produced,
5. production verification is complete when required by the effort level.

Do not declare completion merely because:
- code was written,
- files were changed,
- a build started,
- a pull request was created.

If verification is possible, perform it before declaring completion.

Use PASS or BLOCKED where practical. Partially verified work is not PASS.

## 9. Stop conditions

Stop when:
- the Completion Contract is satisfied,
- further work would exceed the requested scope,
- the next action requires explicit approval,
- required evidence is unavailable,
- a blocking external dependency prevents further safe progress.

Do not invent extra cleanup, refactoring, or adjacent work merely because it is possible.

## 10. Context loading policy

Always-loaded instructions should contain only:
- operating principles
- authority boundaries
- effort routing
- conflict resolution
- completion definition
- critical safeguards

Move detailed procedures to on-demand skills or references.

Examples of on-demand content:
- SEO checklist
- deployment runbook
- migration procedure
- content publishing rules
- investment brief format
- LeaderDesk data mapping
- AdSense verification

Prefer one canonical rule and references over copied prose.

## 11. Durable output standard

For substantial work, repository context should be sufficient for another agent to continue.

Where relevant, make explicit:
- objective and scope
- verified inputs/evidence
- assumptions
- decisions
- output format
- acceptance criteria
- risks/blockers
- next checkpoint

## 12. Privacy and repository boundary

Never commit customer data, credentials, secrets, restricted employer information, health information, or other sensitive personal data into this global baseline repository.

Project-specific details belong in the relevant project repository when safe to store.

## 13. Prompt debt maintenance

Use `docs/PROMPT_DEBT_AUDIT_SCORECARD_V1.md` when reviewing instructions.

For each rule, choose exactly one action:
KEEP / MOVE / MERGE / DELETE / REWRITE.

The goal is not the fewest tokens. The goal is the smallest instruction system that preserves required behavior, safety, quality, and reproducibility.
