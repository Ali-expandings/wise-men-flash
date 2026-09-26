# arm: llm-council (aiwithremy/claude-skills-llm-council 55ee36e89e0f) | question: R504 | orchestrator: general-purpose/sonnet | run: 2026-09-25 (round 5, PREREG-5 rules)
# minutes: 16.1 | subagent calls: 11 (transcripts matched: 11) | tokens in/out/cache-read/cache-write: 32/200522/758731/715933 | list-price USD: 5.92

## Council Verdict: The $15,000 LTV Estimate

### Where the Council Agrees

All five peer reviews, working independently, ranked the Executor and First Principles Thinker as the top two responses, and all five independently named the Expansionist as the council's biggest blind spot — five-for-five on both calls, with no coordination between reviewers. That level of agreement is worth leaning on.

Every advisor, including the Expansionist, agrees the $15,000 figure can't be trusted as calculated. Nobody defends flat 1.2% churn extending to month 83. The disagreement starts only after that point.

Four of five advisors — Outsider, Contrarian, Executor, First Principles Thinker — independently built a bounded estimate using only the 36 months actually observed, zero extrapolation past that point. Different methods, same neighborhood: $4,900 to $6,480, roughly a third of $15,000. The two most rigorous versions — Executor and First Principles Thinker, both survival-weighting revenue instead of assuming it flat ($180 × 0.988^t, summed across months 1–36) — independently converge on the identical number: ~$5,300. Two advisors reasoning separately landing on the same figure via the same formula is the strongest single data point this council produced.

LTV and CAC are also being compared on the wrong basis: LTV as calculated is revenue, CAC is cost. Without a gross-margin haircut, any ratio between them overstates real coverage by however many points separate the two.

There's also convergence on the fix: stop gating growth spend on an LTV:CAC multiple built on an unobservable tail, and gate on CAC payback period instead — computed entirely from data already in hand, re-run every quarter as real month-40 and month-50 cohorts start to exist.

### Where the Council Clashes

The one real fight: which direction the unobserved tail breaks. The Contrarian, Outsider, Executor, and First Principles Thinker all treat months 37–83 as unknown territory that should default to caution. The Expansionist argues the same absence of data cuts the other way: subscription churn curves typically decline with tenure, net revenue retention often runs above 100%, and a single blended ceiling risks starving the best segments of spend they could support.

Both sides are reasoning from the same gap in the data — that's what makes this a genuine clash, not a mistake on one side. Four advisors convert "we don't know" into "assume the worst until proven otherwise," because the company is three years old, cash-constrained, and errors compound as spend scales — an asymmetry the Expansionist never directly answers. The Expansionist converts the same uncertainty into "it might be better than it looks," and treats under-spending on strong segments as the costlier mistake. Every peer review scored that case weaker anyway — not because declining hazard curves and rising NRR are implausible in general, but because none of it is shown to be true here, and it arrives with no bounded number despite the question asking for one directly.

Secondary clash, lower stakes: how to build the bounded estimate. Undiscounted revenue over 36 months ($6,480, Outsider) versus a flat margin haircut ($4,900, Contrarian) versus true survival-weighting that accounts for in-window churn ($5,300, Executor/First Principles Thinker). The dollar gap is small but the rigor gap is real — the first two ignore that customers are already churning inside the observed window, so even the "conservative" numbers overstate slightly.

### Blind Spots the Council Caught

Four things no single advisor saw, that only showed up once the reviews were compared side by side.

**Compositional risk.** Raising the CAC ceiling doesn't just let the company spend more on the same customers — it changes who gets bought. A higher ceiling opens new channels and lower-intent segments. The 1.2% churn, bounded or not, was measured on customers already acquired; nothing says a customer bought at a new, higher CAC shares that churn profile. Three separate reviews flagged this independently.

**CAC got a free pass.** The council interrogated the $15,000 LTV hard and took the $5,000 CAC figure — and the $180 ARPU underneath the LTV — on faith. Nobody asked whether CAC is fully loaded, whether it stays at $5,000 once the company actually spends against a higher ceiling (CAC typically climbs as spend pushes into costlier channels), or whether $180 ARPU is itself clean.

**The Expansionist's method, not its instinct.** All five reviews named the Expansionist the biggest blind spot, and most for the identical reason: it attacks the flat-churn extrapolation in its opening line, then extrapolates its own preferred direction (improving retention, a $25,000 segment) on identical zero evidence. The underlying instinct — that segments likely vary a lot — is directionally reasonable. The problem is presenting a guess as a finding.

**Even $5,300 isn't pure observation.** It still assumes constant hazard within the 0–36 month window to build the curve — a smaller extrapolation than reaching for month 83, but not zero. Related and unresolved: whether the 1.2% is logo or revenue churn, whether the blended rate is skewed by a growing (and therefore younger-skewing) customer base, and no discount rate was actually applied despite two advisors naming the gap. The 25–36 month band — the exact part of the curve this decision hinges on — is also the smallest, noisiest cohort in the dataset.

### The Recommendation

Don't approve the $5,000 CAC ceiling. The number it's built on is wrong by roughly 3x, and roughly two-thirds of the claimed $15,000 comes from 47 months of customer behavior nobody at this company has ever observed.

The defensible LTV, built two independent ways by two different advisors, is approximately $5,300 in revenue terms over the observed 36-month window — before margin. Apply gross margin and it drops further. If a single number is needed today under the existing 3x framework, it's roughly $1,600–1,800, not $5,000. That's not a rounding difference from what growth is asking for — it's a different decision.

Better than patching the multiple: retire LTV:CAC as the gate entirely and switch to CAC payback period — cap spend at whatever pays back within 12–18 months on gross margin per customer. That threshold needs no assumption about years four through seven, uses only data the company already has, and can be recalculated every quarter as the book ages.

Keep the Expansionist's segmentation instinct — some segment probably does support a higher ceiling than the blended average. That's an argument for building segment-level survival curves before approving more spend anywhere, not for approving $5,000 blended today on the hope it's true. And since the person proposing the higher ceiling is also the person whose numbers improve if it's approved, have someone without that stake own the recalculation.

### The One Thing to Do First

Pull the cohort-by-signup-month data that already exists and split churn into three tenure buckets — months 1–12, 13–24, 25–36 — to see whether the hazard rate is flat, rising, or falling. Every one of the five peer reviews independently ranked this the single strongest move on the table: it's buildable this week from data already in the system, and it directly resolves the one real disagreement in the room — whether churn improves with tenure or the "assume the worst" default is what's actually happening in this business. Nothing else in this verdict should be acted on before that number exists.
