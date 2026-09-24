# Round 4, read for wise-men-flash

**What was measured.** Round 4 of the `wise-men` head-to-head ran five arms: the full `wise-men` 3.13.0 council, its three-member `--fast` profile, Warp's council, llm-council and a plain answer. The `--fast` arm is the profile `wise-men-flash` ships — a practitioner anchor and a Devil's Advocate on the strong model, one domain member on mid, no peer review, a cheap-tier check of the draft against the question — so its row is this skill's evidence. It was measured inside `wise-men`, before this repository existed; this skill's own standalone round is pre-registered in [`../PREREG-1.md`](../PREREG-1.md) and has not run yet.

**Stopped early: 5 of 8 questions.** The round was pre-registered at eight questions and stopped after five at the repository owner's request, to conserve the account's usage allowance. The decision was made while the fifth question was running, after the scores of the first three were known, so it was not a blind stop. R406, R407, R408 (writing, ethics, a personal decision) were never run: no answer or judgment exists for them, and nothing here says how any arm does on those kinds of question. Every comparison below is over five questions; intervals are 95% percentile bootstraps over those five.

Eight questions written for the round by an author that knew nothing about the arms ([`PREREG-4.md`](PREREG-4.md), [`questions-r4.yaml`](questions-r4.yaml)); five arms; three blind Opus judges per question with sealed orders ([`blinding4.yaml`](blinding4.yaml)) and an error-first judge prompt ([`judge-prompt-5.txt`](judge-prompt-5.txt)). Minutes are the orchestrator's first-to-last transcript timestamp; calls are its subagent spawns; USD prices every token the run used — the orchestrator's and every spawned agent's, input, output, cache reads and cache writes — at 2026-07 list rates. No council can be faster or cheaper than the plain answer; the pre-registered time and cost comparisons are against the rival councils.

| round 4 (5 of 8 questions) | total /25 | correct | insight | practical | risk | dissent | median minutes | median calls | median list-price USD |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| wise-men 3.13 full council | 23.8 | 4.0 | 5.0 | 4.9 | 4.9 | 5.0 | 37.3 | 11 | 9.59 |
| **wise-men-flash** (measured as wise-men 3.13 `--fast`) | 23.3 | 4.3 | 4.7 | 4.7 | 4.9 | 4.7 | 10.8 | 4 | 2.09 |
| llm-council | 17.9 | 3.1 | 3.9 | 3.3 | 3.8 | 3.7 | 18.0 | 11 | 6.43 |
| Warp council | 17.5 | 3.4 | 3.5 | 4.0 | 3.7 | 3.0 | 9.3 | 3 | 2.03 |
| plain answer | 16.3 | 3.9 | 3.5 | 4.2 | 2.9 | 1.8 | 1.8 | 0 | 0.27 |

- wise-men-flash against Warp council: +5.7 [+4.8, +6.7], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash against llm-council: +5.4 [+3.4, +7.9], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash against plain answer: +6.9 [+5.5, +8.3], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash against wise-men 3.13 full council: −0.5 [−1.2, +0.1], W–T–L 1–0–4 — behind, with an interval that includes zero.

- Axes: wise-men-flash had the highest correctness of the five arms, tied with the full council for the highest risk awareness, and scored above every rival on 5 of 5 axes; the full council led insight, practical use and dissent quality.
- Time and cost, medians per question: the plain answer 1.8 min, $0.27; Warp council 9.3 min, $2.03; wise-men-flash 10.8 min, $2.09; llm-council 18.0 min, $6.43; the full wise-men council 37.3 min, $9.59. wise-men-flash was faster and cheaper than the full wise-men council and llm-council; Warp council was 1.5 min quicker and $0.06 cheaper, and scored 5.7 lower.

Judge agreement: mean SD of the three judges' totals 0.58.

## Per question (mean of three judges, total /25)

| question | **wise-men-flash** (measured as wise-men 3.13 `--fast`) | wise-men 3.13 full council | Warp council | llm-council | plain answer |
|---|--:|--:|--:|--:|--:|
| R401 (engineering, choice) | 24.00 | 23.33 | 18.00 | 14.33 | 17.67 |
| R402 (engineering, diagnosis) | 23.67 | 24.33 | 18.33 | 20.00 | 15.00 |
| R403 (product, questionable-premise) | 23.00 | 23.67 | 19.00 | 16.00 | 17.67 |
| R404 (business, trust-a-number) | 23.33 | 23.67 | 16.00 | 20.00 | 14.33 |
| R405 (research, evidence) | 22.33 | 24.00 | 16.33 | 19.00 | 17.00 |

## Deviations and disclosures

- **Inherited, not re-measured.** Every flash number here is the `wise-men-3.13-fast` arm, run as `/wise-men --fast` under wise-men 3.13.0. `wise-men-flash` 0.1.0 packages that profile with the rule wise-men added right after this round (3.13.1: nothing about how the answer was produced appears in it) and a sharper brief for its domain seat and Devil's Advocate; those changes are untested until `PREREG-1` runs.
- **Process notes the judges saw.** Three of the five flash answers closed with a note about how they were produced — "this ran at quick tier … per the requested `--fast` mode" (R402), "a late review flagged …" (R403), and a counter-position introduced as "the council's dissenting position" plus a closing verification note (R405). Judges marked these as process residue. The rule that removes them is in this skill; the scores above include the penalty.
- **The synthesis check** took 0.5–2.1 minutes on every flash run (cheap tier, four of the six checks), against 9–11 minutes on every full-council run.
- **Normalization** is `normalize()` from rounds 1–3 of the wise-men study, unchanged and copied into `flash4.py`: it strips the provenance header and any short status text before an answer's first heading. On R402 it removed a paragraph in which the full council described its checker's findings before its memo — the judges did not see it.
- **Web access.** The rival councils' members run as general-purpose agents and can browse; Warp's did on R401 (33 web tool calls) and on no other question; llm-council's never did. Flash members cannot browse.
- **Time** is the median over runs the usage limit did not interrupt (four of five for each council arm; all five for the plain answer). Cost and calls use all five runs; a resumed run's cost includes re-reading its own context after the wait.
- **Same family.** Every judge and every arm is a Claude model, and every spawned agent in every arm inherited the account's global instruction to write tersely. No human grades and no grades from another model family were collected.
- **Judge calibration** (pre-registered): before any round-4 judgment, the error-first prompt was run once on round 3's Q23 answers, where an earlier wise-men answer overstated a check that a rival correctly limited; `blinded-v4/CAL-Q23.md` and `judgments-v4/CAL-Q23.md` hold the packet and the result.
- R402, wise-men-flash: interrupted by the account's usage limit after its three members had answered, and resumed from its own transcript; left out of the time median
- R402, the full wise-men council: interrupted by the account's usage limit after four of its five members had answered (the fifth died with the limit and was retried on resume), and resumed from its own transcript; left out of the time median
- R402, Warp council: interrupted by the account's usage limit after its three members had answered, and resumed from its own transcript; left out of the time median
- R402, llm-council: interrupted by the account's usage limit after its five advisors had answered, and resumed from its own transcript; left out of the time median

## Reproduce

`python3 eval-data/head-to-head/flash4.py report` prints the table and comparisons; `results` rewrites this file; `verify` rebuilds every blinded packet from the raw answers and re-parses every judgment, and fails on any difference. Time and cost were computed from local agent transcripts when each answer was saved and are stored in the raw file headers; the transcripts themselves are not in the repository. The same data, seen from the full council, is `RESULTS-V4.md` in the [wise-men repository](https://github.com/Ali-expandings/wise-men/blob/master/eval-data/head-to-head/RESULTS-V4.md).
