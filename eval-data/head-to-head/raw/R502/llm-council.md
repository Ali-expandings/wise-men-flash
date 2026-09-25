# arm: llm-council (aiwithremy/claude-skills-llm-council 55ee36e89e0f) | question: R502 | orchestrator: general-purpose/sonnet | run: 2026-09-25 (round 5, PREREG-5 rules)
# minutes: 15.3 | subagent calls: 11 (transcripts matched: 11) | tokens in/out/cache-read/cache-write: 32/203979/849818/625381 | list-price USD: 5.66

## Council Verdict: Deploy Freeze vs. the January Outage Pattern

### Where the Council Agrees
All five advisors independently land on the same mechanism, from five different angles — systems thinking, first-principles, contrarian skepticism, naive outside view, operational experience. The freeze stops deploys, not merges. Code keeps accumulating on mainline for two weeks, then ships as one giant, mutually-untested batch the moment the freeze lifts. Batch size — not any specific bug — is the constant across all three Januaries. That's why every postmortem names a different root cause: with hundreds of interacting changes landing at once, which one trips first is close to random, but something tripping is close to certain. The Contrarian adds the sharpest version of this: large batches also kill clean rollback, since you can't bisect one bad commit out of hundreds tangled together.

Lower January traffic is treated by all five as a non-factor, not counter-evidence. The Executor states it outright: the failure mode was never load, it's blast radius and diagnosis time.

Four of five advisors — Contrarian, First Principles, Outsider, Executor — explicitly reach a net-harmful verdict. The freeze doesn't remove risk, it warehouses and concentrates it, then releases it onto the team at its weakest point of the year: back from leave, cold on the code, thin on-call.

Two structural fixes recur across advisors despite different framing: don't leave deploy and merge decoupled with no bound on the backlog, and fix the postmortem template itself, since bug-level root-cause analysis is structurally blind to a pattern that lives one level above the bug. The Executor's "days of code queued at deploy time" field and the Outsider's "check the calendar" prompt are the same fix in different words.

### Where the Council Clashes
**Verify first, or act now?** The Contrarian alone asks whether the named January root causes have actually been confirmed to trace to freeze-window commits — the big-bang story is circumstantial, and it only takes one of three years pointing somewhere unrelated (fiscal-year jobs, cert expiry, cron) to break it. The Executor takes the opposite stance outright: "none of this needs a study." In peer review, the Executor's response was rated strongest by three of five reviewers for turning the diagnosis into an executable plan; the Contrarian's was rated strongest by two of five specifically for that epistemic discipline. Both instincts are reasonable — rigor-first risks stalling on a failure that recurs every December regardless; urgency-first risks rewriting policy on a theory nobody checked against the org's own data.

**Keep shipping through December, or stop touching it entirely?** First Principles and the Expansionist want deploy and merge fully decoupled — dark-ship everything behind flags all December, keep deploying continuously, redefine "freeze" as "no flag-flips." The Executor's fix runs the opposite direction: freeze mainline merges too, or cut a release branch and stop feeding it, rather than asking anyone to actively deploy through the exact window the freeze exists to protect. Peer review caught the problem with the flags approach: nobody checked whether flag-flips against a skeleton holiday crew just relocates the same risk under a different name.

**Why did the pattern stay invisible for three years?** The Outsider calls it a naive template gap — the retro process has no field for "has this happened before." The Contrarian calls it structural — naming the freeze as cause indicts whoever mandated it, so postmortems steer away from it. Two reviewers each preferred the Contrarian's account as sharper. The two explanations imply different fixes: a template field solves the naive-gap version and does nothing for the political version, where the field can exist and still get filled out to avoid the uncomfortable answer.

### Blind Spots the Council Caught
Two gaps surfaced only through cross-reading the reviews, each independently flagged by four of five reviewers — stronger consensus than anything achieved advisor-side:

1. **Nobody proposed checking the org's own data before prescribing a fix.** Pull commit/deploy counts and batch sizes from the three actual postmortems, correlate with incident severity, and check whether incidents cluster in the days right after each unfreeze, as the mechanism predicts, versus spreading evenly through January. Every advisor built a policy recommendation on a theory that a short data pull would confirm or break.

2. **Nobody asked why the freeze exists.** All five advisors treat it as pure engineering error. It may exist for reasons outside engineering's control — thin holiday on-call, compliance, customer commitments — and that cuts two ways: it constrains which fixes are viable, and it means the "ship continuously behind flags through December" camp may be proposing to relocate the exact risk, a skeleton crew getting paged, that the freeze was built to prevent. Unexamined, the council's own fix repeats the org's mistake in miniature.

A third finding stands out for being unanimous: all five reviewers, independently, flagged the Expansionist as the one response that never delivers a verdict — reframing three years of worst-of-year outages as a "free diagnostic" and a competitive-advantage pitch instead of answering net-harmful-or-not. Nothing else in this exercise hit 5/5 agreement. Read alone, that optimism might pass as framing; only the cross-review exposed it as non-responsive to the brief.

### The Recommendation
Net-harmful. The freeze does not reduce risk — it converts steady, attributable, small-batch deploy risk into a once-a-year concentrated batch that detonates on the least-equipped crew of the year. Three years of an identically-shaped incident, on a fixed calendar date, is not three unrelated bugs. It's one mechanism with a random seed.

The fix is not "cancel the freeze" — that answers a batch-size problem with a calendar move. The actual defect is that deploy and merge got decoupled with no bound on the resulting backlog and no metering on the release valve when it reopens. Fix that specifically.

Adopt the Executor's plan as the backbone — the most operationally complete, and peer review's clear preference. Stop unbounded backlog growth during the freeze: freeze mainline merges too, or cut a release branch and stop feeding it. Meter the unfreeze itself: cap post-freeze deploys at N commits, with canary and bake time — no big-bang release on day one back. Add "days of code queued at deploy time" as a mandatory postmortem field, paired with the Outsider's "check the calendar" prompt, so the pattern surfaces after year one next time, not year three.

Run the Contrarian's verification in parallel, not as a gate. It's cheap, it uses data the org already has, and it's what turns this from an outside council's plausible theory into a fact the org's own engineers will act on. The bounded-backlog fix carries no downside even if the audit turns up a partial exception in one of the three years, so there's no reason to sequence one behind the other.

Treat First Principles' and the Expansionist's flag-driven, fully-continuous-deployment model as the right long-term target, not the immediate move. It's a bigger lift, it assumes flag and dark-launch discipline the facts don't confirm is in place, and it risks relocating the holiday-staffing risk the freeze exists to manage. Greenlight it once the org has actually confirmed why the freeze exists and whether small continuous changes are safe to make during it.

### The One Thing to Do First
Before writing a single new policy line, pull the three January postmortems together with the commit and deploy logs from each freeze-unlock, and check batch size against incident severity, and incident timing against days-since-unfreeze. That's the test four of five reviewers noticed nobody ran. It's fast, it uses data already on hand, it closes the one real epistemic gap in the council's diagnosis, and it's what turns this from a consultant's theory into a chart the org's own engineers can't argue with. Everything else on this list follows it, not precedes it.
