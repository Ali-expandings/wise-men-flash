# arm: direct (no skill) | question: R405 | orchestrator: general-purpose/sonnet | run: 2026-09-18 (round 4, PREREG-4 rules)
# minutes: 1.9 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/9605/36750/33478 | list-price USD: 0.28

Take it seriously as evidence, not as proof. A natural experiment beats a simple before/after or cross-sectional correlation because it at least has a comparison group and a timing shock. But "next best thing to an RCT" is doing rhetorical work — it borrows RCT's credibility without RCT's actual guarantee, which is random assignment. Here, some legislature or agency chose to change the rule in one region and not the other, for reasons. Those reasons are the whole problem: if whatever drove the policy choice also correlates with the outcome trend, the comparison is confounded no matter how clean the chart looks.

Where these designs typically break:

1. **Parallel trends violation.** The load-bearing assumption is that treated and control regions would have moved together absent the policy. If they were already diverging beforehand, the "effect" is just the pre-existing trend continuing. Demand a pre-trend plot with several periods before the change, not a single before/after average.

2. **Selection into treatment / Ashenfelter dip.** Regions don't adopt rules at random moments — often right after a trough or crisis. The subsequent bounce-back then gets credited to the policy when it's partly mean reversion.

3. **Concurrent shocks or bundled reforms.** Anything else change in the treated region at the same time — funding, leadership, other legislation, a local economic shock? Diff-in-diff can't separate simultaneous causes from the one everyone's talking about.

4. **Spillover/contamination.** If people, firms, or activity cross the border in response to the rule (relocation, cross-border shopping, migration), the "control" region is no longer untreated. This quietly breaks the comparison.

5. **Cherry-picked control.** Was this control region chosen because it's genuinely comparable, or because it happens to make the story work? Ask if the result holds against other plausible controls, or better, a synthetic control built from many regions instead of one hand-picked match.

6. **Small-N inference.** One region vs. one region means standard errors from an ordinary regression are close to fiction — serial correlation in the outcome series makes noise look like a real effect (the classic Bertrand-Duflo-Mullainathan problem). Look for clustered SEs, permutation tests, or a design with many treated/control units.

7. **Researcher degrees of freedom.** Time window, functional form, outcome metric, covariates — all bendable after seeing the data. A result that only survives under one specific setup is fragile; ask what happens under a couple of alternative reasonable choices.

8. **Implausible effect size / no mechanism.** Does the claimed effect make sense given what the policy actually does? Real effects usually have a traceable causal path from rule to outcome. If the size is huge and the mechanism is hand-wavy, be skeptical.

9. **External validity.** Even a clean estimate for that specific region-pair may not transfer — different baseline conditions, enforcement, population, complementary institutions. "Worked there" isn't "will work here."

10. **Motivated selection of the example.** A team advocating for a change has an incentive to surface the one comparison that flatters them. One favorable natural experiment is an anecdote; the same direction showing up across multiple region-pairs, time periods, or independent researchers is evidence.

Before crediting this one: ask for the pre-trend chart, ask why that region changed the rule when it did and whether that reason is independent of the outcome trend, ask if the result survives alternate control regions or a synthetic control, ask what else changed at the same time, and ask whether this replicates elsewhere. Clean answers on all of that make it genuinely strong quasi-experimental evidence. Defensiveness about pre-trends or "we only checked this one comparison" means treat it as suggestive, not a basis for the policy call.
