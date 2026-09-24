# arm: warp-council (warpdotdev/common-skills 69b4753651ab; adapted as in PREREG-2) | question: R405 | orchestrator: general-purpose/sonnet | run: 2026-09-18 (round 4, PREREG-4 rules)
# minutes: 7.0 | subagent calls: 3 (transcripts matched: 3) | tokens in/out/cache-read/cache-write: 20/48441/183707/259012 | list-price USD: 1.85

## Council

Model-diverse routing wasn't available (this harness exposes only Claude opus/sonnet/haiku — no GPT/Codex, no open-source model), so per the skill's own fallback rule this used perspective-diversity across Claude's three tiers instead of cross-vendor diversity:

- **Methodology lead — Opus**: what the design formally is, its identifying assumption, what randomization buys that this doesn't.
- **Contrarian / red-team — Sonnet** (strongest remaining model, assigned the deliberately adversarial angle per the skill's substitution rule): argue against taking the evidence at face value; institutional/motivated-sourcing angle.
- **Practitioner checklist — Haiku**: concrete, enumerable due-diligence list to run in the room.

All three ran read-only, closed-book (no file/web access), independently, in parallel.

## Recommendation

Take it seriously enough to fund a real follow-up or a reversible pilot — not seriously enough to greenlight the policy change on its own. This design (a two-region before/after comparison) is genuinely stronger than a correlation, but it is not on a smooth continuum with an RCT — "next best thing" describes a hope, not a guarantee, and whether it's earned depends entirely on facts about the comparison that the pitch, as described, doesn't yet establish.

## Why

- **All three reviewers converge on the same root failure mode**: the region didn't get the rule change at random. Something made it change there and not elsewhere — often the very trend leadership is now crediting the policy for (the "Ashenfelter dip": rules get changed *because* a metric was already moving, then mean-reversion mimics a treatment effect). This is the one question that matters most and it's causal-inference-101, not a statistical nicety: *why that region, why then* — and it can't be answered by more data from the same two regions, only by knowing the actual decision process behind the rule change.
- **The comparison itself is unusually fragile with N=1 treated unit.** Any confidence interval or p-value being presented is almost certainly borrowed from individual-level rows, not from a valid sampling distribution over regions — with one treated unit there effectively isn't one. Any coincident event in that region (leadership change, a second reform, a local shock, even a change in how the outcome gets measured) is perfectly confounded with "the rule" and cannot be separated from it by this design.
- **The pitch is being made by an interested party, which is itself evidence.** Independent of the statistics, a team that already wants a decision and reaches for "next best thing to an RCT" unprompted is doing rhetorical work — borrowing randomization's credibility without its properties. That doesn't make the finding wrong, but it means the specific comparison region, window, and outcome definition were very likely chosen after the divergence was already visible (researcher-degrees-of-freedom / cherry-picking), which the pitch as described gives no way to rule out.

## Tradeoffs and risks

- **What's missing is checkable, not theoretical** — ask to see, before this moves anything: (1) a multi-period pre-trend chart for both regions (do they move in parallel *before* the rule changes, not just look similar in a snapshot); (2) a placebo test with a fake treatment date — a real effect should not show up there; (3) the actual reason the rule changed in that region and not the other, and whether it was a response to the metric in question; (4) whether other comparison regions/windows were tried and discarded; (5) whether anything else changed in that region at the same time; (6) whether both regions measure the outcome the same way. Absence of the pre-trend chart and the "why that region" answer are the two disqualifying gaps — everything else is secondary.
- **Where the three reviewers genuinely split is calibration, not substance**: the methodology lead is willing to give this real evidentiary weight (roughly a 2–4x update on a prior, rising toward 5–10x) *if* the checks above come back clean — treating it as a legitimate, if fragile, tool. The red-team reviewer defaults much lower given the internal, motivated-advocate context specifically, discounting toward "near zero until the analysis is opened up" as the starting posture rather than the fallback. Practically: if the policy is cheap and reversible, the red-team's stinginess costs little, so lean that way by default; if the checks come back genuinely clean, the methodology lead's higher weight is earned, not assumed.
- **Spillover risk compounds the uncertainty in a way that matters for THIS decision specifically**: if people, customers, or activity can move between the two regions, the "control" is partly contaminated and the measured gap may reflect displacement rather than net effect — meaning even a clean-looking result may not generalize to a full rollout where there's no longer an untreated region to displace into or out of.

## Final call

Don't approve or reject the policy off this evidence alone. Send it back with a short, specific list: the pre-trend chart, a placebo test, the actual reason that region moved first, and a plain answer on whether other region/window comparisons were tried and dropped. If the answers hold up, treat the result as a solid reason to run a proper staged or randomized rollout — not as a substitute for one. If the "why that region" question comes back as "it was already struggling" or "leadership was already pushing this," downgrade the evidence to near-zero regardless of how clean the chart looks.
