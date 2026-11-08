# Round 6: a format-matched control and a checker on/off test (pre-registration)

Written 2026-11-04 and amended 2026-11-08 (a second control arm, `plain-memo-short`, added at the owner's OK), before any rewrite, run or judgment. The owner approved running it on 2026-11-08. It is committed on `master` on its own before step 1 below; that commit's hash goes at the top of `RESULTS-6.md`. Nothing here changes after that commit except through dated amendments, and every deviation is listed in `RESULTS-6.md`. Round 5 stands as published.

## Why

Round 5 ([`../head-to-head/PREREG-5.md`](../head-to-head/PREREG-5.md), [`RESULTS-V5.md`](../head-to-head/RESULTS-V5.md)) put wise-men-flash 0.1.0 at 23.4/25 and wise-men 3.14.0 at 23.6, against 16.8 for a plain answer. Two objections were never tested. First, LLM judges are known to favour longer, more structured answers (Zheng et al. 2023, the MT-Bench paper), and the plain answers were 471–903 words of loose prose while flash's memos were 1,430–2,000 words under six headings. Second, nothing has measured whether flash's one fresh checker makes the memo better. The wise-men council of 2026-11-04 (`council/2026-11-04-growth-plan-record.md` in the growth project) recommended running both before any public launch, and publishing whatever they show.

Design rule (the repository owner's, below "the owner"): Claude only. Every answer, rewrite, audit, judge and classifier below is a Claude model; no outside model provider is used anywhere. So this round can test a known bias of LLM judges, but it cannot answer "AI validating AI". Only human blind ratings can, and they are a separate step, not part of this file.

## What was looked at before writing this

To size the design, and with no judging and no scores: the round-5 raw answers and their word counts; the local Claude Code transcripts of the round-5 flash runs and of the four 0.2.0 runs in [`../consistency-check/`](../consistency-check/PLAN.md), only to find each run's checker call, read its PASS/FAIL lines, and compare the draft it was given with the memo that shipped; and the judge model recorded in the round-5 judge transcripts. Findings that shape the design:

- The repository keeps only final answers. The pre-checker drafts are not in `eval-data/`, but each run's checker prompt holds the draft it was given, and those transcripts are still on this machine for all 8 round-5 flash runs and all 4 consistency-check runs.
- In round 5 (0.1.0) the checker passed every check on R501, R502, R504 and R506, and the shipped memo is byte-identical to the draft after normalization. On R503, R505 and R507 it failed CLAIMS, and on R508 DISSENT; the Chairman then edited the draft.
- In the four 0.2.0 runs the checker failed at least two checks every time (R502: CLAIMS, COVERAGE, CONSISTENCY; R504: CLAIMS, CONSISTENCY; R506: DISCLOSURE, CLAIMS, COVERAGE, CONSISTENCY; R508: CLAIMS, COVERAGE, CONSISTENCY), and every draft was edited.
- All 24 round-5 judges ran on `claude-opus-5-5`, and the `opus` alias still resolves to it (subagent transcripts, 2026-11-04). Round 5's answers were written with `sonnet` = Sonnet 5 and `haiku` = Haiku 4.5; today `sonnet` resolves to Sonnet 5.5 and `haiku` to Haiku 5.5, as in the 2026-10-22 consistency check.

## Part A: the format-matched control

**The control arm (`plain-memo`).** For each round-5 question, the stored plain answer (`../head-to-head/raw/<Q>/direct.md`) is rewritten into flash's memo format by a fresh Claude subagent, with no new analysis.

- Rewriter: a fresh `wise-member` agent (Read/Grep/Glob only, so no web and no spawning) on `sonnet`, the tier that wrote both the plain answers and flash's memos in round 5. It gets the question, the plain answer, the six headers and the length target, all in the prompt file `rewrite-prompt.txt`. It never sees flash's, wise-men's or any other arm's answer, and is not told what the rewrite is for. The agent's own file asks it to tag unchecked numbers "(unverified)"; the rewrite prompt overrides that for this task, and the script check below catches any tag that slips in.
- Format: exactly `## Recommendation`, `## Why`, `## What to do`, `## Risks of this plan`, `## Strongest counter-position`, `## Confidence`, in that order, nothing before the first and nothing after the last section. Each section takes only what the source says on that point: Recommendation its bottom line, Why its reasons, What to do its steps, Risks the risks and caveats it states, Strongest counter-position the strongest objection or limit the source itself raises against its own answer, at the strength the source gives it. Confidence maps the source's own hedges with a fixed rule: an unhedged claim is High; "likely", "probably", "usually", "typically" or "suggests" is Medium; "may", "might", "could", "possibly" or "unclear" is Low. The unknowns listed are only those the source names. A section the source gives nothing for gets one fixed sentence: "No case against this recommendation is made beyond the risks above." (counter-position), "No further risks are named." (risks), "No unknowns are named." (confidence).
- Length: flash's normalized word count on the same question, ±10% (R501 1,717; R502 1,430; R503 1,617; R504 1,470; R505 2,000; R506 1,579; R507 1,903; R508 1,581).
- **A second control arm, `plain-memo-short`,** separates format from length: the same rewrite under every rule above, except that its length is the plain answer's own normalized word count ±10% instead of flash's. It needs no padding, so it answers the objection that stretching the plain answer makes it repetitive and favours flash. It is produced, checked and audited exactly like `plain-memo`, by separate fresh agents.
- Allowed: restate a source sentence in fuller words, split or merge sentences, move content between sections, restate a point where the memo format calls for it (the Recommendation sums up what the later sections say), and connecting sentences that make no claim. Not allowed: any fact, number, example, mechanism, option, step, risk, caveat, counter-argument or unknown the source does not state, and any change in how certain a claim is, in either direction.

**How "nothing new" is enforced and checked.**

1. Script checks (`fc6.py check <Q>`): the six headers, in order, nothing outside them; the word count in the band; every number in the rewrite (digits, %, $, ranges, dates) appears in the source; no URL, citation or "(unverified" tag the source lacks; the author's first name absent.
2. Blind audit: a fresh `wise-member` on `opus` (the strongest tier, above the rewriter's) gets the question and both texts with every sentence numbered by `fc6.py` (prompt `audit-prompt.txt`). For each rewrite sentence it names the source sentences it restates, or marks it NEW (saying what is new), STRONGER or WEAKER (a change of certainty). The script then marks every source sentence cited nowhere as DROPPED. A rewrite passes with zero NEW, zero STRONGER/WEAKER and zero DROPPED.
3. One retry: a failing rewrite goes back to a fresh rewriter with the audit's list and is audited once more. If it still fails, `fc6.py` deletes every sentence still marked NEW, STRONGER or WEAKER (a section left empty gets its fixed sentence), and any DROPPED content is disclosed rather than put back. No question is excluded for this; every deletion and drop is listed in `RESULTS-6.md`.
4. Human spot check: before any judging, the owner reads source and both rewrites side by side for two questions drawn in `seal6.yaml` (about 15 minutes). Anything he marks as new content is deleted the same way and listed. Judging starts only after the owner's OK.

**Packets.** A rewrite of the plain answer sitting next to the plain answer itself would show the judge two versions of the same content, so the two never share a packet. Each question gets two packet types, three answers each:

- **M**: flash 0.1.0, wise-men 3.14.0 and `plain-memo`;
- **P**: flash 0.1.0, wise-men 3.14.0 and the original plain answer;
- **S**: flash 0.1.0, wise-men 3.14.0 and `plain-memo-short`.

Flash and wise-men are the stored round-5 answers, byte for byte. Every answer is normalized with round 5's `normalize()`: the plain answer by the `direct` rule, every memo by the wise-men rule. For `plain-memo`, the script asserts that this rule removes nothing but the provenance header.

## Part B: the checker on and off

**The comparison.** One flash run gives two texts: the draft the checker was given (after step 6's verification of flagged claims) and the memo that shipped. Both come from the same brief, the same three member answers and the same Chairman, so the member budget is matched exactly. The only difference is the checker's one cheap-tier call and the Chairman's edits in reply to it. This tests checker against no checker; it does not test a fresh checker against the Chairman spending the same call on a second self-review, which would need a new arm.

**B1, the shipped version (0.2.0), primary.** Eight questions.

- R502, R504, R506, R508, from data already on disk: the drafts sit in the checker prompts of the 2026-10-22 runs (session `9adc81fe-890f-46b2-a03e-059fac726935`; agents `a4b33fef412b2ff86`, `aaa7e67bfd9247418`, `a40fc420212bdbc0c`, `a3de0644c5ffd71eb`), and the shipped memos are `../consistency-check/answers/<Q>-new.md`. The SKILL.md those runs read differs from today's only in the version line and the sentence reporting the consistency check's result.
- R501, R503, R505, R507 have no 0.2.0 run, so **four new runs are needed**: flash at `SKILL.md` as of `aaabd74` (unchanged at `1d6a552`), round 5's exact flash arm prompt from [`../head-to-head/arm-prompts-r5.md`](../head-to-head/arm-prompts-r5.md), a fresh `general-purpose` orchestrator on `sonnet`, members and checker as the skill routes them. The arm prompt is not changed to save the draft; the draft is taken from the checker's prompt in the transcript, as for the stored runs. Step-6 web checks are allowed, as the skill allows them, and disclosed.

**B2, the round-5 version (0.1.0), secondary.** All eight drafts are on disk (session `e0ff67b0-e729-4db6-beb1-684d997142d1`; agents R501 `a287e44b3f073d195`, R502 `a99a6cbca9add8005`, R503 `a9379b375d2458bd1`, R504 `a5dbb7d30985e9039`, R505 `aa28d20743e2bd947`, R506 `a815e3ce94d94c7be`, R507 `a96a0a9a730dceb32`, R508 `ad18fe96b0b72aba8`), and the shipped memos are `../head-to-head/raw/<Q>/wise-men-flash.md`. R501, R502, R504 and R506 are identical pairs: they enter as ties (difference 0) and are not judged. Only R503, R505, R507 and R508 are judged. B2 does not test the shipped skill; it tells round 5's readers how much of the 23.4 the checker could have added.

**Extraction** (`fc6.py extract`): the draft is the memo text inside the checker's first prompt, from `## Recommendation` to the end of its `## Confidence` section, which is the `<draft>` block in 0.2.0 and the triple-quoted block after "Draft decision memo to check" in 0.1.0. It is normalized by the wise-men rule, with the first-name redaction `h2h5.py save` applies. Each file's header records the session and agent id and the SHA-256 of the source transcript, but no local path. The transcripts themselves stay off the repository, as round 5's did.

## Judges

As round 5: fresh Opus judges, three per packet, each told to Read its packet and nothing else (the judges' prompt in `arm-prompts-r5.md`, with the path and the answer count changed), run as `wise-member` on `opus` so Read-only is enforced, as in the consistency check. The judge model must be `claude-opus-5-5`, checked on the first judge's transcript; if the alias has moved, stop and ask the owner. The judge prompt is [`../head-to-head/judge-prompt-r5.txt`](../head-to-head/judge-prompt-r5.txt) with only the count and the letters changed (nine to three, A–I to A–C, for Part A; nine to two, A–I to A–B, for Part B, the consistency check's adaptation word for word), saved as `judge-prompt-r6-3.txt` and `judge-prompt-r6-2.txt`. Scores are parsed by round 5's `score_blocks()`.

Sealed orders are in `seal6.yaml`, generated by `fc6.py seal` (seed 20261104) before any rewrite or run, together with the spot-check draw. In each three-answer packet type, a seeded base order is rotated across j1–j3, so every answer sits in every slot once per question. In Part B, j1 is seeded, j2 is j1 reversed and j3 is seeded.

Judgments: Part A 8 questions × 3 packet types × 3 = 72; B1 8 × 3 = 24; B2 4 × 3 = 12; 108 in all.

## Measures

A question score is the mean of the three judges' totals (/25) for that answer in that packet; the axis scores are handled the same way. Comparisons are paired differences over questions, always within one packet type, with a 95% percentile bootstrap over questions (10,000 resamples, seed 20261104; `boot()` from `h2h5.py`). Scores from this round are never compared with round 5's numbers: packet size moves scores (the consistency check's two-answer packets scored the same answers 3.75 lower than round 5's nine-answer packets).

**Part A.** `D_ctrl` = flash − plain-memo (M packets). `D_plain` = flash − plain (P packets). The format effect `F` = `D_plain` − `D_ctrl` per question: how far the rewrite closed the gap, with flash as the anchor in both packets. The share of the gap that format and length explain is `S = F / D_plain`, computed on the means and bootstrapped by resampling questions jointly. The same quantities are computed with wise-men in place of flash. Per arm and packet type: all five axes, correctness first, and word counts.

**Part B.** `C` = shipped − draft, in total /25. Also, per axis, with correctness first: the number of internal contradictions the judges list in PASS 0, counted by a separate blind classifier exactly as in [`../consistency-check/classification.md`](../consistency-check/classification.md) (one fresh `wise-member` on `sonnet` sees only the letters A and B); the number of PASS 0 errors of any kind; and the word-count difference (in the edited pairs on disk, the shipped memo ran 18–139 words longer than its draft).

## Hypotheses and thresholds, fixed now

**A1 (primary): the win over the plain answer survives format matching**, judged by `D_ctrl`:

- **holds** if the interval's lower bound is above 0 and the mean `D_ctrl` is at least half the mean `D_plain`;
- **holds, but smaller** if the lower bound is above 0 and the mean `D_ctrl` is less than half the mean `D_plain`. This means most of the gap was format and length;
- **does not hold** if the interval includes 0 or lies below it.

A replication guard comes first: if the `D_plain` interval includes 0, the 3-answer sitting did not reproduce round 5's gap, A1 is reported as **inconclusive**, and `S` is not reported.

**A2 (secondary):** the same three outcomes and the same guard for wise-men − plain-memo.

**A3 (secondary, a stated prediction, not a gate):** `F` > 0, meaning format and length alone lift the plain answer. It is reported with its interval whatever the sign.

**A5 (secondary, reported, not a gate): format versus length.** `D_short` = flash − plain-memo-short (S packets). The format-only effect `F_fmt` = `D_plain` − `D_short` and the length effect `F_len` = `D_short` − `D_ctrl`, each with its interval. A1's three outcomes are also reported for `D_short`. If `D_short` holds while `D_ctrl` does not, the stretched rewrite, not the format, closed the gap, and the results page says so.

**A4 (secondary, reported, not a gate):** whether the plain answer's correctness lead survives the rewrite: correctness of plain-memo minus flash in M packets, and of plain minus flash in P packets, with intervals.

**B1 (primary): the checker improves the memo** (0.2.0, 8 questions), judged by `C`:

- **clearly improves** if the interval's lower bound is above 0;
- **ahead, not clearly** if `C` > 0 and the interval includes 0;
- **no measured benefit** if `C` ≤ 0 and the interval includes 0;
- **clearly worse** if the interval's upper bound is below 0.

With eight questions, an average gain of roughly 0.7 points or more should show as clear if the per-question differences spread by about a point (a guess, not a power calculation); a smaller real gain will read as "not clearly". **B2 and B3 (secondary):** `C` for 0.1.0 over all 8 questions, ties included; contradictions and correctness for B1.

**Consequences, fixed now.** The skill is not re-tuned on these judgments. If A1 is anything but **holds**, every place that states the round-5 lead over a plain answer (README, DETAILS.md, the opening paragraph and description of SKILL.md, and wise-men's README) puts the format-matched result next to it, in the wording above. If B1 is **no measured benefit**, DETAILS.md's checker line ("the Chairman grading its own homework") is reworded to the measured result and the checker stays, at one cheap call. If B1 is **clearly worse**, the owner decides on a 0.3.0 change after reading the results.

## Exclusions

- Each judgment is parsed strictly. A judgment that fails to parse, or a judge that used any tool but Read or read any other file (checked in its transcript), is re-run once on the same packet by a fresh judge. If it fails again it is dropped and disclosed. A question with fewer than two valid judges in a packet type leaves every comparison that needs that packet type.
- A new flash run that does not finish is re-run once (round 5's rule). If it fails again, it is recorded as absent and B1 runs on seven questions, disclosed.
- If a run's checker prompt has no extractable draft, that pair is dropped and disclosed.
- No question, judge or answer is dropped after its scores are seen, and nothing is re-judged after scores are seen.

## What gets published, whatever the result

`RESULTS-6.md`, generated by `fc6.py results`, opens with two paragraphs before any other number. The first gives correctness: in round 5 a plain answer scored higher on correctness than flash and wise-men (4.3 against 3.8 for both), followed by this round's correctness for every arm. The second is the caveat: every answer, rewrite, audit, judge and classifier here is a Claude model, there are no human grades, and this tests one known bias of LLM judges with LLM judges. Then come A1 and B1 in the pre-registered wording, then everything else. The repository publishes every file this round produces: the rewrites, audits, script checks, the owner's spot-check note, the extracted drafts with their hashes, the new runs with round-5-style provenance headers (minutes, calls, tokens, list-price USD), the packets, judgments, parsed scores and the script. The README and DETAILS.md change in the same commit as the results, as fixed under Consequences. With the owner's OK, the round is copied byte-identical into the wise-men repository, as round 5 was.

## Steps and scripts

`fc6.py` sits next to this file and imports `normalize()`, `score_blocks()`, `boot()`, `rows_of()`, `run_cost()` and `final_text()` unchanged from `../head-to-head/h2h5.py`. Its commands: `seal | rewrite-prompt Q | save-control T Q | check Q | audit-prompt Q | save-audit T Q | extract | save-run T Q | blind | savejudge T part Q j | parse | classify-input | report | results | verify`. In these, T is an agent transcript.

0. The owner approves this file, and it is committed alone.
1. Write `fc6.py`, `rewrite-prompt.txt`, `audit-prompt.txt` and the two judge prompts; run `fc6.py seal`; commit, before any generation.
2. Part A: for each question, `rewrite-prompt` → rewriter → `save-control` → `check` → `audit-prompt` → auditor → `save-audit`, with the one retry where needed. Eight at a time, in parallel.
3. The owner's spot check on the two drawn questions.
4. Part B: `extract` for the twelve stored drafts; the four new 0.2.0 runs (R501, R503, R505, R507) all at once, which is twelve members, under Claude Code's 20-subagent limit; `save-run`, then `extract` for their drafts.
5. Run `fc6.py blind`, then commit the rewrites, audits, drafts, runs and packets before any judge runs.
6. 84 judges, at most 15 at a time; `savejudge`, then `parse`.
7. The Part B contradiction classifier (one call, two if its input is too long).
8. Run `fc6.py results` and `fc6.py verify` (every packet rebuilds byte-identical, every judgment re-parses); add `fc6.py verify` to `scripts/check.sh`; update the README, DETAILS.md, `eval-data/README.md` and CHANGELOG as fixed above; the owner reads the draft results page before it is pushed.

## Cost and time

| step | subagent calls | model | approx. time |
|---|--:|---|---|
| rewrites, two arms (+ at most 16 retries) | 16 (≤ 32) | sonnet | 15 min in parallel |
| audits, two arms (+ at most 16 re-audits) | 16 (≤ 32) | opus | 10 min in parallel |
| new 0.2.0 flash runs | 4 orchestrators + 16 skill calls | sonnet / opus / haiku | about 20 min, all four at once |
| judges, three-answer packets | 72 | opus | about 30 min in waves of 15 |
| judges, two-answer packets | 36 | opus | about 5 min |
| contradiction classifier | 1–2 | sonnet | 2 min |
| **total** | **161 (≤ 193 with every allowed retry, plus any judge re-run)** | | **about 2–3 hours of Claude time, in one or two 5-hour windows** |

At the 2026-07 list prices in `h2h5.py`, this comes to about $65–80 of usage: round 5's medians were $3.95 per flash run, $1.95 per nine-answer judge and $0.23 per two-answer judge. It runs on the owner's Max plan allowance, with no API key and no money spent. The owner's time is about 35 minutes: approving this file (10), the spot check (15) and reading the results before publishing (10). The public launch is planned for 2026-11-10, so the results page is targeted for then.

## Honest limits

- Eight questions and one run per answer, so the intervals are real but wide.
- Claude only, by design, as stated above.
- The length-matched rewrite must roughly double or triple the plain answers (471–903 words to 1,430–2,000) without new content, so it will repeat itself, and judges may mark it down for that, which would favour flash. `plain-memo-short` exists to check this; the audit's sentence map also reports how often a source sentence is reused.
- The rewriter is Sonnet 5.5, while the plain answers were written by Sonnet 5, so the control's prose may be a little more polished than the source's.
- Part A tests the published round-5 answers (flash 0.1.0), not the shipped 0.2.0. It format-matches only the plain answer, not the six rival skills.
- The `F` and `S` estimates compare different judges across the M and P packets, with flash as the shared anchor.
- B1 mixes four runs from 2026-10-22 with four new ones, all 0.2.0 on the same models. The 2026-10-22 four were chosen because their 0.1.0 answers had failed. B1 and B2 use different models and are never compared with each other.
- The drafts come from local transcripts that are not in the repository. The SHA-256 hashes let the owner's machine re-check them; nobody else can.
