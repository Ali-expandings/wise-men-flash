# Head-to-head round 5 results

**In progress: 3 of 8 questions judged.** The remaining questions (R503, R508, R502, R504, R505) run after the account's weekly usage limit resets, in the pre-registered order; this file, the README tables and the charts are regenerated as each one is judged. Every comparison below is over the questions judged so far; intervals are 95% percentile bootstraps over them, and with this few questions they are wide.

Eight questions written for this round by an author that knew nothing about the arms ([`PREREG-5.md`](PREREG-5.md), [`questions-r5.yaml`](questions-r5.yaml)); nine arms, every answer new; three blind Opus judges per question with sealed orders ([`blinding5.yaml`](blinding5.yaml)) and round 4's error-first judge prompt for nine answers ([`judge-prompt-r5.txt`](judge-prompt-r5.txt)). Minutes are the orchestrator's first-to-last transcript timestamp; calls are its subagent spawns; USD prices every token the run used — the orchestrator's and every agent spawned under it, input, output, cache reads and cache writes — at 2026-07 list rates. No council can be faster or cheaper than the plain answer; the pre-registered time and cost comparisons are against the rival councils.

| round 5 (3 of 8 questions) | total /25 | correct | insight | practical | risk | dissent | median minutes | median calls | median list-price USD |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **wise-men 3.14.0** | 23.7 | 3.9 | 5.0 | 4.9 | 5.0 | 4.9 | 49.1 | 16 | 15.64 |
| **wise-men-flash 0.1.0** | 22.9 | 3.7 | 4.9 | 4.7 | 4.7 | 5.0 | 16.8 | 4 | 3.93 |
| Warp council | 19.0 | 4.0 | 3.7 | 4.0 | 4.1 | 3.2 | 11.3 | 3 | 2.83 |
| llm-council | 17.4 | 3.3 | 3.9 | 3.2 | 3.7 | 3.3 | 15.7 | 11 | 4.52 |
| LifeOS Council | 17.3 | 3.0 | 3.8 | 2.9 | 3.4 | 4.2 | 8.7 | 12 | 3.90 |
| plain answer | 16.8 | 4.2 | 3.0 | 4.0 | 3.3 | 2.2 | 1.6 | 0 | 0.26 |
| mattpocock grilling | 16.6 | 3.8 | 3.6 | 3.8 | 3.2 | 2.2 | 4.9 | 0 | 0.59 |
| ECC council | 16.6 | 3.4 | 3.3 | 3.3 | 3.4 | 3.0 | 5.1 | 3 | 1.49 |
| superpowers brainstorming | 15.0 | 2.9 | 3.2 | 3.6 | 3.1 | 2.2 | 5.2 | 0 | 0.68 |

- wise-men 3.14.0 against wise-men-flash 0.1.0: +0.8 [−0.7, +2.7], W–T–L 2–0–1 — ahead.
- wise-men 3.14.0 against Warp council: +4.7 [+3.0, +6.0], W–T–L 3–0–0 — clearly ahead.
- wise-men 3.14.0 against llm-council: +6.2 [+3.7, +9.3], W–T–L 3–0–0 — clearly ahead.
- wise-men 3.14.0 against LifeOS Council: +6.3 [+3.7, +9.7], W–T–L 3–0–0 — clearly ahead.
- wise-men 3.14.0 against ECC council: +7.1 [+6.0, +7.7], W–T–L 3–0–0 — clearly ahead.
- wise-men 3.14.0 against superpowers brainstorming: +8.7 [+6.0, +10.3], W–T–L 3–0–0 — clearly ahead.
- wise-men 3.14.0 against mattpocock grilling: +7.1 [+5.0, +9.3], W–T–L 3–0–0 — clearly ahead.
- wise-men 3.14.0 against plain answer: +6.9 [+6.3, +7.3], W–T–L 3–0–0 — clearly ahead.
- wise-men 3.14.0: beats every rival — clearly ahead of all seven.

- wise-men-flash 0.1.0 against wise-men 3.14.0: −0.8 [−2.7, +0.7], W–T–L 1–0–2 — behind, with an interval that includes zero.
- wise-men-flash 0.1.0 against Warp council: +3.9 [+2.3, +5.7], W–T–L 3–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against llm-council: +5.4 [+1.0, +9.0], W–T–L 3–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against LifeOS Council: +5.6 [+3.0, +10.3], W–T–L 3–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against ECC council: +6.3 [+5.0, +7.3], W–T–L 3–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against superpowers brainstorming: +7.9 [+5.7, +11.0], W–T–L 3–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against mattpocock grilling: +6.3 [+4.3, +9.0], W–T–L 3–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against plain answer: +6.1 [+4.7, +7.7], W–T–L 3–0–0 — clearly ahead.
- wise-men-flash 0.1.0: beats every rival — clearly ahead of all seven.

- Axes, wise-men 3.14.0: the highest insight, practical use and risk awareness of the nine arms; above every rival on 4 of 5 axes.
- Axes, wise-men-flash 0.1.0: the highest dissent quality of the nine arms; above every rival on 4 of 5 axes.
- Time and cost, wise-men 3.14.0: median 49.1 min and $15.64 a question; faster than no rival council, cheaper than no rival council.
- Time and cost, wise-men-flash 0.1.0: median 16.8 min and $3.93 a question; faster than no rival council, cheaper than llm-council.

Judge agreement: mean SD of the three judges' totals 0.71.

## Per question (mean of three judges, total /25)

| question | wise-men 3.14.0 | wise-men-flash 0.1.0 | Warp council | llm-council | LifeOS Council | ECC council | superpowers brainstorming | mattpocock grilling | plain answer |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R501 (engineering, choice) | 23.33 | 24.00 | 20.33 | 17.67 | 13.67 | 17.33 | 13.00 | 18.33 | 16.33 |
| R506 (writing, register) | 23.67 | 23.33 | 17.67 | 14.33 | 20.00 | 16.00 | 17.67 | 14.33 | 17.33 |
| R507 (ethics, obligations) | 24.00 | 21.33 | 19.00 | 20.33 | 18.33 | 16.33 | 14.33 | 17.00 | 16.67 |

## Deviations and disclosures

- Every answer is new: all nine arms answered every question in this round, in the same days and on the same models. No earlier answer is reused.
- Rival versions: each rival skill at its latest commit on 2026-09-24. Only superpowers brainstorming had changed since the earlier rounds (2026-09-19: a shared-understanding step and path-specific approval gates). Two rivals were given files earlier rounds did not supply, because their skill files point at them: LifeOS Council its two workflow files, superpowers brainstorming its visual-companion and spec-reviewer files.
- Adaptations, unchanged from earlier rounds: brainstorming, grilling and ECC's council state the answers they assume instead of waiting for a human; Warp's council runs its members on Claude models only, with no approval pause; LifeOS Council skips its local voice notification.
- Orchestrators run on Sonnet; each skill's own subagents run on the models the skill names, through Claude Code's tier aliases as they resolved during the run. Every judge and every arm is a Claude model, and every spawned agent inherits the account's global instruction to write tersely. No human grades were collected.
- Cost is priced at the 2026-07 list rates in this file; a model released since is priced at its tier's rate.
- R507, wise-men 3.14.0: the orchestrator wrote a status line ('Council complete. Final answer below.') above the memo; normalization cut it, so the judges did not see it; a user would have
- R507, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> here and in the three blinded packets after judging; the judges saw the unredacted path

## Reproduce

`python3 eval-data/head-to-head/h2h5.py report` prints the table and comparisons; `results` rewrites this file; `verify` rebuilds every blinded packet from the raw answers and re-parses every judgment. Time and cost were computed from local agent transcripts when each answer was saved and are stored in the raw file headers; the transcripts themselves are not in the repository.
