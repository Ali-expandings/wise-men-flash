# Contributing

- Run `scripts/check.sh` before every commit. It enforces what the skill and its evidence depend on: version stamps agree, `SKILL.md` is self-contained and free of `$`-digit sequences (Claude Code substitutes them), the member agent's frontmatter is intact, every blinded packet rebuilds byte-identical from the raw answers, the parsed scores match the judgments, `RESULTS.md`, the examples, the README tables and the charts match a fresh regeneration, and a PII sweep of the tree and the git history is clean.
- `eval-data/` is a record, not code. Round 4's files are byte-identical copies from the wise-men repository: never edit them. A new measurement gets a pre-registration committed before its first run — `eval-data/PREREG-1.md` is next.
- A protocol change needs evidence — a pre-registered run, or at least a recorded council run — not only reasoning. Say which in `CHANGELOG.md`.
- Charts in `assets/` are generated: edit `scripts/make_charts.py`, not the SVGs.
- Flash stays four calls. A change that needs peer review or a debate round belongs in the full [`wise-men`](https://github.com/Ali-expandings/wise-men) skill.
- No attribution trailers in commits.
