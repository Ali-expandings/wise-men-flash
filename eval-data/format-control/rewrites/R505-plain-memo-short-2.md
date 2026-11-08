# arm: plain-memo-short (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R505 | attempt: 2 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R505-plain-memo-short-rewrite-2.txt (sha256 13b3ad45ddca4840)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: aeb3aac9e9d37ee0b | transcript sha256: 47b6502e448906a09dcc29de0284de42ad94a64be163928ad5883d93a2af72fd
# minutes: 0.4 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/4102/3185/17164 | list-price USD: 0.13

## Recommendation
Take this seriously enough to raise with her doctor, not seriously enough to act on alone. The right-sized response is a routine medication review that would be good practice anyway. It is not "the study is scary, she needs to stop," and it is not "ignore it." Don't let her stop on her own.

## Why
This isn't one study. It is a small research area on PPIs and dementia going back to around 2015, with relative-risk increases across different studies ranging roughly 20–45%. Your "30% after five-plus years" fits that pattern, possibly a large recent US claims-based cohort (several million patients, risk concentrated in the longest-duration users), which tracks with your mother's decade of use. The finding keeps recurring, which is worth noting. Whether it means the drug causes dementia is a separate question, and that's where this kind of study is structurally weak.

Big records-based studies (insurance claims, EHR data, not trials) are good at spotting patterns across millions of people cheaply. They're bad at telling you why the pattern exists, because nobody was randomized to take the drug. People who end up on it for ten years differ from people who don't, in ways that matter:

- Confounding by indication: decade-long PPI users tend to have more severe GERD and more comorbidities generally, and anything correlated with worse baseline health can also correlate with dementia risk. Researchers adjust for what they can measure, not for everything that's actually different between the groups.
- Reverse causation: dementia has a prodromal phase lasting years before diagnosis. Early, undiagnosed cognitive decline can change diet, self-care, and GI symptoms, so early dementia may help cause the prescription, not the other way around.
- Detection bias: someone refilling a prescription monthly is in the healthcare system constantly, so a cognitive complaint is more likely to get noticed and worked up. Someone on no medications with the same early decline may just go undiagnosed longer, and undercount in the "unexposed" group.
- Comparator choice: studies comparing PPI users to non-users tend to find bigger effects than studies comparing them to people on an alternative reflux drug. That is a fairer comparison, since both groups needed treatment for something. When researchers use the fairer comparison, the association often shrinks or disappears. That is a strong signal that a chunk of the original 30–45% was confounding by indication, not the drug itself.
- Relative vs. absolute risk: "30% more likely" is relative. Hypothetically, if baseline dementia risk over the study's follow-up window is 8%, a 30% relative bump takes it to about 10.4%. That is a real increase, but nowhere near as dramatic as "30%" sounds on its own.

The fuller picture on PPIs is mixed, not one-directional. The original German insurance-claims study (2016, JAMA Neurology) found the association. Since then, other groups, including a large Finnish nationwide study focused specifically on Alzheimer's, found no association once they used tighter designs. That kind of split across independent datasets is what you'd expect if part of the signal is bias rather than biology, not what you'd expect from a robust causal effect.

No major GI or geriatric society currently recommends stopping PPIs because of the dementia data specifically. It's not considered consistent or strong enough for that. Most do recommend periodically checking whether a long-term patient still needs the drug, and at what dose, because of other, better-established risks: fracture, kidney disease, C. diff infection, B12/magnesium deficiency. That gives you a productive way to act on this without needing to believe the dementia link is causal.

## What to do
1. First, confirm what she's actually taking. "Common acid-reflux medication" usually means a proton pump inhibitor (PPI), such as omeprazole, esomeprazole, pantoprazole or lansoprazole. An H2 blocker like famotidine is a different drug class with different (thinner) dementia data. If she's on an H2 blocker, this specific research may not even apply to her. This matters enough to check first.
2. Don't let her stop on her own.
3. At her next visit, ask her prescriber to review whether she still needs the drug and at what dose, with a B12 level checked while they're at it. There is a mechanism worth taking seriously on its own merits, separate from the dementia headlines: long-term acid suppression can reduce B12 absorption, and B12 deficiency is an established, reversible cause of cognitive symptoms in older adults. It's worth ruling out for her regardless.
4. Her doctor can weigh her actual reflux history (erosive esophagitis, Barrett's, prior bleeding) against a taper.
5. For the next scary-study headline, use a fast checklist:
   - What's the comparator: non-users, or people on an alternative treatment?
   - Is the headline number relative or absolute risk?
   - Does it replicate across independent datasets and designs?
   - Is there a plausible mechanism, and is the evidence for it human or animal/cell?
   - Has any professional society changed its guidance because of it?

   When most of those point weak, it's a hypothesis worth tracking, not a verdict.

## Risks of this plan
Long-term PPI use causes rebound acid hypersecretion, so quitting cold can produce a worse flare than she started with. The amyloid/brain-mechanism angle sometimes cited alongside this is much weaker, mostly mouse and cell-culture work, not established in humans.

## Strongest counter-position
The finding keeps recurring, which is worth noting, and a 30% relative bump is a real increase. Whether the drug causes dementia is a separate question that this kind of study can't settle.

## Confidence
- Records-based studies are bad at telling you why a pattern exists: High.
- Long-term PPI use causes rebound acid hypersecretion: High.
- B12 deficiency is an established, reversible cause of cognitive symptoms in older adults: High.
- No major society currently recommends stopping PPIs because of the dementia data: High.
- Most societies recommend periodically checking whether a long-term patient still needs the drug: High.
- The association often shrinks or disappears with the fairer comparison: High.
- The amyloid/brain-mechanism angle is much weaker: High.
- "Common acid-reflux medication" usually means a PPI: Medium.
- Decade-long PPI users tend to have more severe GERD and more comorbidities: Medium.
- Comparisons with non-users tend to find bigger effects: Medium.
- Your study is possibly a large recent US claims-based cohort: Low.
- Early dementia may help cause the prescription: Low.
- An H2 blocker user may not be covered by this research: Low.

Unknowns the source names: whether the drug causes dementia, which is a separate question from the association; which drug she actually takes; and her actual reflux history.
