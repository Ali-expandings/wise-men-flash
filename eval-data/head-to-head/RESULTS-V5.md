# Head-to-head round 5 results

**In progress: 5 of 8 questions judged.** The remaining questions (R502, R504, R505) are being run in the pre-registered order, paced by the account's usage limits; this file, the README tables and the charts are regenerated as each one is judged. Every comparison below is over the questions judged so far; intervals are 95% percentile bootstraps over them, and with this few questions they are wide.

Eight questions written for this round by an author that knew nothing about the arms ([`PREREG-5.md`](PREREG-5.md), [`questions-r5.yaml`](questions-r5.yaml)); nine arms, every answer new; three blind Opus judges per question with sealed orders ([`blinding5.yaml`](blinding5.yaml)) and round 4's error-first judge prompt for nine answers ([`judge-prompt-r5.txt`](judge-prompt-r5.txt)). Minutes are the orchestrator's first-to-last transcript timestamp; calls are its subagent spawns; USD prices every token the run used — the orchestrator's and every agent spawned under it, input, output, cache reads and cache writes — at 2026-07 list rates. No council can be faster or cheaper than the plain answer; the pre-registered time and cost comparisons are against the rival councils.

| round 5 (5 of 8 questions) | total /25 | correct | insight | practical | risk | dissent | median minutes | median calls | median list-price USD |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **wise-men 3.14.0** | 23.7 | 3.9 | 5.0 | 4.9 | 5.0 | 4.9 | 49.1 | 16 | 16.31 |
| **wise-men-flash 0.1.0** | 23.1 | 3.7 | 4.9 | 4.8 | 4.7 | 4.9 | 16.8 | 4 | 3.93 |
| Warp council | 18.5 | 3.9 | 3.7 | 4.0 | 4.1 | 2.8 | 10.0 | 3 | 2.64 |
| LifeOS Council | 17.8 | 3.1 | 3.7 | 3.1 | 3.7 | 4.2 | 8.7 | 12 | 3.90 |
| llm-council | 17.3 | 3.1 | 3.9 | 3.2 | 3.8 | 3.4 | 12.8 | 11 | 4.52 |
| plain answer | 17.0 | 4.1 | 3.1 | 4.1 | 3.5 | 2.2 | 1.5 | 0 | 0.26 |
| ECC council | 16.3 | 3.5 | 3.3 | 3.2 | 3.3 | 3.1 | 4.6 | 3 | 1.30 |
| mattpocock grilling | 16.1 | 3.5 | 3.5 | 3.7 | 3.3 | 2.1 | 5.2 | 0 | 0.63 |
| superpowers brainstorming | 16.0 | 3.3 | 3.2 | 3.6 | 3.5 | 2.5 | 7.9 | 1 | 1.40 |

- wise-men 3.14.0 against wise-men-flash 0.1.0: +0.6 [−0.3, +1.7], W–T–L 4–0–1 — ahead.
- wise-men 3.14.0 against Warp council: +5.3 [+4.1, +6.1], W–T–L 5–0–0 — clearly ahead.
- wise-men 3.14.0 against llm-council: +6.4 [+3.7, +9.1], W–T–L 5–0–0 — clearly ahead.
- wise-men 3.14.0 against LifeOS Council: +5.9 [+4.5, +7.9], W–T–L 5–0–0 — clearly ahead.
- wise-men 3.14.0 against ECC council: +7.4 [+6.5, +8.3], W–T–L 5–0–0 — clearly ahead.
- wise-men 3.14.0 against superpowers brainstorming: +7.7 [+6.1, +9.3], W–T–L 5–0–0 — clearly ahead.
- wise-men 3.14.0 against mattpocock grilling: +7.6 [+5.8, +9.5], W–T–L 5–0–0 — clearly ahead.
- wise-men 3.14.0 against plain answer: +6.7 [+6.4, +7.1], W–T–L 5–0–0 — clearly ahead.
- wise-men 3.14.0: beats every rival — clearly ahead of all seven.

- wise-men-flash 0.1.0 against wise-men 3.14.0: −0.6 [−1.7, +0.3], W–T–L 1–0–4 — behind, with an interval that includes zero.
- wise-men-flash 0.1.0 against Warp council: +4.7 [+3.3, +5.8], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against llm-council: +5.8 [+2.6, +9.0], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against LifeOS Council: +5.3 [+3.4, +7.9], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against ECC council: +6.8 [+5.8, +7.9], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against superpowers brainstorming: +7.1 [+5.8, +9.1], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against mattpocock grilling: +7.0 [+5.1, +9.1], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against plain answer: +6.1 [+5.3, +7.0], W–T–L 5–0–0 — clearly ahead.
- wise-men-flash 0.1.0: beats every rival — clearly ahead of all seven.

- Axes, wise-men 3.14.0: the highest insight, practical use and risk awareness of the nine arms, tied for the highest dissent quality; above every rival on 4 of 5 axes.
- Axes, wise-men-flash 0.1.0: the highest score on no axis of the nine arms, tied for the highest dissent quality; above every rival on 4 of 5 axes.
- Time and cost, wise-men 3.14.0: median 49.1 min and $16.31 a question; faster than no rival council, cheaper than no rival council.
- Time and cost, wise-men-flash 0.1.0: median 16.8 min and $3.93 a question; faster than no rival council, cheaper than llm-council.

Judge agreement: mean SD of the three judges' totals 0.68.

## Per question (mean of three judges, total /25)

| question | wise-men 3.14.0 | wise-men-flash 0.1.0 | Warp council | llm-council | LifeOS Council | ECC council | superpowers brainstorming | mattpocock grilling | plain answer |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R501 (engineering, choice) | 23.33 | 24.00 | 20.33 | 17.67 | 13.67 | 17.33 | 13.00 | 18.33 | 16.33 |
| R503 (product, questionable-premise) | 24.00 | 23.67 | 17.67 | 13.33 | 18.00 | 17.33 | 18.00 | 13.33 | 17.67 |
| R506 (writing, register) | 23.67 | 23.33 | 17.67 | 14.33 | 20.00 | 16.00 | 17.67 | 14.33 | 17.33 |
| R507 (ethics, obligations) | 24.00 | 21.33 | 19.00 | 20.33 | 18.33 | 16.33 | 14.33 | 17.00 | 16.67 |
| R508 (personal, personal) | 23.67 | 23.33 | 17.67 | 21.00 | 19.00 | 14.67 | 17.00 | 17.67 | 17.00 |

## Deviations and disclosures

- Every answer is new: all nine arms answered every question in this round, in the same days and on the same models. No earlier answer is reused.
- Rival versions: each rival skill at its latest commit on 2026-09-24. Only superpowers brainstorming had changed since the earlier rounds (2026-09-19: a shared-understanding step and path-specific approval gates). Two rivals were given files earlier rounds did not supply, because their skill files point at them: LifeOS Council its two workflow files, superpowers brainstorming its visual-companion and spec-reviewer files.
- Adaptations, unchanged from earlier rounds: brainstorming, grilling and ECC's council state the answers they assume instead of waiting for a human; Warp's council runs its members on Claude models only, with no approval pause; LifeOS Council skips its local voice notification.
- Orchestrators run on Sonnet; each skill's own subagents run on the models the skill names, through Claude Code's tier aliases as they resolved during the run. Every judge and every arm is a Claude model, and every spawned agent inherits the account's global instruction to write tersely. No human grades were collected.
- Cost is priced at the 2026-07 list rates in this file; a model released since is priced at its tier's rate.
- R503, wise-men-flash 0.1.0: the orchestrator ran 2 web searches during the skill's post-council verification step (runbook step 6, which checks flagged claims on the web); members stayed offline
- R503, superpowers brainstorming: the author's first name (inherited from global config) redacted to "the user"
- R503, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> before blinding
- R507, wise-men 3.14.0: the orchestrator wrote a status line ('Council complete. Final answer below.') above the memo; normalization cut it, so the judges did not see it; a user would have
- R507, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> here and in the three blinded packets after judging; the judges saw the unredacted path
- R508, superpowers brainstorming: the author's first name (inherited from global config) redacted to "the user"
- R508, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> before blinding
- R508, mattpocock grilling: the skill tells its orchestrator to dispatch a sub-agent to find facts; its one research sub-agent ran 21 web searches and 3 page fetches (Firecrawl) on business-sale norms before the answer was written; the orchestrator itself stayed offline

## Reproduce

`python3 eval-data/head-to-head/h2h5.py report` prints the table and comparisons; `results` rewrites this file; `verify` rebuilds every blinded packet from the raw answers and re-parses every judgment. Time and cost were computed from local agent transcripts when each answer was saved and are stored in the raw file headers; the transcripts themselves are not in the repository.
