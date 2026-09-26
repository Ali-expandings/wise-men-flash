# arm: grilling (mattpocock/skills c55ee46073ed) | question: R505 | orchestrator: general-purpose/sonnet | run: 2026-09-25 (round 5, PREREG-5 rules)
# minutes: 11.6 | subagent calls: 1 (transcripts matched: 1) | tokens in/out/cache-read/cache-write: 26/61993/1259278/262468 | list-price USD: 2.29
# note: the skill tells its orchestrator to dispatch a sub-agent to find facts; its one research sub-agent ran 20 web searches and 2 page fetches (Firecrawl) on the published studies before the answer was written; the orchestrator itself stayed offline

❓ **Q1** - **What's the actual goal here — calibration, a mom conversation, or a doctor conversation?**: Do you want (a) your own calibrated read on how much to trust the study, (b) a way to raise it with your mother, (c) a way to raise it with her doctor/pharmacist, or (d) all three, in some order?

➡️ All three, in this order: calibrate yourself → route the actionable part through her doctor/pharmacist → only then mention it to her, briefly and calmly.

✅ **Assumed:** Your own framing — "don't want to scare her" rules out leading with a dramatic conversation with mom; "don't want to wave away a real risk" rules out doing nothing. That leaves "get informed, then work through the doctor, then mention it calmly" as the only option consistent with both constraints.

---

❓ **Q2** - **Do you actually know why she's on this medication long-term?**: Diagnosed GERD, Barrett's esophagus, history of an ulcer or GI bleed — or did it start for reflux and just never get revisited? This changes the entire risk/benefit calculus, including whether stopping is even medically safe.

➡️ Find this out before deciding anything else about the drug itself.

✅ **Assumed:** Not specified, so treat as unknown — this becomes step one of the plan (find out), not something to guess at.

---

❓ **Q3** - **Has anyone reviewed whether she still needs it, independent of the dementia question?**: Long-term daily use for over a decade — has a doctor revisited dose or necessity recently?

➡️ Probably not.

✅ **Assumed:** Long-term PPI use is notorious for being started once and never reassessed. Worth raising on ordinary deprescribing grounds regardless of what you conclude about the study.

---

❓ **Q4** - **Any current memory/cognitive symptoms, or is this purely precautionary?**: Is there something specific happening with her, or is this entirely driven by reading the headline?

➡️ Treat as precautionary only.

✅ **Assumed:** Nothing mentioned — this is a "worth a calm conversation at the next routine visit" situation, not an urgent one.

---

❓ **Q5** - **Do you want the general skill, the specific verdict, or both?**: "How to read this kind of study" is reusable beyond this one drug; the PPI-specific verdict is what you need right now.

➡️ Both — you asked for both explicitly.

✅ **Assumed:** General framework first, then applied to this case.

---

**Round 2** (unblocked by Round 1's assumed answers)

❓ **Q6** - **Since her specific indication is unknown, what should the doctor/pharmacist ask actually look like?**: A general "get it reviewed" nudge, or a concrete list of questions to bring in?

➡️ Concrete short list — costs you nothing extra and is actually usable at the appointment.

✅ **Assumed:** Include the list.

---

❓ **Q7** - **Do you want example wording for your mother, or just the reasoning to phrase yourself?**: Given Q1's assumption (calm, doctor-anchored, not alarming), how literal should the help be?

➡️ A short adaptable example, not a rigid script.

✅ **Assumed:** Include one short example she'd hear as "let's get this checked" rather than "this might be hurting you."

---

❓ **Q8** - **Should the general framework be a reusable checklist or a one-off explanation?**: You'll hit more headlines like this.

➡️ Compact, reusable checklist.

✅ **Assumed:** Include it as a short standalone list.

---

Frontier is now empty — nothing left that depends on an unanswered question.

## Final recommendation

**Bottom line:** Treat this as a reason to get the prescription reviewed at her next routine visit — not a reason for alarm, and not a reason to dismiss it either. The specific dementia claim is currently better explained by bias in the study design than by a real drug effect, but long-term PPI use has other, firmly established reasons to be reassessed anyway.

**What's usually wrong with "millions of health records" studies like this:**
- **It's an association, not a trial.** Nobody randomized who took the drug, so nothing here proves the drug caused anything.
- **Confounding by indication.** People take acid-reflux medication *because* of something — that underlying reason, not the pill, may drive the outcome.
- **Reverse causation.** Early, undiagnosed disease can change behavior or prescribing years before a diagnosis shows up, making the "cause" look like it came before the "effect" when it didn't.
- **Detection bias.** People who see doctors more for one thing get diagnosed with other things more too — just from more contact with the system, not more actual disease.
- **Unmeasured confounders.** Claims/records databases usually can't fully capture smoking, diet, education, frailty — all of which correlate with both chronic drug use and dementia risk.
- **Multiple comparisons.** Huge databases test many drug-outcome pairs; some "significant" hits are noise dressed up as a finding.
- **Relative vs. absolute risk.** "30% more likely" is a relative number. Without the baseline rate, you can't tell if that's a large or trivial real-world change.
- **Sample-size inflation in reporting.** This exact case is a textbook example, see below.
- **What actually earns credibility:** replication across independent datasets, a dose-response pattern, a plausible mechanism, and — the strongest single check — a "negative control" comparison that survives. If it doesn't survive, that's usually the tell.

**What's actually known about PPIs and dementia specifically:**
- The "over five years, ~30% more likely" framing lines up closely with **Northuis et al. 2023 (Neurology, ARIC cohort)**: >4.4 cumulative years of PPI use, HR 1.33 (95% CI 1.0–1.8). The older, more-cited **Gomm et al. 2016 (JAMA Neurology)**, German insurance-claims data, found HR 1.44 (95% CI 1.36–1.52) — but on an analyzed cohort of **73,679 people**, not "several million." The "millions" figure is almost certainly the insurer's total covered population getting conflated with the actual study sample — a concrete instance of the sample-size-inflation problem above.
- The decisive detail: Northuis's own pre-specified negative-control check — comparing PPI users against H2-blocker users (a similar drug, prescribed for the same reasons, without the proposed PPI mechanism) — **collapsed to null: HR 1.02 (95% CI 0.61–1.70)**. The authors' materials needed a correction conceding the main result may reflect unmeasured confounding rather than a drug effect.
- **Mehta et al. 2023 (Gastroenterology, ASPREE trial post-hoc, N=18,934)** found no association for either PPIs (HR 0.88) or H2 blockers — prompting the American Gastroenterological Association to publicly state PPIs do not cause dementia.
- **Ahn et al. 2023** meta-analysis with bias-adjustment: a modest pooled signal (~RR 1.15) that the authors themselves attribute to plausible residual confounding.
- No randomized trial exists. Mendelian randomization studies are inconsistent. Neither the FDA nor EMA has added a dementia warning to PPI labels.
- Proposed biological mechanisms (effects on amyloid clearance, B12-related cognitive effects) are preclinical/cell-model only, not shown in people, and undercut by H2 blockers causing similar B12 loss without a similar dementia signal.

**What not to do:** don't have her stop it abruptly. Rebound acid hypersecretion is real and well-documented — reflux gets worse for days after stopping. Some conditions (Barrett's esophagus, eosinophilic esophagitis, prior GI bleed, idiopathic pulmonary fibrosis) specifically should *not* have the drug stepped down, per gastroenterology guidance, regardless of the dementia question.

**Concrete next step — questions for her doctor or pharmacist, next routine visit:**
1. Why was this started, and is that reason still present?
2. Is the lowest effective dose, or on-demand dosing instead of daily, appropriate now?
3. Can we check B12 and magnesium? (This is the actually well-established risk of long-term use — not dementia — and it's a cheap blood test with an easy fix.)
4. Is there anything in her history (Barrett's, prior bleed, etc.) that means this drug should stay as-is?

**Talking to her — example framing, adapt freely:** *"I read the studies linking this to dementia are actually pretty shaky — one of the main ones fell apart under closer testing — but it seemed like a good excuse to get your prescription double-checked anyway, since nobody's looked at it in a while. Can we ask about it next time you're in?"*

**Reusable checklist for the next scary health headline:** study design (trial or just records?) → sample size in the actual study, not the database → relative vs. absolute risk → does a negative-control or replication check survive → is there a plausible mechanism shown in humans, not just cells → what do regulators/guidelines actually say.
