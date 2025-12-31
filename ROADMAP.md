# Documentation Site Roadmap (next phase)

> Concise, prioritized plan to stabilize content, improve collaboration workflows, and add practical discovery features — designed for a small contributor team and incremental delivery. ✅

## Background — why a roadmap now

- The repository has active content (`docs/`, `README.md`, `contributing.md`) but the information architecture and contributor experience have grown organically and inconsistently.
- Symptoms observed in this snapshot: duplicated/unclear pages, inconsistent metadata and structure, ad-hoc PRs/edits, and no clear discovery/search capability (see `issues_snapshot.md` and `contributing.md`).
- A short, focused roadmap will reduce edit conflicts, make contributions predictable, and enable parallel work without heavy process overhead.

---

## High-level goals (what success looks like)

- Clear, documented information architecture and content ownership for the majority of pages.
- Fast, low-friction editing: templates, CI checks, and preview deployments.
- Reliable discovery: searchable, well-tagged content and measurable improvements in findability.
- Minimal ongoing maintenance overhead for a small contributor pool.

---

## Phases & milestones

### Phase 1 — Stabilize & Clean (priority: high, 3–5 weeks)
Goal: reduce chaos and make the repository reliably editable.
- Inventory content and create a canonical content map (root sections and page owners).
- Remove or consolidate obvious duplicates and add `front-matter`/metadata to pages (title, section, tags, owner).
- Update `contributing.md` with a short doc-editing workflow and add `ISSUE_TEMPLATE` / `PULL_REQUEST_TEMPLATE` for docs.
- Add a lightweight CI check: markdownlint + broken-link-checker.

Deliverables
- `docs/CONTENT_MAP.md` (or TOC) + list of 1–2 owners per top-level section
- Updated `contributing.md` and created templates
- CI job that fails PRs with broken links or lint errors

Why first: cleanup creates a stable base for parallel work and makes later features (search, tags) effective.

---

### Phase 2 — Editing experience & collaboration (priority: medium, 3–6 weeks — can overlap with Phase 1)
Goal: speed up safe contributions and reduce review friction.
- Add `CODEOWNERS` for docs sections and define minimal review rules.
- Add doc templates and small UX improvements: page template, metadata checklist, clear naming conventions.
- Implement preview/staging for PRs (GitHub Pages, Netlify preview, or similar) so contributors can see changes before merge.
- Add CI spellcheck and a smoke test for the docs build.

Deliverables
- `CODEOWNERS` entries + updated `contributing.md` review flow
- PR preview deployment and CI pipeline improvements
- Short contributor training doc: "How to edit a page" (one-pager)

Parallelism: content editors can continue Phase 1 cleanup while engineers build CI/preview features.

---

### Phase 3 — Discovery & governance (priority: medium/low, 4–8 weeks — depends on Phase 1+2)
Goal: make content findable and introduce light governance when needed.
- Add search (client-side Lunr or hosted Algolia) and tag-based filters.
- Surface metadata in UI: breadcrumbs, section landing pages, related-articles.
- Add basic analytics (page views, top searches) to guide future prioritization.
- Optional: consider role-based write-protection (only if required by policy).

Deliverables
- Search index + UI for tags/categories
- Analytics dashboard (simple spreadsheet or lightweight tool)
- Decisions recorded for any further governance needs

Why later: search and governance rely on a stable IA and consistent metadata from Phases 1–2.

---

## Collaboration & parallel-work strategy 🔧

- Roles (small team):
  - Content Editors — focus on Phase 1 cleanup, taxonomy, and owner assignments.
  - Engineers/DevOps — implement CI, PR preview, and search integration (Phase 2 & 3).
  - UX/Reviewer — create templates, check metadata consistency, and validate discoverability.

- What can run in parallel:
  - Content inventory + metadata enrichment (Phase 1) AND CI/preview pipeline work (Phase 2).
  - Tagging and search prototype (Phase 3) can be developed against a subset of cleaned pages.

- Sequencing constraints:
  - Phase 1 must be at least partially complete (core IA + metadata) before full search and analytics in Phase 3.
  - `CODEOWNERS` and PR templates should be introduced once section owners are agreed (end of Phase 1).

---

## Key uncertainties & decision points ⚠️

- Search backend: open-source client-side (Lunr) vs hosted (Algolia). Trade-offs: cost, relevance, indexing complexity.
- Hosting / preview platform: GitHub Pages vs Netlify/Vercel for PR previews and redirects.
- Permissions model: do we need write controls beyond `CODEOWNERS`? (only if contributor mix or compliance requires it).
- Scope creep risk: migrating to a new CMS or frontend framework — requires a separate, funded initiative.
- Contributor availability — timeline must remain flexible given a small team.

---

## Out of scope / Not now ❌

- Full CMS migration (e.g., moving to Confluence or an enterprise CMS) — high cost and major migration effort.
- Multi-tenancy or complex RBAC for docs — only consider if there is a clear, funded requirement.
- Paid search services unless budget is approved — prefer a free prototype first.
- Large visual redesign or frontend-framework rewrite — this roadmap focuses on content, workflow, and incremental discovery improvements.

Rationale: each item above adds significant maintenance cost or project risk that exceeds the current project constraints.

---

## Quick measurable milestones / success metrics

- Phase 1 complete: content map + 80% pages have metadata, broken links reduced to 0–2.
- Phase 2 complete: PR preview working, `CODEOWNERS` in place, average docs PR review time ≤ 48 hours.
- Phase 3 complete: search returns relevant results for top 20 queries; tags applied to ≥ 60% of pages.

---

## Next recommended immediate steps (0–2 weeks) ▶️

1. Run a 1–2 day content inventory: produce `docs/CONTENT_MAP.md` and tag obvious duplicates.
2. Add/standardize front-matter metadata on high-traffic pages (top 10).
3. Create `PULL_REQUEST_TEMPLATE` + simple CI markdownlint and broken-link checks.
4. Assign owners for top-level sections and add `CODEOWNERS` draft.

---

## Living document

This roadmap is intended to evolve. Revisit priorities after Phase 1 and update timelines and scope with real contributor capacity and usage metrics.

---

*Prepared for the repository snapshot on file — small, iterative, low-risk plan to make the docs sustainable and easier to contribute to.*
