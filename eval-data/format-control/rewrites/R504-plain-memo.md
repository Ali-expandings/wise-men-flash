# arm: plain-memo (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R504 | attempt: 2 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R504-plain-memo-rewrite-2.txt (sha256 a9836012ac212997)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: a1006be5d6a3b54fb | transcript sha256: 496cd119b261cdd70c6fa59e00fb50fc071af3201a4083acdb581620bdcfd121
# minutes: 0.3 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/3558/3185/17033 | list-price USD: 0.12
# final: attempt 2 with 1 sentence(s) deleted under PREREG-6 Part A rule 3 (R57); 0 source sentence(s) cited nowhere, disclosed in audits/R504-plain-memo-final.yaml

## Recommendation

Do not build a spending decision on the $15,000 lifetime value figure. The arithmetic in it is fine, but the assumption underneath it is not, and the gap between what the formula claims and what the business has actually observed is big enough to flip the decision.

Raising the acquisition target to $5,000 off the $15,000 figure would spend real, sticky dollars against a number that is roughly two-thirds extrapolation beyond the company's own lifetime. The better course is to rebuild the estimate from actual cohort curves and real gross margin. If a 3:1 ratio survives that rebuild, you can raise the target with confidence. If the honest number lands closer to 1:1, raising the target is the wrong direction to move.

## Why

The formula is a constant-hazard shortcut. LTV = ARPU / churn assumes that every customer, in every month of their relationship, carries the same 1.2% chance of leaving, forever. That math implies an average customer lifetime of 1/0.012 = 83 months, or about 6.9 years. The company is 36 months old. So the formula asserts behavior for years 4 through 7 of a customer relationship that has never once been observed. No customer exists yet who could confirm or contradict it.

Most of the $15,000 is therefore invented rather than real. Split it at the 36-month mark, using the company's own churn rate. Expected revenue collected in months 0 to 35 is 180 × [1 − 0.988³⁶] / 0.012, which is about 180 × 29.4, or roughly $5,290. That is the slice of "lifetime value" that falls inside a window the business has actually been able to watch happen. The other roughly $9,700, which is about two-thirds of the claimed number, is revenue the formula expects from month 37 onward, a period with zero observed customers. Whatever assumption drives that piece, it is not evidence.

Several other things make the figure worse.

- Revenue versus margin: $180 is revenue, but acquisition cost is a cash cost, so it belongs against gross profit rather than revenue. The cost to serve a customer is not zero. A generic 70% gross margin (swap in your real number) turns the naive $15,000 into $10,500, and the honest 36-month figure into about $3,700.

- Blended churn: the 1.2% is presumably measured across the whole active base at once, with new signups and 34-month veterans together. If churn declines with tenure, which is the usual pattern, that blended number tells you little about what a five-year-tenured customer's actual odds are, in either direction.

- No discounting: nothing in the calculation present-values months 40 to 83. Revenue in year 6 is not worth what revenue in year 1 is.

- Single point estimate: presenting $15,000 as one clean number hides exactly the uncertainty that matters for this call.

The payback cross-check points the same way. At a $5,000 acquisition cost and roughly 70% margin, monthly margin per customer is $126, so payback is about 5,000/126, or roughly 40 months. That is longer than the company has existed. You would be betting that a customer acquired today behaves like your best three-year survivors, sustained past the point where any survivors exist to check against, just to break even.

## What to do

First, build actual per-cohort survival curves instead of assuming one constant hazard rate. That means the percentage of the month-1 signup cohort still active at month 2, 3, and on through 36, and the same for the month-12 cohort, and so on. This is what the data can actually support.

Second, report lifetime value capped at the observed window of 36 months as the defensible figure, and label anything past that as a scenario, not a fact. The wording could read: "$5,290 revenue / ~$3,700 margin-adjusted, observed; $15,000 only if post-36-month churn holds flat forever (unverified)."

Third, switch the numerator to gross margin dollars, and discount if you are projecting years out. Use your real gross margin in place of the generic 70% figure.

Fourth, cross-check with the payback period on acquisition cost, which needs less extrapolation. At $5,000 and roughly 70% margin, monthly margin per customer is $126, so payback is about 40 months, longer than the company has existed.

Finally, once the cohort-based, margin-based figure exists, compare it with the acquisition target. If 3:1 survives, raise the target with confidence. If the honest number lands closer to 1:1, do not raise it.

## Risks of this plan

The risks here are mostly those of acting on the existing figure, and the caveats the source attaches to its own numbers.

The main risk is spending real, sticky dollars against a number that is roughly two-thirds extrapolation beyond the company's own lifetime. Whatever assumption drives the portion past month 36, it is not evidence.

The 70% gross margin used in the adjusted figures is a generic assumption. You should swap in your real number, so the $10,500, the $3,700 and the $126 monthly margin, and therefore the 40-month payback, all depend on a placeholder rather than a measured margin.

The 1.2% churn rate is presumably a blended measure across new signups and long-tenured customers together. If churn declines with tenure, which is the usual pattern, that blended figure tells you little about what a five-year-tenured customer's actual odds are, in either direction.

The calculation is also not discounted, so later revenue is overstated relative to early revenue, and presenting a single point estimate hides the uncertainty that matters for this decision.

Finally, the $15,000 figure holds only if churn after month 36 holds flat forever, which is unverified. Betting on it means betting that a customer acquired today behaves like your best three-year survivors, past the point where any survivors exist to check against, just to break even.

## Strongest counter-position

The source makes no case that $15,000 is right. The nearest thing to a limit on its own answer is the conditional it states: the $15,000 figure holds only if post-36-month churn stays flat forever, and that is unverified. The source also says that if 3:1 survives the rebuild from actual cohort curves and real gross margin, you can raise the target with confidence.

The source's point is that the number tells you little, not that it is necessarily too optimistic or too pessimistic.

The source's own caveat on its numbers is that the 70% margin is generic and should be replaced with your real number.

## Confidence

Claims stated without a hedge are High.

- High: LTV = ARPU / churn assumes the same 1.2% chance of leaving in every month, forever.

- High: That math implies an average customer lifetime of 83 months, about 6.9 years, against a company that is 36 months old.

- High: No customer exists yet who could confirm or contradict behavior in years 4 through 7.

- High: Expected revenue in months 0 to 35 is about $5,290, and the remainder, about $9,700, which is roughly two-thirds of the claimed number, falls from month 37 onward, a period with zero observed customers.

- High: Acquisition cost is a cash cost and belongs against gross profit, not revenue, and the cost to serve a customer is not zero.

- High: A generic 70% gross margin turns the naive $15,000 into $10,500 and the honest 36-month figure into about $3,700.

- High: Nothing in the calculation present-values months 40 to 83.

- High: Presenting a single clean number hides the uncertainty that matters for this call.

- High: Per-cohort survival curves are what the data can actually support.

- High: At a $5,000 acquisition cost and roughly 70% margin, monthly margin is $126 and payback is about 40 months, longer than the company has existed.

Claims stated with a hedge:

- Medium: The 1.2% churn rate is presumably measured across the whole active base at once.

- Medium: Churn declining with tenure is the usual pattern.

Unknowns the source names:

- Whether churn after month 36 holds flat forever, which is unverified.

- Your real gross margin, which replaces the generic 70%.

- What a five-year-tenured customer's actual odds of leaving are, in either direction.

- Whether the honest number lands at 3:1 or closer to 1:1 once rebuilt from cohort curves and real gross margin.
