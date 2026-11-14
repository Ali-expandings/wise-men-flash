# Round 6 results: a format-matched control and the checker on and off

Pre-registration: [`PREREG-6.md`](PREREG-6.md), committed as `f7bba85` before any rewrite, run or judgment, and amended before any judge ran (Amendment 2, `191188c`, 2026-11-10).

Correctness first. In round 5 a plain answer scored higher on correctness than flash and wise-men (4.3 against 3.8 for both). In this round, correctness out of 5 (mean of three judges, then of questions), by packet type: M packets: flash 0.1.0 3.75, wise-men 3.14.0 3.88, plain-memo 2.92; P packets: flash 0.1.0 3.71, wise-men 3.14.0 3.88, plain answer 3.71; S packets: flash 0.1.0 3.88, wise-men 3.14.0 3.88, plain-memo-short 3.04; B1: draft 3.76, shipped memo 4.19; B2: draft 3.75, shipped memo 3.92.

The caveat. Every answer, rewrite, audit, judge and classifier here is a Claude model, there are no human grades, and this tests one known bias of LLM judges with LLM judges. It cannot answer whether AI validating AI can be trusted; only human blind ratings can, and they are a separate step. The owner's spot check of two rewrites before judging (Part A, rule 4) was skipped: he left the call to the analyst (Amendment 2), so the blind audits are the only check that the rewrites add nothing to the answer they restate.

**A1 (primary): the win over the plain answer survives format matching — holds.** Flash − plain-memo (`D_ctrl`, M packets): +8.3 [+7.5, +9.3] over 8 questions; flash − plain answer (`D_plain`, P packets): +5.8 [+4.8, +7.0] over 8 questions.

Read A1 with this: the control is a faithful rewrite of the plain answer under the pre-registered rules, not a format-only twin of it. The rewriters carried the prompt's word "the source" into every long rewrite and half the short ones, and most judges of those packets named it as a fault; both rewrites scored below the plain answer they restate. So this round rules out length as the driver of the gap (long and short rewrites scored alike) more firmly than it rules out format. Details under Honest limits.

**B1 (primary): the checker improves the memo (0.2.0) — clearly improves.** Shipped − draft (`C`, total /25): +2.0 [+1.2, +2.5] over 7 questions. B1 measured wise-men-flash 0.2.0, whose practitioner anchor and Devil's Advocate ran on `opus` (`claude-opus-5-5`); 0.3.0, released on 2026-11-10, routes those two seats to `fable` (falling back to `opus`), which no round has measured.

## Part A: the format-matched control

- A1 (flash 0.1.0): holds. `D_ctrl` +8.3 [+7.5, +9.3] over 8 questions; `D_plain` +5.8 [+4.8, +7.0] over 8 questions.
- A3 (flash 0.1.0): format effect `F` = `D_plain` − `D_ctrl` −2.5 [−3.3, −1.7] over 8 questions; share of the gap format and length explain, `S` = −0.43 [−0.67, −0.26]. Both are negative: next to the same anchor, the format-matched rewrite scored below the plain answer it restates, so format and length explain none of the gap, and the stated prediction (`F` > 0) did not hold.
- A5 (flash 0.1.0): `D_short` +8.9 [+7.6, +10.2] over 8 questions (holds by A1's rule); format only `F_fmt` = `D_plain` − `D_short` −3.1 [−4.0, −2.2] over 8 questions; length `F_len` = `D_short` − `D_ctrl` +0.6 [−0.2, +1.3] over 8 questions.
- A4 (flash 0.1.0): correctness, plain-memo − flash 0.1.0 (M) −0.8 [−1.3, −0.3] over 8 questions; plain answer − flash 0.1.0 (P) +0.0 [−0.5, +0.5] over 8 questions; plain-memo-short − flash 0.1.0 (S) −0.8 [−1.3, −0.4] over 8 questions.

- A2 (wise-men 3.14.0): holds. `D_ctrl` +10.3 [+9.5, +11.3] over 8 questions; `D_plain` +8.2 [+7.4, +9.1] over 8 questions.
- A3 (wise-men 3.14.0): format effect `F` = `D_plain` − `D_ctrl` −2.2 [−2.6, −1.8] over 8 questions; share of the gap format and length explain, `S` = −0.27 [−0.33, −0.21]. Both are negative: next to the same anchor, the format-matched rewrite scored below the plain answer it restates, so format and length explain none of the gap, and the stated prediction (`F` > 0) did not hold.
- A5 (wise-men 3.14.0): `D_short` +10.2 [+9.3, +11.2] over 8 questions (holds by A1's rule); format only `F_fmt` = `D_plain` − `D_short` −2.0 [−2.7, −1.4] over 8 questions; length `F_len` = `D_short` − `D_ctrl` −0.1 [−0.6, +0.4] over 8 questions.
- A4 (wise-men 3.14.0): correctness, plain-memo − wise-men 3.14.0 (M) −1.0 [−1.5, −0.4] over 8 questions; plain answer − wise-men 3.14.0 (P) −0.2 [−0.7, +0.4] over 8 questions; plain-memo-short − wise-men 3.14.0 (S) −0.8 [−1.3, −0.3] over 8 questions.

| M packets (8 questions) | total /25 | correct | insight | practical | risk | dissent | words |
|---|--:|--:|--:|--:|--:|--:|--:|
| flash 0.1.0 | 21.21 | 3.75 | 4.21 | 4.33 | 4.46 | 4.46 | 1662 |
| wise-men 3.14.0 | 23.21 | 3.88 | 5.00 | 4.75 | 4.88 | 4.71 | 2076 |
| plain-memo | 12.88 | 2.92 | 2.83 | 3.25 | 2.50 | 1.38 | 1595 |

| P packets (8 questions) | total /25 | correct | insight | practical | risk | dissent | words |
|---|--:|--:|--:|--:|--:|--:|--:|
| flash 0.1.0 | 20.83 | 3.71 | 4.08 | 4.25 | 4.33 | 4.46 | 1662 |
| wise-men 3.14.0 | 23.17 | 3.88 | 4.96 | 4.67 | 4.88 | 4.79 | 2076 |
| plain answer | 15.00 | 3.71 | 3.13 | 3.63 | 2.96 | 1.58 | 664 |

| S packets (8 questions) | total /25 | correct | insight | practical | risk | dissent | words |
|---|--:|--:|--:|--:|--:|--:|--:|
| flash 0.1.0 | 21.83 | 3.88 | 4.29 | 4.42 | 4.67 | 4.58 | 1662 |
| wise-men 3.14.0 | 23.13 | 3.88 | 4.96 | 4.71 | 4.88 | 4.71 | 2076 |
| plain-memo-short | 12.92 | 3.04 | 2.83 | 3.33 | 2.29 | 1.42 | 819 |

## Part B: the checker on and off

| B1 (0.2.0, 7 questions judged) | total /25 | correct | insight | practical | risk | dissent | words |
|---|--:|--:|--:|--:|--:|--:|--:|
| draft | 21.19 | 3.76 | 4.38 | 4.29 | 4.19 | 4.57 | 1291 |
| shipped memo | 23.14 | 4.19 | 4.38 | 5.00 | 4.86 | 4.71 | 1351 |

| B2 (0.1.0, 4 questions judged) | total /25 | correct | insight | practical | risk | dissent | words |
|---|--:|--:|--:|--:|--:|--:|--:|
| draft | 20.75 | 3.75 | 4.00 | 4.58 | 4.67 | 3.75 | 1736 |
| shipped memo | 21.75 | 3.92 | 4.08 | 4.67 | 4.75 | 4.33 | 1775 |

- B1 per axis, shipped − draft: correctness +0.4 [+0.1, +0.8] over 7 questions; insight +0.0 [+0.0, +0.0] over 7 questions; practical use +0.7 [+0.4, +0.9] over 7 questions; risk awareness +0.7 [+0.3, +1.0] over 7 questions; dissent quality +0.1 [+0.0, +0.4] over 7 questions.
- B2 (0.1.0, secondary): `C` over all 8 questions, the four identical pairs entering as ties: +0.5 [+0.0, +1.3] over 8 questions; over the four judged questions only: +1.0 [+0.0, +2.5] over 4 questions.
- B3 (B1): internal contradictions the judges listed, summed over judges, draft → shipped: R502 7 → 1; R503 3 → 4; R504 6 → 2; R505 0 → 0; R506 8 → 0; R507 5 → 4; R508 3 → 1; all PASS 0 errors: 88 → 29.
- B3 (B2): internal contradictions the judges listed, summed over judges, draft → shipped: R503 4 → 4; R505 0 → 0; R507 3 → 2; R508 5 → 3; all PASS 0 errors: 52 → 47.
- Words, B1, shipped − draft: R502 +54, R503 +74, R504 +139, R505 +56, R506 +24, R507 +16, R508 +58.
- Words, B2, shipped − draft: R503 +37, R505 +7, R507 +18, R508 +94.

## Per question (mean of the valid judges, total /25)

| M | flash 0.1.0 | wise-men 3.14.0 | plain-memo |
|---|--:|--:|--:|
| R501 | 20.67 | 24.00 | 13.33 |
| R502 | 21.67 | 23.00 | 10.33 |
| R503 | 20.33 | 23.33 | 13.67 |
| R504 | 21.33 | 21.33 | 12.67 |
| R505 | 22.33 | 23.33 | 14.67 |
| R506 | 21.67 | 23.33 | 13.33 |
| R507 | 19.67 | 23.33 | 11.67 |
| R508 | 22.00 | 24.00 | 13.33 |

| P | flash 0.1.0 | wise-men 3.14.0 | plain answer |
|---|--:|--:|--:|
| R501 | 21.33 | 24.00 | 15.00 |
| R502 | 21.33 | 23.00 | 12.33 |
| R503 | 19.67 | 23.33 | 15.67 |
| R504 | 21.33 | 21.00 | 13.67 |
| R505 | 22.00 | 23.33 | 16.67 |
| R506 | 20.67 | 24.00 | 16.33 |
| R507 | 19.67 | 23.00 | 14.00 |
| R508 | 20.67 | 23.67 | 16.33 |

| S | flash 0.1.0 | wise-men 3.14.0 | plain-memo-short |
|---|--:|--:|--:|
| R501 | 22.00 | 24.00 | 13.00 |
| R502 | 23.00 | 23.00 | 10.67 |
| R503 | 19.33 | 23.67 | 14.00 |
| R504 | 21.67 | 20.67 | 13.00 |
| R505 | 22.67 | 23.33 | 13.33 |
| R506 | 21.67 | 23.00 | 14.00 |
| R507 | 21.33 | 23.33 | 11.67 |
| R508 | 23.00 | 24.00 | 13.67 |

| B1 | draft | shipped memo |
|---|--:|--:|
| R502 | 21.67 | 24.33 |
| R503 | 20.00 | 22.33 |
| R504 | 22.33 | 24.00 |
| R505 | 23.33 | 23.33 |
| R506 | 20.33 | 23.00 |
| R507 | 20.00 | 22.00 |
| R508 | 20.67 | 23.00 |

| B2 | draft | shipped memo |
|---|--:|--:|
| R503 | 21.67 | 21.67 |
| R505 | 22.67 | 22.67 |
| R507 | 20.00 | 20.67 |
| R508 | 18.67 | 22.00 |

## The rewrites: audit results

NEW / STRONGER / WEAKER / DROPPED as each audit found them, before the deletion rule. Attempt 3 is Amendment 2's length-only retry (`plain-memo` R502, R507, R508). Words and band are the final's.

| question | arm | from attempt | attempt 1 | attempt 2 | attempt 3 | deleted | dropped, disclosed | words | band |
|---|---|--:|---|---|---|--:|--:|--:|---|
| R501 | plain-memo | 2 | 1/1/2/0 | 0/0/0/0 | – | 0 | 0 | 1,693 | 1,546–1,888, in |
| R501 | plain-memo-short | 2 | 3/0/0/0 | 0/0/0/0 | – | 0 | 0 | 1,021 | 813–993, out (band dropped) |
| R502 | plain-memo | 3 | 2/0/1/0 | 0/0/0/0 | 3/0/0/0 (1,355 words, used) | 3 | 0 | 1,355 | 1,287–1,573, in |
| R502 | plain-memo-short | 2 | 0/0/1/0 | 0/0/0/0 | – | 0 | 0 | 629 | 481–587, out (band dropped) |
| R503 | plain-memo | 2 | 1/0/0/0 | 0/0/0/0 | – | 0 | 0 | 1,502 | 1,456–1,778, in |
| R503 | plain-memo-short | 2 | 0/1/1/0 | 0/0/0/0 | – | 0 | 0 | 735 | 424–518, out (band dropped) |
| R504 | plain-memo | 2 | 1/0/1/0 | 0/1/0/0 | – | 1 | 0 | 1,372 | 1,323–1,617, in |
| R504 | plain-memo-short | 2 | 1/0/2/0 | 0/0/0/0 | – | 0 | 0 | 699 | 513–627, out (band dropped) |
| R505 | plain-memo | 2 | 8/5/4/0 | 0/1/0/0 | – | 1 | 0 | 1,882 | 1,800–2,200, in |
| R505 | plain-memo-short | 2 | 2/0/1/0 | 0/1/0/0 | – | 1 | 0 | 1,078 | 771–941, out (band dropped) |
| R506 | plain-memo | 2 | 0/1/0/0 | 2/0/0/0 | – | 2 | 0 | 1,645 | 1,422–1,736, in |
| R506 | plain-memo-short | 2 | 1/1/0/1 | 0/0/0/0 | – | 0 | 0 | 624 | 517–631, in (band dropped) |
| R507 | plain-memo | 2 | 2/0/0/0 | 0/0/0/0 | 0/0/0/0 (1,710 words, not used) | 0 | 0 | 1,648 | 1,713–2,093, out |
| R507 | plain-memo-short | 2 | 0/0/0/0 | 0/0/0/0 | – | 0 | 0 | 831 | 599–731, out (band dropped) |
| R508 | plain-memo | 3 | 2/0/2/0 | 0/0/1/0 | 0/1/0/0 (1,664 words, used) | 1 | 0 | 1,664 | 1,423–1,739, in |
| R508 | plain-memo-short | 2 | 0/0/0/0 | 0/0/0/0 | – | 0 | 0 | 937 | 665–811, out (band dropped) |

## Judges

- 105 valid judgments (M 24, P 24, S 24, B1 21, B2 12), each by a fresh `wise-member` agent on `opus` that read its packet and nothing else. 1 judgment(s) failed and were re-run once by a fresh judge on the same packet: judgments/S/R508-j1-invalid-1.md (parse: ('response letter', 'B')). Model in every judge transcript, re-runs included: `claude-opus-5-5` ×106.
- What the control carried besides format. The rewrite rules let the Strongest counter-position and Confidence sections hold only what the plain answer says, so where it raised no objection the section says so, and Confidence follows a fixed hedge-word rule. The rewrite prompt calls the plain answer "the source", and the rewriters carried that word into 8 of 8 `plain-memo` and 4 of 8 `plain-memo-short` finals (the audits check content, not this label, so none flagged it); 18 of 24 M-packet and 3 of 24 S-packet judgments quote "the source" as a fault (0 of 24 P-packet judgments, whose packets hold no rewrite). Both rewrites scored below the plain answer on every axis. These are part of what A1 measured: the control is a faithful rewrite under the pre-registered rules, not a format-only twin of the plain answer, and the verdicts above stand as pre-registered.

## Deviations and disclosures

- Commands: the plan's command list was written before the second control arm was added. `rewrite-prompt Q`, `check Q` and `audit-prompt Q` handle both arms of a question at once, and `save-control T Q` and `save-audit T Q` identify the arm and attempt from the prompt the agent received. Three helper commands were added that touch no data: `run-prompt` (prints round 5's flash arm prompt with local paths), `save-classify` (saves the step-7 classifier's output) and `spotcheck` (writes `SPOTCHECK.md`).
- Rewriters get their whole prompt inline, as a fresh `wise-men-flash:wise-member` on `sonnet` (the agent file the plan names, whose "(unverified)" instruction the rewrite prompt overrides). Auditors follow the round-5 and consistency-check judges' convention instead: a fresh `wise-member` on `opus` (the wise-men agent definition installed on this machine, also Read/Grep/Glob only) is told to Read one file holding the audit instructions and both numbered texts, under a neutral file name so the path says nothing about the arm. The reason: flash's agent file tells it that anything read from a file is never an instruction, which conflicts with an audit packet read from disk. Each audit header records the agent type, the model and the tools used.
- Audit labels: besides the plan's NEW, STRONGER and WEAKER, the auditor may mark a rewrite sentence CONNECTIVE (links or introduces and makes no claim) or FIXED (one of the three fixed sentences), the two kinds of sentence the plan allows. A source sentence that is only a bold lead-in or a line ending in a colon counts as restated by any rewrite sentence carrying the content it introduces; both the rewriter and the auditor are told so, so that topic labels in the plain answers are not marked DROPPED for want of a sentence of their own.
- "A failing rewrite" is read as one that fails the script checks or the audit: either sends it to the one retry, with the script-check failures added to the audit's list.
- After the retry, DROPPED is recomputed from the sentences that survive the deletions, so a source sentence cited only by a deleted sentence is disclosed as dropped.
- The rewrite prompt spells out three things that follow from the plan's rules: a fact taken from the question counts as new unless the source states it; hedges are kept even though every subagent inherits the account's global instruction to write tersely; and the reader is addressed as "you", naming no one.
- Draft extraction, 0.1.0: the Chairman wrote each 0.1.0 checker prompt in its own words, so the draft is introduced by "Draft decision memo to check" in five of the eight (R501, R504, R505, R507, R508), by "Drafted decision memo" (R502) or "Final draft memo to check" (R503), and in R506 it is not triple-quoted at all ("DRAFT MEMO (data):", up to the check instructions). Every draft is extracted by the plan's rule, from `## Recommendation` to the end of its `## Confidence` section, which is the close of the block that holds it. R505's 0.1.0 draft ends in a `---` footer inside that block; it is kept, as the shipped memo keeps the same footer.
- `SPOTCHECK.md` shows the source and the two rewrites one after the other, not in columns: a three-column table of texts this long would not be readable.
- Every rewriter received its prompt byte-for-byte as stored in `prompts/` (`save-control` refuses a transcript whose prompt differs), used no tool, and ran on `claude-sonnet-5-5`; every auditor read only its one packet and ran on `claude-opus-5-5` (each header records it).
- A parser fix after the first audits, before any retry: R502 `plain-memo-short`'s auditor marked "Unknowns: No unknowns are named." as FIXED, and `fc6.py` at first accepted FIXED only on the bare sentence, so it rejected a valid audit. The check now allows a short label or list marker before a fixed sentence. The same audit transcript was re-parsed; no auditor was re-run for it.
- Every first attempt in R501–R504 failed (each audit found at least one NEW, STRONGER or WEAKER sentence, and all four `plain-memo-short` rewrites ran 24–61% longer than the plain answer they rewrote, 12–47% above the top of their band), so all eight went to the one retry.
- **Not covered by the plan, held for the owner: rewrites that still fail a script check after the one retry.** The plan's rule after the retry repairs only audit findings (deletion) and drops (disclosure); it says nothing about a rewrite still outside its word band. In R501–R504 every `plain-memo-short` retry passed its audit with zero NEW, STRONGER, WEAKER and DROPPED but stayed over the band (R501 1,021 words against 813–993; R502 629 against 481–587; R503 735 against 424–518; R504 699 against 513–627), and R502 `plain-memo` passed its audit but came in 2 words under its band (1,285 against 1,287–1,573). Carrying every source sentence, adding a Recommendation that sums up and a Confidence section that restates each load-bearing claim makes a memo longer than its source, so the short arm's band is hard to meet without dropping content. No third attempt was made and nothing was trimmed by hand. These finals are stored and audited like the others, but `fc6.py blind` does not build a packet from a rewrite that fails its script checks; the owner decides whether to use them as they are (disclosed), allow a length-only retry by amendment, or report A5 without them.
- R504 `plain-memo`: the retry's audit found one STRONGER sentence (R57, which dropped the source's "if churn declines with tenure" condition); it was deleted under the plan's rule. No source sentence was left uncited after the deletion, and the final still passes every script check.
- `fc6.py` changes made during step 2, none touching an agent's input: the final rewrite's header note now says when a final still fails a script check (it had said "passed the script checks" for any final with nothing to delete), and `blind` skips a packet whose rewrite fails its script checks.
- Every first attempt in R505–R508 failed too, so all sixteen rewrites went to the one retry (32 rewriter calls, 32 auditor calls in all; no rewriter or auditor was re-run, and every agent's prompt or packet matched its stored file byte for byte).
- Deletions under the plan's rule after the retry's audit: R504 `plain-memo` R57 (STRONGER), R505 `plain-memo` R9 (STRONGER), R505 `plain-memo-short` R54 (STRONGER), R506 `plain-memo` R65 and R80 (NEW), R508 `plain-memo` R68 (WEAKER). After the deletions no source sentence is left uncited in any of the sixteen finals, so nothing is disclosed as DROPPED.
- **Held for the owner, final count: 10 of the 16 finals are outside their word band after the one retry**, every one of them clean on the audit. `plain-memo` (band = flash's length ±10%): R502 1,285 words (band 1,287–1,573), R507 1,648 (1,713–2,093), R508 2,092 after its deletion (1,423–1,739). `plain-memo-short` (band = the plain answer's length ±10%): R501 1,021 (813–993), R502 629 (481–587), R503 735 (424–518), R504 699 (513–627), R505 1,078 after its deletion (771–941), R507 831 (599–731), R508 937 (665–811). Only R506 `plain-memo-short` meets its band. As built, `blind` makes M packets for 5 questions (R501, R503–R506) and S packets for 1 (R506); A1 as pre-registered needs M packets on all eight. The owner's options, none taken here: judge the out-of-band finals as they are, with the gaps disclosed (the short ones are still far shorter than flash: 629–1,078 words against 1,430–2,000); amend the plan to allow one length-only retry, audited the same way; or run A1 on the five in-band questions and report A5 as not run.
- The auditor applied the fixed hedge rule literally: words outside its two lists ("tend to", "often", "roughly", "presumably", "can", "some") count as no hedge, so a claim the source states with them is High, and a rewrite that labelled one Medium or Low was marked WEAKER. That is the plan's rule as written; it made the Confidence section the commonest source of findings.
- Reuse of source sentences (how often one source sentence is restated, from the audit maps): the long finals restate each source sentence 2.9–7.4 times on average, the short ones 1.5–3.8 times. The highest single counts (R501 `plain-memo` 39, R506 `plain-memo` 26) are lead-in lines such as "On your three specific worries:", which the auditor cites with every sentence that carries their content. Per-file figures are in `audits/<Q>-<arm>-final.yaml`.
- All twelve stored drafts are their run's first checker call (each checker's parent transcript was checked). The four 0.1.0 pairs the plan calls identical (R501, R502, R504, R506) are byte-identical after normalization.
- A figure in the plan: Part B says the edited pairs on disk ran "18–139 words" longer once shipped. Measured on the extracted drafts, the eight edited pairs differ by 7 to 139 words (0.1.0: R503 +37, R505 +7, R507 +18, R508 +94; 0.2.0: R502 +54, R504 +139, R506 +24, R508 +58). Nothing in the design depends on it.
- The four new 0.2.0 runs (R501, R503, R505, R507) ran all at once on 2026-11-08, each a fresh `general-purpose` orchestrator on `sonnet` given round 5's flash arm prompt verbatim apart from local paths (checked by `save-run`), with `~/.agents/skills/wise-men-flash` on `master` and `SKILL.md` identical to `aaabd74`. All four finished on the first try: four calls each (anchor and Devil's Advocate on `claude-opus-5-5`, domain member on `claude-sonnet-5-5`, checker on `claude-haiku-5-5`), 2.3–3.2 minutes and 0.95–1.43 list-price USD a run, memos of 1,001–1,296 words. No run used web search or fetch, so there was no step-6 web check to disclose.
- **R501 leaves B1 under the plan's exclusion rule.** Its orchestrator wrote the draft to a file in its scratch folder, gave the checker a prompt whose `<draft>` block reads only "(see the file above)" with an instruction to Read that file, and edited the file three more times after the check. The checker's prompt therefore holds no extractable draft, so the pair is dropped and disclosed, and B1 runs on seven questions (R502–R508). The run itself finished and is kept in `runs/`; the plan re-runs only runs that do not finish. The text the checker read survives as its Read result in the checker's transcript (agent `ae9a529ed8df627c5`, 7,570 characters), so an amendment could recover it; it was not used. Passing the draft by file departs from the skill's own checker template, which puts the draft inline.
- Checker verdicts in the new runs: R501 CONSISTENCY failed; R503 CLAIMS and CONSISTENCY; R505 CLAIMS, COVERAGE and CONSISTENCY; R507 CLAIMS, COVERAGE and CONSISTENCY. Every new draft was edited before it shipped (R503 +74 words, R505 +56, R507 +16).
- Amendment 2 (commit `191188c`) settled the held items above. `plain-memo-short`: the ±10% band is dropped and all eight finals are judged as they are, at 1,021 (R501), 629 (R502), 735 (R503), 699 (R504), 1,078 (R505), 624 (R506), 831 (R507) and 937 (R508) words, against flash's 1,430–2,000. `plain-memo`: R502, R507 and R508 got the one length-only retry; no other rewrite was touched.
- The retry prompt, filling the amendment's "the same prompt plus the target": attempt 2's prompt, byte for byte, followed by one paragraph (the `LENGTH RETRY` section of `rewrite-prompt.txt`) that gives the earlier memo's word count, says whether it was under or over the band, and restates the band and the target. `fc6.py length-retry Q` writes it and refuses any question outside R502, R507 and R508. Each went inline to a fresh `wise-men-flash:wise-member` on `sonnet` (all three ran on `claude-sonnet-5-5` and used no tool); each was audited by a fresh `wise-member` on `opus` (all three `claude-opus-5-5`, one Read of a neutrally named copy of the audit packet each). Six calls in all, none re-run.
- How "clean and in band" was read: the retry goes through the same script checks and the same deletion rule as any attempt, and it replaces the earlier rewrite if, after the deletions, no source sentence is left uncited and every script check passes, the band included. This is how the amendment itself uses "clean" (R508's earlier final, which it calls clean, had a sentence deleted).
- R502 `plain-memo`: the retry came to 1,401 words; its audit marked three sentences NEW (R65, a caveat that both aggravating factors "would still be present" in any January that ships a large batch; R77, "No further case against this recommendation is made beyond the risks above.", which is not the fixed sentence word for word; R97, a claim that no source claim carries a Low-level hedge, though the source says "unclear"). They were deleted, leaving 1,355 words (band 1,287–1,573) with every source sentence still cited, so the retry replaces attempt 2 (1,285 words). Deleting R97 leaves the Confidence section's "Low:" label with nothing under it; the rule is mechanical and nothing was edited by hand.
- R507 `plain-memo`: the retry's audit was clean, but it came to 1,710 words, 3 under the band's floor of 1,713, so it does not replace attempt 2, which is judged as it is at 1,648 words (band 1,713–2,093), 87% of flash's 1,903.
- R508 `plain-memo`: the retry came to 1,681 words; its audit marked one sentence STRONGER (R27, which drops the condition that the seller shares the risk only through seller financing or an earnout). It was deleted, leaving 1,664 words (band 1,423–1,739) with every source sentence still cited, so the retry replaces attempt 2 (2,092 words after its own deletion).
- After the amendment, `plain-memo` is inside flash's band on 7 of 8 questions (all but R507), and every final of both arms has zero NEW, STRONGER, WEAKER and DROPPED sentences after the deletion rule.
- `fc6.py` changes for the amendment, none touching an agent's input: the `length-retry` command; `save-control`, `check`, `audit-prompt` and `save-audit` accept attempt 3; `final_build` applies the rule above; `blind` no longer holds back a `plain-memo-short` final for its length, or a `plain-memo` final for its length once its length-only retry has been audited. The header note of every final that is outside its band now says why it is judged anyway; the memo bodies are unchanged, and packets never include those headers.
- `fc6.py blind` then built 105 of the 108 packets: all 72 of Part A (M, P and S for all eight questions), 21 of B1 and all 12 of B2; the three it does not build are B1 R501, the pair dropped in step 4. The 75 packets built in step 5 are unchanged, and `fc6.py verify` rebuilds all 105 byte-identical. These were committed before any judge ran.
- The owner's spot check (step 3) was not done: the owner left it to the analyst's verdict, and the blind audits found no NEW, STRONGER, WEAKER or DROPPED sentence left in any final. `SPOTCHECK.md` is kept as it was prepared on 2026-11-08; no one marked anything in it.
- The judges' spawn prompt is round 5's (`arm-prompts-r5.md`, "judges") with only the path and the count changed: "three responses labeled A–C" and "the three fenced `scores` blocks" for Part A, "two responses labeled A–B" and "the two" for Part B. The path is the packet's own path in this repository, as in round 5. Each judge was a fresh `wise-member` agent (the wise-men agent definition installed here, Read/Grep/Glob only, as for the auditors and the consistency-check judges) on `opus`.
- The model check came first: one judge (Part A, R501 M j1) ran alone, its transcript showed `claude-opus-5-5`, and only then did the rest start. `savejudge` refuses any transcript on another model; all 106 judge transcripts are on `claude-opus-5-5`.
- Order and pacing: Part A by question and packet type, then B1, then B2, in waves of at most 15 judges (1, 14, then six waves of 15, then 1). Each saved judgment was first checked to have read exactly the packet it was mapped to.
- One judgment failed the strict parse: S R508 j1 wrote a second `scores` block for response B to correct its own risk score, and `score_blocks()` rejects a repeated letter. It is kept as `judgments/S/R508-j1-invalid-1.md` and, as the exclusion rule says, a fresh judge re-ran the same packet; the re-run parsed. No judge used a tool other than Read or read any file but its packet. Nothing else was re-judged.
- One judge (M R508 j3) fenced its PASS 0 and PASS 1 text as `scores-pass0` and `scores-pass1`; the parser reads only blocks fenced exactly as `scores`, so its three score blocks parsed as written.
- Judgments: 105 valid (Part A 72, B1 21, B2 12) instead of the plan's 108, because B1 R501 was dropped in step 4. No question has fewer than three valid judges in any packet type.
- The contradiction classifier ran once: `classify/input-1.md` holds all 33 Part B PASS 0 lists (42,488 characters, under the 60,000 at which it would split), read by a fresh `wise-member` on `sonnet` (`claude-sonnet-5-5`, one Read of that file). Its output parsed for all 33 sections. It covers B2 as well as B1, so B3 is reported for both.
- Calls in this session's part of the round (2026-11-10): 3 rewriters and 3 auditors (Amendment 2), 106 judges, 1 classifier: 113 calls, 32.44 list-price USD at `h2h5.py`'s prices (judges 30.83, median 0.8 minutes each), on the owner's Max plan with no API key. The round in all: 35 rewriter, 35 auditor, 4 flash orchestrators with 16 skill calls, 106 judge and 1 classifier calls, 197 in all. The plan's ceiling was 193 with every allowed retry plus any judge re-run; the difference is Amendment 2's 6 calls, less the 3 B1 R501 judges that were never needed, plus the 1 re-run.
- `fc6.py` changes for step 8, none touching a judgment or a score: `RESULTS-6.md` now also states the skipped spot check (Amendment 2), the version note on B1, the judge counts and models, what the control carried besides format, and an attempt-3 and band column in the rewrites table; when `F` is negative the A3 line says so in words. `fc6.py verify` was added to `scripts/check.sh`.
- Version: B1's seven questions measured wise-men-flash 0.2.0, whose two strong seats ran on `opus` (`claude-opus-5-5`). 0.3.0, released on 2026-11-10 before the judges ran, routes those seats to `fable` (falling back to `opus`); this round does not measure 0.3.0.
- Consequences (PREREG-6): A1 holds and B1 clearly improves, so neither triggers a change to the README, DETAILS.md, SKILL.md or the wise-men README; none was made. `eval-data/README.md` and the CHANGELOG list the round.

## Credits

- Part B, the checker on and off, was asked for by Shuai Wu (University of Colorado Boulder), credited with his permission.

## Reproduce

`python3 eval-data/format-control/fc6.py report` prints this page; `results` rewrites it; `verify` rebuilds every packet from the stored answers, rewrites and drafts, every final rewrite from its attempt and audit, and re-parses every judgment. The drafts and the new runs were taken from local agent transcripts, which are not in the repository; their headers carry each transcript's SHA-256, so the owner's machine can re-check them.
