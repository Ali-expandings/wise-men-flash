# Spot check: two rewrites to read before any judging

The owner reads these before any judge runs (PREREG-6 Part A, step 4 of "How nothing new is enforced"). The two questions, R503 and R506, were drawn in `seal6.yaml` before any rewrite existed.

For each question there are three texts, one after the other: the plain answer from round 5 (the source), with every sentence numbered S1, S2, …; then the two rewrites of it, the long one (`plain-memo`, stretched to flash's length) and the short one (`plain-memo-short`, at the plain answer's own length). After every rewrite sentence, in brackets, are the source sentences it restates, as the blind auditor mapped them. CONNECTIVE means the auditor found it only links or introduces; FIXED is one of the three set sentences for an empty section.

What to look for: any rewrite sentence that says something the source does not say (a new fact, number, example, step, risk or argument), or that sounds more certain or less certain than the source. Note it by question, arm and R number (for example "R503 plain-memo R14: adds a new step"). Anything marked is deleted the same way the audit's findings are, and listed in the results.

## R503

**The question.** Of the last ten mid-size deals we lost, our sales team logged 'missing automation features' as the reason for seven, and our closest competitor has a polished automation builder. I'm deciding whether to spend two quarters building our own or to buy a small startup that already has one, which would use up most of our cash reserve. For a company of about 80 people, which path makes more sense?

### The source: round 5's plain answer, numbered

**S1** Before picking a lane, pressure-test the "7 of 10" number. **S2** Sales-logged loss reasons skew toward whatever's easiest to blame — "missing feature" is a lot more comfortable to write up than "we got outsold" or "we were priced wrong" or "we pitched the wrong buyer." **S3** Pull 3-4 of those deals and check with the actual prospect or the AE's notes/call recordings whether automation was really the deciding factor or just the visible excuse. **S4** If it holds up, keep reading.

**S5** **The real choice isn't binary.** **S6** Build vs. buy skips a third option that fits your situation better: license or embed an existing automation engine (Workato, Tray.ai, n8n, Zapier's partner/embed API) into your product. **S7** That gets a genuinely polished builder in front of prospects in weeks, costs a subscription or rev-share instead of your cash reserve, and buys you real data on whether automation actually closes deals before you commit two quarters or your war chest to it.

**S8** **Why "buy" is the riskier of your two named options.** **S9** At 80 people, your cash reserve isn't spare change — it's your runway through a bad quarter, a slow raise, a downturn. **S10** Spending most of it to acquire a small startup for one feature is a bet-the-company move, and small-company acquisitions almost never save the time you think they will: replatforming the acquired product onto your auth/billing/data model, retaining the founding team past their cliff, merging support and docs — that's typically 12-18 months, not zero. **S11** You don't skip the two quarters, you add integration risk and cash risk on top of a similar timeline. **S12** It only makes sense if you're already profitable (reserve isn't your survival buffer), the price is small relative to reserve rather than "most of it," or the team's expertise is the real prize and the product is secondary.

**S13** **Why "build in two quarters" is optimistic.** **S14** The core workflow engine might land in two quarters. **S15** The polish — templates, edge-case handling, reliability, the UX refinement that's actually what "polished" means to a buyer comparing you to a competitor who's had a head start — usually runs 2-3x that. **S16** And pulling meaningful engineering headcount off roadmap for two-plus quarters at an 80-person company has real opportunity cost elsewhere; account for what else slips.

**S17** **Recommendation:** don't spend most of your cash reserve on this. **S18** Stop the bleeding now with a partner/embed integration, build the differentiated core in-house on a realistic (not optimistic) timeline, and keep the acquisition option only for a target priced well under "most of reserve" or where you're clearly buying a team, not a feature. **S19** If you're already cash-flow positive and the reserve isn't your lifeline, or no embeddable option fits your stack (heavily regulated, on-prem, etc.), that changes the math toward buy — but as framed, spending your buffer to fix one feature gap is disproportionate to the risk.

### The long rewrite (`plain-memo`, attempt 2, 1502 words)

**Recommendation**

Don't spend most of your cash reserve on this. [R1: S17] Of the two paths you named, the acquisition is the riskier one, and the two-quarter in-house build is optimistic. [R2: S8, S13] The recommended course is to stop the bleeding now with a partner or embed integration. [R3: S18] Then build the differentiated core in-house on a realistic timeline rather than an optimistic one. [R4: S18] Keep the acquisition option only for a target priced well under "most of reserve", or one where you are clearly buying a team, not a feature. [R5: S18]

The choice you face is not really binary. [R6: S5] Build versus buy skips a third option that fits your situation better: licensing or embedding an existing automation engine into your product. [R7: S6] Before committing to anything, pressure-test the "7 of 10" number, since sales-logged loss reasons skew toward whatever is easiest to blame. [R8: S1, S2] If it holds up, keep reading and follow the plan below. [R9: S4]

As framed, spending your buffer to fix one feature gap is disproportionate to the risk. [R10: S19] The circumstances that would move the math toward buying are listed under the strongest counter-position. [R11: CONNECTIVE]

**Why**

**The "7 of 10" number needs a test first.** [R12: S1] Sales-logged loss reasons skew toward whatever is easiest to blame. [R13: S2] "Missing feature" is a lot more comfortable to write up than "we got outsold," "we were priced wrong," or "we pitched the wrong buyer." [R14: S2] So the figure should be pressure-tested before it drives a decision of this size. [R15: S1]

**A third option beats the binary.** [R16: S5, S6] You can license or embed an existing automation engine in your product, such as Workato, Tray.ai, n8n or Zapier's partner/embed API. [R17: S6] That gets a genuinely polished builder in front of prospects in weeks. [R18: S7] It costs a subscription or rev-share instead of your cash reserve. [R19: S7] It also buys you real data on whether automation actually closes deals, before you commit two quarters or your war chest to it. [R20: S7]

**Buying is the riskier of your two named options.** [R21: S8] At 80 people, your cash reserve is not spare change. [R22: S9] It is your runway through a bad quarter, a slow raise, or a downturn. [R23: S9] Spending most of it to acquire a small startup for one feature is a bet-the-company move. [R24: S10] Small-company acquisitions almost never save the time you think they will. [R25: S10] Replatforming the acquired product onto your auth, billing and data model takes work. [R26: S10] So does retaining the founding team past their cliff, and so does merging support and docs. [R27: S10] Together that is typically 12-18 months, not zero. [R28: S10] So you do not skip the two quarters. [R29: S11] You add integration risk and cash risk on top of a similar timeline. [R30: S11]

Buying only makes sense in three cases. [R31: S12] The first is that you are already profitable, so the reserve is not your survival buffer. [R32: S12] The second is that the price is small relative to the reserve rather than "most of it". [R33: S12] The third is that the team's expertise is the real prize and the product is secondary. [R34: S12]

**Building in two quarters is optimistic.** [R35: S13] The core workflow engine might land in two quarters. [R36: S14] The polish usually runs 2-3x that. [R37: S15] Polish here means templates, edge-case handling, reliability, and the UX refinement that is actually what "polished" means to a buyer comparing you to a competitor who has had a head start. [R38: S15] Pulling meaningful engineering headcount off the roadmap for two-plus quarters at an 80-person company also has real opportunity cost elsewhere, so you need to account for what else slips. [R39: S16]

**Putting it together.** [R40: CONNECTIVE] The embed route addresses the gap now without touching the reserve. [R41: S7, S18] The in-house build is kept for the differentiated core. [R42: S18] The acquisition is held back because, as framed, spending your buffer to fix one feature gap is disproportionate to the risk. [R43: S18, S19]

**What to do**

1. Pressure-test the "7 of 10" number first. [R44: S1] Pull 3-4 of those lost deals and check with the actual prospect, or with the account executive's notes and call recordings, whether automation was really the deciding factor or just the visible excuse. [R45: S3] If it holds up, keep reading, which means moving on to the remaining steps. [R46: S4]

2. Stop the bleeding now with a partner or embed integration. [R47: S18] License or embed an existing automation engine (Workato, Tray.ai, n8n, Zapier's partner/embed API). [R48: S6] That puts a polished builder in front of prospects in weeks, paid for by a subscription or rev-share instead of your cash reserve. [R49: S7]

3. Use the embedded builder to gather real data on whether automation actually closes deals. [R50: S7] Do this before you commit two quarters or your war chest to a larger investment. [R51: S7]

4. Build the differentiated core in-house, on a realistic timeline, not an optimistic one. [R52: S18] Remember that the core workflow engine might land in two quarters while the polish usually runs 2-3x that. [R53: S14, S15] Account for what else slips when meaningful engineering headcount comes off the roadmap. [R54: S16]

5. Do not spend most of your cash reserve. [R55: S17] Keep the acquisition option only for a target priced well under "most of reserve", or where you are clearly buying a team, not a feature. [R56: S18]

6. Check the conditions that change the math. [R57: S19] If you are already cash-flow positive and the reserve isn't your lifeline, or no embeddable option fits your stack (heavily regulated, on-prem, etc.), the math moves toward buy. [R58: S19]

**Risks of this plan**

The loss data is a risk to the whole decision. [R59: S1, S2] Sales-logged reasons skew toward whatever is easiest to blame. [R60: S2] The check on 3-4 deals is there to establish whether automation was really the deciding factor or just the visible excuse. [R61: S3]

Buying is the riskier of your two named options. [R62: S8] At 80 people your cash reserve is your runway through a bad quarter, a slow raise, or a downturn. [R63: S9] Spending most of it on a small startup for one feature is a bet-the-company move. [R64: S10] Small-company acquisitions almost never save the time you think they will. [R65: S10] Replatforming onto your auth, billing and data model, retaining the founding team past their cliff, and merging support and docs typically take 12-18 months, not zero. [R66: S10] You would add integration risk and cash risk on top of a similar timeline. [R67: S11]

Building in-house also carries risk. [R68: S13] Two quarters is optimistic. [R69: S13] The core workflow engine might land in that time, but the polish usually runs 2-3x that. [R70: S14, S15] Your competitor has had a head start, and buyers compare you to it. [R71: S15] Pulling meaningful engineering headcount off the roadmap for two-plus quarters at an 80-person company has real opportunity cost elsewhere, and you need to account for what else slips. [R72: S16]

**Strongest counter-position**

The source limits its own answer in one place. [R73: CONNECTIVE] If you are already cash-flow positive and the reserve isn't your lifeline, or if no embeddable option fits your stack (heavily regulated, on-prem, etc.), that changes the math toward buy. [R74: S19]

The same logic appears in the case for buying. [R75: CONNECTIVE] It only makes sense if you are already profitable, if the price is small relative to the reserve rather than "most of it", or if the team's expertise is the real prize and the product is secondary. [R76: S12]

The source holds to its view even so. [R77: CONNECTIVE] As framed, spending your buffer to fix one feature gap is disproportionate to the risk. [R78: S19]

**Confidence**

**High** [R79: CONNECTIVE]

- Sales-logged loss reasons skew toward whatever is easiest to blame, so the "7 of 10" number should be pressure-tested. [R80: S1, S2]

- Licensing or embedding an existing automation engine gets a genuinely polished builder in front of prospects in weeks. [R81: S6, S7] It costs a subscription or rev-share instead of your cash reserve, and it buys real data on whether automation closes deals. [R82: S7]

- Buying is the riskier of your two named options. [R83: S8] Spending most of the reserve on a small startup for one feature is a bet-the-company move. [R84: S10]

- Small-company acquisitions almost never save the time you think they will, and buying adds integration risk and cash risk on top of a similar timeline. [R85: S10, S11]

- Buying only makes sense if you are already profitable, if the price is small relative to the reserve, or if the team's expertise is the real prize. [R86: S12]

- Pulling meaningful engineering headcount off the roadmap has real opportunity cost elsewhere. [R87: S16]

- Don't spend most of your cash reserve on this. [R88: S17] Being cash-flow positive, or having no embeddable option that fits your stack, changes the math toward buy. [R89: S19]

**Medium** [R90: CONNECTIVE]

- Replatforming, retaining the founding team, and merging support and docs typically take 12-18 months, not zero. [R91: S10]

- The polish usually runs 2-3x the time the core engine takes. [R92: S15]

**Low** [R93: CONNECTIVE]

- The core workflow engine might land in two quarters. [R94: S14]

**Unknowns the source names** [R95: CONNECTIVE]

- Whether automation was really the deciding factor in the lost deals or just the visible excuse. [R96: S3]

- Whether you are already profitable or cash-flow positive, so that the reserve is not your survival buffer or lifeline. [R97: S12, S19]

- Whether the acquisition price would be small relative to the reserve rather than "most of it". [R98: S12]

- Whether the team's expertise is the real prize and the product secondary. [R99: S12]

- Whether an embeddable option fits your stack, given cases such as heavily regulated or on-prem environments. [R100: S19]

- What else slips on the roadmap when engineering headcount is pulled off it. [R101: S16]

Length: 1,502 words; its pre-registered band is 1,456–1,778 (inside).

Audit result for this version (after the one retry): NEW 0, STRONGER 0, WEAKER 0, DROPPED 0. Nothing deleted.

### The short rewrite (`plain-memo-short`, attempt 2, 735 words)

**Recommendation**

Don't spend most of your cash reserve on this. [R1: S17] Stop the bleeding now with a partner or embed integration. [R2: S18] Build the differentiated core in-house on a realistic (not optimistic) timeline. [R3: S18] Keep the acquisition option only for a target priced well under "most of reserve" or where you are clearly buying a team, not a feature. [R4: S18] As framed, spending your buffer to fix one feature gap is disproportionate to the risk. [R5: S19]

**Why**

The real choice isn't binary. [R6: S5] Build versus buy skips a third option that fits your situation better: license or embed an existing automation engine. [R7: S5, S6] That gets a genuinely polished builder in front of prospects in weeks. [R8: S5, S7] It costs a subscription or rev-share instead of your cash reserve. [R9: S5, S7] It also buys you real data on whether automation actually closes deals before you commit two quarters or your war chest to it. [R10: S5, S7]

Buying is the riskier of your two named options. [R11: S8] At 80 people, your cash reserve isn't spare change. [R12: S8, S9] It is your runway through a bad quarter, a slow raise, or a downturn. [R13: S8, S9] Spending most of it to acquire a small startup for one feature is a bet-the-company move. [R14: S8, S10] Small-company acquisitions almost never save the time you think they will. [R15: S8, S10] Replatforming the acquired product onto your auth, billing and data model, retaining the founding team past their cliff, and merging support and docs is typically 12-18 months, not zero. [R16: S8, S10] You don't skip the two quarters. [R17: S8, S11] You add integration risk and cash risk on top of a similar timeline. [R18: S8, S11]

Building in two quarters is optimistic. [R19: S13] The core workflow engine might land in two quarters. [R20: S13, S14] The polish usually runs 2-3x that. [R21: S13, S15] Polish means templates, edge-case handling, reliability, and the UX refinement that is actually what "polished" means to a buyer comparing you to a competitor who has had a head start. [R22: S13, S15] Pulling meaningful engineering headcount off roadmap for two-plus quarters at an 80-person company has real opportunity cost elsewhere. [R23: S13, S16]

**What to do**

1. Before picking a lane, pressure-test the "7 of 10" number. [R24: S1] Sales-logged loss reasons skew toward whatever is easiest to blame. [R25: S2] "Missing feature" is a lot more comfortable to write up than "we got outsold," "we were priced wrong," or "we pitched the wrong buyer." [R26: S2]

2. Pull 3-4 of those deals. [R27: S3] Check with the actual prospect, or the AE's notes and call recordings, whether automation was really the deciding factor or just the visible excuse. [R28: S3] If it holds up, keep reading. [R29: S4]

3. License or embed an existing automation engine, such as Workato, Tray.ai, n8n, or Zapier's partner/embed API. [R30: S5, S6, S18]

4. Build the differentiated core in-house on a realistic timeline, and account for what else slips. [R31: S16, S18]

5. Keep the acquisition option only for a target priced well under "most of reserve," or where you are clearly buying a team, not a feature. [R32: S18]

**Risks of this plan**

Building pulls engineering headcount off roadmap, so other work slips. [R33: S16] The "7 of 10" figure may turn out to be the visible excuse rather than the real cause. [R34: S2, S3, S4] Your polished builder from a licensed engine depends on an embeddable option fitting your stack. [R35: S7, S19]

**Strongest counter-position**

Acquisition only makes sense if you're already profitable (reserve isn't your survival buffer), the price is small relative to reserve rather than "most of it," or the team's expertise is the real prize and the product is secondary. [R36: S8, S12] If you're already cash-flow positive and the reserve isn't your lifeline, or no embeddable option fits your stack (heavily regulated, on-prem, etc.), that changes the math toward buy. [R37: S19] But as framed, spending your buffer to fix one feature gap is disproportionate to the risk. [R38: S19]

**Confidence**

High: your reserve is your runway; spending most of it on a one-feature acquisition is a bet-the-company move; small-company acquisitions almost never save the time you think they will; buying adds integration risk and cash risk on top of a similar timeline; sales-logged loss reasons skew toward easy blame; embedding gets a polished builder in front of prospects in weeks at subscription or rev-share cost; the recommendation is disproportionate-risk as framed. [R39: S2, S7, S9, S10, S11, S19]

Medium: replatforming and related integration is typically 12-18 months; polish usually runs 2-3x the core build. [R40: S10, S15]

Low: the core workflow engine might land in two quarters. [R41: S14]

Unknowns: whether automation was really the deciding factor in those deals; whether you are already profitable or cash-flow positive; the price relative to reserve; whether the team's expertise is the real prize; whether an embeddable option fits your stack. [R42: S3, S4, S12, S19]

Length: 735 words; its pre-registered band is 424–518 (outside the band, which the plan's rules could not repair; the owner decides how it is used, see DEVIATIONS.md).

Audit result for this version (after the one retry): NEW 0, STRONGER 0, WEAKER 0, DROPPED 0. Nothing deleted.

## R506

**The question.** Three months ago I wrote the analysis our executives used to justify closing our smallest regional office, and I've just found a formula error that overstated that office's losses by about 40%. The office is already closed and its staff were laid off. I can't decide whether my correction to the executive team should read as a plain technical fix or a personal apology, or whether it should say anything about how the decision might have gone with the right numbers. What tone is right for a message like this, and how do these usually go wrong?

### The source: round 5's plain answer, numbered

**S1** Separate three things you're currently treating as one decision, because collapsing them is exactly how these letters go wrong: the factual correction, the acknowledgment of fault, and the claim about what would have happened. **S2** They don't deserve equal airtime.

**S3** **Tone: factual and briefly owned, not clinical and not penitential.** **S4** Lead with the correction itself — what the formula error was, why it happened, what the corrected loss figure is — plainly, in the first paragraph, no hedging. **S5** That's what executives actually need and will act on. **S6** Then own it in one direct sentence: you found the error, it was yours, you're correcting it. **S7** Don't extend that into three paragraphs of remorse. **S8** Over-apologizing doesn't read as more accountable — it shifts the message's center of gravity from the numbers to your feelings, and it quietly puts the burden on the reader to reassure you. **S9** A memo that's mostly apology also buries the one thing they urgently need, which is the corrected number.

**S10** **Don't assert the counterfactual — that's the part to be most careful about.** **S11** "I made a formula error" and "the office shouldn't have closed" are different claims, and the second one you probably can't back. **S12** The original decision likely weighed things beyond this one figure — lease terms, strategic footprint, other offices under review — that you may not have full visibility into, and a corrected loss number alone doesn't tell you what the call would have been. **S13** State the correct numbers clearly and let the executives draw their own conclusion. **S14** If someone asks you directly whether it would have changed the outcome, "I don't know — that's not just my call to make" is honest, not evasive.

**S15** **This is exposure, not just tone.** **S16** The closure meant real layoffs. **S17** A written statement asserting the decision rested on bad numbers, paired with speculation that the outcome would have differed, is the kind of sentence that can resurface later if anyone affected ever disputes their termination. **S18** That's not a reason to soften the facts — get them exactly right and say them clearly — but it's a reason to keep speculation out of the written record, and if your company has any legal/HR function, loop them in before this goes to the full executive team, given people's jobs were on the line.

**S19** Where these usually go wrong, concretely:

- **S20** **Burying the correction under apology** — executives have to dig for the actual number.

- **S21** **Defensive minimizing** — "small error," "probably wouldn't have mattered anyway." **S22** Reads as covering yourself, especially given the stakes, and erodes trust in your next analysis more than the error itself does.

- **S23** **Asserting the counterfactual as fact** — claiming the decision would or wouldn't have changed, when you don't actually know that.

- **S24** **No remediation** — stating what broke without saying what you're checking elsewhere (same formula used in other models?) or what changes in your review process. **S25** Without that, the memo just documents a mistake instead of closing the loop.

- **S26** **Wrong sequencing** — the exec team finding out cold, with your manager blindsided alongside them. **S27** Give whoever owns that relationship a heads-up first.

**S28** Structurally: correction and corrected numbers first, one sentence of ownership, what you're checking/fixing going forward, then open for questions. **S29** Consider a short verbal heads-up to your manager or the decision-owner before the written version goes to the full executive team — for something this consequential, the first they hear of it shouldn't be a cold email.

### The long rewrite (`plain-memo`, attempt 2, 1645 words)

**Recommendation**

Separate three things you are currently treating as one decision, because collapsing them is exactly how these letters go wrong. [R1: S1] They are the factual correction, the acknowledgment of fault, and the claim about what would have happened. [R2: S1] They don't deserve equal airtime. [R3: S2]

The right tone is factual and briefly owned, not clinical and not penitential. [R4: S3] Lead with the correction itself, plainly, in the first paragraph, with no hedging. [R5: S3, S4] Say what the formula error was, why it happened, and what the corrected loss figure is. [R6: S3, S4] Then own it in one direct sentence: you found the error, it was yours, and you are correcting it. [R7: S3, S6] Don't extend that into three paragraphs of remorse. [R8: S3, S7]

Don't assert the counterfactual. [R9: S10] That is the part to be most careful about. [R10: S10] State the correct numbers clearly and let the executives draw their own conclusion. [R11: S10, S13]

This is exposure, not just tone. [R12: S15] Keep speculation out of the written record. [R13: S15, S18] If your company has any legal or HR function, loop them in before this goes to the full executive team, given people's jobs were on the line. [R14: S15, S18] Consider a short verbal heads-up to your manager or the decision-owner before the written version goes to the full executive team. [R15: S29] For something this consequential, the first they hear of it shouldn't be a cold email. [R16: S29]

Structurally, the message runs in this order. [R17: S28] Put the correction and the corrected numbers first. [R18: S28] Add one sentence of ownership. [R19: S28] Then say what you're checking and fixing going forward, and open the floor for questions. [R20: S28]

**Why**

The correction leads because it is what executives actually need and will act on. [R21: S3, S4, S5] Over-apologizing doesn't read as more accountable. [R22: S3, S8] It shifts the message's center of gravity from the numbers to your feelings, and it quietly puts the burden on the reader to reassure you. [R23: S3, S8] A memo that is mostly apology also buries the one thing they urgently need, which is the corrected number. [R24: S3, S9] That is why one direct sentence of ownership is enough. [R25: S3, S6, S7, S8, S9]

The counterfactual is where the most care is needed. [R26: S10] "I made a formula error" and "the office shouldn't have closed" are different claims, and the second one you probably can't back. [R27: S10, S11] The original decision likely weighed things beyond this one figure. [R28: S10, S12] Examples are lease terms, strategic footprint, and other offices under review. [R29: S10, S12] You may not have full visibility into those, and a corrected loss number alone doesn't tell you what the call would have been. [R30: S10, S12] So state the correct numbers clearly and let the executives draw their own conclusion. [R31: S10, S13]

If someone asks you directly whether it would have changed the outcome, "I don't know — that's not just my call to make" is honest, not evasive. [R32: S10, S14]

The exposure point comes from the stakes. [R33: S15, S16] The closure meant real layoffs. [R34: S15, S16] A written statement asserting the decision rested on bad numbers, paired with speculation that the outcome would have differed, is the kind of sentence that can resurface later if anyone affected ever disputes their termination. [R35: S15, S17] That's not a reason to soften the facts. [R36: S15, S18] Get them exactly right and say them clearly. [R37: S15, S18] It is, however, a reason to keep speculation out of the written record. [R38: S15, S18] It is also a reason to loop in any legal or HR function before this goes to the full executive team, given people's jobs were on the line. [R39: S15, S18]

Sequencing matters for the same reason. [R40: S19, S26, S29] If the exec team finds out cold, your manager is blindsided alongside them. [R41: S19, S26] Giving whoever owns that relationship a heads-up first is how you avoid that. [R42: S19, S27]

Remediation matters too. [R43: S19, S24] Stating what broke without saying what you're checking elsewhere, or what changes in your review process, means the memo just documents a mistake. [R44: S19, S24, S25] Saying what you're checking and fixing closes the loop. [R45: S19, S25, S28]

**What to do**

1. Separate the three pieces before you draft: the factual correction, the acknowledgment of fault, and the claim about what would have happened. [R46: S1] Give the correction the most space and the ownership one sentence. [R47: S2, S3, S4, S6]

2. Consider a short verbal heads-up to your manager or the decision-owner before the written version goes to the full executive team. [R48: S29] Give whoever owns that relationship a heads-up first, so the exec team doesn't find out cold with your manager blindsided alongside them. [R49: S19, S26, S27] For something this consequential, the first they hear of it shouldn't be a cold email. [R50: S29]

3. If your company has any legal or HR function, loop them in before this goes to the full executive team, given people's jobs were on the line. [R51: S15, S18]

4. Write the message in this order: [R52: S28]

   - **Correction and corrected numbers first.** [R53: S28] In the first paragraph, plainly and with no hedging, say what the formula error was, why it happened, and what the corrected loss figure is. [R54: S3, S4]

   - **One sentence of ownership.** [R55: S6, S28] You found the error, it was yours, and you are correcting it. [R56: S3, S6] Don't extend that into three paragraphs of remorse. [R57: S3, S7]

   - **What you're checking and fixing going forward.** [R58: S28] For example, say whether the same formula was used in other models. [R59: S19, S24] Also say what changes in your review process. [R60: S19, S24]

   - **Open for questions.** [R61: S28]

5. State the correct numbers clearly and let the executives draw their own conclusion. [R62: S10, S13] Get the facts exactly right and say them clearly, and keep speculation out of the written record. [R63: S15, S18]

6. If someone asks you directly whether it would have changed the outcome, the honest answer is "I don't know — that's not just my call to make." [R64: S10, S14]

7. ~~Check the draft against the ways these go wrong, which are listed in the next section.~~ [R65: NEW — S19; DELETED]

**Risks of this plan**

These are the ways a message like this usually goes wrong. [R66: S19]

- **Burying the correction under apology.** [R67: S19, S20] Executives have to dig for the actual number. [R68: S19, S20]

- **Defensive minimizing.** [R69: S19, S21] Phrases like "small error" or "probably wouldn't have mattered anyway" read as covering yourself, especially given the stakes. [R70: S19, S21, S22] They erode trust in your next analysis more than the error itself does. [R71: S19, S22]

- **Asserting the counterfactual as fact.** [R72: S19, S23] This means claiming the decision would or wouldn't have changed, when you don't actually know that. [R73: S19, S23]

- **No remediation.** [R74: S19, S24] The message states what broke without saying what you're checking elsewhere, such as whether the same formula is used in other models. [R75: S19, S24] It also leaves out what changes in your review process. [R76: S19, S24] Without that, the memo just documents a mistake instead of closing the loop. [R77: S19, S25]

- **Wrong sequencing.** [R78: S19, S26] The exec team finds out cold, with your manager blindsided alongside them. [R79: S19, S26]

~~Two further caveats come from the stakes.~~ [R80: NEW; DELETED] Over-apologizing shifts the message's center of gravity from the numbers to your feelings and quietly puts the burden on the reader to reassure you. [R81: S3, S8] And the closure meant real layoffs. [R82: S15, S16] A written statement that the decision rested on bad numbers, paired with speculation that the outcome would have differed, can resurface later if anyone affected ever disputes their termination. [R83: S15, S17]

**Strongest counter-position**

The source raises no direct argument against its own answer. [R84: CONNECTIVE] It does state limits on it. [R85: CONNECTIVE]

The first limit is on the counterfactual. [R86: CONNECTIVE] The claim that the office shouldn't have closed is one you probably can't back. [R87: S10, S11] The original decision likely weighed things beyond this one figure, and you may not have full visibility into them. [R88: S10, S12] A corrected loss number alone doesn't tell you what the call would have been. [R89: S10, S12] So the advice stops at the numbers, and if asked directly, "I don't know — that's not just my call to make" is honest, not evasive. [R90: S10, S13, S14]

The second limit is on the caution about exposure. [R91: CONNECTIVE] The source says that caution is not a reason to soften the facts. [R92: S15, S18] The facts still need to be exactly right and stated clearly, and only the speculation is kept out of the written record. [R93: S15, S18]

**Confidence**

**High** (stated without a hedge): [R94: CONNECTIVE]

- The three pieces are the factual correction, the acknowledgment of fault, and the claim about what would have happened, and they don't deserve equal airtime. [R95: S1, S2]

- The right tone is factual and briefly owned, not clinical and not penitential. [R96: S3]

- The correction leads, plainly, in the first paragraph, with no hedging. [R97: S3, S4]

- Ownership is one direct sentence, not three paragraphs of remorse. [R98: S3, S6, S7]

- Over-apologizing doesn't read as more accountable, and a memo that is mostly apology buries the corrected number. [R99: S3, S8, S9]

- "I made a formula error" and "the office shouldn't have closed" are different claims. [R100: S10, S11]

- A corrected loss number alone doesn't tell you what the call would have been. [R101: S10, S12]

- You should state the correct numbers clearly and let the executives draw their own conclusion. [R102: S10, S13]

- "I don't know — that's not just my call to make" is honest, not evasive. [R103: S10, S14]

- The closure meant real layoffs, and a written statement of that kind can resurface later if anyone affected ever disputes their termination. [R104: S15, S16, S17]

- Exposure is not a reason to soften the facts. [R105: S15, S18] It is a reason to keep speculation out of the written record and to loop in any legal or HR function. [R106: S15, S18]

- Without remediation, the memo just documents a mistake instead of closing the loop. [R107: S19, S24, S25]

- The structure is the correction and corrected numbers first, one sentence of ownership, what you're checking and fixing, then open for questions. [R108: S28]

- The source suggests considering a short verbal heads-up to your manager or the decision-owner, because the first they hear of it shouldn't be a cold email. [R109: S29]

**Medium** (stated with "probably", "likely" or "usually"): [R110: CONNECTIVE]

- The claim that the office shouldn't have closed is one you probably can't back. [R111: S10, S11]

- The original decision likely weighed things beyond this one figure. [R112: S10, S12]

- These letters usually go wrong in the ways listed: burying the correction, defensive minimizing, asserting the counterfactual, no remediation, and wrong sequencing. [R113: S19, S20, S21, S23, S24, S26]

**Low** (stated with "may", "might", "could" or "possibly"): [R114: CONNECTIVE]

- You may not have full visibility into the other factors the decision weighed. [R115: S10, S12]

**Unknowns the source names:** [R116: CONNECTIVE]

- What the call would have been with the corrected loss number. [R117: S10, S12, S14, S23]

- How much the original decision weighed beyond this one figure, such as lease terms, strategic footprint, and other offices under review, which you may not have full visibility into. [R118: S10, S12]

- Whether the same formula is used in other models. [R119: S19, S24]

Length: 1,645 words; its pre-registered band is 1,422–1,736 (inside).

Audit result for this version (after the one retry and the deletions): NEW 0, STRONGER 0, WEAKER 0, DROPPED 0. Deleted: R65 (NEW: adds a step (check the draft against the listed failure modes) that the source does not prescribe); R80 (NEW: says both following caveats come from the stakes; the source links only the exposure point to the layoffs and never ties the over-apologizing point (S8) to the stakes).

### The short rewrite (`plain-memo-short`, attempt 2, 624 words)

**Recommendation**

Separate three things you're currently treating as one decision, because collapsing them is exactly how these letters go wrong: the factual correction, the acknowledgment of fault, and the claim about what would have happened. [R1: S1] They don't deserve equal airtime. [R2: S2] The tone is factual and briefly owned, not clinical and not penitential. [R3: S3] Structurally: correction and corrected numbers first, one sentence of ownership, what you're checking and fixing going forward, then open for questions. [R4: S28]

**Why**

Lead with the correction itself, plainly, in the first paragraph, with no hedging: what the formula error was, why it happened, and what the corrected loss figure is. [R5: S4] That's what executives actually need and will act on. [R6: S5] Over-apologizing doesn't read as more accountable. [R7: S8] It shifts the message's center of gravity from the numbers to your feelings, and it quietly puts the burden on the reader to reassure you. [R8: S8] A memo that's mostly apology also buries the one thing they urgently need, which is the corrected number. [R9: S9]

Don't assert the counterfactual, which is the part to be most careful about. [R10: S10] "I made a formula error" and "the office shouldn't have closed" are different claims, and the second one you probably can't back. [R11: S11] The original decision likely weighed things beyond this one figure, such as lease terms, strategic footprint, other offices under review, that you may not have full visibility into, and a corrected loss number alone doesn't tell you what the call would have been. [R12: S12]

This is exposure, not just tone. [R13: S15] The closure meant real layoffs. [R14: S16] A written statement asserting the decision rested on bad numbers, paired with speculation that the outcome would have differed, is the kind of sentence that can resurface later if anyone affected ever disputes their termination. [R15: S17] That's not a reason to soften the facts, so get them exactly right and say them clearly, but it's a reason to keep speculation out of the written record. [R16: S18]

**What to do**

Own it in one direct sentence: you found the error, it was yours, you're correcting it. [R17: S6] Don't extend that into three paragraphs of remorse. [R18: S7]

State the correct numbers clearly and let the executives draw their own conclusion. [R19: S13]

Say what you're checking elsewhere (same formula used in other models?) and what changes in your review process. [R20: S24, S28]

If someone asks directly whether it would have changed the outcome, "I don't know — that's not just my call to make" is honest, not evasive. [R21: S14]

If your company has any legal/HR function, loop them in before this goes to the full executive team, given people's jobs were on the line. [R22: S18]

Give whoever owns that relationship a heads-up first. [R23: S27] Consider a short verbal heads-up to your manager or the decision-owner before the written version goes to the full executive team — for something this consequential, the first they hear of it shouldn't be a cold email. [R24: S29]

**Risks of this plan**

Burying the correction under apology, so executives have to dig for the actual number. [R25: S19, S20]

Defensive minimizing, such as "small error" or "probably wouldn't have mattered anyway," which reads as covering yourself, especially given the stakes, and erodes trust in your next analysis more than the error itself does. [R26: S19, S21, S22]

Asserting the counterfactual as fact when you don't actually know that. [R27: S19, S23]

No remediation, which leaves the memo documenting a mistake instead of closing the loop. [R28: S19, S24, S25]

Wrong sequencing: the exec team finding out cold, with your manager blindsided alongside them. [R29: S19, S26]

**Strongest counter-position**

No case against this recommendation is made beyond the risks above. [R30: FIXED]

**Confidence**

High: correction first; over-apologizing buries the number; layoffs create exposure. [R31: S4, S8, S9, S15, S16, S17, S28]

Medium: you probably can't back the second claim; the decision likely weighed other factors; letters usually go wrong as listed. [R32: S11, S12, S19]

Low: you may lack full visibility into those factors. [R33: S12]

Unknowns: what the call would have been. [R34: S12, S14, S23]

Length: 624 words; its pre-registered band is 517–631 (inside).

Audit result for this version (after the one retry): NEW 0, STRONGER 0, WEAKER 0, DROPPED 0. Nothing deleted.
