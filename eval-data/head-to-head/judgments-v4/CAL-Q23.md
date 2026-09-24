# calibration of judge-prompt-5 (PREREG-4): round 3's Q23 answers under the error-first instructions | fresh opus subagent, Read-only | run: 2026-09-18
# slots as round 3's Q23 judge 2: A warp-council, B direct, C wise-men-3.11, D llm-council. Round 3's three judges gave C correctness 5, 5, 5.

I read the file and graded it as specified.

## PASS 0 — Errors

**Response A**
- Treats "effect loses significance in a published-only subset" as "the single strongest sign" of bias — conflates genuine bias with the mechanical power loss from halving the study count; overstated (its later check #3, comparing effect sizes by publication status, is the defensible version).
- Calls a fail-safe N "close to self-contradictory" inside a gray-lit review — a gray search doesn't guarantee the file drawer was emptied, so fail-safe N is independently a poor tool but not contradictory here; overstated.
- "literally what Cochrane/PRISMA recommend" — PRISMA is a reporting guideline (it governs reporting of sources searched), not a conduct recommendation to search gray literature; minor mischaracterization.

**Response B**
- "Cochrane and PRISMA both mandate searching gray literature" — PRISMA mandates *reporting* what was searched, not searching gray literature; Cochrane recommends it (highly desirable in MECIR) rather than mandating it. Overstated on both.
- "the one filter that catches coding mistakes, selective outcome reporting, and shaky stats" — overstates peer review's demonstrated ability to catch any of these three.
- Its sensitivity-analysis item ("published-only subset vs. full pool — same conclusion either way?") carries the same power-loss conflation, though stated more weakly than A's.

**Response C**
- "it's decisive in both directions" / "resolves most of the uncertainty" about the published-only check — overstated, and internally contradicted by C's own later point that retrospective registration or outcome-switching means "the published-only comparison and every other check above can be gamed"; C also never raises the power-loss confound.
- "Most competent meta-analyses in this situation report one [published-only subgroup comparison]" — unsupported empirical claim, and optimistic.
- The repeated "unverified — the specific studies behind this pattern were not confirmed here" markers describe the responder's own process, not the state of the evidence; both hedged claims (grey lit yields smaller effects; meta-analyses run larger than preregistered replications) are in fact well documented, so the hedge miscalibrates downward.

**Response D**
- Asserts that the gray literature was obtained by "contacting authors directly," calls direct-author-solicitation "the actual mechanism here," and states the analysis has "no pre-registration" — none of this is in the question, and the central verdict is built on these invented case facts. Material.
- "Four independent arrivals at the same check is the strongest signal from this exercise," plus the reviewer-vote framing ("every peer reviewer independently rated [it] weakest") — treats agreement among correlated advisors as evidence about the world, and settles a substantive dispute partly by vote count.
- "independent teams doing honest gray-literature searches on the same question are documented to surface substantially different, barely-overlapping study sets" — asserted as documented with no basis given; plausible but overstated as phrased.

## PASS 1 — Ranking

1. **B** — Correct top-line calibration, the broadest accurate failure-mode list per unit of reader attention, a checkable citation (McAuley 2000) where others hedge, and one genuinely sharp point nobody else makes (a gray-lit search *added* after the published-only result looked weak is p-hacking at the meta-analysis level); no process noise, no invented facts.
2. **A** — Nearly the same calibration with the best statistical mechanics in the set (random-effects weighting amplifying small-study effects, trim-and-fill correcting in the wrong direction, DL vs Hartung-Knapp, "unclear" risk-of-bias silently coded as neutral) and a clean ordered triage, but it opens with a block of harness/model-tier narration that is worthless to the reader.
3. **C** — The most complete and most honestly calibrated treatment of failure modes (no enumerable sampling frame, solicitation asymmetry, leave-one-lab-out clustering, field-dependent reversal) with the only explicit falsifiable counter-position, but it is repetitive, template-heavy, and its self-referential "unverified" hedges dilute claims that are actually well established.
4. **D** — Carries the single most valuable correction in the whole set (a significance flip in the published-only half confounds power loss with bias; compare effect sizes side by side instead) plus double-counting and the inverse-variance-weights-reward-precision-not-quality point, but roughly 40% of it is council theater about who agreed with whom, and its central diagnosis rests on retrieval details and a missing pre-registration that the question never stated.

## PASS 2 — Absolute

```scores
response: A
correctness: 4
insight: 4
practical: 4
risk: 4
dissent: 3
```
Correctness 4: no material error, but the "loses significance = strongest sign" and fail-safe-N claims are overstated. Insight 4: random-effects amplifying small-study effects and trim-and-fill reversing direction are real, non-obvious mechanics. Practical 4: excellent ordered triage with stop conditions, docked for the irrelevant process preamble. Risk 4: grouped failure modes covering duplication, unassessable quality, and buried supplement caveats, but misses the power confound and solicitation asymmetry. Dissent 3: notes a contrarian angle existed and flags confidence limits, but never presents a serious counter-argument to its own recommendation.

```scores
response: B
correctness: 4
insight: 4
practical: 5
risk: 4
dissent: 3
```
Correctness 4: the "Cochrane and PRISMA both mandate" and peer-review-as-filter claims are overstated, though nothing changes what the reader should do. Insight 4: the post-hoc-gray-search-as-meta-level-p-hacking point and the funnel-asymmetry/small-study-effects confound are both sharp and rarely stated. Practical 5: every item is checkable in the paper, correctly scoped, with a named-tool checklist and no wasted motion. Risk 4: covers ad hoc retrieval, imputation degrees of freedom, selectively released industry gray lit, and heterogeneity/prediction intervals, but misses double-counting and quality-blind weighting. Dissent 3: it argues against its own reassuring stance ("unless the gray lit was itself selectively released") but offers no explicit strongest counter-position.

```scores
response: C
correctness: 4
insight: 5
practical: 4
risk: 5
dissent: 5
```
Correctness 4: "decisive in both directions" is overstated and sits in tension with its own point that the check can be gamed by outcome-switching. Insight 5: the no-enumerable-sampling-frame framing, solicitation asymmetry, leave-one-lab-out, and field-dependent reversal are the deepest set on offer. Practical 4: correct priority order with realistic time budgets and a good "if they won't send the per-study table, that refusal is the answer" test, but buried in repetition. Risk 5: a dedicated, comprehensive failure-mode section plus material unknowns ranked by how much they'd move the answer. Dissent 5: an explicit strongest-counter-position with a stated condition that would show it wrong.

```scores
response: D
correctness: 3
insight: 4
practical: 3
risk: 4
dissent: 5
```
Correctness 3: capped by the material error of inventing the retrieval channel and the absence of pre-registration and then resting its verdict on them, compounded by treating advisor convergence as evidential weight. Insight 4: the power-loss confound in the published-only check and inverse-variance weighting rewarding precision rather than quality are the sharpest individual catches in the set, but much of the space goes to process rather than content. Practical 3: one very well-specified first action, surrounded by material the reader cannot use and a framing that may misdescribe their paper. Risk 4: catches double-counting and turns the critique on its own headline check, but omits heterogeneity entirely and never questions its own assumed retrieval mechanism. Dissent 5: stages the real clash, steelmans the opposing position fairly, and then undermines its own recommended test.
