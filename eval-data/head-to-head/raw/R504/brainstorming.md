# arm: brainstorming (obra/superpowers 5bf4e7801107, with visual-companion.md and spec-document-reviewer-prompt.md) | question: R504 | orchestrator: general-purpose/sonnet | run: 2026-09-25 (round 5, PREREG-5 rules)
# minutes: 7.1 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 8/39101/333376/79040 | list-price USD: 0.98

This is a spike — you want a verdict and a defensible number, not a maintained artifact — so here's the check and the answer, no spec doc.

Probe I'd have confirmed before running the numbers: *"I'll rebuild the LTV three ways — bounded to what's actually been observed, corrected for margin instead of revenue, and with a couple of longer extrapolation scenarios — then compare each to the $5,000 ask. Sound right?"* Most likely answer: yes, that's the question being asked. Proceeding on that basis.

**Short answer: don't trust it as a working number. Trust it as an optimistic ceiling, at best.**

## What's wrong with the $15,000

The arithmetic is fine. The formula is the problem, applied to a company that hasn't lived long enough to support it.

**1. It assumes 1.2% monthly churn holds forever.** ARPU ÷ churn is shorthand for summing an infinite geometric series — it only works if the same churn rate applies for the customer's entire life. That math implies an average customer lifetime of 83 months, about 7 years. The company is 3 years old. Nobody has ever stayed past month 36, so months 37 through 83 aren't measured, they're assumed. Rerun the identical 1.2% assumption but stop counting at month 36 — the actual edge of what's been observed — instead of running it to infinity, and revenue-basis LTV drops from $15,000 to about $5,300. **Roughly two-thirds of the $15,000 is attributed to customer-months nobody at this company has ever seen.**

**2. It's revenue, not margin.** LTV needs to be dollar-comparable to CAC, which means gross margin, not top-line ARPU. At a plausible 70–80% subscription gross margin, that correction alone — even leaving the infinite-horizon assumption untouched — brings it down to roughly $10,500–$12,000.

Stack both corrections and the honest, evidence-bounded number lands around **$3,700–$4,200** — below the $5,000 CAC being proposed, not comfortably above it.

To be fair to the head of growth: 1.2%/month (~13.5% annualized) isn't an implausible or cherry-picked churn rate on its own — that's a reasonably healthy figure for B2B subscription. The problem is entirely in what got done with it, not the input itself.

## The gut check that doesn't need a model

At $5,000 CAC and 70–80% gross margin, it takes **35–40 months of gross margin just to break even** on that spend — before anything counted above that is profit. That's about as long as the company has existed. Approving $5,000 means betting that customers signed up today behave, three years out, the way no customer in the company's history has yet had the chance to prove.

## A more honest estimate is a range, not a point number

These reuse the same 1.2% blended rate given — just bounded to different, explicitly-stated horizons instead of run to infinity. They are not a claim of real cohort data; that data (per-cohort retention curves, not one blended rate) is the actual next step, listed below.

| Basis | Horizon assumption | Margin-adjusted LTV (70–80% margin) | Implied LTV:CAC @ $5,000 |
|---|---|---|---|
| Floor | Bounded to observed 36mo — no extrapolation | ~$3,700–$4,200 | ~0.7x–0.85x |
| Base case | Modest extrapolation to 60mo (+24mo past observed) | ~$5,400–$6,200 | ~1.1x–1.25x |
| Optimistic | Extrapolation to 72mo (+36mo past observed) | ~$6,100–$7,000 | ~1.2x–1.4x |
| Head of growth's number | Revenue, infinite horizon (83mo implied) | $15,000 raw / ~$10,500–$12,000 margin-fixed | 2.1x–3.0x |

The commonly cited "healthy" LTV:CAC bar is 3x. The presented number just clears it — using the single most generous reading of the data available (undiscounted revenue, unlimited retention horizon). Every methodological fix between that reading and the evidence you actually have pulls the ratio down, and the most defensible version — bounded to what's been observed — puts new customers at or below breakeven at a $5,000 CAC.

## What I'd do

- Don't set $5,000 as the new ceiling on this basis. Raise CAC incrementally if it needs to move, not in one jump justified by an unvalidated 7-year retention assumption.
- Rebuild LTV from actual per-cohort retention curves, not one blended rate — a single 1.2% can hide very different behavior between month-1 and month-30 customers, and the curve shape (flattening vs. staying constant) is the actual answer to "how far can we trust this."
- Use gross margin, not revenue, in every LTV calculation from here on, and apply a discount rate if this number is feeding a real capital-allocation decision — most of the value in a number this size sits years out.
- Set a review trigger, not a one-time fix: revisit the CAC ceiling once the oldest cohorts cross 48 and then 60 months. That's 1–2 years away, not never, and it converts this from a permanent assumption into a number that gets checked against reality on a schedule.
- One factor that could push the honest number up, not just down: if ARPU expands with tenure (upsells, seat growth) rather than holding flat at $180, actual LTV could beat the floor above. Check net revenue retention by cohort — not just logo churn — before locking in a replacement figure.
