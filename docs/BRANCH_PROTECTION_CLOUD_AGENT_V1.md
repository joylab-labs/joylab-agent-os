# Branch Protection Target — Cloud Agent GOLD V1

This document is the desired protection state for `main`.

The repository governance SSOT remains authoritative. Apply these settings only when they do not weaken central policy.

## Target controls

- Require pull request before merging.
- Require at least one human approval for Cloud-Agent-authored changes.
- Require conversation resolution before merge.
- Require repository CI / GOLD checks defined by central policy.
- Block force pushes to `main`.
- Block deletion of `main`.
- Do not allow automation to bypass the Human Gate.
- Do not grant Claude Code Cloud permission to merge solely because it can push branches.

## Agent authority

Allowed:
- read repository;
- create feature branch;
- edit bounded files;
- run verification;
- commit to feature branch;
- push feature branch;
- create Draft PR.

Not allowed:
- direct push to `main`;
- merge;
- protection bypass;
- secret or permission escalation;
- destructive production action.

## Verification

Protection is considered operational only after GitHub repository settings confirm the effective rules. Documentation alone is not proof of enforcement.
