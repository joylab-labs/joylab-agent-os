# JoyLab Spec Kit Adoption Standard V1.0

Status: ADOPTED — documentation standard; actual agent integration and per-project runtime gates remain separately verified
Owner: JoyLab Agent OS
Reference: https://github.com/github/spec-kit

## Purpose
Use GitHub Spec Kit as an optional structured specification and delivery tool underneath the existing JoyLab Agent OS. Existing S0–S4 risk classification, project contracts, executable GOLD tests, and release approvals remain authoritative.

## Applicability
| Effort | Default Spec Kit use | Existing JoyLab gate |
| --- | --- | --- |
| S0 | None | Minimal verification |
| S1 | Optional lightweight specification | Relevant test |
| S2 | Specify + plan + tasks when useful | Review + relevant tests + GOLD Light if regression risk |
| S3 | Constitution + specify + clarify + plan + checklist + tasks + analyze + implement + converge | GOLD Standard + rollback + production verification |
| S4 | S3 sequence plus architecture, migration and recovery plans | GOLD Full + migration replay + approval for irreversible action |

Spec Kit never downgrades a mandatory S3/S4 escalation. A generated checklist is not evidence of a passing test. No auto-merge or auto-deploy is implied.

## Authority / conflicts
1. Security, privacy, data integrity, existing project AGENTS.md and contracts, central repository tier and release policy win over generated Spec Kit artifacts.
2. Do not replace an existing SPEC.md or AGENTS.md with generated files.
3. Keep generated artifacts scoped to the feature (e.g. specs/NNN-feature/) and reference existing authoritative documents.
4. Changes to KPI denominators, calculations, financial gates, data retention, PII handling, backup/restore or production workflows require explicit impact analysis and regression evidence.
5. Never include customer-level records, internal transcripts, private keys or credentials in prompts, specs, tests, commits or AI tool outputs. Use synthetic fixtures.

## Feature lifecycle
1. Read the global bootstrap and project-specific rules.
2. Classify S0–S4 and record the reason.
3. For material features, define user story, scope, non-goals, measurable acceptance criteria and applicable invariants.
4. Resolve ambiguity before coding. Implement only approved scope.
5. Break work into reviewable tasks and identify affected files and rollback method.
6. Run existing project tests and new acceptance tests; record actual commands, logs and outcomes.
7. Compare implementation to spec, capture unresolved deviations, then use the established project PR, GOLD and release process.
8. If requirements change, update spec, plan, tasks and tests together, not only code.

## Required evidence record for S2+
- feature ID / owner / repository / base commit
- effort rating and applicable contracts
- spec, plan, tasks and acceptance test references
- command results with PASS / BLOCKED / UNVERIFIED
- diff review and regression notes
- rollback plan for S3+, verified recovery for S4
- deployment and production smoke evidence where applicable

## Safe adoption in existing repositories
Run `specify check` first. Inventory existing .specify, AGENTS.md, SPEC.md, specs/, commands and CI. Use a clean branch and a dry-run or isolated scratch checkout for initial CLI initialization. Inspect all generated diffs before moving them into the actual repository. Never use --force or overwrite existing files as an onboarding shortcut.

## First pilot
Pilot on one additive, non-production feature in joylab-product-hub. Validate the spec/plan/tasks linkage and pre-existing tests before extending to LeaderDesk, Publishing OS and Core8. No global rollout until pilot evidence passes.
