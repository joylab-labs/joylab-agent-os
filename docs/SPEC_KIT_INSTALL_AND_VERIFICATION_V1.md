# Spec Kit Installation and Verification — JoyLab V1.0

Reference: https://github.github.com/spec-kit/installation.html
Target: developer-managed Windows/macOS/Linux environments. This document does not claim installation has occurred on those machines.

## Prerequisites
- Python 3.11 or newer
- uv package manager
- supported coding agent (Codex integration must be checked against the installed version)
- clean git working tree or dedicated temporary checkout

## Install
```bash
python3 --version
uv --version
uv tool install specify-cli
specify --version
specify check
```

Use `uv tool upgrade specify-cli` for deliberate upgrades after reviewing release notes. Pin the version in a team bootstrap once pilot validation passes.

## Existing repository onboarding
1. Record the repository URL, default branch, commit SHA, existing change status and existing test command.
2. Inventory AGENTS.md, SPEC.md, .specify/, specs/, project workflows and CI.
3. Create a separate feature branch.
4. Try initialization in a disposable copy before running it in the real repository. Confirm the exact integration key with `specify init --help`.
5. Review generated diff for overwrite, duplicated instruction, secrets and unexpected workflow changes.
6. Keep existing project policies and tests authoritative.
7. Execute the project-specific baseline tests, then the generated feature checks.
8. Open a reviewed PR; no automatic main-branch change or production deployment.

## Acceptance matrix
| ID | Check | PASS condition |
| --- | --- | --- |
| INSTALL-01 | CLI installation | `specify --version` exits 0 |
| INSTALL-02 | Integration | `specify check` identifies usable tooling |
| SAFE-01 | Existing source protection | no existing app code, AGENTS.md, SPEC.md or CI file overwritten |
| SAFE-02 | Credentials / data | no secrets or customer records added |
| SPEC-01 | Traceability | every in-scope requirement maps to task and acceptance test |
| GATE-01 | Existing tests | project regression suite passes, with logs |
| GATE-02 | Impact | S3/S4 rollback and GOLD evidence present |
| RELEASE-01 | Review | PR reviewed and approved under existing project rules |

Unrun checks are UNVERIFIED, not PASS.
