# Roadmap — Team Reminder Service

> Concise, 3-phase plan to make the codebase and docs sustainable for a small contributor pool.

## Background — why a roadmap is needed

The repository has grown organically and is currently in active use. The snapshot in `README.md`, `docs/contributing.md` and `docs/issues_snapshot.md` shows recurring problems that block safe, parallel contribution:

- Mixed API styles and inconsistent error handling across endpoints.
- Partial in-memory storage alongside code that assumes a relational DB.
- No background worker for scheduled reminders and limited observability.
- No formal roadmap, ownership, or CI guardrails (contributing notes are out-of-date).

A short, prioritized roadmap is needed now to reduce friction for contributors, prevent accidental breakage, and enable parallel work while the team remains small.

---

## Summary (high level)

- Phase 1 — Stabilize & triage (2–4 weeks): clean information architecture, triage technical debt, set contribution guardrails.
- Phase 2 — Developer experience & core platform (4–8 weeks): standardize storage interfaces, add minimal background processing, CI/tests, and observability.
- Phase 3 — Capabilities & ergonomics (4–8 weeks): search/tags, lightweight permissions/versioning, improve discoverability and contributor UX.

Each phase targets low-risk, high-impact changes and intentionally defers high-cost architecture shifts until decision points are resolved.

---

## Phase 1 — Stabilize & triage ✅ (2–4 weeks)

Goals
- Reduce immediate contributor friction and risk of breaking changes.
- Create clear ownership and lightweight governance for documentation and code.

Key deliverables
- `ROADMAP.md`, `docs/architecture.md`, and `docs/ownership.md` (owners for `app/`, `api/`, `docs/`).
- Issue triage: label backlog, create 3 epics (IA, infra, platform).
- Small, high-impact fixes: unify error response format for core endpoints, add 5 end-to-end tests for `users` and `notifications`.
- CI baseline: lint, type-check, and run core tests on PRs.
- Contribution hygiene: PR template, issue template, `CODEOWNERS` (minimal).

Acceptance criteria (measurable)
- CI passes on main for all new PRs; at least 5 smoke tests added and green.
- `docs/contributing.md` updated with explicit small-PR guidelines and ownership.
- Top 10 issues triaged and assigned to an epic.

Who works on this / parallelization
- Docs/IA owner(s): reorganize `docs/` and add templates.
- Backend maintainer(s): standardize error responses and add tests.
- Automation: set up CI — these can proceed in parallel because they touch different layers.

Why first
- Low-risk wins that immediately reduce merge conflicts and onboarding time.

---

## Phase 2 — Developer experience & core platform 🔧 (4–8 weeks)

Goals
- Introduce stable extension points so contributors can add features without large rewrites.
- Replace brittle assumptions (storage, scheduling) with clear, incremental plans.

Key deliverables
- Define and implement a `Repository` adapter interface and add one non-breaking SQL adapter stub (e.g., SQLAlchemy-ready, behind feature flag).
- Background job MVP: scheduled runner (simple APScheduler or lightweight queue prototype) with end-to-end test in staging.
- Increase test coverage for core flows to ~60% for API surface; add integration test for scheduled reminders.
- Minimal observability: structured logs + single metrics counter (request failures) and health-check expanded to include storage & scheduler.
- Enforce code style + type checking in CI.

Acceptance criteria
- Repository adapter exists and is documented; in-memory remains default but SQL adapter compiles and is covered by tests.
- Scheduler runs in a staging environment and executes scheduled reminder at least once under CI-emulated conditions.
- Test coverage and CI protections reduce regressions (defined as <1 critical bug per release window).

Sequencing & parallel work
- The repository interface design is a gating decision (short design doc, 1–2 days). Once agreed, storage adapters and scheduler work can proceed in parallel.
- API contract improvements (Pydantic everywhere) should be done incrementally per endpoint to avoid large breaking PRs.

Trade-offs
- Defer full DB migration until an adapter is tested in Phase 2; prefer an adapter-first approach to avoid a blocking big-bang migration.

---

## Phase 3 — Capabilities & contributor ergonomics ⚙️ (4–8 weeks)

Goals
- Make the product more discoverable and enable safe, lightweight governance for power features.

Key deliverables
- Search & discoverability: add simple docs search (Lunr/Typesense or hosted Algolia for docs) and tag model for reminders/docs.
- Lightweight permissions: introduce contributor roles and a simple RBAC guard for sensitive endpoints (opt-in).
- API versioning policy and deprecation guidelines documented.
- Improvements to onboarding: onboarding PR checklist, exemplar issues, and a 1-page contributor playbook.

Acceptance criteria
- Docs search is available and returns relevant results for 80% of top queries.
- Tagging exists for reminders/docs and is documented in `docs/`.
- RBAC implemented behind a feature flag and covered by tests.

Why this is later
- These features require stable primitives (storage interface, CI, scheduler) to avoid rework.

---

## Collaboration & parallel-work strategy

- Layers and owners: content/IA, API/contract, storage/infra. Assign one owner per layer and one `integration owner` to resolve cross-layer decisions.
- Parallelizable work:
  - Docs reorg, PR/issue templates, and CODEOWNERS (Phase 1) — fully parallel.
  - Adapter implementation and background-worker prototype (Phase 2) — parallel once the interface is agreed.
- Sequenced work:
  - DB migration and API versioning must be gated by design docs and an adapter-proof-of-concept.
- Lightweight rules to avoid blocking:
  - PRs < 300 LOC, single-responsibility, link to an issue/epic.
  - Feature flags or opt-in branches for risky changes.

Suggested cadence
- Weekly triage for small fixes; biweekly roadmap sync for owners; milestone review at the end of each phase.

---

## Key uncertainties & decision points ⚠️

- Storage choice (keep in-memory + adapter vs immediate Postgres migration). Recommendation: adopt an adapter pattern in Phase 2 and defer full migration.
- Background processing model (APScheduler vs Celery/Redis). Recommendation: prototype with a scheduler or lightweight queue first; choose heavier queue only if SLA requires it.
- Search provider (hosted Algolia vs self-hosted Typesense/Lunr). Recommendation: start with Lunr for docs; revisit for product search if usage grows.
- API versioning approach (URI vs header vs semantic). Recommendation: document a policy in Phase 2 and use non-breaking evolution where possible.

Each of the above should have a 1–2 page decision record and be resolved before Phase 2’s major work proceeds.

---

## Out of scope / Not now 🚫

- Full rewrite or frontend framework migration — high cost; only consider after Phase 2 proves the platform shape.
- Multi-tenant architecture and enterprise RBAC — high complexity and maintenance burden; defer until clear user need.
- Advanced analytics or AI-driven search ranking — low ROI for current user base.

Rationale: focus limited team effort on lowering contributor friction and stabilizing core platform first.

---

## Quick start checklist (first 2 weeks)

1. Create `ROADMAP.md` (this file) and link in `docs/contributing.md`.
2. Triage and label top 10 issues; create three epics: `IA`, `infra`, `platform`.
3. Add CI that runs lint, types, and 5 smoke tests for core endpoints.
4. Add `CODEOWNERS` and a small PR template enforcing issue linkage and size limits.
5. Design decision record for `Repository` adapter (1–2 pages).

---

## Metrics of success (first 3 months)

- Mean time to merge for small PRs < 48 hours.
- Core API smoke tests green on every push; fewer than 2 regressions per month in core flows.
- Contributors report onboarding time reduced (survey or quick feedback) and fewer 'who owns X' questions in issues.

---

> This roadmap is intentionally conservative: it prioritizes sustaining contributors, reducing merge friction, and creating safe extension points. Treat it as a living plan — update `ROADMAP.md` at the end of each phase.
