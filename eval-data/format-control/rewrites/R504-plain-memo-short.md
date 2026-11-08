# arm: plain-memo-short (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R504 | attempt: 2 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R504-plain-memo-short-rewrite-2.txt (sha256 c83c020f79d89d9c)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: a97e5903cb3b15854 | transcript sha256: 3a006b662791996fc796b842606b7e8a575385ad541d78fa7846c90de113dc73
# minutes: 0.4 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/3681/3185/15887 | list-price USD: 0.12
# final: attempt 2; it passed the audit but still fails the script check(s) words after the one retry, which PREREG-6 gives no rule for (see DEVIATIONS.md)

## Recommendation

Don't build a spending decision on $15,000. The arithmetic is fine; the assumption underneath it isn't, and the gap is big enough to flip the decision. Raising CAC to $5,000 off the $15,000 figure spends real, sticky dollars against a number that's roughly two-thirds extrapolation beyond the company's own lifetime. Rebuild it off actual cohort curves and real gross margin. If 3:1 survives that, raise the target with confidence. If the honest number lands closer to 1:1, this is the wrong direction to move.

## Why

LTV = ARPU / churn is the constant-hazard shortcut: it assumes every customer, in every month of their relationship, carries the same 1.2% chance of leaving, forever. That implies an average customer lifetime of 1/0.012 = 83 months (~6.9 years). The company is 36 months old. The formula asserts behavior for years 4 through 7 of a customer relationship that has never once been observed. No customer exists yet who could confirm or contradict it.

Split it at the 36-month mark, using their own churn rate. Expected revenue collected in months 0–35 is 180 × [1 − 0.988³⁶] / 0.012 ≈ 180 × 29.4 ≈ $5,290. That is the slice of "lifetime value" that falls inside a window the business has actually been able to watch happen. The other ~$9,700, roughly two-thirds of the claimed number, is revenue the formula expects from month 37 onward, a period with zero observed customers. Whatever assumption drives that piece, it isn't evidence.

Other things make it worse:
- Revenue vs. margin: $180 is revenue; CAC is a cash cost, so it belongs against gross profit, not revenue. Cost to serve a customer isn't zero. A generic 70% gross margin (swap in your real number) turns the naive $15,000 into $10,500, and the honest 36-month figure into ~$3,700.
- Blended churn: 1.2% is presumably measured across the whole active base at once, new signups and 34-month veterans together. If churn declines with tenure (the usual pattern), that blended number tells you little about what a 5-year-tenured customer's actual odds are, in either direction.
- No discounting: nothing here present-values months 40–83. Revenue in year 6 isn't worth what revenue in year 1 is.
- Single point estimate: presenting $15,000 as one clean number hides exactly the uncertainty that matters for this call.

## What to do

- Build actual per-cohort survival curves instead of assuming one constant hazard rate: the percentage of the month-1 signup cohort still active at month 2, 3 and on to 36, and the same for the month-12 cohort, and so on. This is what the data can actually support.
- Report LTV capped at the observed window (36 months) as the defensible figure, and label anything past that as a scenario, not a fact: "$5,290 revenue / ~$3,700 margin-adjusted, observed; $15,000 only if post-36-month churn holds flat forever (unverified)."
- Switch the numerator to gross margin dollars, and discount if projecting years out.
- Cross-check with CAC payback period, which needs less extrapolation: at $5,000 CAC and ~70% margin, monthly margin per customer is $126, so payback ≈ 5,000/126 ≈ 40 months, longer than the company has existed. You'd be betting a customer acquired today behaves like your best 3-year survivors, sustained past the point where any survivors exist to check against, just to break even.

## Risks of this plan

The 70% gross margin is generic, and the payback figure rests on the same ~70%, so swap in your real number. Anything past the 36-month window stays a scenario rather than a fact.

## Strongest counter-position

No case against this recommendation is made beyond the risks above.

## Confidence

- High: the constant 1.2% hazard implies an 83-month lifetime, against a 36-month-old company.
- High: about $5,290 falls in the observed window; the other ~$9,700, roughly two-thirds of the claimed number, comes from month 37 onward.
- High: CAC belongs against gross profit, and payback is about 40 months at $5,000 CAC and ~70% margin.
- Medium: the 1.2% is presumably a blended rate across the whole active base.

Unknowns: your real gross margin, and whether churn after month 36 holds flat, since no customer has been observed there.
