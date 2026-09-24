# arm: brainstorming (obra/superpowers 5bf4e7801107, with visual-companion.md and spec-document-reviewer-prompt.md) | question: R507 | orchestrator: general-purpose/sonnet | run: 2026-09-24 (round 5, PREREG-5 rules)
# minutes: 7.9 | subagent calls: 1 (transcripts matched: 1) | tokens in/out/cache-read/cache-write: 20/45966/885057/119880 | list-price USD: 1.40
# note: a local scratch-folder path in the answer (it contains the author's machine username) was redacted to <scratch> here and in the three blinded packets after judging; the judges saw the unredacted path

This is architectural — a real hiring decision with competing stakeholder interests, non-reversible consequences either way, and a written artifact worth keeping — so I'm following the full path: questions, approaches, sectioned design, written spec, self-review.

## Questions asked, and the answers assumed

**How much weight does "formal investigation, unknown outcome" carry?** Treated as a reason to look closer, not a reason to conclude anything — a lead, not a verdict.

**Where does the process stand — offer out, or still deciding?** Read as still open, since the question is framed as what you *owe* people, which is only live pre-decision.

**Has every legitimate diligence channel been used, or just the standard one?** Read as just the standard one — "formal references" reads as the candidate's own curated list; back-channel references and HR-to-HR outreach haven't been described as tried.

**Is this about this candidate only, or also about handling the next tip like this?** Read as primarily this candidate; the memo generalizes but doesn't expand scope to a general policy.

## Approaches considered

1. **Proceed on the documented record** — safest and fastest, but only comfortable if "I heard something and did nothing further" is a sentence you're fine standing behind later, for a role with direct authority over junior staff.
2. **Quiet, proportionate diligence** — broaden references (add a peer/direct-report reference), add structured management-focused interview questions. Requires citing no one; can still be fooled by a smooth interviewer or a stonewalling ex-employer.
3. **Institutional escalation** — loop HR in now, generically, no source named; let them decide how far to push. Converts one person's judgment call on hearsay into an institutional, documented one.
4. **Rejected: act on the tip directly** — deprioritizing the candidate now on a pretext, or confronting them with the claim. Both create real exposure and the second unmasks your colleague.

**Recommendation:** run 2 and 3 together, HR-first — not instead of each other.

Spec written to `<scratch>/R507/brainstorming/2026-09-24-candidate-investigation-tip-design.md`. Self-review: **Approved**, one clause tightened for a sequencing ambiguity the review flagged (recommendation text now matches the literal order in the action sequence). Proceeding on the assumption you'd want the finished memo rather than another review round.

---

# Candidate Background Concern — Decision Memo

**Date:** 2026-09-24
**For:** Hiring manager, team lead role
**Path:** Architectural (brainstorming skill)

## Situation

A former colleague privately told you that your leading candidate for a team lead opening left their last job while an internal investigation into their treatment of junior staff was still open. Two limits on the tip: your colleague doesn't know how the investigation concluded, and she asked you not to repeat what she said. Separately, the candidate's formal references — the ones supplied through the normal hiring process — are glowing.

Three facts, held separately rather than blended into one story:

- **A formal process existed.** Companies don't open internal investigations into management conduct casually; this clears the bar of "someone was annoyed," even though it says nothing about the finding.
- **The finding is unknown.** Investigations end substantiated, unsubstantiated, or inconclusive/settled-quietly. Your source doesn't know which, so neither do you.
- **The glowing references don't contradict the tip.** Candidate-supplied references are curated by definition — they wouldn't include a manager who was party to an investigation unless specifically asked to be. Clean formal references and an open internal investigation aren't inconsistent; they're two different, incomplete windows into the same person.

The role itself is the fact pattern's fault line: team lead means direct authority over junior staff, which is exactly the relationship the alleged conduct concerned. That raises the cost of getting this wrong in either direction — reject a good candidate on a rumor, or hand a bad manager direct power over the people you're trying to protect.

## Assumptions (asked and answered)

**How much weight does "formal investigation, unknown outcome" carry?**
Treated as a reason to look closer, not a reason to conclude anything. It's a lead, not a verdict — it justifies spending diligence you wouldn't otherwise spend, not a decision made on its own.

**Where does the process stand — offer out, or still deciding?**
Read as still open. Asking what you owe people is a live question only if the decision isn't made yet. If an offer has already gone out and been accepted, several steps below — especially the additional-reference ask — get harder to run cleanly, and this memo would need to shift toward onboarding-stage safeguards instead of pre-offer diligence.

**Have every legitimate diligence channel already been used, or just the standard one?**
Read as: just the standard one. "Formal references" specifically, in most processes, means the candidate's own curated list. Back-channel references, candidate-provided peer or direct-report references, and HR-to-HR outreach are different tools, and nothing in the question suggests they've been tried yet.

**Is this about this candidate only, or also about handling the next tip like this?**
Read as primarily this candidate. The memo is decision-specific, but the approach generalizes, and it's written generic enough to reuse.

## What's owed to each party

**The candidate.** A decision based on evidence they can see and respond to, not on a claim they never get to answer. Whatever gets concluded should trace to something citable — an interview answer, a reference, a documented pattern — not to "someone told me something." That cuts both ways: it means the tip alone can't be used to penalize them, and it also means they shouldn't be waved through unexamined just because acting on the tip feels awkward.

**The people who'd report to them.** A genuine effort to check fit for a supervisory role before handing someone authority over them — proportional effort, not a witch hunt, but not nothing either. This is the one obligation that doesn't go away just because verification is hard. "It couldn't be confirmed" is a reasonable stopping point after real effort; it's not a reasonable reason to skip the effort. In many jurisdictions this also tracks a real legal concept (often called negligent hiring or negligent retention) when an employer places someone in a position of authority despite a reasonably available red flag and that person then harms someone in that role. Specifics vary by jurisdiction and this isn't legal advice — loop in HR/Legal for anything jurisdiction-specific — but it's a good proxy for the ethical floor even where it isn't binding law.

**The former colleague.** Her name and the fact that she said anything stay out of everything that happens next. She asked for that explicitly, and she has more to lose from being identified than there is to gain from naming her — professional blowback, being read as a gossip, strain with the old employer or the candidate if the industry is small. Every step below is written to work without ever citing her, including in escalations to HR. She's also owed accuracy: she handed over a lead, not an accusation, and it should be carried that way — not inflated into more certainty than she gave it.

## Approaches considered

**1. Proceed on the documented record.** Ignore the tip, decide on interviews and the references already in hand. Simplest, fastest, fully respects the candidate's due process, and it's the safest posture if the decision is ever questioned. The gap: it only works if "I heard something and did nothing further" is a comfortable answer later, if this candidate turns out to be exactly what the tip implied — and for a role with direct authority over junior staff, that's a harder sentence to stand behind than it sounds.

**2. Quiet, proportionate diligence.** Don't disclose the tip anywhere. Broaden what gets checked instead: ask the candidate for additional references beyond the initial list — specifically former peers or people who reported to them, a standard ask for a leadership hire that needs no special justification — and add structured interview questions probing management style, handling of underperformance, and specific examples of supporting junior staff, scored for consistency and specificity rather than polish. Proportionate, requires citing no one, and treats the tip as what it is — a reason to dig, not a verdict. Real failure mode: a candidate who mismanaged people can still give smooth interview answers, and a former employer can stonewall a back-channel call as easily as a formal one.

**3. Institutional escalation.** Loop in HR (and Legal, if the org's process calls for it) now, described generically — "a concern has reached me about this candidate's management conduct at their last role; I can't verify it or say more about the source" — and let them decide how far to push, including whether an HR-to-HR call reaches further than a standard reference check. This converts one manager's private judgment call into an institutional, documented one: fairer to the candidate, since the call isn't riding on one person's gut reaction to hearsay, and safer for the hiring manager, since this is exactly the kind of decision that shouldn't rest on one person quietly sitting on secondhand information. Slower, and it widens the circle of people who know something is being checked — though never who told you.

**Rejected outright: act on the tip directly.** Two moves that feel responsive but aren't on the table — quietly deprioritizing the candidate now while citing some other reason, or confronting them directly with the investigation. The first is an adverse decision made on unverifiable, uncitable information; examined later, it looks exactly like a pretextual decision, which is the fact pattern that creates real legal exposure regardless of whether the underlying tip was true. The second identifies the colleague as the source the moment the candidate starts asking who knew, breaks the one promise she explicitly asked to have kept, and puts an unproven claim in front of the person it's about as though it were established fact.

## Recommendation

Run institutional escalation and quiet diligence together: loop HR in first, then run both in parallel without waiting on HR's own outreach to conclude. Tell HR now, generically and without naming the source, and have them run (or authorize running) the broadened reference and structured-interview steps as a normal part of closing out this hire. Most of what "quiet diligence" needs — additional references, a back-channel call — goes through recruiting/HR anyway, so this isn't two plans, it's one plan where HR owns the record and the hiring manager owns the extra questions.

## Action sequence

1. **Talk to HR before doing anything else.** Frame: "A concern about this candidate's people-management conduct at their previous role has reached me informally. I can't verify it and I'm not able to identify the source. I'd like to run additional reference checks and management-focused interview questions before we finalize." No name, no company detail beyond what HR needs to act.
2. **Ask the candidate for two more references** — specifically a former peer and, if possible, someone who reported to them. Standard practice for a leadership hire; needs no justification beyond "we like a couple more angles for people-lead roles."
3. **Add or re-run structured interview questions** on conflict handling, feedback delivery, and specific examples of developing junior staff. Score for specificity and consistency, not polish — and do this regardless of what step 2 turns up, since it's good practice for any people-lead hire.
4. **Let HR decide on further outreach.** An HR-to-HR call to the former employer sometimes gets more candor than a manager-level reference call, precisely because it isn't attributable to the hiring manager or the colleague.
5. **Decide on the combined record** — interviews, all references, whatever step 4 returns — never on the original tip, which stays a reason to look, never a reason to rule.

## Guardrails

Don't write the tip down anywhere it could be read as a factual claim about the candidate — describe it as an unverified concern, always. Don't let it reach anyone else on the interview panel in a form more specific than "extra diligence on management fit for this role is underway." Don't extend the process indefinitely hoping something surfaces — if step 4 comes back clean, that's a real answer, not a delay to keep re-litigating. If anyone asks how this started, the honest answer is "an informal concern came to me that I couldn't verify and can't attribute" — true, complete enough to explain the actions taken, and protective of the colleague without requiring a lie.

## Decision criteria

Proceed if the broadened references and structured interviews come back clean or unremarkable — that's a genuinely stronger record than the starting point, not just an absence of evidence. Pause and go deeper if anything concrete surfaces independently through steps 2–4 — a named incident, a reference who hesitates in a specific, describable way — not just a vibe. Don't treat "nobody confirmed it" as equivalent to "it didn't happen," but do treat it as the honest limit of what can be acted on: there's no obligation to solve an unsolvable verification problem, only to make a good-faith attempt proportionate to the role.

## Closing the loop with the colleague

No report on what was done is owed, but if the relationship allows it, a short private "thanks for the heads-up — I took it seriously and handled it without using your name" closes the loop without adding detail. It tells her the risk she took wasn't wasted, without asking her to carry any more of it than she already has.
