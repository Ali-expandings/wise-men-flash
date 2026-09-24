# arm: brainstorming (obra/superpowers 5bf4e7801107, with visual-companion.md and spec-document-reviewer-prompt.md) | question: R503 | orchestrator: general-purpose/sonnet | run: 2026-09-24 (round 5, PREREG-5 rules)
# minutes: 9.9 | subagent calls: 1 (transcripts matched: 1) | tokens in/out/cache-read/cache-write: 18/56604/792370/122228 | list-price USD: 1.55
# note: the author's first name (inherited from global config) redacted to "the user"
# note: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> before blinding

# Automation Builder: Build vs. Buy — Recommendation

**Classifying this first:** this is the heaviest path in the brainstorming process — a resource-allocation decision sized like a new strategic initiative (two quarters of engineering capacity, or most of the company's cash reserve, for an 80-person company). That gets the full treatment: clarifying questions, competing approaches with trade-offs, a sectioned design, and a written decision memo — not a quick take.

*(Visual companion: not offered. Nothing here is a mockup, layout, or diagram question — it's a financial and organizational trade-off, which reads better as text and one comparison table than as a browser mockup tool.)*

## Clarifying questions (asked, with the most likely answer assumed so the analysis could proceed)

1. **Is the goal competitive parity or a broader automation platform play?** → Parity. The request is framed as closing a specific, evidenced gap, not an open-ended strategic bet — scoped accordingly.
2. **How solid is "missing automation features" as a diagnosis?** → A real but biased signal (sales tends to name the most visible product gap). 7/10 plus independent competitive intel is strong enough to act on, not strong enough to skip a two-day sanity check before spending a quarter's headcount or the cash reserve.
3. **What does "most of our cash reserve" imply about risk tolerance?** → Treated as a hard constraint, not a rhetorical flourish — it caps how much acquisition risk is acceptable no matter how good a target looks.
4. **Does the in-house team already have this expertise (workflow engines, visual builders)?** → Not stated; defaulted to "no specialized depth," since that's the typical profile at 80 people, which makes "two quarters" an optimistic floor for something *polished*, not a guaranteed ceiling.
5. **Is there already a specific acquisition target in diligence?** → No — treated as pre-diligence, so integration cost and founder-retention risk are scored as open unknowns, not assumed away.

## The approaches

I'd lead with a third option neither "build" nor "buy" names directly.

- **Build in-house (2 quarters):** full control, no cash outlay, but "polished" — the actual bar, per the competitor comparison — is the hard part, not "functional." Two quarters is realistic for an MVP, optimistic for something that matches a mature competitor product. You keep losing automation-flagged deals for the entire build window.
- **Buy the startup:** fastest-looking option, but not actually instant — integrating an acquired codebase typically eats one to two quarters on its own, and the value you're buying lives mostly in the founding engineers staying past vesting. Spending most of the cash reserve on one feature gap, pre-diligence, is a concentrated bet with low reversibility for a company this size.
- **Recommended: validate, then partner/embed + scoped build.** A cheap, days-long validation pass on the seven lost deals, then license or embed a third-party automation/workflow engine to close the gap in weeks at a fraction of the cost, while a smaller in-house effort builds real differentiation on a realistic timeline instead of racing a deadline. Reversible, cash-light, fast.

## Design walkthrough

**Approach & rationale.** Both options as posed are expensive, low-reversibility bets on a signal that hasn't been independently checked. A licensed/embedded automation engine is a boring, proven pattern for exactly this problem (plenty of SaaS products add "Zapier-like" automation this way) and gets the objection off the table fastest. *(Looks right — continuing.)*

**Execution plan.** Days 1–10: pull deal notes on the seven losses, run 2–3 real win-loss calls, confirm which automation capabilities actually matter. Weeks 2–6: shortlist and integrate an embeddable engine scoped to what validation found. Quarter 2, in parallel and smaller in scope: decide, now with real usage data instead of a guess, whether an in-house differentiated builder is still worth it. *(Looks right — continuing.)*

**Financial impact.** Build: opex/headcount cost, no cash-reserve hit, real opportunity cost against the rest of the roadmap. Buy: very high cash impact, "most of reserve," low reversibility. Partner/embed: licensing opex only, cash reserve stays intact. *(Looks right — continuing.)*

**Risk handling & fallback triggers.** If validation shows automation wasn't the real blocker, stop and re-scope. If no embeddable engine fits the architecture, fall back to a tightly-scoped in-house build (not the full guessed feature set). If a specific acquisition target later shows a price that's a small fraction — not most — of the reserve, with credible retention terms, Buy becomes worth real diligence. *(Looks right — continuing.)*

**Success metric.** Win rate on deals where automation was previously logged as the loss reason, tracked after the embedded solution ships. *(Looks right — continuing.)*

**Spec written** to `<scratch>/R503/brainstorming/2026-09-24-automation-builder-build-vs-buy-design.md`. Self-review plus an independent reviewer pass caught one internal inconsistency (a mitigation bullet in Risks & Mitigations had misattributed Option C's speed/cost/reversibility to the Option A fallback) — fixed inline. Independent review: **Approved**, no open issues. Spec review gate: approved, proceeding.

## Bottom line

For an 80-person company, don't spend most of the cash reserve on this acquisition as currently framed, and don't default straight to a from-scratch two-quarter build either. Validate the diagnosis in about a week, then close the gap fast and cheap with a licensed or embedded automation engine, and only fund the bigger in-house build — or revisit the acquisition — once you know, from real usage, what's actually still missing. Keep Buy alive only as a fallback, conditional on a target whose price is a small fraction of reserve with credible team-retention terms — nothing in the numbers as given clears that bar yet.

---

## Full decision memo

# Automation Builder: Build vs. Buy vs. Partner — Decision Memo

**Date:** 2026-09-24
**Status:** Draft for review
**Decision owner:** the user (or delegate)

## 1. Problem Statement

Of the last ten mid-size deals lost, sales logged "missing automation features" as
the reason for seven. The closest competitor has a polished automation builder.
The company (~80 people) is choosing between:

- **Build:** spend two quarters building an in-house automation builder.
- **Buy:** acquire a small startup that already has one, consuming most of the
  cash reserve.

The real question isn't "build or buy" — it's how to close a validated
competitive gap at the lowest risk to cash, roadmap, and execution certainty.

## 2. What We Know / What We're Assuming

| # | Question | Assumed answer (stated or inferred from the request) |
|---|----------|--------------------------------------------------------|
| 1 | Is the goal to hit competitive parity on automation, or to make automation a broad new strategic platform? | Parity/close-the-gap. The request frames this as a reaction to lost deals and a specific competitor feature, not an open-ended platform ambition. Scope the response accordingly — don't let either path balloon into a bigger bet than the evidence supports. |
| 2 | How solid is "missing automation features" as a diagnosis? | Sales-logged reasons are a real signal but a biased one — sales tends to blame the most visible product gap rather than pricing, messaging, or their own execution. 7/10 is a strong pattern, reinforced by independent competitive intel (the competitor's builder is a known strength), so it's credible enough to act on — but not solid enough to skip a near-free validation step before committing two quarters of engineering or most of the company's cash. |
| 3 | What does "most of our cash reserve" imply about runway risk? | For an 80-person company, cash reserve is the buffer against a slow quarter, a stretched-out fundraise, or the need to make an unrelated critical hire. "Most of it" on one feature gap is treated here as a genuine constraint, not a rhetorical flourish — it caps how much acquisition risk is acceptable regardless of how attractive a target looks. |
| 4 | Does the in-house team have the specific expertise this requires (workflow engines, visual builders, reliability at scale)? | Not stated. Default assumption for an 80-person company: engineering is roughly 15–30 people, and a "polished" builder is a genuinely hard product surface (drag-drop UI, trigger/action framework, execution reliability, monitoring). A dedicated 3–6 person pod for two quarters is a meaningful slice of total capacity, so the opportunity cost against the rest of the roadmap is real, and "two quarters" is treated as an optimistic floor for a *polished* result rather than a guaranteed ceiling. |
| 5 | Is there a specific acquisition target already in diligence, or is "buy" still a hypothetical class of action? | Phrased generically ("a small startup that already has one"), so treated as pre-diligence. Integration cost, retention risk of the founding team, and code quality are unknowns and are scored as open risk, not assumed away. |

## 3. Options Considered

### Option A — Build in-house (two quarters)

Dedicate a small pod to build the automation builder natively into the product.

- **Pro:** full control of architecture and integration with the existing data
  model; no cash outlay; no acquisition/culture/retention risk; IP fully owned.
- **Con:** "polished" is the hard part, not "functional" — two quarters is a
  realistic timeline for an MVP, an optimistic one for something that matches
  a competitor's mature builder. The company keeps bleeding deals with
  automation-shaped objections for the full build window, with no interim
  relief. Meaningful opportunity cost against the rest of the roadmap.

### Option B — Buy the startup (acquisition)

Acquire a small company that already has a working automation builder.

- **Pro:** immediate access to a product that's already validated by the
  market (a company was built around it); specialized team with deep
  expertise in a genuinely hard problem; possible option value beyond the
  single feature (their customers, their IP, their roadmap).
- **Con:** "most of the cash reserve" for one feature gap is a concentrated,
  low-optionality bet for a company this size — it trades away the buffer
  that protects against a bad quarter or a slow raise. It's also not as fast
  as it looks: integrating an acquired codebase (auth, billing, data model,
  UX) commonly takes one to two quarters on its own, and the value being
  bought is disproportionately in the founding engineers' heads — if they
  don't stay past vesting, the company has spent the cash and may still end
  up rebuilding.

### Option C — Validate, then partner/embed + scoped build (recommended)

Two-step approach: a near-free validation sprint, followed by licensing or
embedding a third-party automation/workflow engine to close the urgent gap
fast, while a smaller in-house effort builds the specific, differentiated
pieces that actually matter for this product — on a realistic timeline, no
longer racing to cover the whole surface area from zero.

- **Pro:** closes the validated gap in weeks, not quarters, at a fraction of
  the cost of either extreme; preserves the cash reserve and most of the
  engineering roadmap; lets the in-house build (if still wanted) target real
  differentiation instead of parity-under-deadline; reversible — if the
  embedded solution doesn't move the win rate, the company hasn't spent its
  reserve finding that out.
- **Con:** some loss of differentiation and dependency on a vendor's roadmap,
  pricing, and reliability; may need real integration work to not feel
  bolted-on; doesn't fully resolve the strategic question of owning this
  capability long-term — it buys time and evidence to make that call properly.

### Comparison

| | Cash impact | Time to close gap | Execution risk | Reversibility |
|---|---|---|---|---|
| A. Build | Low (opex/headcount) | ~2 quarters, optimistic for "polished" | High — hard product surface, no interim relief | High — can redirect the pod |
| B. Buy | Very high (most of reserve) | 1–2 quarters realistic (integration), not instant | High — integration + retention + culture risk | Low — cash is spent, team may still leave |
| C. Validate + partner/embed | Low (licensing opex) | Weeks | Low — proven third-party component | High — can drop or swap vendor |

## 4. Recommendation

Lead with **Option C**: validate the diagnosis in the next one to two weeks,
then close the immediate gap with a licensed/embedded automation engine
while a right-sized in-house effort builds genuine differentiation on a
realistic timeline. Do not spend most of the cash reserve on the
acquisition as currently framed.

Reasoning: the two options as posed are both expensive, low-reversibility
bets on a signal (sales-logged loss reasons) that hasn't been independently
checked yet. Build risks shipping an unpolished v1 on a deadline for a
problem where polish is the actual bar. Buy risks the company's cash
buffer on integration and retention outcomes that are unknown pre-diligence,
and is not as fast as it looks once integration time is counted. A licensed
or embedded automation engine is a mature, boring solution to exactly this
problem (many SaaS products add "Zapier-like" automation this way) and gets
the competitive objection off the table fastest, cheapest, and most
reversibly — which buys the room to make the build-vs-buy call properly
instead of under deal-loss pressure.

**Keep Buy on the table, but only as a conditional fallback**, triggered if
diligence on a specific target shows: the price is a small fraction of the
reserve (not "most" of it), the founding team has real, credible multi-year
retention terms, the technology is hard to replicate or license, or the
target brings strategic value beyond this one feature (existing customers,
adjacent IP). None of that is known yet from the numbers as given.

## 5. Risks & Mitigations

- **Validation sprint finds automation wasn't the real blocker.** Mitigation:
  the sprint is cheap (days, using data already in the CRM plus two or three
  win-loss calls) — sized so a wrong diagnosis costs little, unlike
  committing two quarters or the cash reserve first and finding out after.
- **No suitable embeddable engine fits the product's architecture.** Mitigation:
  this is the explicit fallback trigger for Option A — build in-house, but
  scoped to what validation actually showed mattered, not the full surface
  of a "polished builder" guessed from a competitor's marketing. This
  fallback is slower and costlier than Option C (weeks, low cost,
  reversible) — it inherits Option A's own two-quarter, higher-execution-risk
  profile from Section 3, just with a tighter, validated scope.
- **Embedded solution feels bolted-on to customers.** Mitigation: scope the
  integration work (auth, branding, data model) as part of Option C's plan,
  not as an afterthought; this is real but bounded engineering effort, far
  short of a full builder from scratch.
- **Competitor keeps extending its lead while we validate.** Mitigation: the
  validation sprint is days, not weeks, specifically to avoid this; it runs
  in parallel with vendor evaluation for Option C, not sequentially before it.

## 6. Decision Criteria (what would change this recommendation)

- If validation shows automation is a minor factor and something else (price,
  packaging, integration ecosystem) is the real driver — stop, re-scope, this
  memo's premise no longer holds.
- If no embeddable/licensable engine can integrate within the product's
  architecture at reasonable cost — fall back to Option A, scoped tightly to
  validated needs, not the full guessed feature set.
- If a specific acquisition target emerges whose price is a small fraction
  (not "most") of the cash reserve, with credible retention terms — Option B
  becomes competitive and should be diligenced properly rather than ruled out.

## 7. Next Steps (roughly 30/60/90)

1. **Days 1–10 — Validate:** pull deal notes for the seven flagged losses;
   run two to three real win-loss calls; confirm which specific automation
   capabilities (trigger types, integrations, visual builder vs. simple
   rules) actually matter.
2. **Weeks 2–6 — Close the gap fast:** shortlist two or three embeddable/
   white-label automation engines; pick one; integrate a scoped version
   (auth, branding, the specific triggers/actions validation surfaced).
3. **Quarter 2 (parallel, smaller scope) — Differentiate:** with the urgent
   bleeding stopped, decide with product/eng leadership whether a
   right-sized in-house build is still worth it for long-term
   differentiation and cost control, now informed by real usage data from
   the embedded solution rather than a guess.
4. **Ongoing:** track win rate on deals where automation was previously an
   objection, as the success metric for whether this closed the gap.
