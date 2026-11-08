# arm: plain-memo (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R501 | attempt: 2 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R501-plain-memo-rewrite-2.txt (sha256 4f6b101479b84f09)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: a4da71499b46c0150 | transcript sha256: 10b4a29bd6d3f8525caba467ada833dc28fcc171403c451cf0ce3461ca0210b9
# minutes: 0.4 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/4501/3185/18848 | list-price USD: 0.14
# final: attempt 2, which passed the script checks and the audit

## Recommendation

Pick row-level security (RLS), but as an added layer and not as a replacement for what you have. Keep the ORM auto-scoping and the lint rule, and make RLS the backstop that holds even when those are wrong, bypassed, or simply not in the loop. This is defense in depth, not a swap.

The reasoning rests on what the near-miss shows. It was an internal report that nearly crossed tenants, and it was not a bug in ORM-generated code. After an incident caused by an access path nobody anticipated, the property you actually want is one that holds regardless of what is issuing the query, and RLS provides that by moving the check into the data itself.

On your three worries, the position is that connection pooling is the one real landmine but is a solved problem, that debugging is harder mainly if you debug as a superuser or table owner, and that performance should be measured and not guessed at. The recommended rollout is table by table, starting with `invoices`. Several conditions that would change the answer are set out below.

## Why

The near-miss already tells you where the app-layer approach fails. It was an internal report that nearly crossed tenants, not a bug in ORM-generated code. A query wrapper and lint rule only protect the code path that runs through your CI pipeline. They do not protect ad hoc scripts, BI tools (Metabase, Looker or whatever you use), a read replica someone connects to with psql, migrations, admin tooling, or the next internal service that talks to this database without importing your lint config. That is exactly the gap the incident found.

A lint rule pattern-matches against source text. It can be defeated by dynamic SQL, string-built queries, views, or just by not running in that repo. RLS moves the check into the data itself, so it holds regardless of what is issuing the query. After an incident caused by an unanticipated access path, that invariance is the property you actually want.

The existing controls are still worth keeping. They are cheap, they give fast feedback in code review, and they keep common-case queries efficient and correct. RLS becomes the backstop that is true even when they are wrong, bypassed, or not in the loop.

On the pooling worry, the failure mode is using a session-level `SET` with a pooler in transaction mode (PgBouncer). A connection can then be reused across different logical requests without resetting state. The fix is a standard pattern for RLS-based multi-tenancy, and it composes fine with transaction-mode pooling.

On the debugging worry, RLS is invisible to superusers and table owners by default. If you debug as one of those, you can "fix" something locally that does not reproduce, because you unknowingly bypassed the policy.

On the performance worry, a policy like `customer_id = current_setting('app.tenant_id', true)::uuid` is just another indexed predicate. You already need `customer_id` indexed today, since the ORM filters on it on every query. Postgres pushes the policy qual into the plan alongside your other WHERE clauses, so it composes with existing indexes and does not add a separate filter pass.

On scale, 2000 tenants in one database is squarely within RLS's comfort zone. It is not a scale where you would need schema-per-tenant or database-per-tenant instead. If you were looking at tens of thousands of tenants with hard contractual isolation requirements, that would be a different conversation, and you are not there.

Compliance points the same way. If you are heading toward a compliance review (SOC 2, enterprise security questionnaires), that pushes further toward RLS and not away from it. "Is tenant isolation enforced at the database layer or only in application code" is a standard question, and app-only isolation is a known red flag in vendor reviews.

## What to do

1. Keep the ORM auto-scoping and the lint rule running the whole time. Add RLS as the backstop.
2. Enable RLS table by table, starting with `invoices`, since that is what almost leaked.
3. Scope the tenant setting to the transaction. Always use `SET LOCAL` (or `set_config(name, value, true)`, where the `true` means local), issued inside the same transaction as the query. This is the standard pattern for RLS-based multi-tenancy and it composes fine with transaction-mode pooling.
4. Make the policy fail closed. `current_setting('app.tenant_id', true)` returns NULL if unset instead of erroring, and `customer_id = NULL` is never true. A request that forgets to set the tenant context therefore returns zero rows, not all rows. Test that explicitly before rollout. It is the difference between "worst case, a bug breaks a customer's report" and "worst case, a bug leaks data," which is the whole point.
5. Run `ALTER TABLE ... FORCE ROW LEVEL SECURITY` so the policy applies even to the owner, and make sure your app's connection role does not have `BYPASSRLS`. Debug using the same restricted role production uses, not a privileged one.
6. Do not take performance on faith. Pull your top 10-20 heaviest or slowest queries, run them against prod-scale data with RLS enabled in a staging environment, and compare plans before flipping it on broadly. This is exactly the kind of thing worth measuring, not guessing at.
7. Keep one narrowly scoped, audited "admin" role for legitimate cross-tenant operations (support tooling, billing reconciliation), rather than leaving every query capable of seeing everything by default.
8. Load-test the heavy queries before each table goes live.

## Risks of this plan

Connection pooling is the one real landmine. If you use a session-level `SET` with a pooler in transaction mode (PgBouncer), a connection can get reused across different logical requests without resetting state. This is treated as a solved problem and not a reason to avoid RLS, provided you use the transaction-scoped setting described above.

Debugging can mislead you. Because RLS is invisible to superusers and table owners by default, debugging as one of them can make a problem appear fixed locally when it does not reproduce, since you unknowingly bypassed the policy.

Performance has some non-obvious risks:
- A policy that calls a non-`STABLE` function gets re-evaluated per row instead of once.
- Joins across multiple RLS-protected tables each add a predicate, which can matter on your heaviest queries.
- If any table is partitioned, verify that RLS does not interfere with partition pruning.

A request that forgets to set the tenant context must return zero rows and not all rows. That is why the fail-closed behavior should be tested explicitly before rollout.

Your platform matters too. If you are not on real Postgres, for example a compatible-but-limited managed service, verify that its RLS support and planner behavior match vanilla Postgres before betting on it. Some do not push policy quals as well.

## Strongest counter-position

The main limit on this answer is about where the near-miss came from. If it turns out the near-miss query actually did run through ORM-covered application code, meaning it was raw SQL sitting in your repo and not an out-of-band report or script, then the gap is narrower than assumed. In that case, tightening CI enforcement buys you more than would otherwise be credited. The lean would still be toward RLS given 2000 tenants and invoice data, but the urgency shifts.

There is also a performance limit. If you profile your actual heaviest queries at real data volume (watch for skewed tenants with much larger row counts) and find a regression that indexing or partitioning genuinely cannot fix, the advice would be to scope RLS to the higher-risk tables only and not apply it blanket. The rest would be treated as a longer-term project.

## Confidence

High confidence, because the source states these claims without a hedge:
- RLS should be added as a layer and not as a replacement for the existing controls.
- The near-miss was an internal report that nearly crossed tenants, and it was not a bug in ORM-generated code.
- A query wrapper and lint rule only protect the code path that runs through your CI pipeline, and they do not protect ad hoc scripts, BI tools, a read replica, migrations, admin tooling, or other internal services.
- RLS moves the check into the data itself, so it holds regardless of what is issuing the query.
- Connection pooling is a solved problem, and the fix is `SET LOCAL` or `set_config(..., true)` inside the same transaction as the query.
- A request that forgets to set the tenant context returns zero rows, because `customer_id = NULL` is never true.
- RLS is invisible to superusers and table owners by default, and `FORCE ROW LEVEL SECURITY` plus a role without `BYPASSRLS` addresses this.
- The policy is just another indexed predicate, and Postgres pushes it into the plan alongside your other WHERE clauses.
- A policy that calls a non-`STABLE` function gets re-evaluated per row instead of once.
- Joins across multiple RLS-protected tables each add a predicate, which can matter on your heaviest queries.
- Some compatible-but-limited managed services do not push policy quals as well.
- 2000 tenants in one database is squarely within RLS's comfort zone.
- Compliance reviews push further toward RLS, and app-only isolation is a known red flag in vendor reviews.

Medium confidence: none. The source uses none of the words that set this level ("likely", "probably", "usually", "typically", "suggests") on any claim.

Low confidence: none. The source uses none of the words that set this level ("may", "might", "could", "possibly", "unclear") on any claim.

Unknowns the source names:
- Whether your heaviest queries show a regression at real data volume, including with skewed tenants that have much larger row counts, and whether indexing or partitioning can fix it.
- Whether you are on real Postgres or a compatible-but-limited managed service, and whether its RLS support and planner behavior match vanilla Postgres.
- Whether the near-miss query actually ran through ORM-covered application code, as raw SQL sitting in your repo, or came from an out-of-band report or script.
- Whether you are heading toward a compliance review (SOC 2, enterprise security questionnaires).
- Whether any of your tables are partitioned, and whether RLS interferes with partition pruning on them.
