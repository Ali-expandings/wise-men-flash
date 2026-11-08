# arm: wise-men-flash (Ali-expandings/wise-men-flash SKILL.md v0.2.0, aaabd74, unchanged at 1d6a552) | question: R503 | orchestrator: general-purpose/sonnet | run: 2026-11-08 (round 6, PREREG-6 rules)
# minutes: 2.3 | subagent calls: 4 (transcripts matched: 4) | tokens in/out/cache-read/cache-write: 16/23058/373754/117138 | list-price USD: 0.95
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | orchestrator agent: aa78087f72a7a8e21 | orchestrator model: general-purpose/claude-sonnet-5-5 | transcript sha256: 537ab19725f944192876ed61c239de57aaf8b721aec870461728a74de04807f9
# arm prompt: round 5's flash arm prompt (arm-prompts-r5.md), verbatim apart from local paths: yes | spawned: wise-member/haiku = claude-haiku-5-5 x1; wise-member/opus = claude-opus-5-5 x2; wise-member/sonnet = claude-sonnet-5-5 x1 | checker calls: 1
# note: no tool beyond Read and Agent anywhere in the run, so no web check at step 6

## Recommendation

Do not buy the startup now, and do not commit to the two-quarter build yet. Spend two to three weeks confirming why the seven deals were lost. In parallel, ship a narrow fix for the specific automations buyers asked for, using an embedded automation platform or a few native workflows. If win rate improves and buyers name workflows that layer can't cover, build a scoped native version. Don't buy.

## Why

Seven of ten is a weak signal. With ten deals, the 95% interval for the true share runs from roughly 40% to 89%. The reason was also logged by the reps who lost the deals. Reps often favor "missing features" over pricing, weak discovery or a lost champion, because it blames them least (unverified: check against any buyer interviews you already have). Independent win/loss interviews often give a different main reason than the CRM entry (unverified: same check). Neither path fixes a wrong diagnosis.

Buying is the worse of the two offered paths. It puts most of the cash reserve into one bet, so if the diagnosis is wrong you have no money left to try anything else. A small startup's code usually sits on a different data model, login system and multi-tenant setup. Integration therefore often takes about as long as building it yourself (unverified: typically 2 to 4 quarters). The founders and key engineers can also leave when retention terms end.

Building is a bounded cost, but a polished workflow builder usually costs more than it looks (unverified: "two quarters" often becomes three or four). The canvas is the easy part. Retries, error handling, versioning, permissions, audit logs and debugging tools are the slow part. Your competitor's builder likely took years, so a rougher copy shipped late can still lose the side-by-side demo. The build also pulls engineers off the roadmap that serves your current customers.

The option your question leaves out is cheaper than either. Close the specific gap quickly, then decide. Embedded automation vendors (for example Workato Embedded, Tray Embedded, Paragon, Prismatic, Cyclr) or a Zapier/Make integration plus a few native triggers and actions can cover the few workflows buyers named. That takes weeks to about a quarter, for a licence that typically costs tens of thousands of dollars a year (unverified: get quotes). You can stop it at any time, and it shows whether closing the gap moves win rate.

## What to do

1. **Weeks 1 to 3, diagnose.** Someone outside sales (a product manager or an outside win/loss firm) reviews the evidence you already have for the seven lost deals: call recordings, RFPs, email threads and the CRM competitor field. They then interview 5 to 8 of the lost buyers and 3 to 5 recent mid-size wins. The review answers four questions:
   - Who won each deal?
   - Was automation a written requirement?
   - Which exact workflows were wanted?
   - What is the combined value of the seven deals?
2. **In parallel, price the fix.** Get quotes for an embedded-automation prototype of the top two or three workflows buyers named.
3. **Decision date at the end of week 3.** If at least 5 of the 7 buyers independently say the builder decided the deal, ship the named workflows on the embedded layer or natively. Aim for a first release in 4 to 8 weeks and full coverage in about a quarter. Track win rate on deals shown it.
4. **Scope the native build.** Move to a scoped native build only if win rate improves and buyers name workflows the embedded layer can't cover.
5. **Revisit buying only if all of these hold:**
   - Buyers name a native visual builder as a hard requirement.
   - The startup's stack is compatible.
   - Its key engineers commit to staying.
   - The price still leaves at least 18 months of runway.
6. **Stop and re-diagnose** if fewer than 5 of 7 buyers confirm automation. The real cause then lies elsewhere: price, demo quality, integrations or segment fit.

## Risks of this plan

Waiting three weeks costs little but isn't free. The competitor keeps selling to the same buyers, and you may lose more deals in that window. A narrow fix may be judged against the competitor's full builder, so you could spend a quarter and still lose side-by-side demos. Licences add a recurring cost and a vendor dependency, and white-labeled workflows can feel less native. Interviews with lost buyers are also biased by what people remember and are willing to say.

Cost of being wrong: the diagnosis, the interviews and the embedded prototype cost weeks and a licence you can cancel. A native build is a bounded cost but a sunk one: engineering time spent on the wrong thing can't be recovered. The one step that is hard to undo is the acquisition, which this plan postpones. If the counter-position below is right and speed was decisive, you lose about three weeks to a quarter. You then buy or build the full version with your cash reserve intact.

## Strongest counter-position

"Speed matters more than certainty. Your reps lost seven of ten mid-size deals to one gap, your competitor has a polished builder, and every month without parity loses more deals. Interviews and a half-measure only delay the decision. Buyers want a visual builder to compare with theirs, an embedded layer will look bolted on, and a full build slips anyway. Buy the startup now, take the team and the customers with it, and close the gap in the time it takes to sign."

This wins when four things hold:
- The buyers themselves confirm the loss reasons.
- The startup's stack and team are an unusually good fit.
- The price still leaves real runway.
- The lost deals are large enough that a quarter of delay costs more than the acquisition risk.

Buyer interviews and a diligence check of the startup's stack, team and price would show it.

## Confidence

- **Medium** that you shouldn't buy now. This rests on cash being scarce at 80 people, on integration being slow, and on the diagnosis being unconfirmed, because ten rep-logged deals is thin evidence either way.
- **Medium-low** on building natively rather than buying later. That depends on what the buyers say.
- **Material unknowns:**
  - The actual loss reasons.
  - How many months of runway the reserve represents.
  - The startup's price and stack.
  - Which workflows buyers named.
