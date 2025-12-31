# Team Reminder Service

A small Python backend service that lets teams create users, schedule reminder jobs (e.g., daily standups, deadlines), and send notifications through different channels.

This project is currently used by a small internal team. It started as a simple script and gradually evolved as multiple contributors added new endpoints, data models, and experimental features. As a result, the codebase is functional but shows signs of **organic growth**:

- Mixed API styles: some routes use Pydantic models and typed responses, others return raw dicts.
- Inconsistent error handling and HTTP status codes between endpoints.
- Business logic is split between route handlers and `services.py`, with some duplication.
- Part of the data access logic still uses an in-memory store, while other parts assume a relational database.
- Feature ideas are scattered across comments, TODOs, and issues (background jobs, audit logs, multi-tenant support, better observability).

The goal of this repository (for your evaluation setting) is to provide a realistic, slightly messy backend codebase that requires **structured planning and milestones** to continue evolving in a sustainable way.

## Current High-Level Features

- Create and list users.
- Create and list reminder definitions.
- Trigger sending of simple notifications (synchronous, in-process).
- Very basic health check endpoint.

## Known Pain Points (from issues and docs)

- Unclear ownership of some modules (who maintains `services.py` vs `repositories.py`).
- No consistent error and logging strategy.
- No clear plan for moving from in-memory storage to a real database.
- No background worker for scheduled reminders, everything is synchronous.
- Limited tests; some endpoints are untested.

## For Roadmap Evaluation

When evaluating models, you can provide this repository along with `prompt.txt` or `prompt_chinese.txt` and ask the model to propose a roadmap and milestone structure that addresses the above pain points while accounting for limited contributors and time.
