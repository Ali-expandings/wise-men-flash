# PREREG-1 — wise-men-flash, measured as its own skill

Written and committed 2026-09-24, before any run. Nothing below changes once the first flash answer exists; every deviation goes in `RESULTS-1.md`.

## Question

Does `wise-men-flash` 0.1.0 — run as its own skill (this repo's `SKILL.md` and agent, invoked as `/wise-men-flash` in a fresh session per question) — score the same as or better than the `wise-men` 3.13 fast arm it was extracted from, and stay clearly ahead of every rival council?

The 23.3/25 in the README was measured as an arm *inside* `wise-men` (round 4, `PREREG-4.md` in that repo). This round measures the skill people actually install.

## What changed since the fast arm (the enhancement under test)

- **Counter-position sharpened.** The Devil's Advocate is told to attack the load-bearing premise; the memo rule chooses the counter-position by aim; the checker's DISSENT item asks whether a more central attack existed. Target: dissent (fast arm 4.7, full council 5.0).
- **One sharpest domain lens** with a reasoning procedure distinct from the anchor's and the DA's, instead of a generic third seat. Target: insight and practical (fast arm 4.7 / 4.7, full council 5.0 / 4.9).
- **Correctness must not drop** below the fast arm's 4.3 (it beat the full council's 4.0 in round 4).

## Arms

**Part A (main): the five round-4 questions R401–R405.**
New: flash-standalone answers, one per question, fresh session each, skill file verbatim, no extra instructions.
Reused byte-identical from round 4's `raw/`: `wise-men` 3.13 default, `wise-men` 3.13 fast, llm-council, Warp council, plain answer.
Six arms, all six judged in the same sitting — judges drift between rounds (round 2's lesson), so only within-sitting comparisons count; round-4 scores are not compared to this round's directly.

**Part B (only if weekly usage allows after Part A): R406–R408** (writing, ethics, personal — never run in round 4). flash-standalone vs `wise-men` 3.14 full council vs Warp vs llm-council vs plain. Same judging.

## Judging

Three blind Opus judges per question. The round-4 judge prompt (`eval-data/head-to-head/h2h4.py` in the `wise-men` repo — error-first: list every error, then score). Five axes — correctness / insight / practical / risk / dissent — 5 each, 25 total. Arms sealed as A–F per question with a fresh order per judge, seed 20260925. Answers normalized as in round 4 before blinding.

## Analysis

Per arm: mean of the three judges per question, then across questions. Paired differences (flash-standalone minus each arm), 95% percentile bootstrap over questions, 10,000 draws, seed 20260925. Wording rules as `PREREG-4`: **ahead** = mean difference > 0; **clearly ahead** = interval excludes 0; **beats every rival** only when clearly ahead of every rival council on the shared set.

## Pre-stated hypotheses

- **H1** flash-standalone is clearly ahead of Warp, llm-council and plain on Part A.
- **H2** flash-standalone is not clearly behind the `wise-men` 3.13 default arm (interval includes 0, or favours flash).
- **H3 (the enhancement)** flash-standalone's within-sitting mean on insight, practical and dissent is each ≥ the fast arm's, with correctness not below it. Any axis that falls is reported as a regression, not explained away.

H1 is what the README needs to say "measured as its own skill". H3 decides whether the 0.1.0 changes stay: if H3 fails, the changed wording reverts to the fast arm's (`wise-men` commit `bcbad1d`) — it is not re-tuned on these judgments.

## Cost and time

Minutes = first-to-last transcript timestamp; calls = spawned agents; USD at list price per message from the transcripts, as in round 4. Reported in `RESULTS-1.md` next to quality: speed is this skill's purpose, so it is a headline number here, not a footnote.

## Stop rules and disclosures

A run cut by the usage limit is resumed from its transcript, marked interrupted, and excluded from time medians only. Part B skipped for usage is disclosed, not silently dropped. No re-judging after seeing scores; no question dropped after seeing scores. Every deviation from this file is listed in `RESULTS-1.md`.
