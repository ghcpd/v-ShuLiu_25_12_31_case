# Team Reminder Service Roadmap

**Last Updated:** December 2025  
**Status:** Living Document – This roadmap evolves based on feedback and learnings.

---

## Background: Why a Roadmap is Needed Now

The Team Reminder Service has grown organically over time as contributors added features and endpoints independently. While the service is functional and actively used, this growth has introduced friction points:

- **Inconsistent patterns**: Error responses, models, and logging vary across endpoints. Some endpoints follow structured error models; others return raw dicts.
- **Unclear boundaries**: Business logic is split between route handlers, `services.py`, and repositories, with partial duplication.
- **Architectural ambiguity**: The codebase mixes in-memory storage and database-oriented code without committing to a single storage approach.
- **Missing infrastructure**: Reminders are only sent synchronously; there's no background scheduler, no observability, and no health check that validates actual dependencies.
- **Collaboration friction**: Without a shared plan, contributors may duplicate effort, introduce incompatible patterns, or block each other on core refactors.

**A roadmap provides clarity on:**
- Which layers contributors can safely work on in parallel
- What patterns to follow for consistency
- Where critical decisions must be made before proceeding
- What is intentionally deferred to avoid overload

This enables a small team to scale contributions without chaos.

---

## Three-Phase Roadmap

### Phase 1: Foundation & Consistency (Weeks 1–4)
**Goal:** Establish clear, consistent patterns that enable safe parallel development.

#### Key Deliverables

1. **Standardize data access & storage**
   - Commit to a single storage backend (recommended: SQLAlchemy + SQLite for dev, PostgreSQL for production)
   - Refactor repositories to use a consistent database abstraction (ORM or query builder)
   - Migrate in-memory stores to real persistence
   - Provide a migration/seeding script for existing deployments

2. **Unify error handling & API responses**
   - All endpoints must use `ErrorResponse` model or raise `HTTPException` with structured detail
   - Document standard HTTP status codes (400 for validation, 404 for not found, 500 for server errors)
   - Add consistent error logging at the API layer

3. **Establish logging standards**
   - Configure structured logging (e.g., JSON logs with request ID, timestamp, level)
   - Log all API requests/responses and errors at appropriate levels (INFO for success, ERROR for failures)
   - Add context tracking for debugging (e.g., request ID propagation)

4. **Clarify ownership & module boundaries**
   - **Repositories**: Data access only. Abstract storage backend.
   - **Services**: Business logic (scheduling, validation, notification prep). No direct HTTP knowledge.
   - **API routes**: HTTP interface only. Delegate to services; minimal logic.
   - Document this in `ARCHITECTURE.md` with examples

5. **Improve health check endpoint**
   - Check database connectivity and health
   - Check any external dependencies (task queue, message broker)
   - Return 503 if critical dependencies are down

#### Parallel Work Tracks

- **Track A (Data)**: Finalize storage choice, refactor repositories, handle migration
- **Track B (API)**: Standardize response models, error handling, route ownership
- **Track C (Logging)**: Implement structured logging across the codebase
- All tracks can proceed in parallel with code review checkpoints to ensure consistency

#### Success Criteria

- All API endpoints follow the same error response pattern
- All endpoints have response models defined
- Logging appears consistently across all layers
- A single database backend is in use (no in-memory code for production)
- No TODO comments about "unclear ownership" remain

---

### Phase 2: Reliability & Observability (Weeks 5–8)
**Goal:** Make the service production-ready with reliable reminder delivery and operational visibility.

#### Key Deliverables

1. **Implement background task execution**
   - Integrate a task queue or scheduler for scheduled reminders (recommendation: APScheduler for simplicity, Celery if scaling beyond ~100 concurrent jobs)
   - Create a background worker that picks up scheduled reminders and triggers sends at the correct time
   - Define SLAs: e.g., "reminders are sent within 5 minutes of scheduled time"
   - Add failure handling: retry logic, dead-letter queue, alerting on consecutive failures

2. **Enhance observability**
   - Add basic metrics: number of reminders created, sent, failed (use a simple metrics library like `prometheus_client`)
   - Expose metrics on `/metrics` endpoint for scraping or polling
   - Add tracing context: Request ID propagated through logs and metrics for debugging

3. **Expand test coverage**
   - Unit tests for repositories (with mocked DB) and services
   - Integration tests for API endpoints (using a test database)
   - End-to-end test for the reminder send flow (create reminder → trigger send → verify execution)
   - Aim for >70% code coverage on business logic

4. **API stability & documentation**
   - Generate OpenAPI documentation from FastAPI (automatic)
   - Document known limitations and assumptions in API docs
   - Add endpoint examples and response samples to README

5. **Deployment & configuration**
   - Provide a `.env.example` file showing required configuration
   - Document how to run the app with a real database (e.g., Docker Compose with PostgreSQL)
   - Create a deployment checklist (dependency checks, migrations, etc.)

#### Parallel Work Tracks

- **Track A (Background Jobs)**: Design and implement the task queue integration
- **Track B (Metrics & Logging)**: Add metrics, refine logging, set up scraping
- **Track C (Tests)**: Build comprehensive test suite
- All tracks can proceed after Phase 1 completes, with some overlap possible if repository design is clear

#### Success Criteria

- Reminders can be scheduled and automatically sent at specified times
- At least one failed send has been handled with a retry mechanism
- `/metrics` endpoint exposes meaningful metrics
- All core business logic has unit tests (>70% coverage)
- README documents how to set up and deploy with a real database

---

### Phase 3: Scalability & Extensibility (Weeks 9+)
**Goal:** Support growth in users, contributors, and feature requests without major rework.

#### Key Deliverables

1. **API versioning strategy**
   - Decide: support multiple versions (e.g., `/v1/`, `/v2/`) or use deprecation headers?
   - Document the deprecation timeline for breaking changes
   - Plan for at least one major API evolution (e.g., adding pagination or filtering)

2. **Multi-channel support**
   - Extend the `Channel` enum to support Slack and SMS (in addition to email)
   - Implement handlers for each channel (may be stubs for Slack/SMS initially)
   - Allow users to configure multiple channels per reminder

3. **Access control & permissions (optional)**
   - Add basic role support: "admin", "user"
   - Ensure users can only view/edit their own reminders
   - Admins can view system health and all reminders
   - This prepares for future multi-tenant support if needed

4. **Contributors' guide & decision log**
   - Formalize the contributing.md with clear examples
   - Create an ADR (Architecture Decision Record) document listing key decisions (storage choice, task queue choice, etc.)
   - Add templates for proposing new features (link to dependencies on existing work)

#### Parallel Work Tracks

- **Track A (Versioning)**: Plan and document API versioning strategy
- **Track B (Channels)**: Build multi-channel infrastructure
- **Track C (Access Control)**: Add permission checks and role support
- These can proceed largely independently if Phase 1 & 2 boundaries are solid

#### Success Criteria

- API versioning strategy is documented and one breaking change has been handled per the strategy
- At least one additional channel (Slack or SMS) is partially or fully implemented
- Users cannot access other users' reminders without explicit permission
- Contributors' guide and ADR document are in place

---

## Collaboration & Parallel Work Strategy

### How to Avoid Blocking Each Other

1. **Clear layer ownership**: Once Phase 1 is done, owners of repositories, services, and API layers can work in parallel on different features.

2. **Minimal merge conflicts**: 
   - If Track A (data) finalizes storage first, Track B (API) can use consistent interfaces immediately
   - New endpoints can be added to the API layer without touching repositories, as long as the interface is stable

3. **Feature branches & reviews**:
   - All refactors require a code review to ensure consistency
   - Use feature branches to isolate large changes
   - Coordinate via GitHub issues or team discussions before starting major work

4. **Cross-phase flexibility**:
   - Phase 2 work (background jobs) may be deferred if Phase 1 takes longer
   - Phase 3 work (versioning) can start as soon as Phase 1 boundaries are clear, without waiting for Phase 2

---

## Key Uncertainties & Decision Points

### 1. Storage Backend
**What:** Should we use SQLAlchemy + PostgreSQL, SQLite, or keep in-memory for now?  
**Why it matters:** This affects data persistence, scaling, and query capabilities.  
**Recommendation:** Commit to SQLAlchemy + SQLite (dev) / PostgreSQL (prod) in Phase 1. Provides durability without over-engineering.  
**Decision deadline:** Week 1 of Phase 1.

### 2. Task Queue / Scheduler
**What:** APScheduler (in-process, simpler) vs. Celery (external, more robust) vs. simple cron?  
**Why it matters:** Affects reliability, complexity, and operational overhead.  
**Recommendation:** Start with APScheduler in Phase 2; migrate to Celery only if the team scales significantly.  
**Decision deadline:** Week 5 (start of Phase 2).

### 3. Observability Stack
**What:** Structured logging + Prometheus metrics vs. full observability platform (Datadog, New Relic)?  
**Why it matters:** Cost, operational complexity, and visibility into failures.  
**Recommendation:** Phase 2 should use structured logging + `prometheus_client`. Defer commercial platforms to Phase 3 or later.  
**Decision deadline:** Week 5 (start of Phase 2).

### 4. Multi-Tenancy
**What:** Should the service support multiple teams/organizations, or remain single-tenant?  
**Why it matters:** Affects schema design, access control, and deployment model.  
**Recommendation:** Assume single-tenant for now. Design Phase 1 data models so that multi-tenancy can be added later (e.g., add `tenant_id` column without enforcing it). Revisit if business needs change.  
**Decision deadline:** By end of Phase 1, for schema design.

### 5. API Versioning Strategy
**What:** Do we introduce `/v1/` path-based versioning now, or handle breaking changes via headers/deprecation?  
**Why it matters:** Affects client integration and backward-compatibility burden.  
**Recommendation:** Defer to Phase 3. Use deprecation headers for now. Introduce versioning only if breaking changes are imminent.  
**Decision deadline:** Week 9 (start of Phase 3).

---

## Out of Scope / "Not Now"

The following capabilities are **intentionally deferred** to avoid overloading the team and maintain focus:

### 1. Web UI / Dashboard
**Why not now:** Unclear ROI for internal team use; CLI and API are sufficient.  
**When to revisit:** When multiple teams request UI features or non-technical users need to manage reminders.

### 2. Full Audit Logging
**Why not now:** Requires significant schema and infrastructure work; structured logging provides 80% of the debugging value.  
**When to revisit:** If compliance requirements (SOC 2, etc.) mandate it.

### 3. Advanced Authentication (SAML, SSO)
**Why not now:** Team is small and internal; API keys or basic auth are sufficient.  
**When to revisit:** When integrating with enterprise identity systems or opening to external partners.

### 4. Real-Time Notifications via WebSocket
**Why not now:** Adds significant complexity; email/scheduled delivery is sufficient for reminders.  
**When to revisit:** If use case evolves toward instant alerts (currently it does not).

### 5. Distributed Tracing (OpenTelemetry, Jaeger, etc.)
**Why not now:** Over-engineering for a single service; structured logging covers most troubleshooting needs.  
**When to revisit:** If the service becomes part of a larger distributed system.

### 6. Role-Based Access Control (Phase 3 optional)
**Why not now:** Single-tenant assumption; can defer until multi-team support is needed.  
**When to revisit:** In Phase 3 if business direction changes.

### 7. Advanced Scheduling Features
**Why not now:** Cron-like scheduling (once, daily, weekly) is sufficient MVP; rrule, timezone handling, etc. are nice-to-haves.  
**When to revisit:** After core background job infrastructure is stable and team requests more complex scheduling.

---

## Timeline & Milestones

| Phase | Duration | Key Milestone | Owner(s) |
|-------|----------|---------------|----------|
| **Phase 1** | Weeks 1–4 | All endpoints follow consistent patterns; single storage backend in place | TBD |
| **Phase 2** | Weeks 5–8 | Background job execution works; 70%+ test coverage; observability in place | TBD |
| **Phase 3** | Weeks 9+ | API versioning strategy documented; multi-channel support started | TBD |

---

## How to Use This Roadmap

1. **At the start of each phase**, review the deliverables with the team and assign owners to each track.
2. **Weekly syncs**: Discuss progress on each track, identify blockers, and adjust timeline if needed.
3. **End of each phase**: Review success criteria. If not all met, carry forward to the next phase (don't let perfect be the enemy of good).
4. **Feedback loop**: Update this roadmap based on learnings, changing priorities, or unforeseen blockers.

---

## Related Documents

- [Contributing Guidelines](docs/contributing.md) – Updated with ownership clarifications and examples
- [Architecture Decision Records](docs/ADR.md) – To be created in Phase 1 with key decisions
- [README](README.md) – Updated with deployment and configuration instructions

---

**Questions or feedback?** Open an issue or start a discussion. This roadmap is a team artifact, not a decree.
