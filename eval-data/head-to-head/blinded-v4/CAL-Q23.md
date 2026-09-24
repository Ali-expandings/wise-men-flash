You are grading four different responses to the same question. Four different methods produced these responses. Your job is to assess answer quality only. Do not try to guess which method produced which response — that will bias your scoring. Ignore length: a longer answer is not a better answer.

The question:
"""
How seriously should I take a meta-analysis that finds a significant effect when half the underlying studies are unpublished and were located via a "gray literature search"? What are the actual failure modes here?

"""

Response A:
"""
## Council

No `run_agents` launcher in this harness, so each member ran as a direct, foreground, read-only subagent (no filesystem/web access, no file edits) — reasoning from domain knowledge only, independently, with no visibility into each other's answers. Cross-vendor model diversity (GPT/Codex, open-source) wasn't available in this harness — only Claude models were — so per the skill's own fallback rule, diversity came from three distinct model tiers paired with three non-redundant angles instead:

- **Opus** — methodological/statistical rigor reviewer (pooling models, heterogeneity, whether bias-detection tools still work here)
- **Sonnet** — practitioner/evidence-appraisal reviewer (checkable red/green flags, verification cost, context-dependent scrutiny)
- **Haiku** (weakest available model, used per the skill's "strongest remaining model" fallback since no third frontier or open-source model existed — noted as a real capability gap, not just a formality) — contrarian reviewer (steelman gray-lit inclusion, then find what survives the steelman)

## Recommendation

Don't discount it just because half the studies are unpublished — a deliberate gray-literature search is standard, bias-*reducing* practice (it's literally what Cochrane/PRISMA recommend to counteract the file-drawer problem), so the 50% figure alone isn't a red flag. But don't take the topline "significant" at face value either: treat it as provisional until two specific checks are done, which together do most of the work of turning "significant" into either "solid" or "fragile."

## Why

- All three council members converge on the same starting point: excluding unpublished studies is not the methodologically safe default, it's the biased one. Published-only literatures skew toward significant/positive results because that's what clears peer review; a gray-lit search is the field's standard corrective, not a shortcut.
- Convergent check #1, raised independently by all three: does the effect survive a **published-only or low-risk-of-bias-restricted sensitivity analysis**? If the paper doesn't report one, or reports one where the effect shrinks or loses significance, that's the single strongest sign the "significant" result is being carried by the harder-to-verify half of the evidence.
- Convergent check #2: do **published and unpublished studies show similar effect sizes**? Agreement is stronger evidence than either subset alone (it isn't just "exciting enough to clear review"); systematic divergence in either direction means the pooled point estimate is unstable and should be read as a range, not a fact.
- The statistical-rigor review adds a mechanical wrinkle worth knowing: random-effects pooling (the default model) gives relatively more weight to small studies, and gray lit skews small (theses, pilots, conference work) — so if any small-study effect is present, the "more careful" random-effects model can amplify it rather than guard against it. That cuts against the common intuition that random-effects is automatically the conservative choice.
- Source type matters more than the published/unpublished label itself: trial-registry or regulatory gray lit is often higher-quality than a journal article; industry-, advocacy-, or agency-funded gray lit can reintroduce the exact outcome-motivated selection that gray-lit searching was supposed to cure — "unpublished" is not a synonym for "disinterested."

## Tradeoffs and risks

Concrete failure modes, grouped:

- **Statistical mechanics that quietly inflate the estimate.** Standard heterogeneity estimators (e.g., DerSimonian-Laird) tend to understate between-study variance under real heterogeneity, giving a falsely tight/significant confidence interval unless a more robust adjustment (Hartung-Knapp-type) or a prediction interval is reported. Trim-and-fill — a tool often cited as reassurance — can adjust the pooled estimate in the *wrong* direction if the gray-lit skew is toward small, null-ish studies. A "fail-safe N" cited as a bias defense here is close to self-contradictory: it asks how many hidden null studies would overturn the result, inside a review whose entire premise is that it went and found them.
- **Retrieval isn't neutral.** "Gray literature search" spans everything from exhaustive trial-registry extraction to an afternoon on Google Scholar. Without a documented protocol (named sources, dates, search terms, a PRISMA-style flow diagram, ideally a dated pre-registration), you can't tell which end you're on — and the retrieval process itself is a fresh, non-random filter (who responds to author-contact requests, which institutions/languages get covered).
- **Duplication.** A thesis, a derived journal article, and a conference abstract from the same underlying dataset are much easier to double-count in gray lit than in an indexed published database — this artificially narrows the confidence interval and inflates the apparent evidence count.
- **Quality control gaps.** Risk-of-bias tools (RoB 2, ROBINS-I, GRADE) often can't be fully scored from thin gray-lit writeups. Missing information tends to get coded "unclear" and then quietly treated as neutral rather than flagged as genuinely unassessable — which specifically hides bias in the studies hardest to check.
- **Buried caveats.** A line like "effect was attenuated/non-significant when restricted to published studies" can sit in a supplement while the abstract headlines the full pooled number — the most decisive information often isn't in the part most readers actually read.

## Final call

Run this in order against the actual paper:

1. Check the methods section for a documented gray-lit protocol — named databases/registries, dates, search terms, a flow diagram, ideally pre-registration. A one-line mention of "gray literature was also searched" with no detail is a yellow flag.
2. Look for a published-only or low-risk-of-bias-only sensitivity analysis and whether the effect survives it. Highest-value check, usually minutes if it's reported at all.
3. Check whether the forest plot or results table breaks out effect size by publication status. Similar → reassuring. Divergent → treat the pooled estimate as a range, not a fact.
4. Identify what the "unpublished" studies actually are — trial-registry/regulatory data, dissertations, industry/advocacy reports, conference abstracts. That distinction predicts trustworthiness far better than the published/unpublished label does.
5. If a real decision (medical, financial, policy) rides on this and none of the above is resolvable from the paper, don't treat one meta-analysis as sufficient — look for an independent corroborating review before acting.

Confidence is high on checks 2 and 3 as the two highest-yield tests; lower on any single numeric verdict, since no field or specific paper was given — clinical/regulatory gray lit and advocacy-group gray lit carry very different risk profiles, and that distinction moves the read more than the 50% figure does.
"""

Response B:
"""
**Bottom line:** half-unpublished, found via gray-lit search, is not itself a red flag. Cochrane and PRISMA both mandate searching gray literature — it's the standard countermeasure to the file-drawer problem, not a shortcut around it. A meta-analysis that skipped gray lit entirely should worry you more than this one. Judge it on execution, not the ratio.

Actual failure modes to check for:

**Search wasn't really systematic.** "Gray literature search" covers a huge range — from OpenGrey/ProQuest Dissertations/trial registries with documented search strings and dual independent screening, down to Googling around and emailing colleagues. Ad hoc search just swaps one selection bias (what journals accepted) for another (what the analysts happened to stumble on — their network, language, digitization luck). Check the methods section for named databases, search strings, date range, independent screeners.

**No peer review, more undetected errors.** Unpublished work skipped the one filter that catches coding mistakes, selective outcome reporting, and shaky stats. Check whether they ran formal risk-of-bias scoring (RoB2, Newcastle-Ottawa) and whether the unpublished studies scored worse.

**Incomplete reporting forces imputation.** Missing SDs, vague randomization, thin methods — common in theses and reports — get patched with assumptions. Each patch is a hidden researcher degree of freedom you can't see in the forest plot.

**Direction usually cuts the other way.** Methods literature on this (McAuley et al. 2000 is the classic) generally finds unpublished studies show smaller effects than published ones, not larger. A real gray-lit search usually pulls the pooled estimate toward null. So an effect that stays significant after honestly folding in the unpublished half is evidence for it, not against — conditional on the search actually being systematic.

**Unless the gray lit was itself selectively released.** Industry white papers, advocacy-org reports, think-tank output: "unpublished" but not randomly so. Favorable ones get released; unfavorable ones sit in a corporate drawer instead of a journal one. Same file-drawer dynamic, one layer up, minus peer review. Check authorship/funding of the gray-lit half for conflict-of-interest patterns.

**Small-study effects confound the bias story.** Gray lit skews small — pilot data, single-site theses. Funnel-plot asymmetry from that can reflect genuine small-study effects (heterogeneity, real precision-effect correlation), not publication bias per se. Don't auto-read an asymmetric funnel as "biased."

**A significant pooled effect can hide heterogeneity.** Check I²/tau², and especially the prediction interval, not just the CI on the mean. High heterogeneity plus a prediction interval crossing zero means "significant on average" is fully compatible with a lot of individual studies showing nothing.

What actually tells you whether to trust it — look for:
- Named gray-lit sources, search strings, screening process (systematic vs. ad hoc)
- Risk-of-bias assessment, broken out by published/unpublished status
- Sensitivity analysis: published-only subset vs. full pool — same conclusion either way?
- Heterogeneity stats plus prediction interval, not just the pooled p-value
- Leave-one-out / influence diagnostics
- Funnel plot plus Egger's test or PET-PEESE even after gray-lit inclusion — residual bias can survive it
- Whether the gray-lit search was pre-registered (PROSPERO protocol) or added after the published-only result looked weak — the latter opens a new p-hacking surface at the meta-analysis level itself

The published/unpublished ratio alone tells you almost nothing. What tells you something is whether the search was reproducible, whether quality was actually assessed rather than assumed, and whether the effect holds up under subgroup and sensitivity analysis. A rigorous 50/50 split beats a lazy journals-only search that never looked for the file drawer in the first place.
"""

Response C:
"""
## Recommendation

Don't calibrate trust by the 50% figure itself — on its own, a large gray-literature share is not evidence against a meta-analysis, and in most fields it points the opposite direction from the instinct to discount it. Treat the ratio as a prompt to run specific checks, not as a verdict: whether the effect survives on the published studies alone, where the unpublished half actually came from, and whether the analysis was locked in before or after the results were visible. The verdict falls out of those checks; nothing meaningful can be concluded from the ratio alone.

## Why

Publication bias operates mainly as a filter on what gets into peer-reviewed journals: null and negative results are disproportionately left unpublished, which mechanically inflates a published-only pooled estimate relative to the true effect. A gray-literature search exists specifically to recover some of what that filter removed. The methodology literature on this generally reports that meta-analyses restricted to published studies produce larger, more favorable effects than ones that also include gray literature (unverified — the specific studies behind this pattern were not confirmed here, and whether it holds in the field behind this particular meta-analysis is exactly what needs checking). Running a gray-literature search is also expensive and time-consuming, and it exposes the analysis to exactly the kind of scrutiny you're applying now — which is itself a mild, independent reason a gray-heavy meta-analysis is not automatically the more suspect one.

That correction is only as good as its assumptions, though, and two of them matter more than the published/unpublished ratio itself. First, "unpublished" is not one thing: trial registries and mandated-reporting sources are close to unbiased recoveries of the missing data, while solicited data, dissertations, conference abstracts, and advocacy or sponsor reports each carry their own, different selection pressure — an author sitting on a null result has little reason to dig it out when asked, while an author with an unpublished positive result often does, which can reintroduce a pro-effect tilt into exactly the sample meant to correct for one. Second, the unpublished universe has no enumerable sampling frame — there is no denominator for "how much of the file drawer did this search actually find" — so a gray-literature search can be said to reduce publication bias by an unknown amount, never to correct it outright; any read of the paper that treats the 50% figure as having settled the question has overstated what the design can support.

The single most direct test that resolves most of the uncertainty is whether the effect holds in the published-only subset alone. If it does — same direction, similar magnitude — the gray-literature half is doing what it's supposed to do: narrowing the estimate, not manufacturing it, and the result deserves real trust. If the published-only subset is null or reversed and significance only appears once the unpublished half is added, that is backwards from the normal direction of a publication-bias correction and is the single strongest reason for suspicion. This diagnostic — not the ratio, not a general aversion to unpublished data — is what should actually drive your confidence.

## What to do

This is an evaluation question, not an action with a deadline, so the useful output is a short triage, in priority order:

1. Check the scale and the paper trail before anything else: how many studies total (k), and was the review pre-registered (e.g., PROSPERO) with a primary outcome and analysis plan that matches what's actually reported? "Half unpublished" of 8 studies is a much thinner evidence base than of 80, and retrospective registration or a switched primary outcome means the analytic choices were made after the results were already visible — a fast, often-decisive check. (~15 minutes)
2. Find the published-only subgroup comparison. Most competent meta-analyses in this situation report one — check the forest plot or supplementary tables for a pooled estimate restricted to peer-reviewed studies, and compare it in direction and magnitude to the full-sample estimate. (15–30 minutes if supplementary data exists.) Of everything on this list, this single check carries the most diagnostic weight.
3. Check where the unpublished half actually came from: a registry or mandated-reporting database (low concern) versus author-solicited data, dissertations/theses, conference abstracts, or advocacy/sponsor reports (higher concern) — and whether any of it originated from the review team's own lab or network rather than independent sources.
4. Check whether the gray-only subset shows a larger effect than the published-only subset. This is the one pattern that inverts the whole argument: unpublished studies outperforming published ones is the signature of a solicited, non-representative gray sample rather than a genuine file-drawer correction.
5. If you want a real audit rather than a sanity check: pull the per-study data table (effect size, N, variance, source, and how each gray study was obtained) and re-run the pooled estimate with a random-effects model reporting a 95% prediction interval alongside the confidence interval, plus a leave-one-lab-out sensitivity analysis (not just leave-one-study-out) to catch gray studies that cluster by author network rather than replicate independently, and a check for the same sample appearing twice under different labels (conference abstract and later full paper, for instance). If the authors won't supply the per-study table on request, treat the finding as an unverified hypothesis rather than a result — that refusal is itself the answer. Budget roughly a day for this level; each individual check above is far cheaper.

## Risks of this plan

These are the actual failure modes behind a meta-analysis like this one, independent of whether you run the checks above:

- No enumerable sampling frame for the unpublished half: there's no way to compute what fraction of the true file drawer a gray search actually found, so any bias-correction claim is bounded, not proven, no matter how thorough the search looks.
- Solicitation asymmetry: unpublished data obtained by contacting authors is systematically more likely to come from people with a positive result to share than a null one to bury, which can quietly reintroduce the exact bias the gray search was meant to remove.
- Double counting: the same underlying sample can enter the pool more than once under different labels (a conference abstract, a thesis, and the eventual paper), which shrinks the pooled standard error and can manufacture significance directly. This is one of the least-checked failure modes in gray-heavy syntheses.
- Non-independence / clustering: gray studies are often found through the review team's own professional network rather than a systematic database, so they can be correlated with each other (and with the reviewers' own prior beliefs) rather than acting as independent evidence.
- Unappraisable quality treated as neutral: unpublished sources frequently can't be risk-of-bias-rated at all (missing methods detail), and standard weighting schemes tend to treat "can't assess" as equivalent to "acceptable" rather than as its own source of uncertainty.
- Small-study statistical artifacts: with a modest number of studies and real heterogeneity, standard confidence intervals can under-cover, and a result reported as significant under a less conservative variance estimator can lose significance under more conservative ones (Hartung-Knapp-type adjustments) — a real threat to the headline number independent of the gray-literature question entirely.
- Retrospective registration or outcome-switching: if the analysis plan was locked in (or never registered) after results were already visible, then the published-only comparison and every other check above can be gamed by choosing after the fact which outcome or subgroup to report.
- Field-dependent reversal: this entire argument assumes a field where the publication filter favors positive results and gray sources are low-incentive (registries, theses). In fields where gray literature is itself produced by organizations with an incentive to report success (advocacy groups, program evaluators who need to justify continued funding, industry-adjacent reports), the direction can flip — the unpublished half can be more biased toward a positive result than the published literature, not less.
- Background base rate: independent of the gray-literature question entirely, meta-analytic point estimates in general tend to run larger than the corresponding effect found in large, direct, pre-registered replications (unverified — the specific studies behind this pattern were not confirmed here). This is a reason for calibrated caution on any "significant" meta-analytic finding, gray literature aside.

If you act on the finding without running the published-only check: the check itself is cheap (well under an hour in the common case) and can be run at any time before or after acting — but committing to a real decision on the strength of the topline number alone, when the published-only subset turns out to be null, means acting on a result manufactured by exactly the failure mode described above.

## Strongest counter-position

The case that the correct default is suspended judgment, not elevated trust: the gray-literature universe has no enumerable sampling frame, which means a search "reduces publication bias by an unknown amount, never corrects it outright" — and the practical consequence is that most readers encountering a meta-analysis will never get the per-study table needed to actually check any of this. On this view, "if it is not in the supplement and the authors will not send it, stop; the analysis is unauditable and the conclusion is a hypothesis" should be the default posture toward any meta-analysis leaning heavily on gray literature, not a fallback for the unlucky case where verification fails. This position wins whenever the published-only subgroup result, the per-study provenance breakdown, or the underlying data table isn't reported and isn't supplied on request — which is the common case for a reader who isn't a systematic-review team auditing its own work. What would show it wrong: the paper reporting the published-only subgroup comparison and provenance breakdown up front, making the "unauditable" objection moot.

## Confidence

Medium on the core mechanism — that publication bias inflates published-only estimates and that a gray-literature search is a designed correction for this — because it's standard methodological reasoning, but whether it holds in the specific field behind this meta-analysis is unverified, and that gap matters more than anything else here. This recommendation leans on one unverified premise: that this field's publication filter suppresses null or negative results, and that its gray sources are low-incentive channels (registries, mandated-reporting databases, theses) rather than high-incentive ones (advocacy groups, solicited positive results, sponsors with a stake in the outcome). That premise is the single most important thing to check before trusting this recommendation strongly — it inverts in fields where gray literature is itself produced by organizations incentivized to report success, such as program evaluation or complementary-medicine research.

Low on any specific numeric claim about how much meta-analytic estimates typically overstate direct-replication effects — the qualitative direction (meta-analyses tend to run larger than replications) is plausible but was not verified here, only the general pattern was asserted.

High that the published-only-subgroup comparison is the correct single diagnostic to run first, regardless of field: it directly answers the one question that matters (did the unpublished half change the conclusion), it needs no new data collection beyond what a competent meta-analysis should already report, and it's decisive in both directions.

Material unknowns, in order of how much they'd change the answer: (1) whether this field's publication filter and gray-literature incentive structure run in the usual direction or the advocacy/fundraising-driven direction; (2) whether the paper reports a published-only subgroup comparison at all; (3) the actual provenance of the gray half (registry/mandated-reporting vs. solicited/advocacy); (4) whether the review was pre-registered and whether the reported outcome matches it; (5) whether any included studies double-count the same underlying sample.
"""

Response D:
"""
## Council Verdict: Trusting a Gray-Literature-Heavy Meta-Analysis

### Where the Council Agrees
Four of five advisors — the Contrarian, the First Principles Thinker, the Outsider, and the Executor — independently arrived at the same concrete test without seeing each other's work: split the pooled estimate by publication status and compare the peer-reviewed-only subset against the unpublished-only subset. Four independent arrivals at the same check is the strongest signal from this exercise.

Three of those four also converge on the same mechanism: "unpublished data obtained by contacting authors directly" is not a neutral fix for publication bias — it's a new selection filter. Whoever is reachable, still has the file, and is willing to send it is not a random draw from everyone who ran the study, and willingness-to-share plausibly correlates with not being embarrassed by the result. The Contrarian frames it as trading journal-editor gatekeeping for author-goodwill gatekeeping with no record of who declined; the Outsider calls it a favor, not a search; the Executor calls it a network sample, not a systematic one. Same diagnosis, three vocabularies, zero coordination.

The peer-review layer converged even harder: all five reviewers independently flagged the same advisor (the Expansionist) as weakest, and four of five named the same advisor (the Contrarian) as strongest.

### Where the Council Clashes
The fault line: does loading a meta-analysis with unpublished studies make a significant result *harder* to fake, because unpublished work trends toward null and drags against significance (the Expansionist) — or does the specific retrieval channel here, cold-contacting authors for unpublished data, introduce a fresh selection filter just as capable of inflating the result as deflating it (the other four)?

The Expansionist's strongest case: there's a documented pattern where a study's thesis version shows a smaller or null effect than its own later published version, because pressure to land on something clean operates at the publication stage. If that holds here, a significant effect that survived dilution by null-leaning material is the harder result to produce.

The rest of the council's answer: that argument proves something more general than what this meta-analysis needs proven. "Gray literature in general trends toward null" isn't the same claim as "gray literature obtained by emailing authors and asking if they have anything lying around trends toward null" — the second is the actual mechanism here, and reluctant authors sitting on a disappointing result are more likely to just not reply. Industry/NGO reports folded into the same bucket cut against the Expansionist's case further, since those are sometimes produced by parties with a stated interest in the conclusion. Neither side is arguing in bad faith — thesis-deflation is real, so is reluctant-author non-response — they're different mechanisms that can each dominate in different corners of what's being lumped together as one "gray literature" number.

### Blind Spots the Council Caught
Four things surfaced only through peer review, absent from all five original responses:

No one named the actual statistical toolkit for this exact problem — funnel plots, Egger's regression, trim-and-fill, PET-PEESE, Copas selection models, p-curve. All five peer reviewers independently caught that the four skeptical advisors reinvented an informal version (the published-vs-unpublished split) without noting that sharper, formal versions already exist.

Nobody flagged double-counting: a single underlying study can enter the pool more than once — as a thesis, then a conference abstract from the same data, then an eventual journal article — breaking the independence assumption the pooled variance depends on and manufacturing significance out of one result counted twice.

Weighting corrects for precision, not quality: inverse-variance weighting rewards a study for a small variance (typically just a large sample), not for being well-conducted. One large, low-quality unpublished study can dominate the pooled estimate regardless of what share of study *count* is gray literature.

The council's own consensus test has a hole: dropping the unpublished half doesn't just remove potential bias, it roughly halves the sample, which mechanically widens the confidence interval. A significance flip is consistent with real bias — but equally consistent with simple power loss, true effect unchanged. The Executor and First Principles Thinker both stated their version of this check as if a significance flip settles the matter outright, with no such caveat.

### The Recommendation
Don't trust the topline finding yet, and don't dismiss it either. Treat it as unverified pending one specific, cheap check, and put the burden of proof on whoever wants you to act on it now.

The case for trusting it immediately (the Expansionist's position) was the one every peer reviewer independently rated weakest: it generalizes a real pattern to a retrieval mechanism it was never shown to apply to, and proposes no way to check itself against this dataset — the exact over-trust failure mode the question flagged. But nobody on the council argued for reflexive dismissal either; even the most skeptical advisors built an explicit path to trusting the result, conditional on a named check. A good-faith gray-literature search is not automatically a red flag. The real problem is narrower: direct-author-solicitation is an under-scrutinized channel with a plausible bias toward flattering results, sitting on top of an analysis process — data pulled and computed on the spot for the meta-analyst — with no pre-registration and no independent check.

One caveat survives even a clean check: independent teams doing honest gray-literature searches on the same question are documented to surface substantially different, barely-overlapping study sets. This result is somewhat contingent on which theses and conference programs this particular team happened to find, in a way the published-only check doesn't fully retire. A clean result earns trust. It doesn't buy certainty.

### The One Thing to Do First
Get the study-level data behind the forest plot, split it into peer-reviewed vs. unpublished, and compute the effect size and confidence interval for each half side by side — not just whether the peer-reviewed half alone still clears p<0.05, which conflates losing half the sample's power with actually removing bias. If the unpublished-only estimate runs materially larger than the peer-reviewed-only estimate, the finding is most likely inflated by relocated selection bias and isn't ready to act on. If the two estimates land close together, or the unpublished half is smaller, the finding has earned its significance and the gray-literature search did the job it was supposed to do.
"""


Grade in three passes.

PASS 0 — Errors. For each of A–D, list the factual or logical errors you can identify on the page, one line each, or write "none found". An overstated claim counts as an error when the point made only supports a weaker one ("decisive", "always", "proves" where the honest word is "suggests"); so does advice that contradicts the facts the question states. Do not count omissions here.

PASS 1 — Ranking. Rank the four responses from best to worst on overall usefulness to the person asking, one sentence per response on why it sits where it does.

PASS 2 — Absolute. Correctness must agree with PASS 0: a response with any error you listed cannot score 5 on correctness, and one with a material error — one that would change what the reader does or believes — cannot score above 3. For each of A–D, score each axis 1-5 independently, with one-line justification. Axes: Correctness (factually right, logic intact), Insight (non-obvious, generative), Practical usefulness (actionable, right scope), Risk awareness (what could go wrong, hidden assumptions), Dissent quality (are the strongest counter-arguments to its own recommendation presented, and presented fairly). Use this fenced format exactly so the orchestrator can parse:

```scores
response: A
correctness: 1-5
insight: 1-5
practical: 1-5
risk: 1-5
dissent: 1-5
```

[Repeat for B, C, D.]
