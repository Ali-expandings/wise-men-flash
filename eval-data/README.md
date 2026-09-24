# Evidence

Two things live here.

**[`PREREG-1.md`](PREREG-1.md)** — the pre-registration of this skill's own standalone round, committed before any run. It has not run yet.

**[`head-to-head/`](head-to-head/)** — round 4 of the wise-men head-to-head, the round that measured the profile this skill ships (as the `--fast` arm of wise-men 3.13.0). Every file in it except `flash4.py` and `RESULTS.md` is a byte-identical copy of the [wise-men repository](https://github.com/Ali-expandings/wise-men)'s `eval-data/head-to-head/` at commit `770c75a`:

| file | what it is |
|---|---|
| `PREREG-4.md` | the round's pre-registration, committed before any round-4 run |
| `question-author-prompt.txt`, `questions-r4.yaml` | the blind question author's prompt and the eight questions it wrote, used as returned |
| `raw/R401` … `raw/R405` | every arm's answer, each with a provenance header: arm and commit, minutes, subagent calls, tokens, list-price cost, and any deviation note |
| `blinding4.yaml` | the sealed answer order for every question and judge (seed 20260919), R406–R408 included |
| `judge-prompt-5.txt` | the error-first judge prompt |
| `blinded-v4/` | exactly what each judge read, plus `CAL-Q23.md`, the pre-registered calibration packet |
| `judgments-v4/` | what each judge wrote |
| `parsed-v4/` | the scores, one file per question |
| `flash4.py` | the analysis, read for flash — `report`, `results` (writes `RESULTS.md`), `examples` (writes `../../examples/`), `verify` |
| `RESULTS.md` | generated: tables, intervals, per-question scores, disclosures |

`python3 eval-data/head-to-head/flash4.py verify` rebuilds every blinded packet from the raw answers and the judge prompt and requires it to be byte-identical to what the judge read, re-parses every judgment into the scores, and checks the examples against the raw answers. Questions R406–R408 (writing, ethics, a personal decision) were never run — the round stopped at five — and no answer or judgment exists for them.

The same data seen from the full council, and rounds 1–3 of the study: the wise-men repository's [`eval-data/head-to-head/`](https://github.com/Ali-expandings/wise-men/tree/master/eval-data/head-to-head).
