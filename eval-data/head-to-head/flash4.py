#!/usr/bin/env python3
"""Round 4 of the wise-men head-to-head (PREREG-4.md), read for wise-men-flash.
  report | results | readme | examples | verify
Run from the repo root. Every other file in this directory is a byte-identical copy of the wise-men repository's
eval-data/head-to-head/ at commit 770c75a; this script only reads them. normalize() and score_blocks() are copied
verbatim from that repository's h2h.py, and the analysis (means, bootstrap, seed, wording) is its h2h4.py's, so every
number here matches wise-men's RESULTS-V4.md — seen from the flash arm instead of the full council."""
import os, re, sys, glob, random, statistics as st, yaml
from decimal import Decimal, ROUND_HALF_UP

H = os.path.dirname(os.path.abspath(__file__))
AXES = ["correctness", "insight", "practical", "risk", "dissent"]
AXIS_NAME = {"correctness": "correctness", "insight": "insight", "practical": "practical use", "risk": "risk awareness", "dissent": "dissent quality"}
HERO, SIB = "wise-men-3.13-fast", "wise-men-3.13"
ARMS = [HERO, SIB, "warp-council", "llm-council", "direct"]
RIVALS = ["warp-council", "llm-council", "direct"]; COUNCILS = ["warp-council", "llm-council"]
JUDGES = ["j1", "j2", "j3"]
NAMES = {HERO: "**wise-men-flash** (measured as wise-men 3.13 `--fast`)", SIB: "wise-men 3.13 full council", "warp-council": "Warp council", "llm-council": "llm-council", "direct": "plain answer"}
SHORT = {HERO: "wise-men-flash", SIB: "the full wise-men council", "warp-council": "Warp council", "llm-council": "llm-council", "direct": "the plain answer"}
QS = {q["id"]: q for q in yaml.safe_load(open(os.path.join(H, "questions-r4.yaml")))}
BLIND = yaml.safe_load(open(os.path.join(H, "blinding4.yaml")))["map"]

STOPPED = ("**Stopped early: {n} of {total} questions.** The round was pre-registered at eight questions and stopped after five at the repository owner's request, to conserve the account's usage allowance. "
           "The decision was made while the fifth question was running, after the scores of the first three were known, so it was not a blind stop. {todo} (writing, ethics, a personal decision) were never run: "
           "no answer or judgment exists for them, and nothing here says how any arm does on those kinds of question. Every comparison below is over five questions; intervals are 95% percentile bootstraps over those five.")
PROVENANCE = ("**What was measured.** Round 4 of the `wise-men` head-to-head ran five arms: the full `wise-men` 3.13.0 council, its three-member `--fast` profile, "
              "Warp's council, llm-council and a plain answer. The `--fast` arm is the profile `wise-men-flash` ships — a practitioner anchor and a Devil's Advocate on the strong model, one domain member on mid, "
              "no peer review, a cheap-tier check of the draft against the question — so its row is this skill's evidence. It was measured inside `wise-men`, before this repository existed; "
              "this skill's own standalone round is pre-registered in [`../PREREG-1.md`](../PREREG-1.md) and has not run yet.")
DISCLOSURES = [
    "- **Inherited, not re-measured.** Every flash number here is the `wise-men-3.13-fast` arm, run as `/wise-men --fast` under wise-men 3.13.0. `wise-men-flash` 0.1.0 packages that profile with the rule wise-men added right after this round (3.13.1: nothing about how the answer was produced appears in it) and a sharper brief for its domain seat and Devil's Advocate; those changes are untested until `PREREG-1` runs.",
    "- **Process notes the judges saw.** Three of the five flash answers closed with a note about how they were produced — \"this ran at quick tier … per the requested `--fast` mode\" (R402), \"a late review flagged …\" (R403), and a counter-position introduced as \"the council's dissenting position\" plus a closing verification note (R405). Judges marked these as process residue. The rule that removes them is in this skill; the scores above include the penalty.",
    "- **The synthesis check** took 0.5–2.1 minutes on every flash run (cheap tier, four of the six checks), against 9–11 minutes on every full-council run.",
    "- **Normalization** is `normalize()` from rounds 1–3 of the wise-men study, unchanged and copied into `flash4.py`: it strips the provenance header and any short status text before an answer's first heading. On R402 it removed a paragraph in which the full council described its checker's findings before its memo — the judges did not see it.",
    "- **Web access.** The rival councils' members run as general-purpose agents and can browse; Warp's did on R401 (33 web tool calls) and on no other question; llm-council's never did. Flash members cannot browse.",
    "- **Time** is the median over runs the usage limit did not interrupt (four of five for each council arm; all five for the plain answer). Cost and calls use all five runs; a resumed run's cost includes re-reading its own context after the wait.",
    "- **Same family.** Every judge and every arm is a Claude model, and every spawned agent in every arm inherited the account's global instruction to write tersely. No human grades and no grades from another model family were collected.",
    "- **Judge calibration** (pre-registered): before any round-4 judgment, the error-first prompt was run once on round 3's Q23 answers, where an earlier wise-men answer overstated a check that a rival correctly limited; `blinded-v4/CAL-Q23.md` and `judgments-v4/CAL-Q23.md` hold the packet and the result.",
]

def r1(x): return str(Decimal(str(x)).quantize(Decimal("0.1"), ROUND_HALF_UP))
def r2(x): return str(Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))
def sg(x): return ("+" if x >= 0 else "−") + r1(abs(x))
def cnt(x): return str(int(x)) if float(x).is_integer() else r1(x)
def and_join(xs): return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1] if xs else "none"

# --- copied verbatim from wise-men's eval-data/head-to-head/h2h.py (rounds 1-4 use the same two functions) ---
def normalize(arm, txt):
    lines = txt.split("\n")
    while lines and (lines[0].startswith("# ") or lines[0].strip() == ""): lines.pop(0)  # provenance header block (all '# ' lines at top)
    t = "\n".join(lines).strip()
    # orchestrator status text that precedes the skill's own output (not part of any skill's user-facing format):
    # for skills whose output is headed, cut to the first '## ' heading if what precedes it is short status prose
    if arm in ("lifeos-council", "llm-council", "wise-men", "ecc-council", "warp-council"):
        m = re.search(r"^## ", t, re.M)
        if m and m.start() > 0 and len(t[:m.start()].split("\n")) <= 4: t = t[m.start():]
    if arm == "wise-men":  # same rule as the N=29 eval: strip the audit footer + status/process text; never edit content
        m = re.search(r"^(\*Note: brief format upgraded|## )", t, re.M)  # skill output starts at its first heading/note
        if m: t = t[m.start():]
        t = re.sub(r"^\*Note: brief format upgraded.*?\*\n+", "", t)
        t = re.split(r"\n---\n\n## Full audit( trail)?", t)[0].strip()
        t = re.sub(r"\n+\*One process note:.*?\*\s*$", "", t, flags=re.S).strip()  # orchestrator environment note (harness artefact, not skill output)
    return t


def score_blocks(text, letters):
    """Every fenced scores block in a judgment, parsed strictly: exactly one response letter and the five axes, each an
    integer 1-5 on its own line, no duplicate keys, no duplicate letters. A malformed block raises instead of being truncated."""
    out = {}
    for b in re.findall(r"```scores\n(.*?)```", text, re.S):
        d = {}
        for line in (l.strip() for l in b.strip().splitlines() if l.strip()):
            m = re.fullmatch(r"(\w+):\s*(\S+)", line)
            assert m and m[1] not in d, ("malformed or duplicate line in scores block", line)
            d[m[1]] = m[2]
        assert set(d) == {"response", *AXES}, ("scores block keys", sorted(d))
        assert d["response"] in letters and d["response"] not in out, ("response letter", d["response"])
        assert all(re.fullmatch(r"[1-5]", d[a]) for a in AXES), ("axis score must be an integer 1-5", d)
        out[d["response"]] = {a: int(d[a]) for a in AXES}
    return out
# --- end of verbatim copy ---

def load():
    R = {}
    for f in sorted(glob.glob(os.path.join(H, "parsed-v4", "R*.yaml"))):
        d = yaml.safe_load(open(f)); R[d["question_id"]] = {a: {k: st.mean(d["judges"][j][a][k] for j in JUDGES) for k in AXES + ["composite"]} for a in ARMS}
        R[d["question_id"]]["_sd"] = {a: st.pstdev([d["judges"][j][a]["composite"] for j in JUDGES]) for a in ARMS}
    return R

def costs():
    """Per arm: minutes, calls and USD read back from the raw headers; runs whose note says they were interrupted are left out of the time figures only."""
    C = {a: {"min": [], "usd": [], "calls": []} for a in ARMS}
    for q in QS:
        for a in ARMS:
            p = os.path.join(H, "raw", q, a + ".md")
            if not os.path.exists(p): continue
            h = open(p).read().split("\n\n", 1)[0]; m = re.search(r"minutes: ([\d.]+) \| subagent calls: (\d+).*list-price USD: ([\d.]+)", h)
            if not m: continue
            C[a]["usd"].append(float(m[3])); C[a]["calls"].append(int(m[2]))
            if "interrupted" not in h: C[a]["min"].append(float(m[1]))
    return C

def med(v): return st.median(v) if v else float("nan")
def boot(d, seed=20260919, n=10000):  # h2h4.py's percentile bootstrap and seed
    rng = random.Random(seed); k = len(d); means = sorted(st.mean(rng.choice(d) for _ in range(k)) for _ in range(n)); return means[int(0.025 * n)], means[int(0.975 * n) - 1]
def compare(R, a, b=HERO):
    d = [R[q][b]["composite"] - R[q][a]["composite"] for q in R]; lo, hi = boot(d); m = st.mean(d)
    word = "clearly ahead" if lo > 0 else "ahead" if m > 0 else "level" if m == 0 else "clearly behind" if hi < 0 else "behind, with an interval that includes zero"
    return {"diff": m, "lo": lo, "hi": hi, "w": sum(x > 0 for x in d), "t": sum(x == 0 for x in d), "l": sum(x < 0 for x in d), "word": word}
def table(R): return {a: {"mean": st.mean(R[q][a]["composite"] for q in R), "axes": {x: st.mean(R[q][a][x] for q in R) for x in AXES}} for a in ARMS}

def lines():
    R = load(); n = len(R); T = table(R); C = costs(); L = []
    L += [f"| round 4 ({n} of {len(QS)} questions) | total /25 | correct | insight | practical | risk | dissent | median minutes | median calls | median list-price USD |", "|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|"]
    for a in sorted(ARMS, key=lambda a: -T[a]["mean"]):
        L += [f"| {NAMES[a]} | {r1(T[a]['mean'])} | " + " | ".join(r1(T[a]["axes"][x]) for x in AXES) + f" | {r1(med(C[a]['min']))} | {cnt(med(C[a]['calls']))} | {r2(med(C[a]['usd']))} |"]
    L += [""]
    for a in RIVALS + [SIB]:
        c = compare(R, a); L += [f"- wise-men-flash against {NAMES[a]}: {sg(c['diff'])} [{sg(c['lo'])}, {sg(c['hi'])}], W–T–L {c['w']}–{c['t']}–{c['l']} — {c['word']}."]
    L += [""]
    lead ={x: [a for a in ARMS if abs(T[a]["axes"][x] - max(T[z]["axes"][x] for z in ARMS)) < 1e-9] for x in AXES}
    alone = [AXIS_NAME[x] for x in AXES if lead[x] == [HERO]]; shared = [AXIS_NAME[x] for x in AXES if HERO in lead[x] and len(lead[x]) > 1]
    sib = [AXIS_NAME[x] for x in AXES if HERO not in lead[x] and SIB in lead[x]]
    above = sum(all(T[HERO]["axes"][x] > T[a]["axes"][x] for a in RIVALS) for x in AXES)
    L += ["- Axes: wise-men-flash had the highest " + (and_join(alone) if alone else "score on no axis") + " of the five arms" + (f", tied with the full council for the highest {and_join(shared)}" if shared else "") +
          f", and scored above every rival on {above} of 5 axes; the full council led {and_join(sib)}."]
    both = [a for a in [SIB] + COUNCILS if med(C[HERO]["min"]) < med(C[a]["min"]) and med(C[HERO]["usd"]) < med(C[a]["usd"])]
    quicker = [a for a in [SIB] + COUNCILS if med(C[a]["min"]) <= med(C[HERO]["min"])]
    def edge(a):
        s = f"{SHORT[a]} was {r1(med(C[HERO]['min']) - med(C[a]['min']))} min quicker"
        if med(C[a]["usd"]) < med(C[HERO]["usd"]): s += f" and ${r2(med(C[HERO]['usd']) - med(C[a]['usd']))} cheaper"
        return s + f", and scored {r1(T[HERO]['mean'] - T[a]['mean'])} lower"
    L += ["- Time and cost, medians per question: " + "; ".join(f"{SHORT[a]} {r1(med(C[a]['min']))} min, ${r2(med(C[a]['usd']))}" for a in sorted(ARMS, key=lambda a: med(C[a]["min"]))) +
          f". wise-men-flash was faster and cheaper than {and_join([SHORT[a] for a in both])}" + ("; " + "; ".join(edge(a) for a in quicker) if quicker else "") + "."]
    sds = [R[q]["_sd"][a] for q in R for a in ARMS]; L += ["", f"Judge agreement: mean SD of the three judges' totals {r2(st.mean(sds))}."]
    return L

def report(): print("\n".join(lines()))
def readme(): print("\n".join(lines()))
def results():
    R = load(); todo = [q for q in QS if q not in R]
    L = ["# Round 4, read for wise-men-flash", "", PROVENANCE, ""] + ([STOPPED.format(n=len(R), total=len(QS), todo=", ".join(todo)), ""] if todo else [])
    L += ["Eight questions written for the round by an author that knew nothing about the arms ([`PREREG-4.md`](PREREG-4.md), [`questions-r4.yaml`](questions-r4.yaml)); five arms; three blind Opus judges per question with sealed orders ([`blinding4.yaml`](blinding4.yaml)) and an error-first judge prompt ([`judge-prompt-5.txt`](judge-prompt-5.txt)). "
          "Minutes are the orchestrator's first-to-last transcript timestamp; calls are its subagent spawns; USD prices every token the run used — the orchestrator's and every spawned agent's, input, output, cache reads and cache writes — at 2026-07 list rates. No council can be faster or cheaper than the plain answer; the pre-registered time and cost comparisons are against the rival councils.", ""] + lines()
    L += ["", "## Per question (mean of three judges, total /25)", "", "| question | " + " | ".join(NAMES[a] for a in ARMS) + " |", "|---|" + "--:|" * len(ARMS)] + [f"| {q} ({QS[q]['domain']}, {QS[q]['shape']}) | " + " | ".join(r2(R[q][a]["composite"]) for a in ARMS) + " |" for q in R]
    notes = [f"- {q}, {SHORT[a]}: {l[8:]}" for q in QS for a in ARMS if os.path.exists(os.path.join(H, "raw", q, a + ".md")) for l in open(os.path.join(H, "raw", q, a + ".md")).read().split("\n\n", 1)[0].splitlines() if l.startswith("# note: ")]
    L += ["", "## Deviations and disclosures", ""] + DISCLOSURES + notes + ["", "## Reproduce", "",
          "`python3 eval-data/head-to-head/flash4.py report` prints the table and comparisons; `results` rewrites this file; `verify` rebuilds every blinded packet from the raw answers and re-parses every judgment, and fails on any difference. "
          "Time and cost were computed from local agent transcripts when each answer was saved and are stored in the raw file headers; the transcripts themselves are not in the repository. "
          "The same data, seen from the full council, is `RESULTS-V4.md` in the [wise-men repository](https://github.com/Ali-expandings/wise-men/blob/master/eval-data/head-to-head/RESULTS-V4.md).", ""]
    out = "\n".join(L)
    if os.environ.get("FLASH4_STDOUT"): sys.stdout.write(out); return
    open(os.path.join(H, "RESULTS.md"), "w").write(out); print("wrote RESULTS.md:", len(R), "questions")

EXAMPLES = {"engineering-choice": ("R401", "an engineering choice"), "trust-a-number": ("R404", "how far to trust a vendor's number")}
EX_DIR = os.path.join(os.path.dirname(os.path.dirname(H)), "examples")

def example(name):
    """A worked example: the question, how the judges scored every arm, and the flash answer exactly as the judges read it."""
    q, what = EXAMPLES[name]; R = load(); raw = open(os.path.join(H, "raw", q, HERO + ".md")).read(); head = raw.split("\n\n", 1)[0]
    c = re.search(r"minutes: ([\d.]+) \| subagent calls: (\d+).*list-price USD: ([\d.]+)", head); js = yaml.safe_load(open(os.path.join(H, "parsed-v4", q + ".yaml")))["judges"]
    L = [f"# Example: {what}", "", f"The question — round 4, {q} ({QS[q]['domain']}, {QS[q]['shape']}), written by an author that knew nothing about the skills being tested:", "", "> " + QS[q]["text"], "",
         f"**What happened.** The profile this skill ships — measured as wise-men 3.13.0 run with `--fast` — answered in {c[1]} minutes with {c[2]} subagent calls (${c[3]} at list price). "
         f"Three blind judges, each reading five unlabeled answers in its own sealed order, scored it {', '.join(str(js[j][HERO]['composite']) for j in JUDGES[:-1])} and {js[JUDGES[-1]][HERO]['composite']} of 25:", "",
         "| arm | mean /25 | correct | insight | practical | risk | dissent |", "|---|--:|--:|--:|--:|--:|--:|"]
    for a in sorted(ARMS, key=lambda a: -R[q][a]["composite"]):
        nm = "**wise-men-flash**" if a == HERO else SHORT[a].replace("the ", "", 1)
        L += [f"| {nm} | {r1(R[q][a]['composite'])} | " + " | ".join(r1(R[q][a][x]) for x in AXES) + " |"]
    L += ["", f"The answer below is the text the judges read, verbatim: the raw file minus its provenance header ([`raw/{q}/{HERO}.md`](../eval-data/head-to-head/raw/{q}/{HERO}.md)). "
          f"What each judge wrote about it: [`judgments-v4/{q}-j1.md`](../eval-data/head-to-head/judgments-v4/{q}-j1.md), [`j2`](../eval-data/head-to-head/judgments-v4/{q}-j2.md), [`j3`](../eval-data/head-to-head/judgments-v4/{q}-j3.md) — the letter for each arm is in [`blinding4.yaml`](../eval-data/head-to-head/blinding4.yaml).",
          "", "---", "", normalize("wise-men", raw), ""]
    return "\n".join(L)

def examples():
    os.makedirs(EX_DIR, exist_ok=True)
    for name in EXAMPLES: open(os.path.join(EX_DIR, name + ".md"), "w").write(example(name)); print("wrote examples/" + name + ".md")

def verify():
    """The judges saw exactly the normalized raw answers, and parsed-v4/ holds exactly what the judgments say."""
    for name in EXAMPLES:
        p = os.path.join(EX_DIR, name + ".md")
        assert os.path.exists(p) and open(p).read() == example(name), ("example differs from a regeneration", name)
    tpl = open(os.path.join(H, "judge-prompt-5.txt")).read(); packets = parsed = 0
    for q in sorted(QS):
        if not os.path.exists(os.path.join(H, "parsed-v4", q + ".yaml")): continue
        for j in JUDGES:
            parts = [f'Response {slot}:\n"""\n{normalize("wise-men" if arm.startswith("wise-men") else arm, open(os.path.join(H, "raw", q, arm + ".md")).read())}\n"""\n' for slot, arm in BLIND[q][j].items()]
            want = tpl.replace("{question}", QS[q]["text"]).replace("{responses}", "\n".join(parts))
            assert open(os.path.join(H, "blinded-v4", f"{q}-{j}.md")).read() == want, ("blinded packet differs from a rebuild", q, j); packets += 1
        got = {}
        for j in JUDGES:
            got[j] = {}
            for slot, sc in score_blocks(open(os.path.join(H, "judgments-v4", f"{q}-{j}.md")).read(), set(BLIND[q][j])).items():
                got[j][BLIND[q][j][slot]] = dict(sc, composite=sum(sc.values()))
            assert set(got[j]) == set(ARMS), (q, j)
        assert yaml.safe_load(open(os.path.join(H, "parsed-v4", q + ".yaml")))["judges"] == got, ("parsed scores differ from the judgments", q); parsed += 1
    print(f"verify: {packets} blinded packets rebuilt byte-identical from raw/, {parsed} parsed files match their judgments, {len(EXAMPLES)} examples match the raw answers")

if __name__ == "__main__":
    {"report": report, "results": results, "readme": readme, "verify": verify, "examples": examples}[sys.argv[1]](*sys.argv[2:])
