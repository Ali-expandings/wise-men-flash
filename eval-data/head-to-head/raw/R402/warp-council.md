# arm: warp-council (warpdotdev/common-skills 69b4753651ab; adapted as in PREREG-2) | question: R402 | orchestrator: general-purpose/sonnet | run: 2026-09-18 (round 4, PREREG-4 rules)
# minutes: 151.1 | subagent calls: 3 (transcripts matched: 3) | tokens in/out/cache-read/cache-write: 20/77897/146632/293806 | list-price USD: 2.42
# note: interrupted by the account's usage limit after its three members had answered, and resumed from its own transcript; left out of the time median

## Council

Three members, read-only, no file/codebase access (none applicable — this is a standalone diagnosis question, not tied to a repo). Independent, no cross-sharing.

- **Opus** — architecture/correctness lead: systemic race/resource-contention analysis.
- **Sonnet** — substituted for the GPT seat (no GPT model available in this harness) — operations/implementation-feasibility lead.
- **Haiku** — substituted for the open-source seat (none available) — contrarian/red-team lead, per the skill's own fallback rule for that case.

## Recommendation

The pipeline has no precondition contract: it fires on a wall-clock schedule instead of on verified proof that upstream data (and/or capacity) is actually ready. On nights upstream lands late, partial, or unusually large — or a shared compute/connection/memory ceiling is tight — the pipeline reads incomplete data or hits a resource wall, and whichever stage touches that gap first throws whatever error the gap happens to produce. Manual reruns pass because by the time someone reruns, hours later, the condition has cleared — same code, now-complete data, no bug actually fixed. Two of three council members converged on this independently; it's the one mechanism that explains all three symptoms at once.

## Why

- **Different error each time is expected, not random.** Which stage trips depends on which specific data or resource was thin that night — one precondition failure sampled through many code paths, not many unrelated bugs. (Opus + Sonnet consensus.)
- **"Rerun with no code change fixes it" is diagnostic, not luck.** The automated retries the team added run on a short backoff (minutes); they can't bridge an upstream delay measured in hours. The manual rerun that actually closes each incident happens later, after the precondition clears. That's why two years of retries never moved the rate — they operate on the wrong timescale for this failure class. (Opus + Sonnet.)
- **Two years of unmoved rate, independent of which bug got patched.** Every postmortem fixed the proximate exception (a null-check here, a longer timeout there) and closed the ticket. Incidents get implicitly deduped and filed by error message, so the several dozen occurrences over two years were never lined up against each other — the recurring precondition was structurally invisible to a process that groups by symptom text. All three members flagged this independently; it's the strongest single point of agreement on the council.
- **Dissent worth keeping.** Haiku's independent lead hypothesis is upstream schema/data-contract drift (bad field content, not lateness), and it argued against the timing-race framing on the grounds that retries "should" fix a real race. That argument only holds for short automated retries — it doesn't touch the hours-later manual rerun the team actually depends on, so it doesn't rule out the majority hypothesis. But the underlying alternative (upstream sends structurally bad data, not just late data) is real, distinct, and worth checking in the same diagnostic pass, not dismissed.

## Tradeoffs and risks

- **Possible silent-failure population underneath the visible one.** If the mechanism is "read partial data," some nights may already be succeeding on marginal or incomplete input instead of throwing — the visible failure rate could be a floor over an invisible layer of quietly-wrong output. Worth ruling out before declaring any fix done. (Sonnet.)
- **The confirming evidence doesn't exist yet in usable form.** No one has pulled orchestrator start/end times, upstream completion timestamps, per-source volume, and cluster/queue load and lined them up per incident, against clean nights too. That correlation pass, not more logging, is the missing step.
- **Falsifier.** If that pass shows failures scattered with no timing/volume/load pattern at all, this whole family is wrong and a rarer cause (a floating dependency version, a write race internal to the pipeline itself) moves up — lower-probability, but real. (Opus.)
- **Confidence:** medium-high on the mechanism class (a precondition/capacity race sitting outside the pipeline's own code boundary); lower on timing-lateness vs. resource-contention vs. data-contract-drift as the specific trigger — these are related, not mutually exclusive, and the correlation pass below is what distinguishes them.

## Final call

Do now: pull the last 10-15 incidents and line them up by time-since-upstream-landed, data volume, and resource load at the failure timestamp — not by error text. That single correlation pass, on data that already exists, confirms or kills this diagnosis in days. In parallel, start logging upstream readiness/completion state on every run, not just failed ones — that's the instrumentation gap, not more exception detail.

Do later, once confirmed: replace the wall-clock trigger with a real readiness gate (an upstream completion signal, or a row-count/checksum-stable sensor the orchestrator blocks on) and add capacity headroom if contention is implicated too. That's the actual fix. Retries, alerting, and more logging aren't, because all three operate inside the pipeline's own boundary while the cause sits outside it — in whether upstream and capacity were actually ready when the clock struck.
