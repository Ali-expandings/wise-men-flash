# arm: plain-memo-short (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R501 | attempt: 2 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R501-plain-memo-short-rewrite-2.txt (sha256 484d6ea7abbf3a53)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: abada446065ec4b75 | transcript sha256: 8a5620a10df9d3f53d24b2329722cb2fe8dfb4d1fedaa5509b4e73ac121c52fe
# minutes: 0.5 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/4878/3185/17124 | list-price USD: 0.14

## Recommendation
Pick RLS, but as an added layer, not a replacement for what you have. Keep the ORM auto-scoping and the lint rule. RLS becomes the backstop that is true even when those are wrong, bypassed, or simply not in the loop. This is defense in depth, not a swap. Enable it table by table, starting with `invoices`, and leave the lint rule running the whole time.

## Why
The near-miss already tells you where the app-layer approach fails. It was an internal report that nearly crossed tenants, not a bug in ORM-generated code. A query wrapper and lint rule only protect the code path that runs through your CI pipeline. They don't protect ad hoc scripts, BI tools (Metabase/Looker/whatever), a read replica someone connects to with psql, migrations, admin tooling, or the next internal service that talks to this database without importing your lint config. That is exactly the gap the incident found. A lint rule is pattern-matching against source text. It can be defeated by dynamic SQL, string-built queries, views, or just not running in that repo. RLS moves the check into the data itself, so it holds regardless of what is issuing the query. After an incident caused by an unanticipated access path, that invariance is the property you actually want.

The ORM auto-scoping and lint rule are cheap, give fast feedback in code review, and keep common-case queries efficient and correct.

A policy like `customer_id = current_setting('app.tenant_id', true)::uuid` is just another indexed predicate. You already need `customer_id` indexed today, since the ORM filters on it on every query. Postgres pushes the policy qual into the plan alongside your other WHERE clauses, so it composes with existing indexes rather than adding a separate filter pass.

2000 tenants in one database is squarely RLS's comfort zone, not a scale where you'd need schema-per-tenant or database-per-tenant. A compliance review (SOC 2, enterprise security questionnaires) would push further toward RLS, not away. "Is tenant isolation enforced at the database layer or only in application code" is a standard question, and app-only isolation is a known red flag in vendor reviews.

## What to do
- Connection pooling is a solved problem, not a reason to avoid RLS. Always scope the tenant setting to the transaction with `SET LOCAL` (or `set_config(name, value, true)`, where `true` means local), issued inside the same transaction as the query. That is the standard pattern for RLS-based multi-tenancy, and it composes fine with transaction-mode pooling.
- Make the policy fail closed. `current_setting('app.tenant_id', true)` returns NULL if unset rather than erroring, and `customer_id = NULL` is never true. A request that forgets to set the tenant context therefore returns zero rows, not all rows. Test that explicitly before rollout. It is the difference between "worst case, a bug breaks a customer's report" and "worst case, a bug leaks data," which is the whole point.
- For debugging, run `ALTER TABLE ... FORCE ROW LEVEL SECURITY` so it applies even to the owner. Make sure your app's connection role doesn't have `BYPASSRLS`. Debug using the same restricted role production uses, not a privileged one.
- For performance, don't take it on faith. Pull your top 10-20 heaviest/slowest queries, run them against prod-scale data with RLS enabled in a staging environment, and compare plans before flipping it on broadly. This is worth measuring, not guessing at. Load-test the heavy queries before each table goes live.
- Keep one narrowly-scoped, audited "admin" role for legitimate cross-tenant operations (support tooling, billing reconciliation). Don't leave every query capable of seeing everything by default.

## Risks of this plan
- Connection pooling is the one real landmine. The failure mode is using session-level `SET` with a pooler in transaction mode (PgBouncer), where a connection can get reused across different logical requests without resetting state.
- Debugging is harder mainly if you debug as a superuser or table owner, since RLS is invisible to those roles by default. You can "fix" something locally that doesn't reproduce because you unknowingly bypassed the policy.
- Performance risks are non-obvious. A policy that calls a non-`STABLE` function gets re-evaluated per row instead of once. Joins across multiple RLS-protected tables each add a predicate, which can matter on your heaviest queries. If any table is partitioned, verify RLS doesn't interfere with partition pruning.
- If you're not on real Postgres, such as a compatible-but-limited managed service, verify its RLS support and planner behavior match vanilla Postgres before betting on it. Some don't push policy quals as well.

## Strongest counter-position
- If you profile your actual heaviest queries at real data volume (watch for skewed tenants with much larger row counts) and find a regression that indexing/partitioning genuinely can't fix, the source would scope RLS to the higher-risk tables only rather than blanket-applying it, and treat the rest as a longer-term project.
- If the near-miss query actually did run through ORM-covered application code (raw SQL sitting in your repo, not an out-of-band report or script), the gap is narrower than assumed, and tightening CI enforcement buys you more than otherwise credited. The source would still lean RLS given 2000 tenants and invoice data, but the urgency shifts.
- If you were looking at tens of thousands of tenants with hard contractual isolation requirements, that would be a different conversation. You're not there.

## Confidence
- High: every claim above is stated without a hedge. That covers the app-layer gap shown by the near-miss, RLS holding regardless of the issuing query, the `SET LOCAL` pooling pattern, the fail-closed behavior, the `FORCE ROW LEVEL SECURITY` and `BYPASSRLS` steps, the policy composing with existing indexes, the non-`STABLE` re-evaluation, the 2000-tenant comfort zone, and the compliance point.
- Medium: none stated.
- Low: none stated.

Unknowns the source names:
- Whether your heaviest queries regress at real data volume, including with skewed tenants, in a way indexing or partitioning can't fix.
- Whether you are on real Postgres or a managed service whose RLS support and planner behavior differ.
- Whether the near-miss query ran through ORM-covered application code.
- Whether any table is partitioned and RLS interferes with partition pruning.
