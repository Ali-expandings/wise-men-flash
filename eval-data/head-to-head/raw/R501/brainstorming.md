# arm: brainstorming (obra/superpowers 5bf4e7801107, with visual-companion.md and spec-document-reviewer-prompt.md) | question: R501 | orchestrator: general-purpose/sonnet | run: 2026-09-24 (round 5, PREREG-5 rules)
# minutes: 4.8 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 6/26111/211010/60656 | list-price USD: 0.68

This is a spike: the question asks for a recommendation between two options, not an implementation ("which would you pick" — the output is an answer, not code to keep). No approval gate beyond the initial probe applies. Running that gate now, since no one's available to nod it through:

**Probe I'd present:** *"I'll compare RLS and app-level enforcement against the failure mode that actually happened — an internal report nearly crossing tenant lines — and against your three named risks (pooling, debugging, performance), then give you a pick and the conditions that would flip it. Sound good?"* — **Assumed answer: yes**, since that's exactly what was asked.

---

## Recommendation

Turn on row-level security. Keep the query wrapper and lint rules too — they're not really competing with RLS, they're a different layer, and dropping either one leaves a gap the other doesn't cover.

**If forced to pick exactly one: RLS.** Here's why it's not close.

The near-miss was an *internal report* almost crossing tenant lines. Reports and BI tools are precisely the code path a query wrapper and lint rule don't reach — they typically query the database directly or through a separate tool (Metabase, Looker, a data warehouse sync, an analyst's notebook), not through your application's ORM layer. A lint rule scans source code in your repo; it has no jurisdiction over a SQL editor. So the app-level fix, however well built, would not have prevented the incident that prompted this whole question. RLS would have, because it's enforced by Postgres itself regardless of what issued the query — ORM, raw SQL, a report, a future migration script, an engineer debugging in psql.

The wrapper's real value is different: it's a fast, loud, dev-time signal ("this query has no tenant filter — fix it before it ships"), caught in code review and CI. RLS's value is a silent, unbypassable, prod-time guarantee. You want the loud check where mistakes are cheap to fix (your codebase) and the silent guarantee where mistakes are catastrophic (production data). That's not redundancy, that's defense in depth — the same reason you'd keep input validation in application code *and* a `NOT NULL`/foreign-key constraint in the database, rather than treating them as alternatives.

## Your three worries, and why none of them changes the pick

**Connection pooling.** This is the one worry that's genuinely well-founded, not just a general RLS concern — but it has a known fix. At 2,000 tenants you're almost certainly running PgBouncer (or similar) in transaction-pooling mode, and a bare `SET app.tenant_id = ...` at the session level *will* leak across requests when connections are reused mid-session. The fix is to never use bare `SET`: wrap every unit of work in an explicit transaction and set the GUC with `SET LOCAL` as the first statement inside it. `SET LOCAL` is transaction-scoped and clears automatically at commit/rollback, which is exactly what transaction-mode pooling expects. This becomes one thing to get right — the transaction-acquisition path in your connection/middleware layer — instead of "every query, everywhere," which is a smaller and far more auditable surface than what you have today. Do this once, centrally, and it's done; write a test that asserts it (open a transaction, don't set the GUC, confirm zero rows — not an error).

**Harder debugging.** Real, but it's a one-time tooling cost, not a recurring one. RLS fails silently — missing GUC returns zero rows, not an error — so give engineers a documented "debug as tenant X" snippet (`SET ROLE app_user; SET LOCAL app.tenant_id = '<id>';`) and make sure your app's structured logs include the current tenant GUC next to slow-query logs, so "why is this empty" has an immediate answer. This is exactly where keeping the wrapper's loud dev-time error pays for itself — most missing-filter mistakes get caught there, before they ever reach a silent RLS result in prod.

**Performance surprises.** For a simple policy — `customer_id = current_setting('app.tenant_id')::uuid` — Postgres pushes the predicate down and uses the same index your app-level filter already relies on; the overhead is close to zero, because it's the same `WHERE` clause, just added by the database instead of the ORM. The actual risk shows up if any policy needs more than equality — a join to a memberships/org-hierarchy table, for instance — which can defeat pushdown and force a worse plan. Don't guess: before flipping this on in production, run `EXPLAIN ANALYZE` on your top 10–20 heaviest queries in a staging environment with production-scale data, with RLS on, and check that the policy predicate is using the `customer_id` index rather than filtering after a sequential scan. Fix policy or index mismatches you find there. If one or two specific analytical queries genuinely can't be made cheap under RLS, exempt just those (a read replica or a pre-filtered reporting table with its own tightly scoped access) rather than abandoning RLS on the other 95% of your schema over the worst case.

One more factor worth naming since it wasn't in your list: if "business customers" ever means SOC 2, ISO 27001, or a security questionnaire in your future, auditors treat a database-enforced control as real evidence and a code-review convention as weak evidence. That's a second reason RLS is the sturdier fix, independent of the pooling/debugging/performance questions.

## Rollout, concretely

1. Enable RLS with `FORCE ROW LEVEL SECURITY` on every tenant-scoped table; policy is a simple equality check against a session GUC.
2. Move all runtime app traffic to a role without `BYPASSRLS` and without table ownership. Reserve superuser/owner access for migrations only, and treat that as a deliberate, audited, human-gated path — not the app's default identity.
3. Set the GUC via `SET LOCAL` inside your existing transaction-per-request pattern; this is the one centralized change, not a per-query one.
4. Route the report/BI access that caused the near-miss through a role that also has RLS enforced (or, better, through an API rather than direct database access at all).
5. Benchmark the heaviest queries with `EXPLAIN ANALYZE` before enabling in production; fix any policy/index mismatches surfaced.
6. Keep the wrapper and lint rule exactly as planned — they're your CI-time signal now, not your only line of defense.
7. Add a CI test that runs queries as the actual limited-privilege app role and asserts cross-tenant access returns zero rows. This is the test that would have caught the near-miss, and it should exist regardless of which mechanism you pick.

## What would change my answer

- If, after policy and index tuning, `EXPLAIN ANALYZE` shows real regression on specific heavy analytical queries because tenant access is hierarchical rather than simple equality — keep RLS everywhere it's cheap (nearly everything), and give just those specific queries a read replica or pre-filtered reporting layer instead of abandoning RLS wholesale.
- If your connection and transaction handling is scattered across enough disparate services and job frameworks that "set the GUC before the first query" genuinely can't be centralized soon — sequence it: ship RLS first wherever you can guarantee that (almost certainly the main app), track the remaining paths explicitly with an owner and a deadline, rather than treating the wrapper alone as the finished fix.
- If you're about to physically split tenants into per-schema or per-database isolation in the near term, RLS is still worth doing now given how close you came to a real leak — just keep the implementation lean, since it may be a stopgap rather than a permanent structure.
