# arm: wise-men-flash (Ali-expandings/wise-men-flash SKILL.md v0.2.0, aaabd74, unchanged at 1d6a552) | question: R501 | orchestrator: general-purpose/sonnet | run: 2026-11-08 (round 6, PREREG-6 rules)
# minutes: 2.9 | subagent calls: 4 (transcripts matched: 4) | tokens in/out/cache-read/cache-write: 24/30723/697200/177508 | list-price USD: 1.43
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | orchestrator agent: a0ba5e98a835b1deb | orchestrator model: general-purpose/claude-sonnet-5-5 | transcript sha256: 654db5a88e7d79e92a5752e7bfe6c598f5b1c690a5b270e6d5798abdae25cf2b
# arm prompt: round 5's flash arm prompt (arm-prompts-r5.md), verbatim apart from local paths: yes | spawned: wise-member/haiku = claude-haiku-5-5 x1; wise-member/opus = claude-opus-5-5 x2; wise-member/sonnet = claude-sonnet-5-5 x1 | checker calls: 1
# note: tools beyond Read and Agent, across the run: Edit x4, Write x1

## Recommendation

Turn on row-level security as a fail-closed backstop underneath your existing ORM filter, and keep the query wrapper and lint rules as a cheap extra layer. Don't choose RLS instead of the application check, and don't choose the application check alone. First spend half a day finding out which database role and code path the near-miss report actually used, because that decides whether RLS would have stopped that incident.

## Why

The application-only option depends on every future code path remembering the filter. Lint reliably catches literal raw SQL. It misses SQL assembled at runtime, views, functions, jobs, migrations and ad-hoc psql sessions. Your setup already has one such side door (raw SQL), and step 1 below establishes whether the near-miss used it. RLS enforces in the database for any direct table access by an ordinary role, whatever code issued the query, and returns zero rows when no customer is set. Views and owner-rights functions need the extra care described below.

Your worries each have a standard answer, and the bypass rules hide a bigger trap than any of them.

- **Pooling:** under PgBouncer transaction pooling, a session-level `SET` carries one customer's ID into the next client's transaction, so RLS would cause the leak it is meant to prevent. Set the customer with `SET LOCAL` or `set_config('app.customer_id', $1, true)` inside an explicit transaction on every request. Autocommit ORM reads must be wrapped in one.
- **Bypass:** superusers and roles with BYPASSRLS skip RLS, and so does the table owner unless you run `FORCE ROW LEVEL SECURITY`. If the app connects as the owner, RLS is on and enforces nothing while tests pass. The app needs its own non-owner, non-BYPASSRLS role, separate from the migration role. Views run with their owner's rights and skip policies unless created `security_invoker` (PostgreSQL 15 and later). Materialized views cannot carry policies. Functions defined to run with their owner's rights (`SECURITY DEFINER`) also run as the owner. Audit each of these for customer-owned data.
- **Performance:** a bare equality policy such as `customer_id = nullif(current_setting('app.customer_id', true), '')::bigint` lets indexes work, and the `nullif` makes an unset value return no rows instead of an error. Slowdowns typically come from policies containing subqueries or joins. They also come from the planner evaluating the policy before your own conditions that use non-leakproof functions (some LIKE, jsonb and full-text operators). Your own filter stays in the query as well, and the duplicate predicate is cheap.
- **Debugging:** failures show up as silently empty results. Make the wrapper raise when no customer is set, and log the customer ID per request.

Schema-per-customer or database-per-customer is a poor fit at 2,000 customers, because migrations fan out across every schema.

## What to do

1. **Half a day:** trace the near-miss to its exact query, database role and code path. Decide whether the filter was missing, wrong, or missing only on a joined table.
   - Check the app role's `rolsuper` and `rolbypassrls` flags, whether it owns the tables, and the pooler mode.
   - Pull queries from `pg_stat_statements` that touch customer tables without a customer predicate, to size the side door.
2. **One week:** pilot on the five largest customer tables, invoices included.
   - Create the non-owner app role, add `FORCE ROW LEVEL SECURITY` and the bare-equality policy, and wrap each request in a transaction that sets the customer with `set_config(..., true)`.
   - Run `EXPLAIN ANALYZE` on your ten heaviest queries before and after.
   - Add a test that connects as the app role with no customer set and asserts zero rows.
   - Add a two-customer test that runs every report as customer A and fails if any of B's rows appear.
3. **Reporting path:** give cross-customer reporting, BI and background jobs a separate, audited role and path, and keep that list short. If the near-miss ran through such a role or carried the wrong customer ID, RLS would not have stopped it. The fix for that incident is this reporting path plus an output check that every invoice in a document or report carries the requested customer ID, failing loudly otherwise.
4. **Decision at the end of week one:** fall back to wrapper, lint and the output check if either of these holds.
   - A heavy query is still more than about 2x slower after you have simplified the policy.
   - The pilot shows the leaking paths must bypass RLS anyway.

   Otherwise roll out to the remaining customer tables, table by table.
5. **Outside the database:** neither database option covers caches, search indexes, file-storage keys or exports. Scope those by customer ID separately.

## Risks of this plan

- The app still connects as the owner or a BYPASSRLS role, so RLS enforces nothing and nobody notices. The non-owner role and the zero-rows test are the guard.
- A session-level `SET` under transaction pooling hands one customer's context to the next request.
- The reporting path becomes the new leak, since it must bypass RLS by design.
- Developers who hit silently empty results under deadline pressure push for a convenience bypass role. People also stop reviewing the application filters because the data feels protected.
- Heavy queries regress because of policy shape. The week-one measurement finds this before rollout.
- A filter that is present but carries the wrong customer ID passes both RLS and the lint rule.
- **Cost of waiting:** until a database-level check exists, the next raw-SQL path or hotfix can repeat the near-miss, and nothing in the current setup would stop it.

Cost of being wrong: the pilot is reversible, since policies can be dropped or disabled per table. What is hard to undo is any actual disclosure of one customer's invoices to another. If the counter-position below is right, you lose about a week of pilot effort and keep the ORM filter, wrapper, lint and output check you would have built anyway.

## Strongest counter-position

"The whole comparison rests on one unchecked premise: that the near-miss was an ordinary tenant-scoped query with a missing filter. It happened in a report. Reports usually run across customers by design, often under the table owner or a reporting role, through BI tools, notebooks or views, and RLS does not apply to those. The other common cause is a filter that is present but carries the wrong customer ID, from a parameter bug or leftover context. RLS returns the wrong customer's rows without complaint, and lint passes the query because a filter is there. Either option could ship and the same incident would happen again. Take the wrapper and lint plus an output check that every row in a document carries the requested customer ID now, and keep RLS for later, once the root cause shows it covers the path that failed. Meanwhile RLS gives a false sense of safety, silent empty results, and a 3 a.m. owner-role connection that sees every customer's rows."

This wins if the half-day trace shows a privileged role or a wrong customer ID. Then RLS is a separate hardening project, and the output check and reporting path are the real fix. It loses if the trace shows an ordinary-role query missing a filter.

## Confidence

- RLS with `FORCE`, a non-owner role and per-transaction `SET LOCAL` closes direct-table-access side doors for ordinary roles: **High**, as these are standard Postgres behaviours. Coverage of views and owner-rights functions: **Medium**, until you have audited them.
- RLS as a backstop is worth its cost with simple equality policies: **Medium**, pending your `EXPLAIN ANALYZE` results on the heaviest queries.
- RLS would have stopped this specific near-miss: **Low**, until the role and code path are known.

Material unknowns: the near-miss's role and path, the pooler mode, whether customers have parent/child or partner access that would force subqueries into policies, and your PostgreSQL version.
