# Head-to-head round 5 results

**In progress: 7 of 8 questions judged.** The remaining questions (R504) are being run in the pre-registered order, paced by the account's usage limits; this file, the README tables and the charts are regenerated as each one is judged. Every comparison below is over the questions judged so far; intervals are 95% percentile bootstraps over them, and with this few questions they are wide.

Eight questions written for this round by an author that knew nothing about the arms ([`PREREG-5.md`](PREREG-5.md), [`questions-r5.yaml`](questions-r5.yaml)); nine arms, every answer new; three blind Opus judges per question with sealed orders ([`blinding5.yaml`](blinding5.yaml)) and round 4's error-first judge prompt for nine answers ([`judge-prompt-r5.txt`](judge-prompt-r5.txt)). Minutes are the orchestrator's first-to-last transcript timestamp; calls are its subagent spawns; USD prices every token the run used — the orchestrator's and every agent spawned under it, input, output, cache reads and cache writes — at 2026-07 list rates. No council can be faster or cheaper than the plain answer; the pre-registered time and cost comparisons are against the rival councils.

| round 5 (7 of 8 questions) | total /25 | correct | insight | practical | risk | dissent | median minutes | median calls | median list-price USD |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **wise-men 3.14.0** | 23.7 | 3.9 | 5.0 | 4.9 | 5.0 | 4.9 | 49.1 | 16 | 16.31 |
| **wise-men-flash 0.1.0** | 23.4 | 3.8 | 5.0 | 4.9 | 4.8 | 5.0 | 16.8 | 4 | 3.93 |
| Warp council | 19.0 | 3.9 | 3.8 | 4.1 | 4.1 | 3.1 | 10.0 | 3 | 2.64 |
| LifeOS Council | 17.9 | 3.1 | 3.7 | 3.2 | 3.7 | 4.0 | 9.1 | 12 | 3.90 |
| plain answer | 16.9 | 4.1 | 3.2 | 4.0 | 3.3 | 2.1 | 1.5 | 0 | 0.26 |
| llm-council | 16.8 | 2.9 | 3.9 | 3.1 | 3.6 | 3.2 | 15.3 | 11 | 4.89 |
| superpowers brainstorming | 16.1 | 3.3 | 3.3 | 3.7 | 3.4 | 2.4 | 7.9 | 1 | 1.40 |
| ECC council | 15.9 | 3.4 | 3.0 | 3.1 | 3.2 | 3.0 | 5.1 | 3 | 1.35 |
| mattpocock grilling | 15.0 | 3.1 | 3.3 | 3.5 | 3.1 | 2.0 | 5.2 | 0 | 0.63 |

- wise-men 3.14.0 against wise-men-flash 0.1.0: +0.3 [−0.4, +1.2], W–T–L 4–0–3 — ahead.
- wise-men 3.14.0 against Warp council: +4.6 [+3.5, +5.7], W–T–L 7–0–0 — clearly ahead.
- wise-men 3.14.0 against llm-council: +6.9 [+4.8, +8.9], W–T–L 7–0–0 — clearly ahead.
- wise-men 3.14.0 against LifeOS Council: +5.8 [+4.7, +7.3], W–T–L 7–0–0 — clearly ahead.
- wise-men 3.14.0 against ECC council: +7.8 [+6.9, +8.8], W–T–L 7–0–0 — clearly ahead.
- wise-men 3.14.0 against superpowers brainstorming: +7.5 [+6.4, +8.8], W–T–L 7–0–0 — clearly ahead.
- wise-men 3.14.0 against mattpocock grilling: +8.6 [+6.8, +10.3], W–T–L 7–0–0 — clearly ahead.
- wise-men 3.14.0 against plain answer: +6.8 [+5.2, +8.5], W–T–L 7–0–0 — clearly ahead.
- wise-men 3.14.0: beats every rival — clearly ahead of all seven.

- wise-men-flash 0.1.0 against wise-men 3.14.0: −0.3 [−1.2, +0.4], W–T–L 3–0–4 — behind, with an interval that includes zero.
- wise-men-flash 0.1.0 against Warp council: +4.3 [+3.3, +5.3], W–T–L 7–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against llm-council: +6.6 [+4.0, +8.9], W–T–L 7–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against LifeOS Council: +5.5 [+4.0, +7.4], W–T–L 7–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against ECC council: +7.5 [+6.3, +8.8], W–T–L 7–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against superpowers brainstorming: +7.2 [+6.1, +8.7], W–T–L 7–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against mattpocock grilling: +8.3 [+6.2, +10.3], W–T–L 7–0–0 — clearly ahead.
- wise-men-flash 0.1.0 against plain answer: +6.5 [+4.9, +8.5], W–T–L 7–0–0 — clearly ahead.
- wise-men-flash 0.1.0: beats every rival — clearly ahead of all seven.

- Axes, wise-men 3.14.0: the highest insight and risk awareness of the nine arms, tied for the highest practical use; above every rival on 4 of 5 axes.
- Axes, wise-men-flash 0.1.0: the highest dissent quality of the nine arms, tied for the highest practical use; above every rival on 4 of 5 axes.
- Time and cost, wise-men 3.14.0: median 49.1 min and $16.31 a question; faster than no rival council, cheaper than no rival council.
- Time and cost, wise-men-flash 0.1.0: median 16.8 min and $3.93 a question; faster than no rival council, cheaper than llm-council.

Judge agreement: mean SD of the three judges' totals 0.67.

## Per question (mean of three judges, total /25)

| question | wise-men 3.14.0 | wise-men-flash 0.1.0 | Warp council | llm-council | LifeOS Council | ECC council | superpowers brainstorming | mattpocock grilling | plain answer |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R501 (engineering, choice) | 23.33 | 24.00 | 20.33 | 17.67 | 13.67 | 17.33 | 13.00 | 18.33 | 16.33 |
| R502 (engineering, diagnosis) | 23.33 | 24.00 | 20.00 | 15.00 | 18.67 | 16.00 | 16.00 | 12.00 | 12.33 |
| R503 (product, questionable-premise) | 24.00 | 23.67 | 17.67 | 13.33 | 18.00 | 17.33 | 18.00 | 13.33 | 17.67 |
| R505 (research, evidence) | 23.67 | 24.00 | 21.00 | 15.67 | 17.33 | 13.33 | 17.00 | 12.67 | 20.67 |
| R506 (writing, register) | 23.67 | 23.33 | 17.67 | 14.33 | 20.00 | 16.00 | 17.67 | 14.33 | 17.33 |
| R507 (ethics, obligations) | 24.00 | 21.33 | 19.00 | 20.33 | 18.33 | 16.33 | 14.33 | 17.00 | 16.67 |
| R508 (personal, personal) | 23.67 | 23.33 | 17.67 | 21.00 | 19.00 | 14.67 | 17.00 | 17.67 | 17.00 |

## Deviations and disclosures

- Every answer is new: all nine arms answered every question in this round, in the same days and on the same models. No earlier answer is reused.
- Rival versions: each rival skill at its latest commit on 2026-09-24. Only superpowers brainstorming had changed since the earlier rounds (2026-09-19: a shared-understanding step and path-specific approval gates). Two rivals were given files earlier rounds did not supply, because their skill files point at them: LifeOS Council its two workflow files, superpowers brainstorming its visual-companion and spec-reviewer files.
- Adaptations, unchanged from earlier rounds: brainstorming, grilling and ECC's council state the answers they assume instead of waiting for a human; Warp's council runs its members on Claude models only, with no approval pause; LifeOS Council skips its local voice notification.
- Orchestrators run on Sonnet; each skill's own subagents run on the models the skill names, through Claude Code's tier aliases as they resolved during the run. Every judge and every arm is a Claude model, and every spawned agent inherits the account's global instruction to write tersely. No human grades were collected.
- Cost is priced at the 2026-07 list rates in this file; a model released since is priced at its tier's rate.
- Order: each question's first arm started in the pre-registered order, but to fit the account's usage limits the questions overlapped — a later question's arms ran while an earlier question's slowest arm finished — and R505 was judged before R504. Judges saw one question each, so the order of judging touches no score.
- Web use: every arm ran with the tools Claude Code gives a general-purpose agent, web search included, and no arm prompt mentions the web. A scan of every run's transcripts — the orchestrator and every agent spawned under it — found web use only in the runs whose notes below say so.
- R502, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> before blinding
- R503, wise-men-flash 0.1.0: the orchestrator ran 2 web searches during the skill's post-council verification step (runbook step 6, which checks flagged claims on the web); members stayed offline
- R503, superpowers brainstorming: the author's first name (inherited from global config) redacted to "the user"
- R503, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> before blinding
- R505, wise-men 3.14.0: the orchestrator ran 4 web searches (Firecrawl) to check figures the members had marked unverified — 3 after the members answered and before peer review (nothing from them entered the reviewers' grading packet), 1 after the synthesis check; the memo's closing line reports the one figure it corrected; members and reviewers stayed offline
- R505, wise-men-flash 0.1.0: the orchestrator wrote a paragraph above the memo (that the checker failed the draft on CLAIMS and that it fixed the draft instead of spending a fifth call on a re-check); normalization cut it, so the judges did not see it; a user would have
- R505, Warp council: its council members ran 5 web searches (Firecrawl) between them on the published studies; nothing in the skill or the prompt asks for or forbids it; the orchestrator itself stayed offline
- R505, mattpocock grilling: the skill tells its orchestrator to dispatch a sub-agent to find facts; its one research sub-agent ran 20 web searches and 2 page fetches (Firecrawl) on the published studies before the answer was written; the orchestrator itself stayed offline
- R507, wise-men 3.14.0: the orchestrator wrote a status line ('Council complete. Final answer below.') above the memo; normalization cut it, so the judges did not see it; a user would have
- R507, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> here and in the three blinded packets after judging; the judges saw the unredacted path
- R508, superpowers brainstorming: the author's first name (inherited from global config) redacted to "the user"
- R508, superpowers brainstorming: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> before blinding
- R508, mattpocock grilling: the skill tells its orchestrator to dispatch a sub-agent to find facts; its one research sub-agent ran 21 web searches and 3 page fetches (Firecrawl) on business-sale norms before the answer was written; the orchestrator itself stayed offline

## Reproduce

`python3 eval-data/head-to-head/h2h5.py report` prints the table and comparisons; `results` rewrites this file; `verify` rebuilds every blinded packet from the raw answers and re-parses every judgment. Time and cost were computed from local agent transcripts when each answer was saved and are stored in the raw file headers; the transcripts themselves are not in the repository.
