# arm: plain-memo-short (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R501 | attempt: 1 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R501-plain-memo-short-rewrite-1.txt (sha256 82ea7a1043a60d38)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: ac85aa2c801bc4a9d | transcript sha256: 5c1b4693f2f40787dedb2f055b772029bec7626c78e49df48654518a009d9189
# minutes: 0.2 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/2341/3185/14311 | list-price USD: 0.09

## Recommendation
Pick row-level security (RLS), but as an added layer and not a replacement for what you have. Keep the ORM auto-scoping and the lint rule. RLS becomes the backstop that holds even when those are wrong, bypassed, or not in the loop. This is defense in depth, not a swap. On your three worries (connection pooling, debugging, performance), each has a standard mitigation, and the performance one should be measured and not taken on faith. Rollout is table-by-table, starting with `invoices`.

## Why
The near-miss already shows where the app-layer approach fails. It was an internal report that nearly crossed tenants, not a bug in ORM-generated code. A query wrapper and lint rule only protect the code path that runs through your CI pipeline. They don't protect ad hoc scripts, BI tools (Metabase, Looker or similar), a read replica someone connects to with psql, migrations, admin tooling, or the next internal service that talks to this database without importing your lint config. That is exactly the gap the incident found.

A lint rule pattern-matches against source text. It can be defeated by dynamic SQL, string-built queries, views, or just not running in that repo. RLS moves the check into the data itself, so it holds regardless of what is issuing the query. After an incident caused by an unanticipated access path, that invariance is the property you actually want.

The ORM auto-scoping and lint rule are cheap, give fast feedback in code review, and keep common-case queries efficient and correct, so they stay.

On performance, a policy like `customer_id = current_setting('app.tenant_id', true)::uuid` is just another indexed predicate. You already need `customer_id` indexed today, since the ORM filters on it on every query. Postgres pushes the policy qual into the plan alongside your other WHERE clauses, so it composes with existing indexes rather than adding a separate filter pass.

Also, 2000 tenants in one database is squarely RLS's comfort zone. It is not a scale where you would need schema-per-tenant or database-per-tenant instead.

## What to do
- Enable RLS table-by-table, starting with `invoices`, since that is what almost leaked.
- Connection pooling: this is the one real landmine, but it is a solved problem. Always scope the tenant setting to the transaction with `SET LOCAL` (or `set_config(name, value, true)`, where `true` means local), issued inside the same transaction as the query. That is the standard pattern for RLS-based multi-tenancy and it composes fine with transaction-mode pooling.
- Make the policy fail closed. `current_setting('app.tenant_id', true)` returns NULL if unset rather than erroring, and `customer_id = NULL` is never true, so a request that forgets to set the tenant context returns zero rows, not all rows. Test that explicitly before rollout. It is the difference between a bug breaking a customer's report and a bug leaking data.
- Debugging: run `ALTER TABLE ... FORCE ROW LEVEL SECURITY` so the policy applies even to the owner, and make sure your app's connection role doesn't have `BYPASSRLS`. Debug using the same restricted role production uses, not a privileged one.
- Performance: pull your top 10-20 heaviest or slowest queries, run them against prod-scale data with RLS enabled in a staging environment, and compare plans before flipping it on broadly. Load-test the heavy queries before each table goes live. This is worth measuring, not guessing at.
- Keep one narrowly-scoped, audited "admin" role for legitimate cross-tenant operations (support tooling, billing reconciliation), rather than leaving every query capable of seeing everything by default.
- Leave the lint rule running the whole time.

## Risks of this plan
- Connection pooling is the one real landmine. The failure mode is using session-level `SET` with a pooler in transaction mode (PgBouncer), where a connection can get reused across different logical requests without resetting state.
- Debugging is harder mainly if you debug as a superuser or table owner, since RLS is invisible to those roles by default. You can "fix" something locally that doesn't reproduce because you unknowingly bypassed the policy.
- Performance has non-obvious risks. A policy that calls a non-`STABLE` function gets re-evaluated per row instead of once. Joins across multiple RLS-protected tables each add a predicate, which can matter on your heaviest queries. If any table is partitioned, verify RLS doesn't interfere with partition pruning.
- If you are not on real Postgres, such as a compatible-but-limited managed service, verify that its RLS support and planner behavior match vanilla Postgres before betting on it. Some don't push policy quals as well.

## Strongest counter-position
The source's strongest limit on its own answer is performance. If you profile your actual heaviest queries at real data volume (watch for skewed tenants with much larger row counts) and find a regression that indexing or partitioning genuinely can't fix, the source would scope RLS to the higher-risk tables only, rather than blanket-applying it, and treat the rest as a longer-term project.

It also names a second limit. If the near-miss query actually did run through ORM-covered application code (raw SQL sitting in your repo, not an out-of-band report or script), the gap is narrower than it assumes, and tightening CI enforcement buys you more than it would otherwise credit. It would still lean RLS given 2000 tenants and invoice data, but the urgency shifts.

It adds that if you were looking at tens of thousands of tenants with hard contractual isolation requirements, that would be a different conversation, though you are not there. A compliance review (SOC 2, enterprise security questionnaires) would push further toward RLS, not away, because "is tenant isolation enforced at the database layer or only in application code" is a standard question, and app-only isolation is a known red flag in vendor reviews.

## Confidence
- High: the near-miss shows the app-layer gap, and lint and wrapper protect only code paths through CI. RLS holds regardless of what issues the query. The pooling fix is `SET LOCAL` or `set_config(..., true)` inside the same transaction. An unset tenant setting fails closed. `FORCE ROW LEVEL SECURITY` and no `BYPASSRLS` address owner and superuser bypass. The policy composes with existing indexes. A non-`STABLE` function is re-evaluated per row. Multi-table joins each add a predicate. 2000 tenants is within RLS's comfort zone. The compliance review point pushes toward RLS.
- Medium: none stated.
- Low: none stated.

Unknowns the source names:
- Whether your heaviest queries regress at real data volume, including with skewed tenants, in a way indexing or partitioning can't fix.
- Whether you are on real Postgres, or a managed service whose RLS support and planner behavior differ.
- Whether the near-miss query ran through ORM-covered application code.
- Whether any table is partitioned and whether RLS interferes with partition pruning.
