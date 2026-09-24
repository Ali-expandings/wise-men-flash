# arm: grilling (mattpocock/skills c55ee46073ed) | question: R501 | orchestrator: general-purpose/sonnet | run: 2026-09-24 (round 5, PREREG-5 rules)
# minutes: 7.0 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 4/39739/121059/39145 | list-price USD: 0.78

**Design tree: multi-tenant Postgres isolation — row-level security vs. application-layer enforcement**

## Round 1

❓ **Q1** - **Either/or, or both?**: You've framed this as RLS vs. the wrapper+lint approach. Is it actually a replacement decision, or could RLS become the enforcement boundary while the wrapper/lint stays on as a separate, cheaper layer?

➡️ Both. Not a compromise — RLS becomes the actual trust boundary, the app layer becomes a fast-feedback/DX layer that nobody relies on for the real guarantee.

**Assumed:** Layered defense, with a designated authority (settled in Q5), not a straight swap of one for the other.

---

❓ **Q2** - **What else touches this database?**: Is the ORM-mediated app the only thing that ever queries this database, or are there admin/support tools, cron/billing jobs, a BI or reporting tool, warehouse ETL, or engineers running ad hoc SQL? Note that the incident that prompted this question was "an internal report" nearly leaking data — that phrasing points at a reporting/analytics path, which usually sits outside the main app's ORM and lint-checked codebase.

➡️ Assume yes: at 2,000 B2B customers there's almost certainly a support console for looking up a specific customer, some scheduled billing/invoicing job, and a reporting path — very likely the exact origin of the near-miss.

**Assumed:** Multiple non-ORM paths exist, and the near-miss most likely came from one of them — meaning a lint rule scoped to the app repo wouldn't have caught it.

---

❓ **Q3** - **Connection topology?**: Direct connections, or pooled (PgBouncer / RDS Proxy / Supavisor / similar)? If pooled, session, transaction, or statement mode?

➡️ Assume pooled, transaction-mode specifically — the standard choice at this scale, and the most constraining case for RLS context-binding, so designing for it is safe even if reality turns out looser.

**Assumed:** Transaction-mode pooling: any tenant-context mechanism must survive a physical connection being handed to a different logical caller between transactions.

---

❓ **Q4** - **What's actually at stake in a leak?**: The data in question is invoices between business customers — commercial/financial data, typically covered by a contractual confidentiality clause or DPA even without personal data involved. Is the exposure here material (contract terms, SOC2/ISO commitments), or is this a lower-stakes internal system?

➡️ Assume material: B2B invoicing at this scale almost always sits under some isolation promise, and "nearly showed one customer another's invoices" is the kind of thing that becomes a disclosure obligation if it actually happens.

**Assumed:** Real contractual/business risk, not just internal embarrassment — raises the bar for what "sturdier" is worth.

## Round 2

❓ **Q5** - **Which layer is authoritative, and who's exempt?**: With both layers kept (Q1) and non-ORM paths confirmed (Q2): which one is the actual security boundary, and do admin/cron/BI paths run under the same RLS-constrained role, or do some legitimately need cross-tenant access?

➡️ RLS is authoritative for every role except a small, explicitly named, logged set of trusted paths (migrations, and a deliberately-scoped admin/support role) — never a blanket bypass, never the default app role.

**Assumed:** One dedicated, non-owner, non-superuser, non-BYPASSRLS role for all normal app traffic — RLS applies to it automatically once enabled on a table. Migrations run as the owning role and stay exempt by design. Cross-tenant access, where genuinely needed, is a separate named role, audited.

---

❓ **Q6** - **How is tenant context bound to the session?**: Under transaction-mode pooling (Q3), context-setting must survive a physical connection being reused by a different tenant moments later. Options: session-level `SET app.customer_id = ...`, or `SET LOCAL app.customer_id = ...` at the start of every transaction (auto-reverts at commit/rollback).

➡️ `SET LOCAL`, inside every transaction, every time — never a bare session-level `SET`. This is the standard pattern precisely because it can't leak across pooled connection reuse.

**Assumed:** Every DB transaction opens with `SET LOCAL app.customer_id`; nothing depends on session-level state.

---

❓ **Q7** - **Fail loud or fail silent?**: If tenant context is unset when a query runs, should it match zero rows (silent — looks like a data bug) or raise clearly?

➡️ Fail loud, and it's nearly free: `current_setting('app.customer_id')` — called *without* the `missing_ok = true` argument — already raises a Postgres error automatically if the setting was never bound in that transaction. The silent-empty-result complaint people have about RLS specifically comes from using the missing-ok variant or a `COALESCE` fallback to be "defensive." Don't. Let it error, and have the app wrapper also refuse to open a transaction without a customer_id, so the failure surfaces at the earliest, clearest point.

**Assumed:** Missing context is a hard error at both layers, not an empty result set — this directly defuses the "harder debugging" worry.

---

❓ **Q8** - **How do you sequence turning it on?**: Postgres RLS is binary per table for a non-exempt role — once enabled, it blocks immediately; there's no built-in log-only mode. Given the stakes from Q4: enable everywhere at once after staging tests pass, or stage it table by table?

➡️ Stage it — lowest-risk tables first, working up to the heaviest/most critical last, each validated against production-shaped data in staging before going live, with an internal or volunteer canary tenant absorbing the first hours of real traffic on each newly-enabled table.

**Assumed:** RLS goes live table-by-table, not a single flip; heaviest tables get the most validation and go last.

## Round 3

❓ **Q9** - **Do the non-ORM paths move onto the same mechanism?**: Admin tools, cron jobs, and reporting paths either start opening transactions with the same `SET LOCAL` discipline, or run under the narrow logged cross-tenant role from Q5. Left untouched, they're either broken by RLS or still a hole.

➡️ Migrate every internal tool that operates per-customer onto the same `SET LOCAL` convention — even a support console looking up "one customer at a time" should bind that customer's ID. Reserve the cross-tenant role only for things genuinely cross-tenant by design (billing reconciliation, warehouse export).

**Assumed:** One consistent context-binding convention across the entire codebase and tooling — this is what actually closes the gap the incident exposed.

---

❓ **Q10** - **Policy predicate shape?**: Plain indexed equality (`customer_id = current_setting('app.customer_id')::int`), or something more elaborate (subqueries, joins to a permissions table)? The app already filters by customer_id on every query today per your description.

➡️ Plain equality against an already-indexed customer_id column everywhere that shape fits. Treat anything that doesn't fit (tenancy not a direct column) as a named special case to test individually.

**Assumed:** Simple, index-friendly predicates on the hot tables; performance risk is concentrated in whatever tables don't fit this pattern, and those get listed explicitly rather than discovered in production.

---

❓ **Q11** - **How do you validate performance before it's load-bearing?**: Will the heaviest queries get `EXPLAIN ANALYZE`'d with policies active, against a staging copy with production-scale data and skew, before any table's RLS is trusted?

➡️ Yes — pull the top 10-20 queries by total cost from `pg_stat_statements`, run them under RLS in a production-shaped staging environment, and check specifically for plan changes (lost index usage, added materialization steps), not just wall-clock time. A plan regression can look fine at low load and fall over at peak.

**Assumed:** A concrete, named validation step gates each table's promotion from Q8 — not "we'll keep an eye on it."

---

❓ **Q12** - **What's the rollback lever if something regresses anyway?**: A global kill switch, or something finer-grained?

➡️ Per-table: `ALTER TABLE ... DISABLE ROW LEVEL SECURITY` (or dropping/relaxing just the offending policy) as an emergency lever on the one affected table, with the app-layer wrapper still live underneath during the bake period, so disabling RLS on one table doesn't mean flying blind on it.

**Assumed:** Rollback is table-scoped, never all-or-nothing, and the app layer is never fully retired as a live check during this period.

## Round 4

❓ **Q13** - **Does the lint rule get retired once RLS is proven?**: Once RLS is authoritative and bake-period-clean, is the wrapper/lint still worth keeping?

➡️ Keep it, permanently. It's cheap, and it catches a missing scope at code-review/CI time with a clear message — a faster feedback loop than a database-level catch, even once the database-level catch is fully trustworthy. It stops being the security boundary; it doesn't stop being useful.

**Assumed:** The wrapper/lint stays indefinitely as a CI/DX layer; RLS is the only layer anyone is allowed to treat as the actual guarantee.

---

❓ **Q14** - **How do you know later if this quietly breaks?**: Six months from now someone adds a new internal tool or table and forgets to wire up either layer. What catches that?

➡️ Two things: a CI/schema check against `pg_class.relrowsecurity` that fails when a new table is created without RLS enabled, and production monitoring that alerts on any query touching a protected table with no tenant context bound (the fail-loud behavior from Q7 turned into an error-rate alert).

**Assumed:** New tables are RLS-enabled by default and CI-enforced; missing-context queries show up as an alertable error rate, not as a silent gap found in the next incident.

---

Frontier empty.

## Final recommendation

Pick row-level security as the enforcement boundary. Keep the query wrapper and lint rule too, but demote them to a DX/CI layer — fast, cheap feedback that catches a missing scope before code ships — not the thing actually trusted to prevent the next incident.

The reasoning that settled it: the near-miss came from "an internal report," almost certainly a path outside the ORM-mediated, lint-checked application code. That's exactly the class of access a lint rule structurally can't see, since it only checks code in the repository it scans. RLS is the only one of the two options that protects a query regardless of what issued it, as long as that thing isn't running as superuser/BYPASSRLS. Given business customers, invoice data, and a near-miss that was close to a contractual/disclosure problem, sturdier is worth the operational cost here.

Implementation shape, in order:

1. One dedicated, non-owner, non-superuser, non-BYPASSRLS role for all normal app traffic; RLS applies to it as soon as it's enabled on a table. Migrations run as the owning role and stay exempt by design.
2. Tenant context bound via `SET LOCAL app.customer_id` inside every transaction — never session-level `SET` — the only pattern safe under transaction-mode pooling.
3. Missing context fails loud (a Postgres error, via the strict form of `current_setting`) at both layers, not a silent empty result — this directly answers the "harder debugging" worry.
4. Plain indexed equality predicates on customer_id everywhere that shape already fits — which, per your own description, is everywhere the ORM already filters today, so it's usually performance-neutral. Anything that doesn't fit gets found and tested individually, not discovered in production.
5. Every internal tool, cron job, and reporting path migrated onto the same context-binding convention, or onto a narrow, logged, explicitly cross-tenant role — no more untracked raw-SQL paths.
6. Rollout table-by-table (Postgres RLS has no built-in audit-only mode, so staging has to happen via a real staging environment plus sequencing, not an in-prod dry run) — least-risk tables first, heaviest last, each validated with `EXPLAIN ANALYZE` against production-shaped data and given canary traffic before being trusted broadly. Rollback lever is per-table, never global.
7. Lint rule kept permanently as a cheap first catch; add a CI check against `pg_class.relrowsecurity` for new tables, and an alert on any query touching a protected table with no tenant context bound.

What would change this answer: if every access path to this database — including every internal tool, every ad hoc script, every future service, forever — is guaranteed to go through the one lint-checked codebase, and the team has no Postgres RLS experience, and the heaviest queries demonstrably regress under RLS in testing with no fixable predicate shape, a hardened app-layer-only approach could be defensible as a long-term choice rather than an interim one. That's a narrow set of conditions, and the incident that prompted this question is itself evidence against the first one — something already got in through a path the lint rule didn't cover. A legacy schema where customer_id isn't consistently present on every table is a real reason to phase RLS in table-by-table rather than all at once, but that's a sequencing argument, not a reason to stop short of it.
