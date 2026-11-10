# Evidence

Five things live here.

**[`head-to-head/` round 5](head-to-head/RESULTS-V5.md)** — this skill's own measurement, run as installed: wise-men-flash 0.1.0 next to wise-men 3.14.0 and every rival from rounds 1–4, on eight new questions, three blind judges each. It is the round the README's headline numbers come from. Its files are byte-identical copies of the [wise-men repository](https://github.com/Ali-expandings/wise-men)'s `eval-data/head-to-head/`, so the same data can be read from either repo:

| file | what it is |
|---|---|
| `PREREG-5.md` | the round's pre-registration, committed before any round-5 run (wise-men `6182087`) |
| `question-author-prompt-5.txt`, `questions-r5.yaml` | the blind question author's prompt and the eight questions it wrote, used as returned |
| `arm-prompts-r5.md` | exactly how each arm was invoked |
| `raw/R501` … `raw/R508` | every arm's final answer, each with a provenance header: arm and commit, minutes, subagent calls, tokens, list-price cost, and any deviation note |
| `blinding5.yaml` | the sealed answer order for every question and judge |
| `judge-prompt-r5.txt` | the error-first judge prompt |
| `blinded-v5/`, `judgments-v5/`, `parsed-v5/` | what each judge read, what each judge wrote, and the scores parsed from it |
| `h2h5.py` | the analysis — `report`, `results` (writes `RESULTS-V5.md`), `readme`, `verify` |
| `RESULTS-V5.md` | generated: tables, intervals, per-question scores, disclosures |

Only final answers were kept, not the members' individual answers, so a later change to the synthesis step cannot be re-run on round 5's exact member answers; it needs fresh runs.

**[`head-to-head/` round 4](head-to-head/RESULTS.md)** — the round that measured the profile this skill was extracted from, as the `--fast` arm of wise-men 3.13.0, on five questions. Every round-4 file except `flash4.py` and `RESULTS.md` is a byte-identical copy of the wise-men repository's `eval-data/head-to-head/` at commit `770c75a`:

| file | what it is |
|---|---|
| `PREREG-4.md` | the round's pre-registration, committed before any round-4 run |
| `question-author-prompt.txt`, `questions-r4.yaml` | the blind question author's prompt and the eight questions it wrote, used as returned |
| `raw/R401` … `raw/R405` | every arm's answer, with the same provenance header |
| `blinding4.yaml` | the sealed answer order for every question and judge (seed 20260919), R406–R408 included |
| `judge-prompt-5.txt` | the error-first judge prompt |
| `blinded-v4/` | exactly what each judge read, plus `CAL-Q23.md`, the pre-registered calibration packet |
| `judgments-v4/`, `parsed-v4/` | what each judge wrote, and the scores, one file per question |
| `flash4.py` | the analysis, read for flash — `report`, `results` (writes `RESULTS.md`), `examples` (writes `../../examples/`), `verify` |
| `RESULTS.md` | generated: tables, intervals, per-question scores, disclosures |

Questions R406–R408 (writing, ethics, a personal decision) were never run — round 4 stopped at five — and no answer or judgment exists for them.

**[`consistency-check/`](consistency-check/RESULTS.md)** — a pre-registered check of the 0.2.0 consistency fix on four round-5 questions (R502, R504, R506, R508): the new answers, the blinded two-answer packets, two blind Opus judges per question, and a blind count of the contradictions they found. A check on a targeted fix, not a new round.

**[`format-control/` round 6](format-control/RESULTS-6.md)** — a pre-registered check of two things round 5 left open ([`PREREG-6.md`](format-control/PREREG-6.md), amended once before any judge ran). Part A rewrote round 5's plain answers into flash's six-section memo with nothing added, once at flash's length (`plain-memo`) and once at about the plain answer's own (`plain-memo-short`), and judged each rewrite next to flash 0.1.0 and wise-men 3.14.0, three blind Opus judges per packet. Flash's lead held: +8.3 [+7.5, +9.3] over the format-matched rewrite and +5.8 [+4.8, +7.0] over the plain answer itself, and the rewrites scored below the plain answer they restate. Part B judged each 0.2.0 memo against the draft its one checker was given: the checker clearly improves the memo, +2.0 [+1.2, +2.5] on seven questions. B1 measured 0.2.0, whose strong seats ran on `opus`; 0.3.0 routes them to `fable`, which no round has measured. Every answer, rewrite, audit, judge and classifier is a Claude model, there are no human grades, and the owner's spot check of the rewrites was skipped.

| file | what it is |
|---|---|
| `PREREG-6.md`, `DEVIATIONS.md` | the plan (committed as `f7bba85`, Amendment 2 as `191188c`) and every deviation, recorded as it happened |
| `seal6.yaml` | the sealed answer order for every packet and judge, and the two spot-check questions (seed 20261104) |
| `rewrite-prompt.txt`, `audit-prompt.txt`, `prompts/` | the rewriter and auditor prompts, and every prompt exactly as sent |
| `rewrites/`, `checks/`, `audits/` | every rewrite attempt and the final that was judged, the script checks, and the blind audits with their sentence maps |
| `SPOTCHECK.md` | the side-by-side prepared for the owner's spot check, which was skipped |
| `drafts/`, `runs/` | each checker's draft, extracted from local transcripts (their SHA-256 in each header), and the four new 0.2.0 runs |
| `judge-prompt-r6-3.txt`, `judge-prompt-r6-2.txt`, `packets/` | round 5's judge prompt for three and for two answers, and exactly what each judge read |
| `judgments/`, `parsed/`, `classify/` | what each judge wrote, the parsed scores, and the blind contradiction count |
| `fc6.py` | the analysis: `report`, `results` (writes `RESULTS-6.md`), `verify` |
| `RESULTS-6.md` | generated: verdicts, tables, intervals, per-question scores, every deviation |

**[`PREREG-1.md`](PREREG-1.md)** — the smaller standalone round first planned for this skill. Its Amendment 2, committed before any run, superseded it with round 5; Parts A and B never ran.

`scripts/check.sh` rebuilds rounds 4 and 5 from the raw data: every blinded packet must be byte-identical to what the judge read, every judgment re-parses into the same scores, and `RESULTS.md`, `RESULTS-V5.md`, the README tables and the charts must match a fresh regeneration. It also runs `fc6.py verify`, which rebuilds every round-6 packet, rebuilds every judged rewrite from its attempts and audits, and re-parses every judgment.

Rounds 1–3 of the study, and the same data seen from the full council: the wise-men repository's [`eval-data/head-to-head/`](https://github.com/Ali-expandings/wise-men/tree/master/eval-data/head-to-head).
