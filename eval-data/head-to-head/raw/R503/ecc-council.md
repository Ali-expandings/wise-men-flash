# arm: ecc-council (affaan-m/ECC bf70150eb2df) | question: R503 | orchestrator: general-purpose/sonnet | run: 2026-09-24 (round 5, PREREG-5 rules)
# minutes: 3.9 | subagent calls: 3 (transcripts matched: 3) | tokens in/out/cache-read/cache-write: 12/33310/343795/158856 | list-price USD: 1.20

## Council: Build vs. buy an automation builder

**Architect:** Verify the loss-reason diagnosis first, ship a thin third-party automation integration as an immediate stopgap, then default to Build over Buy unless the cash reserve is confirmed healthy enough to absorb the spend.
Started from a build-leaning, cash-preservation instinct; the Skeptic and Pragmatist independently converged on "verify before committing the scarce resource," which changed the recommendation to add that step before either bet.

**Skeptic:** Don't fund either option yet — "missing automation features" is sales' self-reported reason for 7 of 10 losses, not independently confirmed data. Test the hypothesis cheaply first by embedding an existing automation engine.
The binary itself may be a false choice: the real fix could be weeks and a fraction of the cost of either option.

**Pragmatist:** Buy, conditionally — a from-scratch 2-quarter build won't reach the competitor's "polished" bar while engineering bandwidth, not cash, is the real binding constraint at 80 people.
But verify the loss reason first and scope any acquisition integration thin, since unscoped integration commonly eats another 1-2 quarters.

**Critic:** Build is the less damaging bet — spending most of the cash reserve against an unverified diagnosis is the bigger unforced error, and a stalling build can be cut and redirected; a signed acquisition can't.
At 80 people with no stated runway, cash is the resource you can't get back.

### Verdict
- **Consensus:** Three of four voices independently arrived at the same prior step: confirm the loss reason with real win/loss interviews before spending either scarce resource, and use a fast, cheap embedded/third-party automation integration as both a stopgap and a live test of the hypothesis.
- **Strongest dissent:** Past that verification step, Pragmatist and Critic disagree on which resource is truly less reversible for this company — engineering-quarters (so buy, spend cash) or the cash reserve itself (so build, spend time). Neither has the company's actual burn rate or runway to settle it.
- **Premise check:** Yes — the Skeptic rejected the build-vs-buy binary as premature, and the other two voices independently backed that with their own "verify first" caveats, elevating it from dissent to the council's lead recommendation.
- **Recommendation:** Don't commit to Build or Buy yet. Spend 1-3 weeks confirming the loss reason with real win/loss interviews, not just the sales log, and in parallel ship a thin embedded third-party automation integration as an immediate stopgap that also tests whether an automation builder actually swings deals. Then choose Build vs. Buy on one question this council can't answer from outside the company: is engineering bandwidth or cash reserve the more binding, less-reversible constraint right now? Thin runway → lean Build, with a hard month-3 walk-away checkpoint. Ample runway and engineering is the real bottleneck → lean Buy, but scope the integration thin, since an unscoped integration routinely erases the speed advantage that justified paying for it.
