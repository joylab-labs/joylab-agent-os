# Prompt Debt Audit Scorecard V1

Use this scorecard to review JoyLab instructions, agent files, skills, hooks, workflow guidance, and completion rules.

Audit only first. Do not modify files during discovery unless the task explicitly requests a cleanup patch.

## 1. Allowed actions

Every reviewed rule must receive exactly one action:

- KEEP — correct, scoped, current, and worth retaining where it is.
- MOVE — valid rule, wrong loading scope; move to a narrower project, folder, skill, runbook, or on-demand reference.
- MERGE — materially duplicates another rule; consolidate into one canonical rule.
- DELETE — obsolete, redundant, harmful, or no longer needed.
- REWRITE — intent is valid but wording, scope, precedence, or completion behavior is unsafe or unclear.

## 2. Debt types

Tag zero or more:

- DUPLICATE
- CONFLICT
- OBSOLETE
- OVERCONTROL
- PREMATURE_STOP
- EXCESSIVE_CONFIRMATION
- TOKEN_WASTE
- UNCLEAR_SCOPE
- MODEL_WORKAROUND
- MISSING_COMPLETION_RULE
- MISSING_VERIFICATION_RULE
- HIDDEN_PRECEDENCE
- BROAD_ALWAYS_LOAD
- STALE_PROJECT_RULE

## 3. Required inventory fields

For each rule capture:

| Field | Meaning |
|---|---|
| Rule ID | Stable audit identifier |
| Source | File/path and section |
| Exact rule | Short verbatim or precise paraphrase |
| Scope | Task / Folder / Project / Repo / Global |
| Load mode | Always / Conditional / On-demand |
| Priority | P1–P9 from AGENTS.md |
| Token estimate | Approximate tokens attributable to this rule |
| Duplicate with | Rule IDs expressing the same requirement |
| Conflict with | Rule IDs that can produce incompatible behavior |
| Debt tags | Zero or more debt types |
| Action | KEEP / MOVE / MERGE / DELETE / REWRITE |
| Canonical target | Destination/source-of-truth if moved or merged |
| Expected benefit | Context, clarity, autonomy, safety, testability, maintenance |
| Verification | How to prove cleanup did not regress behavior |

## 4. Priority and specificity

Use AGENTS.md precedence:

P1 Safety / Security  
P2 Data Integrity / Migration / Rollback  
P3 Production Protection  
P4 Explicit User Intent  
P5 Project Architecture / Data Contracts  
P6 Required QA / GOLD Gates  
P7 Project Workflow Conventions  
P8 Style / Formatting Preferences  
P9 Generic Prompting Guidance

Equal precedence resolves by narrower scope:

Task > Folder > Project > Repository > Global

If still equal, prefer the newer explicit project rule.

Do not lower a P1–P3 safeguard merely to reduce tokens.

## 5. Token-cost model

Estimate four values for each audited source:

- Raw Tokens — total instruction tokens in the source.
- Always-loaded Tokens — tokens loaded for most tasks.
- Conditional Tokens — tokens loaded only for relevant task classes.
- Removable Tokens — tokens safely removable after merge/delete/rewrite.

Primary KPI:

`Prompt Overhead Ratio = Removable Always-loaded Tokens / Total Always-loaded Tokens`

A high token count is not automatically debt. A long, on-demand migration runbook may be healthy. A short duplicated global rule repeated across every agent may be expensive.

## 6. Decision rules

### KEEP
Use when all are true:
- behavior is still required,
- scope is correct,
- precedence is clear,
- wording does not force unnecessary process,
- no canonical duplicate exists.

### MOVE
Use when:
- the rule is valid,
- but it is not needed for most tasks,
- or it belongs to one project/domain/tool.

Typical destinations:
- project AGENTS.md
- folder instructions
- skill
- deployment runbook
- migration guide
- content policy
- domain-specific reference

### MERGE
Use when:
- two or more rules express substantially the same requirement,
- small differences can be captured in one canonical version.

Preserve meaningful exceptions. Replace copies with references.

### DELETE
Use when:
- a rule is obsolete,
- fully duplicated by a canonical rule,
- was a workaround for an older model/tool,
- creates repeated confirmation without risk reduction,
- exposes reasoning without operational value,
- or is no longer reachable/applicable.

### REWRITE
Use when:
- the intent is needed,
- but the current rule is too broad, vague, conflicting, or likely to cause premature stopping.

Prefer narrowing scope over adding exceptions.

## 7. Red-flag heuristics

Inspect carefully when a rule contains patterns such as:

- “always” or “never” without a safety reason,
- “ask before” for reversible work,
- “think step by step” or requests to expose reasoning,
- model-name-specific compensation,
- mandatory full planning for trivial work,
- mandatory full test suites for cosmetic changes,
- “done” immediately after code generation,
- duplicated bootstrap instructions across model-specific files,
- copied release or GOLD procedures in multiple places,
- generic rules that conflict with project-local contracts.

These are signals, not automatic failures.

## 8. Audit workflow

1. Map all instruction-bearing files.
2. Mark scope and load mode.
3. Estimate token cost.
4. Detect duplicates.
5. Detect conflicts.
6. Resolve precedence.
7. Assign debt tags.
8. Choose one action.
9. Propose the smallest cleanup patch.
10. Paper-test the cleaned system.
11. Apply only after review or when explicitly requested.

## 9. Required scenario walkthroughs

Paper-test at least:

### Scenario A — one-line bug fix
Expected: S0/S1 path, no full spec, no unnecessary approval.

### Scenario B — multi-file refactor
Expected: S2 path, short plan, review, targeted regression.

### Scenario C — long autonomous implementation
Expected: sustained execution without repetitive approval loops; completion contract remains explicit.

### Scenario D — production hotfix
Expected: risk-sensitive S2/S3 path; production protection outranks workflow convenience.

### Scenario E — parallel/subagent work
Expected: one canonical rule set; no contradictory bootstrap copies.

### Scenario F — data/schema migration
Expected: mandatory S4, rollback and integrity gates preserved.

## 10. Output template

### Executive Summary
- highest-impact debt findings
- estimated always-loaded token reduction
- safeguards that must remain

### Confirmed Issues
For each:
- source
- rule
- debt type
- action
- rationale
- target
- verification

### Suspected Issues
Keep hypotheses separate from confirmed findings.

### Duplication Map
Canonical rule → redundant copies.

### Conflict Map
Rule A ↔ Rule B → precedence winner → rewrite/move decision.

### Token Cost Map
Always-loaded vs conditional vs removable.

### Minimal Cleanup Patch
Smallest set of changes with highest benefit.

### Verification Checklist
- shorter always-loaded context
- no lost P1–P3 safeguards
- no regression in certified GOLD behavior
- fewer unnecessary approval stops
- clearer completion conditions
- no new contradictory copies

## 11. Initial audit observations for joylab-agent-os

The current repository already shows two likely high-value audit targets:

1. `CLAUDE.md` and `GEMINI.md` repeat the same bootstrap logic already present in `AGENTS.md`.
   - Candidate action: MERGE or REWRITE as thin pointers to the canonical bootstrap.
   - Verify each tool still discovers the repository entry point it needs.

2. `skills/joylab-core/SKILL.md` defines a full default lifecycle:
   `SPEC → PLAN → IMPLEMENT → TEST → REVIEW → REGRESSION → RELEASE GATE`.
   - Candidate action: REWRITE or scope it so the S0–S4 router controls when the full lifecycle applies.
   - Preserve the existing rule that partially verified work is not complete.

These are confirmed only after the source files and tool-loading behavior are checked together.

## 12. Audit principle

Do not optimize for the smallest file.

Optimize for:
- clear precedence,
- minimal always-loaded context,
- risk-adjusted verification,
- durable project knowledge,
- autonomous reversible execution,
- explicit completion,
- preserved safety and data integrity.
