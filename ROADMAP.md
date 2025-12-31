# Documentation Roadmap

> Concise, pragmatic roadmap to improve collaboration, quality, and discoverability of the documentation site.
> This is a living plan — timeboxed and reviewable at the end of each milestone.

---

## Background — Why a roadmap now

- The docs site is actively used but has grown organically and inconsistently.
- Symptoms include: mixed information architecture, duplicated or outdated content, unclear owners, and friction in parallel edits.
- A focused roadmap reduces editor friction, improves quality quickly, and enables safe, incremental platform improvements without a large team.

---

## Phases & Milestones

### Phase A — Stabilize content & information architecture (4–6 weeks) ✅
**Goals**
- Inventory all documentation; identify duplicates, outdated pages, and missing metadata.
- Define a minimal canonical structure (top-level sections) and taxonomy.
- Create page templates and a brief Style & IA guide.

**Deliverables**
- Content inventory (issue or spreadsheet).
- `docs/` structure proposal and templates.
- `CONTRIBUTING.md` updates with quick guidelines for editors.

**Success criteria**
- Majority of pages assigned to a section or flagged for action; templates adopted by contributors.

---

### Phase B — Improve editing experience & collaboration workflow (3–6 weeks) 🔁
**Goals**
- Lower friction for contributors by adding PR/issue templates and lightweight checks.
- Define ownership (section stewards) and review routing.
- Automate simple validations (link checks, markdown lint, front-matter checks).

**Deliverables**
- `pull_request_template.md`, `ISSUE_TEMPLATE.md`, updates to `CONTRIBUTING.md`.
- GitHub Actions (or equivalent) for link-check and markdown lint.
- `OWNERS.md` or `CODEOWNERS` mapping.

**Success criteria**
- PRs run checks; editorial linter prevents common errors; section stewards assigned.

---

### Phase C — Introduce search, tags, and analytics (4–8 weeks) ✨
**Goals**
- Improve discoverability with search and tagging.
- Add basic usage analytics to prioritize further work.
- Pilot features on a single section before adoption across all docs.

**Deliverables**
- Search integration (Algolia/Meilisearch/static index).
- Tagging UI and backfill plan for high-value pages.
- Simple analytics dashboards to guide priorities.

**Success criteria**
- Search provides relevant results for common queries; tags used on major pages.

---

## Collaboration & Parallel Work Strategy

- Roles:
  - Content stewards: triage content, own sections.
  - Engineers: implement CI and infra (link check, search).
  - Contributors: write and update content using templates.

- Parallelism:
  - Phase A and B can be executed in parallel by different people (content triage vs CI/tooling).
  - Tagging and search pilots should wait until templates and metadata conventions are stable.

- Governance:
  - Timebox and evaluate at the end of each phase (6–8 week cadence).
  - Keep `ROADMAP.md` and `CONTRIBUTING.md` up-to-date after each milestone.

---

## Key uncertainties & decision points

- Search: hosted vs self-hosted vs static indexing — affects cost and maintenance.
- Backend needs: current static approach may suffice; dynamic editing or attachments might require re-evaluation.
- Permissions & SSO: only add if clear need and funding.
- Team availability & hosting budget will affect pace and scope.

---

## Out of scope / Not now

- Full site/frontend rewrite — high cost and risk.
- Enterprise SSO and complex RBAC.
- Multi-tenancy or broad platform-level refactor.
- Low-impact features (e.g., gamification) that don't reduce editorial friction.

---

## Quick start checklist (first 4 weeks)

1. Create a content inventory issue and assign owners to top-level sections. 🔍  
2. Add minimal page templates and a short IA guide to `CONTRIBUTING.md`. 📝  
3. Add simple GitHub Actions: markdown-lint and a link-check step. ⚙️  
4. Run a small pilot search/tag feature on one section after metadata stabilizes. 🔬

---

## Notes

- This is a pragmatic, resource-aware plan focused on enabling contributors to work in parallel and safely.
- Re-evaluate after each phase and update this `ROADMAP.md` to reflect learnings and constraints.

---
