# arm: plain-memo (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: R505 | attempt: 2 | run: 2026-11-08 (round 6, PREREG-6 rules)
# rewriter: fresh wise-men-flash:wise-member/sonnet = claude-sonnet-5-5 | tools used: none | prompt: prompts/R505-plain-memo-rewrite-2.txt (sha256 fc9b0e5ac3172aa0)
# session: 3237f3a5-15e9-425e-8e26-e9f420a55eb9 | agent: adf782e4579c980ef | transcript sha256: b16c42c84ac02e77a31dce247d146729264dc340b314ef10750c7eb70a4f933f
# minutes: 0.3 | subagent calls: 0 (transcripts matched: 0) | tokens in/out/cache-read/cache-write: 2/3771/3185/20661 | list-price USD: 0.14

## Recommendation

Take this seriously enough to raise with her doctor, not seriously enough to act on alone. That is the bottom line, and the later sections give the reasons and the steps behind it.

The right-sized response is neither "the study is scary, she needs to stop" nor "ignore it." It is a routine medication review that would be good practice anyway. The useful move is to ask her prescriber, at her next visit, to review whether she still needs the drug and at what dose, with a B12 level checked while they are at it. Her doctor can weigh her actual reflux history against a taper. She should not stop on her own.

Large records-based studies are good at spotting patterns but bad at telling you why a pattern exists, because nobody was randomized to take the drug. Treat the dementia finding as a hypothesis worth tracking, not a verdict. You can act on it through a medication review without needing to believe the dementia link is causal.

## Why

**Check the drug class first.** "Common acid-reflux medication" usually means a proton pump inhibitor (PPI), such as omeprazole, esomeprazole, pantoprazole or lansoprazole, as opposed to an H2 blocker like famotidine. An H2 blocker is a different drug class with different (thinner) dementia data. If she is on an H2 blocker, this specific research may not even apply to her. The source says this matters enough to check first.

**The finding keeps recurring.** On PPIs and dementia, this is not one study. It is a small research area going back to around 2015, with relative-risk increases across different studies ranging roughly from 20 to 45%. Your figure of 30% after five-plus years fits that pattern. It is possibly a large recent US claims-based cohort of several million patients, with risk concentrated in the longest-duration users, which tracks with your mother's decade of use. The finding keeps recurring, which is worth noting. Whether it means the drug causes dementia is a separate question, and that is where this kind of study is structurally weak.

**What records-based studies can and cannot do.** Big records-based studies, meaning insurance claims and EHR data rather than trials, are good at spotting patterns across millions of people cheaply. They are bad at telling you why the pattern exists, because nobody was randomized to take the drug. People who end up on it for ten years differ from people who don't, in ways that matter. The usual ways these studies go wrong are as follows.

- **Confounding by indication.** Decade-long PPI users tend to have more severe GERD and more comorbidities generally. Anything correlated with worse baseline health can also correlate with dementia risk. Researchers adjust for what they can measure, not for everything that is actually different between the groups.
- **Reverse causation.** Dementia has a prodromal phase lasting years before diagnosis. Early, undiagnosed cognitive decline can change diet, self-care, and GI symptoms. This means early dementia may help cause the prescription, not the other way around.
- **Detection bias.** Someone refilling a prescription monthly is in the healthcare system constantly, so a cognitive complaint is more likely to get noticed and worked up. Someone on no medications with the same early decline may just go undiagnosed longer, and undercount in the "unexposed" group.
- **Comparator choice.** Studies comparing PPI users to non-users tend to find bigger effects than studies comparing PPI users to people on an alternative reflux drug. The second comparison is fairer, since both groups needed treatment for something. When researchers use the fairer comparison, the association often shrinks or disappears. That is a strong signal that a chunk of the original 30 to 45% was confounding by indication, not the drug itself.
- **Relative versus absolute risk.** "30% more likely" is relative. Hypothetically, if baseline dementia risk over the study's follow-up window is 8%, a 30% relative bump takes it to about 10.4%. That is a real increase, but nowhere near as dramatic as "30%" sounds on its own.

**The fuller picture on PPIs is mixed, not one-directional.** The original German insurance-claims study (2016, JAMA Neurology) found the association. Since then, other groups, including a large Finnish nationwide study focused specifically on Alzheimer's, found no association once they used tighter designs. That kind of split, across independent datasets, is what you would expect if part of the signal is bias rather than biology. It is not what you would expect from a robust causal effect.

**One mechanism deserves attention on its own merits.** This mechanism is separate from the dementia headlines. Long-term acid suppression can reduce B12 absorption, and B12 deficiency is an established, reversible cause of cognitive symptoms in older adults. It is worth ruling out for her regardless. The amyloid and brain-mechanism angle sometimes cited alongside this is much weaker, mostly mouse and cell-culture work, and not established in humans.

**Professional guidance.** No major GI or geriatric society currently recommends stopping PPIs because of the dementia data specifically. It is not considered consistent or strong enough for that. Most societies do recommend periodically checking whether a long-term patient still needs the drug, and at what dose, because of other, better-established risks: fracture, kidney disease, C. diff infection, and B12 and magnesium deficiency. That gives you a productive way to act on this without needing to believe the dementia link is causal.

## What to do

1. **Confirm what she is actually taking.** Find out whether it is a PPI (omeprazole, esomeprazole, pantoprazole, lansoprazole) or an H2 blocker like famotidine. Do this first, because if it is an H2 blocker this specific research may not apply to her.

2. **Do not let her stop on her own.** Long-term PPI use causes rebound acid hypersecretion, so quitting cold can produce a worse flare than she started with.

3. **Ask her prescriber, at her next visit, to review whether she still needs the drug and at what dose.** Frame it as a routine medication review. It is good practice anyway, because of the better-established risks of long-term use: fracture, kidney disease, C. diff infection, and B12 and magnesium deficiency.

4. **Have a B12 level checked at the same visit.** Long-term acid suppression can reduce B12 absorption, and B12 deficiency is an established, reversible cause of cognitive symptoms in older adults. It is worth ruling out for her regardless.

5. **Let her doctor weigh her actual reflux history against a taper.** The history includes erosive esophagitis, Barrett's, and prior bleeding.

6. **Use a quick checklist on the next scary-study headline.**
   - What is the comparator: non-users, or people on an alternative treatment?
   - Is the headline number relative or absolute risk?
   - Does it replicate across independent datasets and designs?
   - Is there a plausible mechanism, and is the evidence for it human or animal and cell?
   - Has any professional society changed its guidance because of it?

   When most of these point weak, it is a hypothesis worth tracking, not a verdict.

## Risks of this plan

The main risk the source names is stopping the drug without guidance. Long-term PPI use causes rebound acid hypersecretion, so quitting cold can produce a worse flare than she started with. This is why she should not stop on her own.

A second caveat concerns the studies themselves. Researchers adjust for what they can measure, not for everything that is actually different between the groups.

A third caveat is that this research may not apply to her at all. If she is on an H2 blocker rather than a PPI, the dementia data is thinner and different.

A fourth caveat is the size of the number. "30% more likely" is relative, and the source's hypothetical (an 8% baseline rising to about 10.4%) is a real increase but nowhere near as dramatic as "30%" sounds on its own.

## Strongest counter-position

The strongest limit the source raises on its own answer is that the finding should not simply be waved away. The association keeps recurring, and the source calls that worth noting. It goes back to around 2015, with relative-risk increases across studies ranging roughly from 20 to 45%, and your 30% after five-plus years fits that pattern. The original German insurance-claims study in 2016 found it. Whether it means the drug causes dementia is a separate question, and that is where this kind of study is structurally weak.

The source also calls a 30% relative bump a real increase, even though it is not as dramatic as it sounds. And it treats the B12 mechanism as one worth taking seriously on its own merits, which is why the plan includes a B12 check regardless of the dementia headlines.

## Confidence

**High (stated without a hedge)**
- Large records-based studies are good at spotting patterns across millions of people cheaply and bad at telling you why, because nobody was randomized.
- Dementia has a prodromal phase lasting years before diagnosis.
- Decade-long PPI users tend to have more severe GERD and more comorbidities generally.
- Studies comparing PPI users to non-users tend to find bigger effects than studies using an alternative reflux drug as the comparator.
- When researchers use the fairer comparison, the association often shrinks or disappears.
- That shrinkage is a strong signal that a chunk of the original 30 to 45% was confounding by indication.
- A 30% relative increase is relative, and the hypothetical 8% baseline would rise to about 10.4%.
- Long-term acid suppression can reduce B12 absorption.
- B12 deficiency is an established, reversible cause of cognitive symptoms in older adults.
- Long-term PPI use causes rebound acid hypersecretion, so quitting cold can produce a worse flare than she started with.
- No major GI or geriatric society currently recommends stopping PPIs because of the dementia data specifically.
- Most societies do recommend periodically checking whether a long-term patient still needs the drug, and at what dose.
- The original German insurance-claims study (2016, JAMA Neurology) found the association.
- Other groups, including a large Finnish nationwide study, found no association once they used tighter designs.
- The amyloid and brain-mechanism angle is much weaker, mostly mouse and cell-culture work, and not established in humans.
- Researchers adjust for what they can measure, not for everything that is different between groups.
- Comparing PPI users to people on an alternative reflux drug is a fairer comparison than comparing them to non-users.
- Her doctor can weigh her actual reflux history against a taper.

**Medium (stated with "likely", "probably", "usually", "typically" or "suggests")**
- "Common acid-reflux medication" usually means a PPI.

**Low (stated with "may", "might", "could", "possibly" or "unclear")**
- Your figure is possibly a large recent US claims-based cohort of several million patients.
- If she is on an H2 blocker, this specific research may not apply to her.
- Early dementia may help cause the prescription, not the other way around.
- Someone on no medications with the same early decline may just go undiagnosed longer, and undercount in the "unexposed" group.

**Unknowns the source names**
- Whether the association means the drug causes dementia, which the source calls a separate question.
- Whether she is on a PPI or an H2 blocker, which the source says to confirm first.
- Which study you are citing, since the source says only that it is possibly a large recent US claims-based cohort.
