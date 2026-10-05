# Claude Bootstrap for JoyLab

Use `AGENTS.md` as the canonical operating system and precedence source.

Before substantial JoyLab work:
1. Read `AGENTS.md`.
2. Follow its mandatory bootstrap.
3. Load project-local instructions and on-demand skills only when relevant.

Do not duplicate global operating rules in this file. Model-specific guidance belongs here only when Claude requires behavior not covered by `AGENTS.md`.

## Claude Code Cloud Session contract

When a task originates from a GitHub Issue and is executed in Claude Code Cloud:

1. Treat the Issue as the task boundary, not as authority to bypass `AGENTS.md`.
2. Inspect the repository before editing and identify the smallest safe change set.
3. Create or use a dedicated feature branch. Never commit directly to `main`.
4. Do not change unrelated files, dependencies, schemas, permissions, secrets, deployment settings, or production data unless the Issue explicitly requires it and `AGENTS.md` permits it.
5. Run the repository's relevant verification before reporting success.
6. If verification fails, report BLOCKED with the failing check, likely cause, files changed, and safest next action.
7. On success, create a Draft PR containing scope, files changed, verification evidence, risks, and rollback notes when relevant.
8. Never merge the PR. Merge remains a Human Gate.
9. Never weaken or bypass required checks, GOLD gates, branch protection, or the False Autonomy gate to make a task pass.
10. For the Cloud Agent GOLD pilot, follow `docs/CLOUD_AGENT_GOLD_V1.md`.

Cloud execution may continue without the operator's laptop being active, but authority boundaries do not change.
