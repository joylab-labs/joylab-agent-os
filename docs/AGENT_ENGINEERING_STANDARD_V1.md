# JoyLab Agent Engineering Standard V1.0

This document expands the compact rules in `AGENTS.md`. The machine-readable contract is authoritative for CI validation.

## Core model

A persistent agent is not a long prompt. It is a bounded responsibility with state, a trigger, permissions, evidence, failure handling, and a stop path.

```text
Responsibility
→ State
→ Trigger
→ Action
→ Evidence
→ Human Gate when required
→ Next state or Stop
```

## Contract fields

1. **Responsibility** — what the agent continuously owns or monitors.
2. **Goal** — the desired state.
3. **Inputs** — approved sources, accounts/workspaces, and excluded sources.
4. **State** — current state source and prior state source when comparison matters.
5. **Trigger** — exactly one primary type: manual, schedule, event, follow_up.
6. **Actions** — allowed and prohibited operations.
7. **Approval** — human-gated operations.
8. **Evidence** — inspectable artifacts required for completion.
9. **Failure policy** — retry limit, fallback, escalation.
10. **Stop** — end conditions and offboarding actions.
11. **Reporting** — destination, format, alert threshold.

## Trigger rules

- **manual**: started explicitly by an operator.
- **schedule**: include timezone and schedule expression.
- **event**: include source, event name, and verified registration.
- **follow_up**: include the condition that wakes the responsibility again.

A connection or app installation is not a trigger.

## Permission model

Use the narrowest permission compatible with the responsibility:

`CONNECTED → READ → WRITE → EXECUTE → PUBLISH/EXTERNAL SEND → DELETE/IRREVERSIBLE`

Authentication does not prove authorization for downstream actions.

## Evidence

Execution is not completion. Use inspectable evidence such as:
- file or dataset
- URL
- commit or PR
- test log
- deployment result
- production verification

Research-heavy work should distinguish FACT, SOURCE CLAIM, INFERENCE, and UNKNOWN/UNVERIFIED.

## Failure and retry

Failures are durable outputs. Emit a Failure Packet whenever a meaningful responsibility cannot safely continue.

Default repeated-failure discipline:
1. retry once if the failure is plausibly transient;
2. before the second equivalent retry, re-check inputs, environment, permissions, and assumptions;
3. at the configured retry limit, stop that path and escalate with preserved artifacts and last known good state.

## Adoption and ROI

New recurring responsibilities should normally move through:
1. read-only observation;
2. one-off delegation;
3. bounded recurring work;
4. measured keep / expand / stop decision.

Useful metrics include execution count, retries, human review time, usage/external cost, rework, manual baseline time, and net time saved.

## Shutdown

Stopping the visible task is not enough. Offboarding may require:
- stopping delegated/background jobs;
- canceling schedules or events;
- revoking app/local access;
- logging out web sessions;
- preserving or removing generated artifacts;
- handling retained context according to actual product controls.

## Canonical schemas

- `schemas/agent_contract.schema.json`
- `schemas/failure_packet.schema.json`

Validate examples or project contracts with:

```bash
python scripts/validate_agent_contracts.py <agent-contract.json> [...]
python scripts/validate_agent_contracts.py --failure <failure-packet.json> [...]
```
