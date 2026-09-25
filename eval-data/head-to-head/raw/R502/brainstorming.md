# arm: brainstorming (obra/superpowers 5bf4e7801107, with visual-companion.md and spec-document-reviewer-prompt.md) | question: R502 | orchestrator: general-purpose/sonnet | run: 2026-09-25 (round 5, PREREG-5 rules)
# minutes: 9.0 | subagent calls: 1 (transcripts matched: 1) | tokens in/out/cache-read/cache-write: 28/48118/1418446/131679 | list-price USD: 1.64
# note: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> before blinding

Design doc saved to: `<scratch>/R502/brainstorming/2026-09-25-deploy-freeze-january-outages-design.md`

This looked architectural rather than a quick feasibility spike — a recurring, three-year, org-wide pattern touching release process for 60 people, with no existing "flow" to bound it to — so it got the full pass: questions, approaches, a sectioned design, written up and reviewed. No human partner was available to approve each gate live, so every gate below was presented with its most-likely answer and carried forward; the Assumptions section is the record of what to confirm.

---

# Why January Eats What December Freezes

## Direct answer

**What's going wrong:** the freeze stops *deploys*, not *change*. Sixty engineers keep merging for ~10 business days, so a two-week backlog of unreleased, never-jointly-tested changes builds up behind the gate. When the gate opens, that backlog ships as one oversized batch (or a burst of releases in the first few days) instead of the normal small, incremental deploys. Batch size is one of the best-understood drivers of change failure rate in release engineering: the more independent changes land together, the more combinations can interact badly, the harder each one is to review and test in isolation, and — critically here — the harder it is to bisect a failure back to one cause once something breaks. That's what's been hiding the pattern: when 10 business days of merges ship at once and something breaks, there usually *is* a distinct, genuine bug behind each incident. The postmortems aren't wrong — they're answering "what broke," when the recurring question is "why did this much unreviewed-together change hit production at once," and no single incident review is scoped to ask that.

The traffic detail is the tell. If load were the driver, January — lower traffic than December — should be calmer, not worse. It isn't, which rules out demand and points squarely at what *did* change: deploy batch size and timing, not user volume.

**Is the freeze protecting you or moving the risk:** moving it, and likely amplifying it in transit. The freeze probably does what it's meant to during December itself — no deploys, no deploy-caused incidents in that window. But it doesn't delete the risk of those two weeks of changes; it warehouses it and discharges it all at once into early January. Failure risk doesn't scale linearly with batch size — more concurrent changes means more possible bad interactions between them, not just more independent chances to fail — so a doubled or tripled batch is disproportionately riskier, not proportionally. Layer on that early January is typically also when on-call and engineering capacity are still ramping back up from the holidays, and you've moved your largest, least-tested release of the quarter into your thinnest incident-response window. Three years of identical recurrence, with a ruled-out alternative explanation (traffic) sitting right in the question, is strong enough signal to act on now.

## Questions asked, and the answers assumed

Everything else in the question was taken as stated (freeze = deploys only, not merges; two-week window; 60 engineers; per-incident postmortems citing distinct bugs). Six things weren't stated and were assumed at their most likely reading rather than blocking on an answer:

1. **Freeze scope** — assumed a hard freeze on routine deploys with a narrow emergency-hotfix carve-out (standard shape for a holiday freeze).
2. **Shape of the unfreeze** — assumed effectively one big-bang exposure (a single release, or several compressed into the first 1–3 days). Either reading produces the same effective batch size, so it doesn't change the diagnosis.
3. **Rollout tooling** — assumed canary/staged rollout isn't consistently used for the unfreeze release, inferred because a well-canaried release would likely have contained this at low exposure rather than reproducing identically three years running.
4. **Postmortem scope** — assumed reviews capture a proximate cause per incident but nothing that rolls up across incidents. This one is close to stated outright: "each incident review blames a different specific bug, so nobody treats it as one pattern" is the clearest signal in the question.
5. **January staffing** — assumed on-call/engineering capacity is at or below normal strength in early January (holiday schedules still resolving). A compounding factor, not the primary driver.
6. **Whether this needed visual treatment** (mockups/diagrams via a browser companion) — assumed no; this is a causal/process question, not a layout question, so a plain-text treatment is enough. Not offered.

## Recommended validation (do this before investing)

Before committing engineering time, spend a day checking this against real incident history:

- Do the last 3 years of January incidents trace back to commits merged during the prior freeze window?
- Do incidents cluster in the first few days after unfreeze (consistent with a big-bang release), or spread evenly?
- How does change volume in the unfreeze release compare to a typical non-frozen release?
- Do merges cluster right *before* the freeze starts (a pre-freeze cram)? This specifically gates whether a voluntary pre-freeze slowdown is worth adding.

If these confirm, the design below is the fix. If they don't, the real driver is something else (a specific recurring change type, a seasonal dependency, a staffing gap alone) and the design should be re-scoped around what the data shows.

## Approaches considered

| | Approach | What it does | Trade-offs |
|---|---|---|---|
| **A — recommended, near-term** | Fix the reopening | Keep the freeze; replace the single big-bang unfreeze with a staged rollout: small, sequenced, canaried releases over the first 1–2 weeks of January instead of one mass deploy | Cheap, no new infrastructure, directly targets batch size, can be ready this December. Trades ship-speed for safety — that's the point. |
| B | Freeze merges too | Pause merges to main during the freeze, not just deploys | Stops the backlog from growing, but costs ~2 engineer-weeks × 60 people of idled/redirected work, and still needs a staged reopening — some backlog is inevitable in any freeze. Not recommended as the primary fix. |
| **C — recommended, structural** | Decouple merge from release | Feature flags / dark-launching so code merges continuously without exposing behavior; canary + staged rollout become the year-round default; the freeze narrows to only the change types that actually carry holiday risk | Addresses the root cause and removes the January tax entirely rather than softening it. Requires real upfront investment and is a 2–3 quarter initiative, not ready for this December. |

**Recommendation:** run A and C in parallel, not as alternatives — A is the immediate fix available for this turn of the calendar, C is what actually resolves the underlying tension between "quiet December" and "continuous engineering output." B isn't recommended standalone: high organizational cost for a result that's still batched. A short, voluntary pre-freeze slowdown (not a hard merge-freeze) is a reasonable minor addition to A if the validation check shows a real pre-freeze cram.

Independent of which approach you pick: fix the measurement blind spot that let this run three years unnoticed. It's the cheapest change here and the one most directly responsible for "nobody treats it as one pattern."

## The design

**Phase 0 — staged unfreeze protocol (this December).** Replace "everything ships the day the freeze lifts" with a runbook: order the backlog (by dependency, then risk); release in bounded batches close to a normal single-day deploy size, each with a bake period and a go/no-go checkpoint; canary each batch before full exposure; roll back the batch, not the quarter; staff the window like a launch — full on-call, not skeleton holiday coverage, since this is now the known highest-risk window of the year, not the quietest. Success bar: next January's incident count/severity for this window lands in line with a typical two-week stretch, not the annual outlier.

**Phase 1 — decouple merge from release (2027, 2–3 quarters).** Feature flags so merging no longer implies exposing behavior; canary + staged rollout as the default path year-round, not a freeze-season special case; then re-evaluate whether a full freeze is even needed, or whether it can narrow to just the genuinely high-risk change types (schema/data migrations, infra changes) while ordinary feature work keeps deploying safely through December.

**Parallel — fix the postmortem blind spot (immediate, cheap).** Add a contributing-factor field to incident reviews ("release size," "days of accumulated unreleased change," "post-freeze release: yes/no") alongside the proximate root cause, so the shared pattern is visible in the data even when every proximate bug differs. Add a lightweight quarterly (or at minimum pre-freeze annual) look-back across incidents, not just single-incident postmortems — this is the step that would have surfaced the pattern after year one instead of year three.

## Risks and honest costs

- Phase 0 trades speed for safety — the backlog takes longer to fully land than a same-day unfreeze. Intended, not incidental; say so to stakeholders used to a fast reopening.
- Phase 0 needs real on-call commitment for early January, which will be unpopular right after the holidays — weigh it against the outages already being paid for.
- Phase 1 is a genuine infrastructure investment that won't pay off before next December.
- If the validation step comes back negative, this design is solving the wrong problem and should be re-scoped around whatever the data actually shows.

## Scope

This bundles one immediate operational fix (Phase 0), one structural initiative (Phase 1), and one process fix (postmortem taxonomy) under a single diagnosis, presented as a phased roadmap rather than forced apart. Phase 1 is large enough to warrant its own implementation plan and owner once greenlit; Phase 0 and the postmortem fix are this design's immediate scope.

## Next steps

Not a software build, so there's no code implementation plan to hand off — the sequence is: (1) run the validation check against real incident history, a day or two of analysis, owner TBD (release/incident management is the natural fit); (2) if confirmed, write the Phase 0 runbook and lock in January on-call staffing before this year's freeze lifts, owner TBD (release engineering or the on-call lead); (3) add the contributing-factor field to the incident review template now, independent of everything else; (4) scope Phase 1 as its own initiative with its own owner once Phase 0 is running.
