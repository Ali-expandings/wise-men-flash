# arm: warp-council (warpdotdev/common-skills 69b4753651ab; adapted as in PREREG-2) | question: R404 | orchestrator: general-purpose/sonnet | run: 2026-09-18 (round 4, PREREG-4 rules)
# minutes: 9.6 | subagent calls: 3 (transcripts matched: 3) | tokens in/out/cache-read/cache-write: 20/64510/183567/251425 | list-price USD: 2.03

**Council composition:** 3 members. The skill's preferred roster (strongest Claude + strongest GPT + an open-source model) isn't available in this harness — only Claude models are — so per the skill's own fallback rule this substituted the three distinct Claude tiers, giving the "no open-source model available" slot the deliberately adversarial role:
- Opus — quantitative rigor & statistical-validity reviewer
- Sonnet — procurement due-diligence & deal-structuring reviewer
- Haiku — contrarian sales-tactics red-team reviewer

## Recommendation

Put very little weight on the 30% itself — treat it as a best-case anecdote, not an estimate of what you'll get. All three reviewers converge on this independently: a single vendor-selected case study is close to zero evidence for your environment. Budget for something meaningfully lower than 30% (rough independent estimates landed at high-single-digits to mid-teens percent), and don't release meaningful-budget spend without independent verification and outcome-linked contract terms.

## Why

- **It's one cherry-picked data point, not a distribution.** Vendors publish their best result, not a representative one. If 30% were typical, they'd show the full spread across customers — median, percentile range, sample size — instead of one story. Leading with a single testimonial is itself informative, and not in their favor.
- **The featured customer isn't neutral.** Case-study subjects usually get co-marketing benefits, discounts, or a continuing vendor relationship, and have their own reason to want their purchase to look validated. Their number is as much a negotiated artifact as a measurement.
- **"30% reduction" is a soft metric that's easy to inflate without anyone lying.** Deflection counted as resolution, a conveniently bad baseline quarter, changed ticket categorization, concurrent changes at the case-study customer (new KB articles, staffing, pricing), seasonality, or a measurement window caught at the honeymoon-phase peak can all produce "30%" without the tool being the real cause. Nothing needs to be falsified for this number to be meaningless for you specifically.

## Tradeoffs and risks

- **Over-trusting risk:** sizing a budget-significant commitment off a number that may not transfer to your ticket mix, support maturity, or documentation quality — the tool's real ceiling is partly set by inputs (like your KB quality) the case study doesn't control for.
- **Over-discounting risk:** don't let skepticism become a reason to reject a possibly-good tool outright. The right response to weak evidence is to demand better evidence, not to walk away reflexively — though walking away is the right call specifically if the vendor won't produce that evidence (see Final call).
- **Validation is cheap relative to the bet:** independent estimates put this at tens of analyst-hours over a few weeks — small next to a "meaningful chunk of annual budget" and the switching cost of being wrong.
- **Where the reviewers differed (degree, not direction):** the statistics-focused review pegged a realistic expectation around 8–15%, explicitly flagged as judgment rather than a real benchmark; the red-team review defaulted to ~10%. Both are placeholders, not data — the real number for you is unknowable until you run the checks below, and both reviewers said so themselves.

## Final call

Before signing, get from the vendor — this is the "what would I need to see" answer:

1. **Aggregate outcome data across their customer base** — median and spread (e.g., 25th/75th percentile), sample size, not just the one case study. Evasiveness here is itself a signal.
2. **The methodology behind the 30% number** — exact definition of "ticket" and "reduction," the baseline window, what else changed at that customer during the measurement period.
3. **2–3 reference customers you pick** (not ones they hand you) matching your size, industry, and ticket mix — ask them directly what else changed that quarter, re-contact rates, and whether they'd buy again at full price.
4. **A time-boxed pilot (60–90 days)** on a defined segment, measured on your own ticket data and definitions, with an internal owner and a decision rule agreed in advance — not the vendor's dashboard.
5. **Outcome-linked contract terms** — tie a meaningful slice of contract value (reviewers suggested roughly 20–30%) to independently measured results, with a performance-based exit if the pilot doesn't clear your bar.

Do now: items 1–3 (cheap, fast, before you negotiate further). Do before signing anything budget-significant: item 4. Do as a condition of the contract itself: item 5. If the vendor resists the pilot or the outcome-linked terms, that resistance is itself the most decision-useful data point available — a vendor confident in a real 30% should have no problem being paid on it.

Confidence: high on the process (this is standard, low-cost diligence for a claim resting on one uncontrolled data point); low on any specific number for your environment until pilot data exists. The material unknown isn't the vendor's number — it's your own ticket mix, current deflection rate, and documentation quality, which will determine your actual outcome more than their headline figure does.
