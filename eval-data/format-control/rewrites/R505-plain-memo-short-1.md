# arm: plain-memo-short (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R505 | attempt: 1 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R505-plain-memo-short-rewrite-1.txt (sha256 7013d2707ffef369)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: a9340dba374675f9f | transcript sha256: 0cabf05198cae8fa3ccebbdbe9f7d8897c08c2faa935ba654e2d3fae322fa9bf
# minutes: 0.3 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/2560/3185/14101 | list-price USD: 0.09

## Recommendation
Take this seriously enough to raise with her doctor, not seriously enough to act on alone. The right-sized response is a routine medication review that would be good practice anyway. It is not "the study is scary, she needs to stop," and it is not "ignore it." Don't let her stop on her own. Ask her prescriber, at her next visit, to review whether she still needs the drug and at what dose, and have a B12 level checked at the same time. The dementia link is a hypothesis worth tracking, not a verdict, and you can act on it without needing to believe it is causal.

## Why
First, the finding keeps recurring. This is a small research area going back to around 2015, with relative-risk increases across different studies ranging roughly 20–45%. Your "30% after five-plus years" fits that pattern. It is possibly a large recent US claims-based cohort of several million patients, with risk concentrated in the longest-duration users, which tracks with your mother's decade of use. Whether it means the drug causes dementia is a separate question, and that is where this kind of study is structurally weak.

Big records-based studies (insurance claims, EHR data, not trials) are good at spotting patterns across millions of people cheaply. They are bad at telling you why the pattern exists, because nobody was randomized to take the drug. People who end up on it for ten years differ from people who don't, in ways that matter:

- Confounding by indication: decade-long PPI users tend to have more severe GERD and more comorbidities generally. Anything correlated with worse baseline health can also correlate with dementia risk. Researchers adjust for what they can measure, not for everything that is actually different between the groups.
- Reverse causation: dementia has a prodromal phase lasting years before diagnosis. Early, undiagnosed cognitive decline can change diet, self-care, and GI symptoms, so early dementia may help cause the prescription, not the other way around.
- Detection bias: someone refilling a prescription monthly is in the healthcare system constantly, so a cognitive complaint is more likely to get noticed and worked up. Someone on no medications with the same early decline may just go undiagnosed longer, and undercount in the "unexposed" group.
- Comparator choice: studies comparing PPI users to non-users tend to find bigger effects than studies comparing PPI users to people on an alternative reflux drug, which is a fairer comparison since both groups needed treatment for something. When researchers use the fairer comparison, the association often shrinks or disappears. That is a strong signal that a chunk of the original 30–45% was confounding by indication, not the drug itself.
- Relative vs. absolute risk: "30% more likely" is relative. Hypothetically, if baseline dementia risk over the study's follow-up window is 8%, a 30% relative bump takes it to about 10.4%. That is a real increase, but nowhere near as dramatic as "30%" sounds on its own.

The fuller picture on PPIs is mixed, not one-directional. The original German insurance-claims study (2016, JAMA Neurology) found the association. Since then, other groups, including a large Finnish nationwide study focused specifically on Alzheimer's, found no association once they used tighter designs. That kind of split across independent datasets is what you'd expect if part of the signal is bias rather than biology, not what you'd expect from a robust causal effect.

No major GI or geriatric society currently recommends stopping PPIs because of the dementia data specifically, since it is not considered consistent or strong enough for that. Most do recommend periodically checking whether a long-term patient still needs the drug, and at what dose, because of other, better-established risks: fracture, kidney disease, C. diff infection, B12/magnesium deficiency.

## What to do
1. Confirm what she is actually taking. "Common acid-reflux medication" usually means a proton pump inhibitor (PPI), such as omeprazole, esomeprazole, pantoprazole or lansoprazole, as opposed to an H2 blocker like famotidine, which is a different drug class with different (thinner) dementia data. If she is on an H2 blocker, this specific research may not even apply to her. This matters enough to check first.
2. Do not let her stop on her own.
3. At her next visit, ask her prescriber to review whether she still needs the drug and at what dose, with a B12 level checked while they're at it. B12 is worth ruling out for her regardless: long-term acid suppression can reduce B12 absorption, and B12 deficiency is an established, reversible cause of cognitive symptoms in older adults.
4. Let her doctor weigh her actual reflux history (erosive esophagitis, Barrett's, prior bleeding) against a taper.
5. For the next scary-study headline, use a fast checklist:
   - What is the comparator: non-users, or people on an alternative treatment?
   - Is the headline number relative or absolute risk?
   - Does it replicate across independent datasets and designs?
   - Is there a plausible mechanism, and is the evidence for it human or animal/cell?
   - Has any professional society changed its guidance because of it?

   When most of those point weak, it is a hypothesis worth tracking, not a verdict.

## Risks of this plan
Quitting cold is the main risk. Long-term PPI use causes rebound acid hypersecretion, so stopping abruptly can produce a worse flare than she started with. That is why a taper, if any, belongs with her doctor, who can weigh her actual reflux history.

The other caveat is that the study's number is relative, not absolute, and the amyloid/brain-mechanism angle sometimes cited alongside this is much weaker, mostly mouse and cell-culture work, not established in humans. Researchers also adjust only for what they can measure, so some confounding stays hidden.

## Strongest counter-position
The finding keeps recurring, which is worth noting, and a 30% relative increase is a real increase, not nothing. The B12 mechanism is worth taking seriously on its own merits, separate from the dementia headlines. So waving the study away would be a mistake. The source's answer is still that the evidence is mixed: independent datasets split, and the association often shrinks or disappears with the fairer comparison.

## Confidence
- Records-based studies cannot randomize, so they are weak at showing why a pattern exists: High.
- Confounding by indication, reverse causation and detection bias can distort such studies: High.
- Long-term PPI use causes rebound acid hypersecretion, so quitting cold can produce a worse flare: High.
- The B12 deficiency mechanism (reduced absorption, reversible cognitive symptoms) is established: High.
- No major GI or geriatric society currently recommends stopping PPIs because of the dementia data: High.
- "Common acid-reflux medication" usually means a PPI: Medium.
- Decade-long PPI users tend to have more severe GERD and more comorbidities: Medium.
- Studies against non-users tend to find bigger effects than studies against an alternative reflux drug: Medium.
- Most societies recommend periodic review of long-term use: Medium.
- Your study is possibly a large recent US claims-based cohort: Low.
- Part of the signal may be bias rather than biology, and a chunk of the original 30–45% was confounding by indication: stated as what the split would be expected to show, and as a signal; no hedge-free causal claim is made.
- Early dementia may help cause the prescription: Low.
- If she is on an H2 blocker, this research may not apply to her: Low.

Unknowns the source names: whether the drug causes dementia at all, which is a separate question from the association. Also unknown is which drug she takes, and her actual reflux history (erosive esophagitis, Barrett's, prior bleeding).
