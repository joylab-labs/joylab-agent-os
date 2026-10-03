# JoyLab Decision Router V1

Status: SHADOW CANDIDATE  
Owner: JoyLab  
Source of Truth: `joylab-agent-os`

## Mission

Use the smallest safe intelligence layer for every decision.

```text
Deterministic Code -> Jev -> Luna -> Sol -> Astra -> Human
```

This is not a capability ranking. It is an authority and cost-routing model.

## Authority

1. Safety / security
2. Data integrity / rollback
3. Deterministic gates
4. Human approval boundaries
5. Decision Router
6. Model output

A probabilistic model must never override a deterministic hard gate.

## Tier 0 — Deterministic Code

Use code when the answer can be computed exactly, including:
- schema validity
- test PASS/FAIL
- CI state
- snapshot diff
- data-loss count
- checksum equality
- migration idempotency
- render resolution/fps/duration
- certification threshold checks

## Tier 1 — Jev

Jev is eligible only when all are true:
- every valid output is known in advance;
- the task is a fast fuzzy judgment;
- the judgment repeats enough to matter;
- an error is recoverable by fallback or a hard gate;
- the outcome can be evaluated later.

Jev does not own destructive execution, release approval, GOLD certification,
identity merge, permission escalation, financial execution, irreversible
migration, or production deletion.

## Tier 2 — Luna

Use for lightweight exploration, routine language understanding, and low-risk
transformations that exceed bounded classification.

## Tier 3 — Sol

Default engineering worker for multi-file implementation, debugging, tests,
standard architecture application, and substantial synthesis.

## Tier 4 — Astra

Use at three checkpoints:
1. before architecture when the approach itself is uncertain;
2. after repeated targeted failures;
3. before GOLD completion to find omissions.

## Tier 5 — Human

Required immediately before irreversible or authority-changing actions,
including destructive production mutation, permanent deletion, credential or
permission escalation, irreversible migration, financial action, ambiguous
identity merge, or official-record confirmation.

## Routing order

```text
Can deterministic code decide?
  yes -> CODE
  no
Is the output bounded?
  no -> Luna/Sol
  yes
Is this repeated fast judgment?
  no -> Luna/Sol
  yes
Is autonomous error recoverable?
  no -> Sol/Astra/Human
  yes -> Jev candidate
```

## Shadow Mode

V1 is shadow-only.

```text
Input
  |-- existing router -> actual_route -> executes
  '-- Jev router     -> shadow_route -> never executes
```

Production behavior change in Shadow Mode must be zero.

## Initial confidence policy

These values are calibration seeds, not permanent production thresholds.

- confidence >= 0.90: AUTO_CANDIDATE
- 0.70 <= confidence < 0.90: MODEL_FALLBACK
- confidence < 0.70: HIGHER_TIER_REVIEW

Each decision type must eventually own its own calibrated threshold.

## Mandatory safety overrides

Any of the following bypasses autonomous Jev authority:
- security
- credentials
- permissions
- production routing
- data integrity
- identity ambiguity
- database migration
- backup/restore
- financial action
- irreversible change

## False Autonomy Gate

`FALSE_AUTONOMY` means a decision requiring deterministic or human authority
was allowed to execute autonomously.

Hard rule:

```text
FALSE_AUTONOMY == 0
```

If false autonomy is greater than zero:

```text
ROUTER RELEASE = HOLD
```

Accuracy cannot override this gate.

## Metrics

Priority order:
1. False Autonomy
2. hard-gate violations
3. calibration
4. accuracy
5. fallback / unknown rate
6. latency
7. cost

## Project boundaries

### JoyLab Agent OS
Jev candidates:
- effort preclassification
- context-loading choice
- failure triage
- fallback selection
- evidence relevance
- prompt-debt classification

Existing S0-S4 mandatory escalation remains authoritative.

### LeaderDesk
Jev candidates:
- defect type
- GOLD relevance
- failure domain
- data-integrity risk triage
- review priority

Never delegate G01-G10 PASS/FAIL, Snapshot Diff, Data Loss, release GOLD
decision, migration integrity, or identity auto-merge to Jev.

### Motion Factory
Jev candidates:
- visual defect type
- reuse vs extend
- fix vs render vs escalate
- scene complexity
- renderer route

Never delegate schema validity, fps, resolution, duration, file existence,
determinism, or reproducibility to Jev.

## Promotion

Stage 0 — Baseline  
Stage 1 — Shadow only  
Stage 2 — Assisted  
Stage 3 — Controlled Auto by certified decision type  
Stage 4 — Production Certified

Production certification requires:
- False Autonomy = 0
- hard-gate violations = 0
- regression GREEN
- accepted calibration
- verified rollback

Certification is per decision type, never global.
