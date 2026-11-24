# Checker model: Haiku or Sonnet (2026-11-24)

**Why.** An outside tester, running his own checkers on our `consistency-check/` memos, found that Haiku checkers missed contradictions Sonnet checkers caught (0 of 12 against 9 of 12 on the misses he looked at). Flash's Stage 4.5 checker ran on the cheap tier (`haiku`). This asks the same question of flash's own checker.

**What ran.** The Stage 4.5 checker prompt from `SKILL.md` (0.3.0), verbatim, five checks, no `user_call` block. Its input: the question from `head-to-head/questions-r5.yaml`, the brief "None needed — the question is self-contained.", and a memo with its run header stripped (the draft starts at `## Recommendation`). Eight memos: the 0.1.0 flash answers to R502, R504, R506 and R508 (`head-to-head/raw/<Q>/wise-men-flash.md`) and the 0.2.0 answers to the same questions (`consistency-check/answers/<Q>-new.md`). Each memo checked once by a fresh read-only `wise-member` on `haiku` (resolved to Haiku 5.5) and once on `sonnet` (Sonnet 5.5): 16 calls. Prompts are in `prompts/`, the replies verbatim in `outputs/`. The checker read its prompt from a file instead of inline; the text is the same.

**The key.** The 13 distinct internal contradictions the blind Opus judges listed for these eight memos (`consistency-check/classification.md`, both judges merged, duplicates counted once). A checker scores a key item when one of its lines names that contradiction.

## Result

| memo | key contradictions | Haiku named | Sonnet named |
|---|---|:-:|:-:|
| R502 0.1.0 | "fully-staffed" January vs thin staffing; "strictly safer" vs Risks; "commit order" vs "rather than first-merged-first-shipped" | 1 ("strictly safer") | 1 ("strictly safer") |
| R504 0.1.0 | "no customer repaid $5,000" vs its own $5,300 | 0 (flagged the line as unsourced, not as contradicting $5,300) | 1 |
| R506 0.1.0 | "nothing irreversible" vs written exposure; "nothing reaches" staff vs leak risk; figures in writing vs "comparison too risky" | 1 ("nothing irreversible") | 1 ("nothing irreversible"; a related writing-vs-comparison point, not counted) |
| R508 0.1.0 | "job stays intact" / "costs nothing else" vs the stated retirement | 1 | 1 |
| R502 0.2.0 | a "settled fact" claim vs its own later hedge | 0 (CONSISTENCY PASS) | 1 |
| R504 0.2.0 | "rests entirely on the tail" vs $5,287 covering $5,000; net churn "too high" vs "omits expansion" | 0 (CONSISTENCY PASS) | 0 (flagged a related "best-case" vs expansion point, not counted) |
| R506 0.2.0 | rejects a written admission, yet drafts "the error was mine" | 0 (CONSISTENCY PASS) | 1 |
| R508 0.2.0 | salary counted twice vs "both roles" in Why | 0 | 0 (CONSISTENCY PASS) |
| **total** | **13** | **3** | **6** |

- CONSISTENCY returned FAIL on 5 of 8 memos for Haiku and 7 of 8 for Sonnet. Every memo holds at least one key contradiction.
- On the four 0.2.0 memos, the format flash ships today, Haiku named 0 of 5 and passed three of them; Sonnet named 2 of 5.
- Both models flagged things outside the key. Some look real (R504 0.1.0's 18–24 month payback computed at the 24-month end only, flagged by both). One is an artifact of this test: Sonnet on R502 0.2.0 dated a step against today's date, a month after the memo was written.
- Time per call was alike (Haiku 12–31 s, Sonnet 11–31 s).

**Decision.** The checker moves to the mid tier (`sonnet`) in 0.3.1.

**Limits.** One run per memo per model. Thirteen key items, all found by Claude judges, so the key itself is Claude's view (the outside tester's non-Claude grader ruled some of the judges' items false). Scored by the person who ran the test, not blind; the rule was "a line names that contradiction", and the two borderline calls are noted in the table, both against Sonnet. The models were Haiku 5.5 and Sonnet 5.5 on this date; a newer model behind either alias is untested here.
