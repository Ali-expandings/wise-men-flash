# arm: warp-council (warpdotdev/common-skills 69b4753651ab; adapted as in PREREG-2) | question: R503 | orchestrator: general-purpose/sonnet | run: 2026-09-24 (round 5, PREREG-5 rules)
# minutes: 6.3 | subagent calls: 3 (transcripts matched: 3) | tokens in/out/cache-read/cache-write: 20/53205/252055/228915 | list-price USD: 1.95

*Council: 3 Claude-model members — Opus (architecture/correctness), Sonnet (execution/financial feasibility), Haiku (contrarian red-team). The skill's default roster calls for Opus + GPT-5.5 + an open-source model; this harness only exposes Claude (opus/sonnet/haiku), so Sonnet substitutes for the GPT/implementation-grounded seat and Haiku substitutes for the OSS/contrarian seat, per the skill's own fallback rule — model diversity across vendors wasn't available, so diversity was preserved via distinct angles instead.*

## Recommendation

Do neither option as framed. Run a cheap 2–4 week validation pass first, then commit to a narrowly-scoped in-house build (not a full 2-quarter platform) or a cash-light version of the acquisition (not "most of the cash reserve") — decided by what that validation finds.

## Why

- **The evidence is thinner than it looks.** 7 of 10 is a sample of 10, self-reported by sales, post-hoc, with no comparison against deals you won and no verification against the buyers themselves. All three reviewers independently flagged this as too weak to justify betting most of the company's cash or a two-quarter engineering slot on, untested.
- **Buying isn't actually the fast option once integration is counted honestly.** Diligence-to-close plus real technical and organizational integration for a company this size runs 3–5 quarters, not faster than a build — while simultaneously draining the cash reserve and adding new ongoing burn (acquired team payroll) right as integration risk, culture clash, and key-engineer attrition peak. This is the single riskiest of the three paths on every reviewer's analysis.
- **A materially cheaper third path exists and all three members converged on it independently:** bridge to a third-party automation engine (Zapier/Make/n8n-style integration or embed). It validates real demand and can ship usable automation in weeks at a fraction of build-or-buy cost, and it forces you to build the event/API layer a real in-house builder needs anyway — so nothing is wasted if you build later.

## Tradeoffs and risks

- Build-without-validation risk: workflow-engine-class projects (durable execution, retries, permissioning, versioning) routinely overrun — 2 quarters commonly becomes 3–4 — and you can still ship a v1 too weak to beat a "polished" competitor.
- Buy-without-validation risk: tenancy/architecture mismatch, expanded compliance scope, possible licensing issues (e.g., AGPL/fair-code engines), and post-close attrition of the engineers you paid for — compounded by a depleted cash cushion if it doesn't move the win rate.
- Validation-first risk: if it turns out "missing automation" is a proxy for pricing, sales execution, or ICP mismatch, you've spent a few weeks finding that out rather than acting immediately — but that's cheap insurance against a much larger misallocation, and the real cause still needs fixing fast once identified.
- Scope discipline is itself a risk on the build side: a build capped to the 2–3 automation patterns actually named in the lost deals is achievable in two quarters; a build implicitly aimed at full parity with a competitor's "polished" builder usually is not.

## Final call

Before committing engineering time or acquisition capital: (1) have someone other than sales interview the 7 lost accounts directly and deep-dive 3 of them (timeline, champion, price, what the competitor actually offered); (2) ship a quick Zapier/Make/n8n-style integration and put it in front of a few live prospects to test real demand. Then branch: if the gap is confirmed and narrow, greenlight a hard-capped build of just those named workflows — not a platform; if the acquisition target is still worth it, only revisit with a deal structured to protect cash (stock/earn-out-heavy, not most-of-reserve cash); if the real cause turns out to be pricing, sales execution, or ICP mismatch, redirect there instead. Do not commit to the full 2-quarter build or the cash-heavy acquisition as currently framed.
