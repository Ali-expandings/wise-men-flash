# Head-to-head round 5 — the current wise-men and wise-men-flash against every rival (pre-registration)

Written and committed 2026-09-24, before the round's questions were written and before any round-5 run. Nothing below changes after this commit except through dated amendments; results go in `RESULTS-V5.md`. Rounds 1–4 stand as published.

## Why round 5

Round 3 was the last round with every rival — Warp's council, llm-council, LifeOS Council, ECC's council, superpowers brainstorming, mattpocock grilling and a plain answer — and it measured wise-men 3.11.0. Round 4 measured 3.13.0 and its fast profile against only Warp's council, llm-council and a plain answer, and stopped at five of eight questions: the writing, ethics and personal questions never ran. Since then 3.13.1 removed process notes from answers, 3.14.0 ships the full council only, and the fast profile became its own skill, wise-men-flash 0.1.0 (github.com/Ali-expandings/wise-men-flash). Round 5 measures both current versions against every rival from rounds 1–4, each at its latest version, on eight new questions — one per slot, so every kind of question runs.

## Questions

Eight questions written for this round by a fresh Opus agent told nothing about the arms, the skills or the study. Its prompt is `question-author-prompt-5.txt`: round 4's prompt word for word, with round 4's eight topics added to the topics to avoid and the ids changed to R501–R508. Its output is `questions-r5.yaml`, used exactly as returned. The slots are round 4's: an engineering choice, an engineering diagnosis, a product decision with a questionable premise, how far to trust a number, how seriously to take a kind of evidence, the register of a hard message, ethical obligations, and a personal decision with a stated leaning.

## Arms — nine per question, 72 runs, every answer new

| arm | source | version | notes |
|---|---|---|---|
| `wise-men-3.14` | Ali-expandings/wise-men `SKILL.md` v3.14.0 | as of `770c75a` | may Read `SKILL.md` and `resources/`, never `eval-data/`; writes only to a scratch folder |
| `wise-men-flash` | Ali-expandings/wise-men-flash `SKILL.md` v0.1.0 | `dbfdcef` | self-contained: may Read only its `SKILL.md`; members run as the Read/Grep/Glob `wise-member` agent |
| `warp-council` | warpdotdev/common-skills `.agents/skills/council/SKILL.md` | `69b4753651ab` (skill file unchanged since round 2) | round 2's adaptations: members launched as Claude Code subagents on Claude models only, no approval pause, members read-only |
| `llm-council` | aiwithremy/claude-skills-llm-council `SKILL.md` | `55ee36e89e0f` (skill file unchanged since `1162f272ab94`) | as round 4 |
| `lifeos-council` | danielmiessler/LifeOS `LifeOS/install/skills/Council/` | `5e2f2e8c0abd` (`SKILL.md` unchanged since `36c6f01e9c2c`, context files since `3baba67056a0`) | as round 1, **plus the two workflow files its `SKILL.md` names** (`Workflows/Debate.md`, `Workflows/Quick.md`), which rounds 1–3 did not supply |
| `ecc-council` | affaan-m/ECC `skills/council/SKILL.md` | `bf70150eb2df` (skill file unchanged since `db7f2a6fd5b0`) | round 2's no-human rule |
| `brainstorming` | obra/superpowers `skills/brainstorming/` | `5bf4e7801107` — **changed since round 1** (2026-09-19: a shared-understanding step, approval gates per path) | round 1's no-human rule, **plus its two companion files** (`visual-companion.md`, `spec-document-reviewer-prompt.md`), which round 1 did not supply; a design document it would write goes to a scratch folder and into its output, never into a project |
| `grilling` | mattpocock/skills `skills/productivity/grilling/SKILL.md` | `c55ee46073ed` (skill file unchanged since `85f83d3fde1d`) | round 1's no-human rule |
| `direct` | no skill | — | round 4's prompt |

**Harness**, identical to rounds 1–4: a fresh `general-purpose` orchestrator on Sonnet per arm per question receives the skill files and the question verbatim; skills spawn their subagents in the foreground on the models they name; each arm may Read only its own skill files and never searches the filesystem or notes; it returns only the finished output; an incomplete run is re-run once, and a second failure is recorded and scored as absent. The prompts are each arm's most recent prompt from rounds 1–4, word for word apart from file paths and the additions in the table; all nine are in `arm-prompts-r5.md`. The flash prompt is the wise-men prompt with the skill path, the readable file and the agent-type note changed.

**Order and pacing.** Questions run in this order, fixed now so that an early stop cannot again leave out the same kinds of question: **R506, R501, R507, R503, R508, R502, R504, R505**. All nine arms of a question run before it is judged; judging may overlap the next question's runs. At most four heavy arms (the six councils) run at once; the three single-pass arms run alongside. The account runs on a plan with 5-hour and weekly limits: a question starts only when the remaining allowance can plausibly cover it, and otherwise the round waits for the reset. A run the limit cuts anyway is resumed from its own transcript, marked, and left out of the time medians only (as round 4).

**Stop rule.** The round runs to eight questions. If it has to stop earlier it is reported as stopped at N, with round 4's disclosure, and nothing is claimed about the questions not run.

## Judges

Three fresh Opus judges per question, 24 judgments. Each judge sees its own sealed order of the nine answers as A–I: `blinding5.yaml`, seed 20260925, generated in this commit by `h2h5.py seal`. Judge prompt `judge-prompt-r5.txt`: round 4's error-first prompt (`judge-prompt-5.txt`) with only the count and letters changed, five (A–E) to nine (A–I). Each judge is told to Read its packet and nothing else, as in round 4. Normalization: `normalize()` from rounds 1–4, unchanged; both wise-men arms get wise-men's rule. The author's first name, which subagents inherit from the author's global config, is redacted to "the user" in raw files before blinding.

## Measures

As round 4 (`PREREG-4.md`, Measures):

- **Quality**: question score = mean of the three judges' totals (max 25); per-arm and per-axis means over the questions; each wise-men arm against every other arm: wins–ties–losses and the mean paired difference with a 95% percentile bootstrap interval over questions (10,000 resamples, seed 20260925); judge agreement.
- **Time**: the orchestrator's first-to-last transcript timestamp; per-arm median over runs no usage limit interrupted.
- **Cost**: every token the run used — the orchestrator's and every agent spawned under it, at any depth, matched by the exact prompt sent — priced at the 2026-07 list rates in `h2h5.py` (a model released since is priced at its tier's rate); per-arm median USD and median calls (the orchestrator's own spawns). Round 4 priced direct children only; its councils spawned nothing deeper, so the two are comparable.

## Hypotheses

- **H1** wise-men 3.14.0 beats every rival: clearly ahead of each of the seven.
- **H2** wise-men-flash 0.1.0 beats every rival.
- **H3** wise-men-flash is not clearly behind wise-men 3.14.0 (the interval of flash minus wise-men does not lie wholly below zero).

`wise-men-flash`'s `PREREG-1.md` H3 — its 0.1.0 changes against the 3.13 `--fast` profile — is not tested here: that would need the old profile re-run on these questions.

## Wording rules

As round 4: "ahead" and "behind" by the mean paired difference; "clearly ahead" when the interval's lower bound is above zero; "beats every rival" when clearly ahead of all seven rivals; "highest on every axis" only if the arm's mean is the highest of the nine on all five axes. Time and cost: "faster than X" or "cheaper than X" when the arm's median is below X's, with the rival councils as targets; no council can be faster or cheaper than the plain answer, so those numbers are reported, never claimed. Anything not met is stated as not met, next to what was.

## Reporting

`RESULTS-V5.md` is generated from `parsed-v5/` and the raw headers by `h2h5.py results`. Both READMEs lead with round 5, whatever it shows, with every deviation disclosed: wise-men's reports quality (as since 3.14.0), wise-men-flash's quality, time and cost. `h2h5.py` and every round-5 file are copied byte-identical into the wise-men-flash repository.
