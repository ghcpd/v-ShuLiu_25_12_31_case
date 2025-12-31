# Issues Snapshot

## Issue 1: Inconsistent Error Handling Across Endpoints

Some endpoints return structured error responses with `detail` and specific HTTP status codes, while others just raise generic exceptions or return `500` with minimal information. This makes it hard for clients to handle errors consistently.

Questions/concerns:
- Should we introduce a shared error handling layer or exception model?
- How do we migrate existing endpoints without breaking current clients?

---

## Issue 2: Mixed Storage Approaches (In-Memory vs Database)

The `repositories` layer is partially implemented. Some operations are still using a simple in-memory dictionary, while others expect a relational database connection.

Questions/concerns:
- Do we commit to a specific database (e.g., Postgres) for the next phase?
- How do we handle migration of existing data, if any?

---

## Issue 3: No Background Worker for Scheduled Reminders

Right now, reminders are only sent when triggered manually via an API call. There is no scheduler or background worker to automatically send notifications at the right time.

Questions/concerns:
- Should we introduce a task queue (e.g., Celery, RQ) or a simpler cron-based approach first?
- How do we define SLAs and failure handling for background jobs?

---

## Issue 4: Limited Observability (Logging, Metrics, Traces)

We have minimal logging and no standardized way to trace requests across services. This is becoming problematic as more teams rely on reminders being sent reliably.

Questions/concerns:
- What is the minimum observability stack we should aim for in the next phase?
- How do we roll this out without overcomplicating the deployment?

---

## Issue 5: Unclear API Versioning Strategy

As new fields and behavior are added to existing endpoints, it's not clear whether we should introduce versioned APIs or evolve the existing ones in-place.

Questions/concerns:
- Do we need explicit API versioning now, or can we defer it?
- How do we communicate breaking changes to consumers?
