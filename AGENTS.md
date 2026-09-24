# For agents other than Claude Code

This repository is a Claude Code plugin/skill. The whole protocol is `SKILL.md` — self-contained, no resource files — and any agent that can spawn parallel sub-tasks can follow it as written. Two things are Claude-Code-specific:

- **The tool-restricted member** (`agents/wise-member.md`, Read/Grep/Glob only) is what makes council recursion structurally impossible. In another runtime, reproduce it with whatever sandboxing you have; without it, members are only *asked* not to spawn.
- **Tier aliases**: the routing table names `opus`, `sonnet` and `haiku`, the values Claude Code's Agent tool takes. Elsewhere, map them to your strong, mid and cheap models.

The evidence in `eval-data/` and the checks in `scripts/check.sh` are runtime-independent.
