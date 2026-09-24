# Security

This is markdown executed by an LLM; the attack surface is prompt injection, not code execution.

Guarded surfaces: the user's question (wrapped as data in every member prompt), file content members Read (data, never instructions), and the draft the checker reads. Members and the checker run as `wise-member` — Read/Grep/Glob only — so a hostile file cannot make them run commands, write, or spawn. The four-call spend ceiling means a crafted "high-stakes" question cannot grow the council; the skill points at the full `wise-men` instead.

Report a bypass by opening an issue with the minimal prompt or file that triggers it.
