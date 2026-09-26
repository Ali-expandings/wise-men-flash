# arm: direct (no skill) | question: R504 | orchestrator: general-purpose/sonnet | run: 2026-09-25 (round 5, PREREG-5 rules)
# minutes: 3.3 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/18256/43305/35284 | list-price USD: 0.42

**Short answer: don't build a spending decision on $15,000. The arithmetic is fine; the assumption underneath it isn't, and the gap is big enough to flip the decision.**

**The mechanical problem**

LTV = ARPU / churn is the constant-hazard shortcut: it assumes every customer, in every month of their relationship, carries the same 1.2% chance of leaving — forever. That math implies an average customer lifetime of 1/0.012 = 83 months (~6.9 years). The company is 36 months old. The formula is asserting behavior for years 4 through 7 of a customer relationship that has never once been observed — no customer exists yet who could confirm or contradict it.

**How much of the $15,000 is real vs. invented**

Split it at the 36-month mark, using their own churn rate: expected revenue collected in months 0–35 = 180 × [1 − 0.988³⁶] / 0.012 ≈ 180 × 29.4 ≈ **$5,290**. That's the slice of "lifetime value" that falls inside a window the business has actually been able to watch happen. The other **~$9,700 — roughly two-thirds of the claimed number** — is revenue the formula expects from month 37 onward, a period with zero observed customers. Whatever assumption drives that piece, it isn't evidence.

**Other things making it worse**

- *Revenue vs. margin*: $180 is revenue; CAC is a cash cost, so it belongs against gross profit, not revenue. Cost to serve a customer isn't zero. A generic 70% gross margin (swap in your real number) turns the naive $15,000 into $10,500, and the honest 36-month figure into ~$3,700.
- *Blended churn*: 1.2% is presumably measured across the whole active base at once — new signups and 34-month veterans together. If churn declines with tenure (the usual pattern), that blended number tells you little about what a 5-year-tenured customer's actual odds are, in either direction.
- *No discounting*: nothing here present-values months 40–83. Revenue in year 6 isn't worth what revenue in year 1 is.
- *Single point estimate*: presenting $15,000 as one clean number hides exactly the uncertainty that matters for this call.

**What a more honest estimate looks like**

- Build actual per-cohort survival curves — % of the month-1 signup cohort still active at month 2, 3…36; same for the month-12 cohort, etc. — instead of assuming one constant hazard rate. This is what the data can actually support.
- Report LTV capped at the observed window (36 months) as the defensible figure, and label anything past that as a scenario, not a fact: "$5,290 revenue / ~$3,700 margin-adjusted, observed; $15,000 only if post-36-month churn holds flat forever (unverified)."
- Switch the numerator to gross margin dollars, and discount if projecting years out.
- Cross-check with CAC payback period, which needs less extrapolation: at $5,000 CAC and ~70% margin, monthly margin per customer is $126, so payback ≈ 5,000/126 ≈ **40 months** — longer than the company has existed. You'd be betting a customer acquired today behaves like your best 3-year survivors, sustained past the point where any survivors exist to check against, just to break even.

Bottom line: raising CAC to $5,000 off the $15,000 figure spends real, sticky dollars against a number that's roughly two-thirds extrapolation beyond the company's own lifetime. Rebuild it off actual cohort curves and real gross margin. If 3:1 survives that, raise the target with confidence. If the honest number lands closer to 1:1, this is the wrong direction to move.
