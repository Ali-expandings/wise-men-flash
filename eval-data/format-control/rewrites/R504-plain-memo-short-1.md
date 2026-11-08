# arm: plain-memo-short (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R504 | attempt: 1 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R504-plain-memo-short-rewrite-1.txt (sha256 c8824cb3c2b0593e)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: aef9d57ec19094d03 | transcript sha256: 20ae7b15f8005c078f59f5162b65b2c22894aa32af2d378c33471cb828085b47
# minutes: 0.2 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/1668/3185/13589 | list-price USD: 0.08

## Recommendation

Don't build a spending decision on $15,000. The arithmetic is fine, but the assumption underneath it isn't, and the gap is big enough to flip the decision. Raising CAC to $5,000 off the $15,000 figure spends real, sticky dollars against a number that is roughly two-thirds extrapolation beyond the company's own lifetime. Rebuild it off actual cohort curves and real gross margin. If 3:1 survives that, raise the target with confidence. If the honest number lands closer to 1:1, this is the wrong direction to move.

## Why

LTV = ARPU / churn is the constant-hazard shortcut. It assumes every customer, in every month of their relationship, carries the same 1.2% chance of leaving, forever. That implies an average customer lifetime of 1/0.012 = 83 months (~6.9 years). The company is 36 months old, so the formula asserts behavior for years 4 through 7 of a customer relationship that has never once been observed. No customer exists yet who could confirm or contradict it.

Split the figure at the 36-month mark, using the same churn rate. Expected revenue collected in months 0–35 is 180 × [1 − 0.988³⁶] / 0.012 ≈ 180 × 29.4 ≈ $5,290. That is the slice of "lifetime value" that falls inside a window the business has actually been able to watch happen. The other ~$9,700, roughly two-thirds of the claimed number, is revenue the formula expects from month 37 onward, a period with zero observed customers. Whatever assumption drives that piece, it isn't evidence.

Other problems make it worse:
- Revenue vs. margin: $180 is revenue, but CAC is a cash cost, so it belongs against gross profit, not revenue. Cost to serve a customer isn't zero. A generic 70% gross margin turns the naive $15,000 into $10,500, and the honest 36-month figure into ~$3,700.
- Blended churn: 1.2% is presumably measured across the whole active base at once, new signups and 34-month veterans together. If churn declines with tenure (the usual pattern), that blended number tells you little about a 5-year-tenured customer's actual odds, in either direction.
- No discounting: nothing here present-values months 40–83. Revenue in year 6 isn't worth what revenue in year 1 is.
- Single point estimate: presenting $15,000 as one clean number hides exactly the uncertainty that matters for this call.

## What to do

- Build actual per-cohort survival curves instead of assuming one constant hazard rate: the percentage of the month-1 signup cohort still active at month 2, 3 and on to 36, and the same for the month-12 cohort, and so on. This is what the data can actually support.
- Report LTV capped at the observed window (36 months) as the defensible figure, and label anything past that as a scenario, not a fact: "$5,290 revenue / ~$3,700 margin-adjusted, observed; $15,000 only if post-36-month churn holds flat forever (unverified)."
- Switch the numerator to gross margin dollars, and discount if projecting years out.
- Cross-check with CAC payback period, which needs less extrapolation. At $5,000 CAC and ~70% margin, monthly margin per customer is $126, so payback ≈ 5,000/126 ≈ 40 months. That is longer than the company has existed. You would be betting that a customer acquired today behaves like your best 3-year survivors, sustained past the point where any survivors exist to check against, just to break even.

## Risks of this plan

The 70% gross margin is a generic figure, and you should swap in your real number. The payback figure rests on that same ~70% margin. The 1.2% churn is presumably a blended rate, so it may mislead about long-tenured customers in either direction. Anything past the 36-month window remains a scenario, not a fact.

## Strongest counter-position

The source raises no objection to its own answer beyond one limit: the $15,000 holds only if post-36-month churn stays flat forever, which is the scenario it labels unverified. No case against this recommendation is made beyond the risks above.

## Confidence

- High: the formula assumes a constant 1.2% monthly chance of leaving, implying an 83-month (~6.9-year) lifetime, against a 36-month-old company.
- High: about $5,290 of the $15,000 falls in the observed window, and the other ~$9,700 comes from month 37 onward with no observed customers.
- High: CAC should be set against gross profit, not revenue.
- High: at $5,000 CAC and ~70% margin, payback is about 40 months.
- Medium: roughly two-thirds of the claimed number is extrapolation.
- Medium: churn usually declines with tenure, so blended churn tells you little about long-tenured customers.
- Low: the blended-churn description rests on a presumption ("presumably").

Unknowns: your real gross margin, what churn does after month 36, and how long-tenured customers actually behave.
