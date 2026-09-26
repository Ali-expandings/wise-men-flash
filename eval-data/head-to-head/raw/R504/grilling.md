# arm: grilling (mattpocock/skills c55ee46073ed) | question: R504 | orchestrator: general-purpose/sonnet | run: 2026-09-25 (round 5, PREREG-5 rules)
# minutes: 6.0 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 4/35011/122176/39895 | list-price USD: 0.71

❓ **Q1** - **Revenue or margin as the basis?**: $180/month — is that gross revenue per customer, or gross margin? A CAC decision compares a cash outlay ($5,000) against cash value returned. Comparing CAC to gross *revenue* overstates the case by whatever it costs to deliver the product. Options: (a) treat $180 as revenue and apply a margin %, (b) treat it as already-margin, (c) get the real figure before deciding anything.

➡️ **Recommended:** (a), applying a representative margin since none was given, flagged as a placeholder for the real number.

✅ **Assumed:** $180 = gross revenue; apply 75% gross margin ⇒ ≈$135/month margin per customer.

---

❓ **Q2** - **Is 1.2% a logo churn rate?**: ARPU ÷ churn only yields a coherent per-customer dollar figure if churn is logo churn (% of customers lost/month), not revenue churn (net of expansion/contraction). Mixing the two breaks the math.

➡️ **Recommended:** treat it as logo churn — the only reading under which the original calculation is internally consistent.

✅ **Assumed:** 1.2% = logo/customer churn.

---

❓ **Q3** - **How far out can this be projected?**: 1/0.012 = 83.3 months of implied average lifetime — 6.9 years. The company is 3 years old; no customer has ever been observed past month 36. Months 37–83 (57% of the implied lifetime) describe behavior nobody has seen. Options: (a) cap the estimate at the observed 36 months, (b) extend to ~48 months as a labeled stretch case, (c) keep the full 83-month projection.

➡️ **Recommended:** (a) as the base case, (b) as an upside scenario, reject (c) — projecting past the edge of the data is the central defect in the $15,000 number.

✅ **Assumed:** base case capped at 36 months; stretch case at 48 months.

---

❓ **Q4** - **What discount rate for future cash?**: The naive formula treats a dollar 6+ years out as worth exactly a dollar today. No cost-of-capital figure was given.

➡️ **Recommended:** a standard small-company hurdle rate, 10–20% annualized, pending the real figure.

✅ **Assumed:** 15% annual, base case.

---

❓ **Q5** - **What does 1.2% actually represent, given the company's age?**: A 3-year-old, presumably still-growing company has a customer base skewed toward short-tenure accounts. Churn is rarely flat over a customer's life. The blended 1.2% mixes cohorts that haven't had a chance to prove anything with the few old enough to matter — and there's zero visibility into whether churn rises, falls, or holds past month 36. Options: (a) assume flat forever, (b) treat the shape beyond month 36 as genuinely unknown, (c) assume it worsens, (d) assume it improves.

➡️ **Recommended:** (b) — don't inject optimism or pessimism without data; this uncertainty is itself a reason to discount confidence in *any* number, including the corrected one.

✅ **Assumed:** no directional adjustment; carried forward as an unresolved risk that argues for staying conservative elsewhere in the model.

---

❓ **Q6** - **Point estimate or range?**: Four stacked assumptions (margin, discount rate, horizon, churn stability) make a single "corrected number" just a new false-precision trap.

➡️ **Recommended:** present low/base/high, not one figure.

✅ **Assumed:** range presentation.

---

❓ **Q7** - **What bar should gate the $5,000 decision?**: The standard SaaS heuristic is LTV:CAC ≥ 3:1. That alone ignores cash timing — a business can have good lifetime economics and still run out of runway waiting to get paid back. Options: (a) ratio only, (b) ratio + a payback-period ceiling (typically 12–18 months), (c) payback only.

➡️ **Recommended:** (b) — require both ≥3:1 on the conservative CLV and payback within ~12–18 months of gross margin.

✅ **Assumed:** gate = 3:1 ratio AND ≤18-month margin payback.

---

**Frontier empty for Round 1. Round 2 — depends on the assumptions above.**

❓ **Q8** - **Does $5,000 clear the bar on the honest number?**: Apply Q1–Q5 to the same formula the head of growth used.

➡️ **Recommended:** compute directly.
Revenue, capped at 36 months, undiscounted: $180 × Σ(0.988ᵗ, t=0..35) ≈ **$5,290**.
Apply 75% margin: ≈ **$3,965**.
Discount at 15%/yr: ≈ **$3,300** — base case.
Low case (24-mo cap, 65% margin, 20% discount): ≈ **$2,100**.
High case (48-mo cap, 80% margin, 10% discount): ≈ **$4,500**.
Honest range: **~$2,100–$4,500**, base **~$3,300** — a 70–86% haircut off $15,000.
At $5,000 CAC: ratio = 0.42:1 (low) to 0.90:1 (high), base 0.66:1 — under 1:1 even at the generous end, nowhere near 3:1. Payback = 35–43 months, base ~37 — double the 18-month gate.

✅ **Assumed:** No, $5,000 does not clear the bar in any scenario tested.

---

❓ **Q9** - **What CAC would the honest data support today?**: Solve for CAC at 3:1 against the range, cross-check against the payback ceiling.

➡️ **Recommended:** ratio-based ceiling: $700 (low) to $1,500 (high), base ≈ $1,100. Payback-based ceiling at 18 months: $2,100–$2,600. The ratio constraint is tighter in every scenario, so it governs.

✅ **Assumed:** defensible CAC ceiling today ≈ **$700–$1,500, centered near $1,100** — not $5,000.

---

❓ **Q10** - **When should this be revisited?**: The Q9 ceiling still rests on placeholder margin/discount figures and an unmeasured retention curve. Options: (a) calendar-based review, (b) data-triggered review.

➡️ **Recommended:** (b) — tie it to actual evidence, not a date.

✅ **Assumed:** revisit once (i) the oldest cohorts clear 48–60 months of real tenure, and (ii) actual gross-margin and cost-of-capital figures replace the 75%/15% placeholders used here.

---

**Frontier empty.**

## Final Recommendation

Trust the $15,000 very little. It isn't conservative-but-defensible — it's structurally broken, and the errors stack in the same direction:

1. **It extrapolates past the data.** ARPU ÷ churn implies an 83-month average customer lifetime on a company that has existed for 36. More than half that implied lifetime (57%) describes behavior no customer has ever lived through.
2. **It uses revenue, not margin,** against a cash cost. CAC should be compared to what a customer actually contributes after cost of delivery, not top-line revenue.
3. **It doesn't discount future cash to present value**, which matters over a multi-year projection.

Correcting for all three — capping the horizon at the actually-observed 36 months, applying a representative margin, discounting future cash — brings the honest figure down to roughly **$2,100–$4,500, centered around $3,300**: a 70–86% haircut off the original claim.

At that honest number, a $5,000 CAC isn't a healthy 3:1 bet — it's 0.4:1 to 0.9:1 depending on assumptions, meaning the company would likely spend as much or more to win a customer than that customer is worth. Cash payback would run 35–43 months, roughly double a normal SaaS payback ceiling.

**Do not raise the CAC ceiling to $5,000.** A defensible ceiling today is closer to **$700–$1,500 (≈$1,100 base case)**. Revisit once cohorts pass 48–60 months of real tenure and actual margin/discount figures replace the placeholders used here — the range should narrow at that point and could move in either direction, but nothing in the current data supports the $15,000 figure or the $5,000 spend it's being used to justify.

Two smaller simplifications remain even after this correction, both cutting toward more uncertainty rather than less: the model still assumes flat ARPU forever (no upsell or downgrade), and it still uses one blended churn number instead of a real cohort-by-cohort retention curve.
