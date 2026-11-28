# Footer and DEFERENCE checks (2026-11-28)

**Why.** An outside tester ran 0.3.1's my-call-first mode on three small-business questions with a wrong call and a right call each, the answer key held by Qwen. The memo pushed back on 3 of 3 wrong calls and held its line on 3 of 3 right ones, and DEFERENCE passed all 6. He reported two things:

1. **The footer rule and DISCLOSURE conflicted.** The runbook requires a footer line naming a fallback agent and one naming the requested and actual tier. DISCLOSURE failed any mention of tiers or council mechanics, so every degraded run failed its own check. His run had both degradations, and DISCLOSURE failed all 6 on the footer alone.
2. **DEFERENCE never failed, because nothing bent.** That shows no bending on those calls. It does not show the check would catch bending. His suggestion: plant a closing section that bends, and see whether DEFERENCE fails it.

0.3.2 fixes the first (`SKILL.md`: a degradation line may name the seat, agent type or tiers; DISCLOSURE says it never fails on one). This folder tests the fix and runs the second.

**Source.** His round 7: the three questions, the two calls for each, the three memos and the six closing sections his writers produced. They are in github.com/mrtooher/fable-mode at commit `26756a9`, `bench/judgment/qwen-rounds/round7/`. That repo has no licence file, so they are not copied here. `build_prompts.py` rebuilds every prompt from a clone of it.

**What ran.** The Stage 4.5 checker prompt from `SKILL.md`, in my-call-first mode (the user's call in the `user_call` block), on the full draft: the memo's six sections, a closing section, then the memo's own footer (the fallback-agent line and the tier-remap line). Each draft was checked once by a fresh read-only `wise-member` on `sonnet` (resolved to Sonnet 5.5), the tier the checker runs on since 0.3.1. 18 calls:

- **9 planted closings** (`planted/`), written for this test to bend, on the 0.3.2 prompt:
  - 3 **blatant** bends toward the wrong call: agreement overstated, the fact that sinks the call left out, a trivial point named as the strongest one against it;
  - 3 **subtle** bends toward the wrong call: the sinking fact named, then argued away with claims the memo does not make ("a short line of credit would usually bridge it", "a gap the first months of new sales would likely close");
  - 3 bends **away** from the right call: disagreement overstated, and a push toward the option the memo rejects.
- **6 honest closings**, the tester's own, on the 0.3.2 prompt (controls: these should pass).
- **3 honest closings** for the wrong calls on the 0.3.1 prompt, to show the conflict on the same inputs.

Replies are verbatim in `outputs/`, each headed with the model that answered. The score is the checker's own PASS or FAIL line; nobody judged the replies.

## Result

| draft | prompt | n | DEFERENCE FAIL | DISCLOSURE FAIL |
|---|---|:-:|:-:|:-:|
| planted, blatant toward the wrong call | 0.3.2 | 3 | 3 | 0 |
| planted, subtle toward the wrong call | 0.3.2 | 3 | 3 | 0 |
| planted, away from the right call | 0.3.2 | 3 | 3 | 0 |
| honest closing (controls) | 0.3.2 | 6 | 0 | 0 |
| honest closing, wrong calls | 0.3.1 | 3 | 0 | 3 |

- **DEFERENCE caught every bend and flagged no honest closing.** Each FAIL named what bent: the misstated agreement, the trivial "strongest point", the sinking fact argued away, or the invented competitor threat.
- **The DISCLOSURE fix holds on these inputs.** On the 0.3.1 prompt, the same footers failed 3 of 3, as the tester found. On the 0.3.2 prompt they passed 15 of 15, and each reply called them allowed degradation lines.
- **Other checks caught the plants too.** CONSISTENCY failed 7 of the 9, where the closing contradicted the memo's own numbers or Recommendation. CLAIMS failed 3, where the closing stated an unsourced claim as fact.
- **The honest closings were not clean on every check.** On question 2, COVERAGE and CONSISTENCY failed for both honest closings on 0.3.2 and for the one on 0.3.1. The objections were to the memo (figures repeated across sections, vendor-picked references as proof, a monthly saving capped at today's volume), not to the closing.

**Decision.** 0.3.2 ships the DISCLOSURE fix. DEFERENCE is unchanged.

**Limits.**
- One run per draft, three questions.
- The planted closings were written by the person who ran the test, a Claude model that knew what DEFERENCE checks. Bends a model produces on its own may be harder to catch than written ones.
- Bending was planted only in the closing section. The six sections are drafted before the user's call, so they were not tested here.
- The memos and honest closings are the tester's, from Claude models on his bench. His Qwen key graded his round, not this one.
- In 2 of 18 replies the checker named the person who ran the test. That name is not in any prompt; the subagents inherit that person's global settings. Nothing else in those replies depends on it.
- Sonnet 5.5 on this date; a newer model behind the alias is untested here.
