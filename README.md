# wise-men-flash

A three-member Claude council that answers a hard question in about eleven minutes.

It is the fast tier of the [`wise-men`](https://github.com/Ali-expandings/wise-men) council, extracted into its own skill for when you want a council-quality answer *fast* rather than the full protocol. Three members reason down three different paths in parallel — a practitioner anchor named for the job, one domain lens, and a Devil's Advocate — the main thread synthesizes one decision memo, and a single fresh checker verifies it before you see it. No peer-review round, no debate: that is the trade for speed.

```
/plugin marketplace add Ali-expandings/wise-men-flash
/plugin install wise-men-flash@wise-men-flash
```

Or clone it into `~/.claude/skills/wise-men-flash` and copy `agents/wise-member.md` to `~/.claude/agents/`. If the full `wise-men` skill is already installed, its `wise-member` copy enforces the same Read/Grep/Glob boundary and works as-is.

Then: *"flash council: should we move everyone to annual billing to cut churn?"*

## What you get

A decision memo — **Recommendation / Why / What to do / Risks of this plan / Strongest counter-position / Confidence** — with none of the council machinery in it. No "the panel agreed", no scores, no vote counts. The dissent is preserved as a real counter-argument against the recommendation, not a hedge.

Four subagent calls: three members plus one synthesis check. Members are offline (Read/Grep/Glob only) and structurally cannot spawn subagents, so a "council" never fans out into a recursion.

## Does it work?

The profile this skill was extracted from ran as the **fast arm** in the `wise-men` project's pre-registered round-4 head-to-head — five questions written by an author blind to the arms, three blind Opus judges per question, a judge prompt that lists every error before it scores:

| arm | total /25 |
|---|--:|
| wise-men (full council) | 23.8 |
| **wise-men-flash (this profile)** | **23.3** |
| llm-council | 17.9 |
| Warp council | 17.5 |
| plain answer | 16.3 |

Flash was **clearly ahead of every rival council on every one of the five questions** (bootstrap intervals excluding zero), and behind the full council by half a point — inside the judges' own disagreement. It did that in roughly eleven minutes and four calls, where the full council took 33–39.

Two honest caveats:

- That 23.3 was measured as an *arm inside* `wise-men`, at the exact profile this repo extracts. This standalone skill's own benchmark is pending a flash-specific run; the number is inherited, not re-measured here. The raw answers, judgments and method live in the [`wise-men` repo](https://github.com/Ali-expandings/wise-men/tree/master/eval-data/head-to-head) (`RESULTS-V4.md`).
- The round was pre-registered at eight questions and stopped at five to conserve usage; the writing, ethics and personal-decision questions were not run. So the result covers engineering, diagnosis, product, business and research questions — not every kind.

## When to use the full `wise-men` instead

Flash is one speed. It does not scale its depth to the stakes. Reach for the full [`wise-men`](https://github.com/Ali-expandings/wise-men) skill — which adds rubric peer review, a conditional debate round, and adaptive solo → quick → standard → deep → paranoid tiers — when the call is irreversible or high-blast-radius, when the question is compound, or when you want the scored peer review and debate. The full council buys back the half point (and more, on genuinely hard multi-part questions) at 3–4× the time and cost.

## How it differs from `wise-men`

| | wise-men-flash | wise-men |
|---|---|---|
| members | 3 (anchor + one domain lens + DA) | 3–7, by tier |
| peer review | none | 3–7 reviewers, rubric-scored |
| debate | none | conditional at deep / paranoid |
| synthesis check | 1 (four checks) | 1 (six checks) |
| tiers | one fixed fast tier | solo / quick / standard / deep / paranoid |
| calls | 4 | 0–25+ |
| time | ~11 min | 2–40 min |
| answer format | the same decision memo | the same decision memo |

## Limits

Single-model (every member is Claude — persona and reasoning-procedure diversity, not architectural diversity). The Chairman is the same thread that picked the roster (the one fresh checker mitigates this, it does not remove it). Members are offline; the orchestrator verifies flagged claims afterwards. No peer review or debate — that is the speed trade, and it is why the full skill exists.

## License

MIT. Extracted from [`wise-men`](https://github.com/Ali-expandings/wise-men). Inspired by [karpathy/llm-council](https://github.com/karpathy/llm-council).
