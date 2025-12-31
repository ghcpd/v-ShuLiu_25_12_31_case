# Contributing to Team Reminder Service

Thank you for your interest in contributing!

This service started as a small internal tool and has been growing organically as more people add features. We are now trying to move toward a more structured, maintainable project.

## Development Setup

- Python 3.10+
- Install dependencies with `pip install -r requirements.txt` (not yet finalized).
- Run the app locally with:
  - `uvicorn app.main:app --reload`

Note: Some modules still assume in-memory storage, others assume a relational database. We have **not** standardized configuration or deployment yet.

## Code Style & Structure

- We prefer FastAPI-style type hints and Pydantic models, but older endpoints may not follow this yet.
- New business logic should go into `services.py` or a new module under `services/`, not directly into route handlers.
- When touching data access, please leave TODO comments if you notice inconsistencies between in-memory and database-based code paths.

## Collaboration Notes

- Please open an issue before proposing large refactors.
- When you see unclear ownership or missing docs, feel free to open a discussion issue describing the context.
- There is **no official roadmap** yet; part of the ongoing work is to make future development more coordinated.
