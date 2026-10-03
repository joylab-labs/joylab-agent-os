# JoyLab Free-Tier CI Policy V1

Status: ACTIVE POLICY CANDIDATE
Scope: private JoyLab GitHub repositories using GitHub-hosted Actions
Primary objective: keep release safety alive while staying inside the monthly included Actions allowance.

## 1. Budget invariant

- Paid Actions usage is not required for normal operation.
- Account-level Actions budget remains $0 with stop-usage enabled.
- CI design target is <= 80% of included monthly minutes.
- Keep >= 20% as reserve for release fixes, emergency verification, and reruns.
- A workflow that cannot fit the free-tier envelope must move to manual execution, a public repository, self-hosted execution, or another free execution plane.

## 2. Priority order

1. Release Gate / production safety
2. PR validation that protects data integrity or production correctness
3. Change-triggered production verification
4. Scheduled telemetry / reporting
5. Convenience dashboards and recurring audits

When capacity is constrained, lower priorities are disabled before higher priorities.

## 3. Private repository trigger rules

### Required / preferred

- Release Gate: PR and/or main push, path-filtered where possible.
- Production verification: trigger from successful deployment or explicit manual dispatch.
- Heavy audits: manual dispatch by default.
- Recurring reports: weekly unless a documented business requirement needs higher frequency.

### Prohibited by default

- Hourly scheduled GitHub-hosted workflows in private repos.
- Daily full builds for dashboards/reports that can run weekly or on demand.
- Windows/macOS build on every PR when the same artifact is only needed for release.
- Duplicate PR + push workflows that run the same expensive build twice for one change.
- Unbounded test matrices on routine PRs.

Exceptions require an explicit documented reason and a monthly minute estimate.

## 4. Runner policy

- Linux is the default validation runner.
- Windows/macOS runners are reserved for platform-specific release or explicit compatibility validation.
- Desktop installer builds are manual/release-candidate only unless a blocking platform regression requires temporary PR validation.

## 5. Matrix policy

Routine PR:
- one canonical runtime only.

Release / compatibility certification:
- multi-version matrix allowed when required by the release contract.

Do not run the same matrix in multiple overlapping workflows.

## 6. Scheduled workflow policy

Default cadence:
- health after deployment: event-driven, not hourly.
- SEO/GSC/AdSense/funnel reports: weekly.
- corpus/evidence audit: weekly.
- full visual/browser QA: manual or change-triggered.
- market/portfolio collectors: keep only where freshness is operationally required.

Every scheduled workflow must answer:
- what decision becomes worse if this does not run today?
- can deployment/change events replace time-based polling?
- can it run weekly?
- can it run locally or outside GitHub Actions?

## 7. Artifact policy

- Default retention <= 14 days.
- Keep 30+ days only for release, compliance, GOLD, or explicit historical evidence.
- Do not upload artifacts when the GitHub job summary is sufficient.
- Release artifacts are exempt when required by the product release contract.

## 8. Concurrency

For non-release workflows:
- use a stable concurrency group;
- prefer cancel-in-progress: true.

Release, migration, backup/restore, and data-write workflows must not be cancelled mid-transaction unless their contract explicitly allows it.

## 9. Free-tier emergency mode

When included Actions minutes reach 90%:
- stop all scheduled non-release workflows;
- keep manual dispatch available;
- keep Release Gate and critical PR checks only.

When usage reaches 100%:
- do not raise the paid budget automatically;
- keep account Actions budget at $0;
- continue work through source review/local execution/public or self-hosted paths;
- resume private GitHub-hosted workflows after monthly reset.

## 10. Repository-specific first actions

### joylab-publishing-os
- remove hourly Production Health schedule; verify after deployment instead;
- remove daily Quality Control Center schedule;
- reduce GSC / AdSense / funnel recurring reports to weekly;
- keep research evidence weekly;
- review rates collectors separately because freshness may be operational.

### joylab-vercel-site
- Article Audit is manual dispatch only under free-tier mode;
- Release Gate remains the primary CI consumer.

### leaderdesk-people-os
- Windows installer validation is manual/release-candidate only;
- signed GOLD and release workflows stay manual.

### joylab-core8-engine
- retain market/portfolio schedules only when their freshness is directly consumed;
- one-off GOLD checkpoint collectors must not remain permanently scheduled.

## 11. Promotion rule

A workflow may gain a higher recurring cadence only when:
- its output is actively consumed;
- there is no cheaper event-driven alternative;
- the expected monthly minute cost fits the 80% operating envelope;
- removing another lower-priority recurring task is considered first.

## 12. Review

Review monthly after Actions reset:
- total included minutes consumed;
- top repositories by gross usage;
- top workflows by run count and duration;
- failed/rerun minutes;
- scheduled runs that produced no meaningful change.

Target: Release Gate remains available through the entire month without paid Actions usage.
