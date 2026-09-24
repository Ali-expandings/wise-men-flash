# arm: llm-council (aiwithremy/claude-skills-llm-council 1162f272ab94) | question: R405 | orchestrator: general-purpose/sonnet | run: 2026-09-18 (round 4, PREREG-4 rules)
# minutes: 18.4 | subagent calls: 11 (transcripts matched: 11) | tokens in/out/cache-read/cache-write: 34/244128/732523/679091 | list-price USD: 6.43

## Council Verdict: Trusting a Natural Experiment for Policy

### Where the Council Agrees

**The "next best thing to an RCT" framing is a red flag, not a credential.** Contrarian, Outsider, and First Principles Thinker independently land on this: the phrase borrows legitimacy from a design it isn't, and evidence that actually holds up doesn't need to reach for that comparison. Treat the line itself as the first finding, not a reassurance.

**"Why did Region A change and Region B didn't" is the load-bearing question.** Contrarian and Outsider raise this independently as the crux, not a footnote. If A was picked for reasons connected to the outcome — budget pressure, a champion pushing for it, the problem already being worse there — then the "divergence" may just be who was already moving before the rule existed. Selection into treatment, not the treatment itself, may be doing all the work.

**Pre-treatment trends are the fastest, most decisive test, and it's checkable today.** Contrarian, Outsider, and Executor all converge on pulling multiple pre-treatment periods for both regions. If A was already diverging from B before the rule changed, the parallel-trends assumption the entire design rests on is dead, and everything downstream is moot.

**One metric out of an unstated number of candidates is a lottery ticket.** Contrarian, Outsider, and Executor all independently ask how many outcome metrics were being watched before this one moved. A single significant result, chosen after the fact from an unknown number of dashboards, isn't a signal.

**Nobody actually argues for an immediate, unconditional full rollout.** Contrarian and Executor say don't fund it yet. First Principles says it licenses a hypothesis, not a rollout. Even Expansionist — the council's most bullish voice — explicitly rejects "roll out everywhere now" as one of two bad options and proposes staggered waves instead. The credulous-vs-dismissive tension the question poses is sharper in the abstract than it is across these five actual answers; the real fight is over what structure should govern the next step, not whether to skip structure entirely.

### Where the Council Clashes

**Can more scrutiny ever make a two-region comparison trustworthy, or is it capped by design?** First Principles' claim is structural: Region A and B are one comparison, not a sample of comparisons. A comparison that passes every check — clean pre-trends, no concurrent shocks, no reverse causality — can still not be distinguished from "these two regions always diverge, rule or not." More diligence doesn't fix an N=2 sample; only independent replication across more region-pairs does. Contrarian and Executor build detailed checklists that implicitly treat "passes the checks" as sufficient grounds to trust the result. Both can't be right at once: either a sufficiently clean single comparison earns real confidence, or it structurally cannot regardless of cleanliness. This is the deepest fault line in the council.

**Does the cost of waiting outweigh the risk of being wrong?** Expansionist argues the council is underpricing delay — every month of caution is a month other regions go without a policy already showing a measurable effect — and proposes collapsing "validate" and "roll out" into one motion: staggered or randomized waves that generate the proof while capturing the benefit. Contrarian and First Principles operate from the opposite default: don't spend resources or capital until the diagnostic bar is cleared, because unwinding a scaled spurious result costs more than the delay does. This is only partly resolvable: Expansionist's fix earns the rigor it claims only if wave assignment is truly randomized, not staggered by administrative convenience — otherwise it just reproduces the original selection problem one region at a time.

**Does the vagueness of the setup itself count as evidence?** Outsider treats the abstraction — "Region A," "the rule," "an outcome metric" — as diagnostic on its own: a real evaluator needs the literal names to check real confounds, and staying this generic when real capital is at stake usually means the details a skeptic would want have already been smoothed over. The other four reason generically about diff-in-diff failure modes without treating the vagueness itself as a signal. Smaller than the first two clashes, but it changes the opening move — Outsider says demand specifics first; everyone else says demand statistics first.

### Blind Spots the Council Caught

**Expansionist's answer is a liability if anyone reads it alone.** Every peer review, independently, flagged the same problem: it assumes the divergence is real and causal ("take the win," "if the effect is even half of what's reported") and explicitly hands the validity question to the Contrarian — inside a brief that was specifically about assessing validity. That division of labor is fine inside a council. Read standalone, it's the exact over-credulous failure the original question warns against. Its actual ideas — pricing the cost of delay, upgrading the design via randomized waves, hunting for hidden heterogeneous effects — are worth keeping, but only after the checks, never in place of them.

**Nobody asked about mechanism.** No advisor asked whether there's a substantive, theory-based reason this specific rule should move this specific metric. A statistical pattern with a plausible causal story behind it is stronger evidence than the identical pattern with none — and it's a cheap question to ask before touching any data.

**Internal validity and transportability got conflated.** Every advisor argued about whether the effect is real in Region A. None asked whether an effect that's real in A would transport to the other regions slated for rollout, which may differ from A in exactly the preconditions the mechanism depends on.

**The evidence bar was never tied to what the decision actually costs.** Nobody weighed the effect size against the cost of the rollout, or asked whether the proposed rollout is cheap and reversible (lower bar defensible) versus expensive and sticky (higher bar required). A tiny effect, however cleanly identified, may not justify a costly rollout; a modest effect might justify a cheap, reversible one even with some doubt left standing.

**Existing statistical fixes for the small-N problem went unmentioned.** Contrarian and First Principles both name the N=1-treated-unit problem precisely, but nobody proposed the standard econometric answers already available: synthetic control or placebo-permutation methods (Abadie-style), which build a counterfactual Region A from many other regions' pre-period data instead of relying on Region B alone, or a quick plausibility check against outside literature on similar rules. Relatedly, nobody asked how many different specifications — not just how many outcome metrics — were tried before this particular comparison was the one shown. Specification-fishing is a distinct risk from metric-fishing and needs its own audit.

**Data integrity got only partial coverage.** No advisor raised: implementation fidelity (did the rule actually bite in Region A in practice, and did Region B stay uncontaminated rather than anticipating the change); measurement comparability (do A and B define and collect the outcome metric identically, so the "divergence" isn't partly a reporting artifact); and analyst independence (who ran this study — if it's the team seeking the rollout budget, that's a conflict-of-interest risk distinct from, and additive to, every statistical confound the council named).

### The Recommendation

Don't fund the broad rollout on this evidence, and don't dismiss it either — both are live failure modes here, and the honest answer isn't the midpoint between them, it's a specific, sequenced test.

This natural experiment has cleared the bar for "worth a rigorous look," not the bar for "worth a broad policy commitment." "Next best thing to an RCT" is doing rhetorical work the design hasn't earned — an RCT's power comes from randomizing across many units, and this has one unit per arm and no randomization. That doesn't make it worthless. It makes it a hypothesis with unusually good production values.

Before another dollar or unit of political capital moves, run the fast diagnostic set the council converged on, and treat any single failure as a stop condition, not a caveat to note and proceed past:

- Pre-trends across multiple periods for both regions
- The "why A not B" selection story, answered concretely
- A concurrent-event scan (what else changed in A at the same time)
- A spillover check (has activity or population moved between A and B)
- A multiplicity check (how many metrics, and how many specifications, were tried)
- A mechanism check (why this rule should plausibly move this metric)
- A measurement-comparability check (do A and B define and collect the metric the same way)

This is days of work against data that mostly already exists, not a new study.

If those checks come back clean, that still isn't license for a full rollout — it's license for the replication the design structurally lacks. Expand to additional regions in waves with genuinely randomized assignment, pre-registering the outcome metric and the kill threshold before anyone sees new data. That does two things at once: it answers the legitimate point that delay has a real cost, by not freezing the whole policy while you wait, and it answers the point that no amount of scrutiny of one pair of regions substitutes for more units, by actually producing more units. Calibrate how much replication you require to what you're committing to — a cheap, reversible next wave can proceed on thinner proof than a costly, organization-wide, hard-to-reverse policy change.

### The One Thing to Do First

Pull the outcome metric for both regions for the 12–24 months before the rule changed and put the two lines on one chart. It's the fastest, cheapest, most decisive test on the table — existing data, no interviews, no committee — and it's a genuine kill switch: if Region A was already diverging from Region B before the rule changed, the natural experiment is dead on arrival, and every other check on the list becomes irrelevant. Do this before scheduling any of the other diagnostics, and long before scheduling the rollout conversation.
