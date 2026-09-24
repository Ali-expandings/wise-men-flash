# arm: brainstorming (obra/superpowers 5bf4e7801107, with visual-companion.md and spec-document-reviewer-prompt.md) | question: R506 | orchestrator: general-purpose/sonnet | run: 2026-09-24 (round 5, PREREG-5 rules)
# minutes: 5.2 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 4/28936/120901/47642 | list-price USD: 0.65

This looks like a spike: you want a judgment call and the common failure patterns, not a document to draft together — treating it that way. Probe: tone recommendation, whether to address the counterfactual, where these usually go wrong, then a structure you can use. Assuming yes on that, since it's the question you already asked — going ahead.

**Tone**

Neither pure technical memo nor personal apology works alone.

Pure technical ("found a formula error, corrected loss figure attached") reads as covering yourself rather than reckoning with what that number did. Given people lost jobs over it, clinical precision alone reads worse, not better.

Pure apology ("I'm so sorry, I feel awful about this...") centers your guilt instead of the facts the exec team now needs. It forces them to manage your emotions instead of deciding what to do next, and can read as fishing for reassurance in the middle of something that isn't about you.

The right register: direct, factual, accountable, no theatrics. Error and corrected number in sentence one. Ownership in one plain sentence — no escalating adjectives ("devastated," "horrified"); those shift focus onto you. One line acknowledging the human stakes, because the office closed and people lost jobs and pretending otherwise is its own tell — but one line, not the centerpiece. Save any relational repair for a live conversation, not the written correction.

**The counterfactual — address it, don't dodge it**

This is the part everyone wants to skip, and skipping it is the single biggest failure mode in messages like this. Cover three things: the corrected number, what role the original (wrong) number played in the recommendation — decisive, or one factor among several — and your honest read on whether the correction plausibly changes the conclusion. Don't overclaim certainty in either direction: office-closure calls usually weigh lease terms, strategic fit, and headcount trends alongside the loss figure, so "the office would still be open" and "nothing would've changed" are both unearned confidence, and both read as self-serving in hindsight. But if a 40%-overstated loss figure was a primary driver of that call, say so plainly. That sentence carries more weight than the apology and more than the methodology.

**Where these go wrong**

- Burying the finding under methodology or preamble — exec readers skim; if the number and its consequence aren't in sentence one, it reads as evasive even when it isn't.
- Word choice that undersells the magnitude — "small discrepancy" for a 40% overstatement burns credibility fast, and looks worse later if anyone re-reads it.
- Over-apologizing, which makes it about your guilt instead of next steps.
- Dodging the counterfactual, or overclaiming it with false certainty either way.
- No scope check — not saying whether the same formula error sits in any other live model. That's the first follow-up question you'll get; have an answer ready or say you're checking.
- Passive voice that diffuses ownership — "it was discovered that an error existed" reads as spin.
- Wrong channel — Slack, or a line buried in a status report, for something this consequential reads as minimizing it.
- No proposed next step — leaving the exec team to work out alone what happens now: anything owed to remaining staff, anyone else who needs to know, whether other pending calls lean on the same model.

**Structure**

1. The correction and corrected number.
2. Cause, one line.
3. The role the error played in the original call, and your honest materiality read.
4. One line of direct ownership.
5. What you're doing now — re-auditing related models for the same bug.
6. A request for a conversation, not just an email left to sit.

Rough skeleton, not a final draft:

"I found an error in the [office] closure analysis I ran in [month]: a formula issue overstated the office's losses by roughly 40%. Corrected figure is [$X], not [$Y].

That loss figure was [the primary driver / one factor among several] in the closure recommendation. With the corrected number, I [believe the case for closure would have been meaningfully weaker / don't believe this changes the underlying case, because ___]. Flagging that directly rather than leaving it unstated.

This was my error and I'm owning it. I'm re-checking [related models] now for the same issue and will report back by [date].

I'd like to walk you through this rather than leave it as an email — do you have 15 minutes [this week]?"

**Before you send it**

Loop your manager in first, and if this touches severance or anything with legal exposure, flag legal/HR too — not to soften the finding, but so it lands coordinated instead of surprising the people who'll get asked about it within the hour.
