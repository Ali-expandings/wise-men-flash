# Head-to-head round 4 — pre-registration

Written and committed 2026-09-18, before any round-4 arm ran. Nothing below changes after this commit except through dated amendments; results go in `RESULTS-V4.md`. Rounds 1–3 stand as published.

## Why a fourth round

Round 3 measured 3.11.0. Since then 3.12.0 changed how flagged claims are checked, how the counter-position is chosen, when a claim is tagged and what a memo may repeat, and 3.13.0 (this commit) attacks the one measure wise-men loses: it was the slowest and most expensive council in round 3. Both are unmeasured. Round 3 also had three weaknesses this round answers: its held-out questions came from the project's own 30-question file; its judges scored correctness generously (one credited a rival for correcting "a mistake the other three make" and still gave wise-men 5); and cost was never measured, only a token counter that leaves out every spawned agent.

## What 3.13.0 changes (speed only)

Measured from the round-3 transcripts, spawned agents included, at list prices: a standard wise-men council cost about $3.6–5.9 and 20–26 minutes against Warp's $1.9 and 7 minutes and llm-council's $5.3 and 17. Members cost $0.02–0.25 each and finish in about two minutes; the orchestrator's turns are 55–64% of the bill, and the single synthesis-check call took 7–11 minutes and 45–70k tokens of deliberation. So:

- **Every tier, no quality mechanism removed**: Read files in one message and only when a step needs one; never re-type what a file holds (the checker Reads the grading packet plus a small scores-and-draft file); the checker works in one pass and replies in the fixed form.
- **`--fast` (the quick tier, redefined)**: practitioner anchor and Devil's Advocate on the strong model plus one domain member, no peer review, a cheap-tier checker that checks the draft against the question (DISSENT, DISCLOSURE, CLAIMS, COVERAGE). Four subagent calls. Opt-in only.

**The quality gate, fixed now.** The default's tier selection and stages are unchanged, and nothing faster replaces the default on the strength of this round unless its total score is not clearly behind the default's (the 95% interval of fast minus default must not lie wholly below zero) **and** it is clearly ahead of every rival. If `--fast` fails either test it stays an opt-in flag and the README says what it costs in quality.

## Questions

Eight questions written for this round by a fresh Opus agent that was told nothing about the arms, the skills or the study — only the slots, the style, and the topics already used. Its prompt is `question-author-prompt.txt`; its output is `questions-r4.yaml`, used exactly as returned (R401–R408: two engineering, product, business, research, writing, ethics, personal; shapes: choice, diagnosis, questionable premise, trust-a-number, evidence, register, obligations, personal). They are new to the project: no earlier eval, round or tuning decision has seen them.

## Arms (five per question, 40 runs)

| arm | what runs |
|---|---|
| `wise-men-3.13` | this commit's protocol, invoked plainly; the skill picks its own tier |
| `wise-men-3.13-fast` | the same, invoked as `/wise-men --fast <question>` |
| `warp-council` | warpdotdev/common-skills `69b4753651ab`, adapted as in PREREG-2 |
| `llm-council` | aiwithremy/claude-skills-llm-council `1162f272ab94` |
| `direct` | no skill |

Harness as in rounds 1–3: a fresh `general-purpose` orchestrator on Sonnet 5 per arm per question, the skill file and the question verbatim, subagents in the foreground, each arm reading only its own skill files, only the finished output returned; an incomplete run is re-run once. Prompts are rounds 1–3's word for word; the wise-men prompts are round 3's (no `eval-data/`, scratch folder only), the fast arm's question prefixed by the invocation. Batches of at most four heavy arms.

## Judges

Three fresh Opus 5 judges per question, 24 judgments, each with its own sealed answer order (`blinding4.yaml`, seed 20260919, generated in this commit). Normalization: `normalize()` in `h2h.py`, unchanged.

**The judge prompt is stricter on correctness** (`judge-prompt-5.txt`): before ranking, the judge lists the errors it can identify in each answer; an answer with a listed error cannot score 5 for correctness, and one with a material error cannot score above 3. Everything else — axes, scale, "ignore length", output format — is round 3's. Scores from this prompt are not comparable with earlier rounds. **Calibration, before any round-4 judgment**: the same three-pass instruction is run once on round 3's Q23 answers, where wise-men 3.11.0 calls a check "decisive in both directions" that a rival correctly shows is not; the result is reported whether or not the judge catches it.

## Measures

- **Quality**: question score = mean of the three judges' totals (max 25); per-arm means and per-axis means over the eight questions; each wise-men arm against every other arm: wins–ties–losses and the mean paired difference with a 95% percentile bootstrap interval over questions (10,000 resamples, seed 20260919); judge agreement as in round 3.
- **Time**: the orchestrator's first-to-last transcript timestamp, in minutes; per-arm median over runs not interrupted by a usage limit (interrupted runs are resumed, disclosed, and left out of the time median only).
- **Cost**: every token the run used — the orchestrator's and every agent it spawned (matched by the exact prompt sent), by billing category (input, output, cache read, cache write) — priced at the 2026-07 list rates in `resources/model-routing.md`; per-arm median USD and median subagent calls. Computed when each answer is saved, stored in the raw file's header.

## Wording rules

- Quality: "ahead", "clearly ahead" (interval's lower bound above zero), "beats every rival" (clearly ahead of Warp council, llm-council and the plain answer) — per wise-men arm. "Highest on every axis" only if its mean is the highest of the five arms on all five axes.
- Time and cost: "faster than X" / "cheaper than X" when the arm's median is below X's. The targets are the rival councils. No council can be faster or cheaper than the plain answer; those numbers are reported, never claimed.
- Anything not met is stated as not met, next to what was.

## Reporting

`RESULTS-V4.md` is generated from `parsed-v4/` and the raw headers by `h2h4.py results`; the README leads with round 4, whatever it shows, with every deviation disclosed.
