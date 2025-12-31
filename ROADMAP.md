# Roadmap for Team Reminder Service

## Background and Why a Roadmap is Needed Now

The Team Reminder Service has grown organically from a simple internal script into a backend used by multiple teams for scheduling and sending notifications. While functional, this evolution has led to inconsistencies that complicate maintenance and collaboration:

- Mixed API styles with inconsistent error handling and response formats
- Hybrid storage implementation (in-memory + partial database support)
- No background processing for scheduled reminders
- Limited observability and testing
- Unclear ownership of modules and no standardized development practices

These issues cause parallel edit conflicts, onboarding challenges for new contributors, and reliability concerns for users. With a small contributor pool, a structured roadmap is essential to align efforts, prevent feature creep, and ensure sustainable growth without breaking existing functionality.

## Phases / Milestones

### Phase 1: Foundation Consolidation (1-2 months)
**Goals:**
- Standardize API response formats and error handling across all endpoints
- Complete migration from in-memory to relational database storage
- Establish clear code patterns for new features (e.g., Pydantic models, typed responses)

This phase addresses core inconsistencies to create a stable base for future work.

### Phase 2: Reliability and Automation (2-3 months)
**Goals:**
- Implement background worker for scheduled reminders
- Add basic observability (structured logging, request tracing, health checks)
- Expand test coverage for critical endpoints and services

This phase improves operational reliability and user trust in automated notifications.

### Phase 3: Advanced Capabilities (3-4 months)
**Goals:**
- Establish API versioning strategy for backward compatibility
- Add basic user permissions and access controls
- Refine development setup and contribution guidelines

This phase enables structured evolution while maintaining simplicity.

## Collaboration and Parallel Work Strategy

With limited contributors, phases allow parallel work on independent modules:
- **Phase 1:** API endpoint teams work concurrently on standardization; dedicated storage lead handles database migration.
- **Phase 2:** Separate teams for background jobs, observability, and testing.
- **Phase 3:** Parallel tracks for versioning (backend) and permissions (if UI added).

Sequencing required for storage (foundation) and versioning (after stability). Regular syncs and clear ownership prevent conflicts.

## Key Uncertainties / Decision Points

- Storage backend choice (PostgreSQL vs. alternatives)
- Task queue selection for background jobs (Celery vs. simpler options)
- Observability stack scope (basic logging vs. full metrics)
- API versioning approach (in-place vs. explicit versions)
- Multi-tenancy timing (now vs. later based on user growth)

## Out of Scope / Not Now

- Audit logs and advanced analytics: High maintenance, low current impact
- Complex multi-tenancy: Unclear dependencies, complicates simple design
- Frontend interface: Shifts focus from API stability
- Advanced integrations (e.g., Slack, email providers): Nice-to-have, not critical yet