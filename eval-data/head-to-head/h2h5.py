#!/usr/bin/env python3
"""Head-to-head round 5 (PREREG-5.md): wise-men 3.14.0 and wise-men-flash 0.1.0 against every rival from rounds 1-4,
at each rival's latest version, on eight new questions; three judges per question; measured time and cost.
  seal | save <agent-transcript.jsonl> <arm> <Q> [note] | savejudge <transcript> <Q> <j> | blind <Q> | parse <Q>
  report | results | readme wise-men|flash | verify
Run from the repo root. Self-contained — normalize() and score_blocks() are copied verbatim from rounds 1-4 (h2h.py) and
the cost code from round 4 (h2h4.py) — so this file is byte-identical in the wise-men and wise-men-flash repositories."""
import os, re, sys, json, glob, random, statistics as st, yaml
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

H = os.path.dirname(os.path.abspath(__file__))
AXES = ["correctness", "insight", "practical", "risk", "dissent"]
AXIS_NAME = {"correctness": "correctness", "insight": "insight", "practical": "practical use", "risk": "risk awareness", "dissent": "dissent quality"}
WM, FL = "wise-men-3.14", "wise-men-flash"
ARMS = [WM, FL, "warp-council", "llm-council", "lifeos-council", "ecc-council", "brainstorming", "grilling", "direct"]
HEROES = [WM, FL]; RIVALS = ARMS[2:]; COUNCILS = ["warp-council", "llm-council", "lifeos-council", "ecc-council"]
JUDGES = ["j1", "j2", "j3"]; SEED = 20260925
QIDS = [f"R50{i}" for i in range(1, 9)]
RUN_ORDER = ["R506", "R501", "R507", "R503", "R508", "R502", "R504", "R505"]  # fixed in PREREG-5: the three kinds round 4 never ran come early
NAMES = {WM: "wise-men 3.14.0", FL: "wise-men-flash 0.1.0", "warp-council": "Warp council", "llm-council": "llm-council", "lifeos-council": "LifeOS Council",
         "ecc-council": "ECC council", "brainstorming": "superpowers brainstorming", "grilling": "mattpocock grilling", "direct": "plain answer"}
HEAD = {WM: "wise-men-3.14 (Ali-expandings/wise-men SKILL.md v3.14.0, as of 770c75a)", FL: "wise-men-flash (Ali-expandings/wise-men-flash SKILL.md v0.1.0, dbfdcef)",
        "warp-council": "warp-council (warpdotdev/common-skills 69b4753651ab; adapted as in PREREG-2)", "llm-council": "llm-council (aiwithremy/claude-skills-llm-council 55ee36e89e0f)",
        "lifeos-council": "lifeos-council (danielmiessler/LifeOS 5e2f2e8c0abd, with Workflows/Debate.md and Workflows/Quick.md)", "ecc-council": "ecc-council (affaan-m/ECC bf70150eb2df)",
        "brainstorming": "brainstorming (obra/superpowers 5bf4e7801107, with visual-companion.md and spec-document-reviewer-prompt.md)",
        "grilling": "grilling (mattpocock/skills c55ee46073ed)", "direct": "direct (no skill)"}
QF = os.path.join(H, "questions-r5.yaml"); BF = os.path.join(H, "blinding5.yaml")
QS = {q["id"]: q for q in yaml.safe_load(open(QF))} if os.path.exists(QF) else {}
BLIND = yaml.safe_load(open(BF))["map"] if os.path.exists(BF) else {}
PRICE = {"haiku": (1, 5), "sonnet": (3, 15), "opus": (5, 25), "fable": (10, 50)}  # USD per million input/output tokens (2026-07 list); cache read 0.1x input, 5-minute cache write 1.25x input

STOPPED = ("**Stopped early: {n} of {total} questions.** The round was pre-registered at eight questions and stopped after {n}. {todo} were never run: no answer or judgment exists "
           "for them, and nothing here says how any arm does on those questions. Every comparison below is over the questions run; intervals are 95% percentile bootstraps over them.")
STATUS = "in progress"  # "in progress" while questions remain to run; "stopped" only if the round ends before eight
IN_PROGRESS = ("**In progress: {n} of {total} questions judged.** The remaining questions ({todo}) run after the account's weekly usage limit resets, in the pre-registered order; "
               "this file, the README tables and the charts are regenerated as each one is judged. Every comparison below is over the questions judged so far; intervals are 95% percentile bootstraps over them, and with this few questions they are wide.")
DISCLOSURES = [
    "- Every answer is new: all nine arms answered every question in this round, in the same days and on the same models. No earlier answer is reused.",
    "- Rival versions: each rival skill at its latest commit on 2026-09-24. Only superpowers brainstorming had changed since the earlier rounds (2026-09-19: a shared-understanding step and path-specific approval gates). "
    "Two rivals were given files earlier rounds did not supply, because their skill files point at them: LifeOS Council its two workflow files, superpowers brainstorming its visual-companion and spec-reviewer files.",
    "- Adaptations, unchanged from earlier rounds: brainstorming, grilling and ECC's council state the answers they assume instead of waiting for a human; Warp's council runs its members on Claude models only, with no approval pause; LifeOS Council skips its local voice notification.",
    "- Orchestrators run on Sonnet; each skill's own subagents run on the models the skill names, through Claude Code's tier aliases as they resolved during the run. Every judge and every arm is a Claude model, and every spawned agent inherits the account's global instruction to write tersely. No human grades were collected.",
    "- Cost is priced at the 2026-07 list rates in this file; a model released since is priced at its tier's rate.",
]

def r1(x): return str(Decimal(str(x)).quantize(Decimal("0.1"), ROUND_HALF_UP))
def r2(x): return str(Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))
def sg(x): return ("+" if x >= 0 else "−") + r1(abs(x))
def cnt(x): return str(int(x)) if float(x).is_integer() else r1(x)
def and_join(xs): return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1] if xs else "none"

# --- copied verbatim from rounds 1-4 (eval-data/head-to-head/h2h.py in the wise-men repository) ---
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

# --- time and cost, as round 4 (h2h4.py) ---
def rows_of(f): return [json.loads(l) for l in open(f)]
def tier(model): return next((k for k in PRICE if k in (model or "")), "sonnet")
def first_prompt(rows):
    r = next((r for r in rows if r.get("type") == "user"), None)
    if not r: return ""
    c = r["message"]["content"]; return c if isinstance(c, str) else "\n".join(x.get("text", "") for x in c if x.get("type") == "text")
def final_text(rows):
    last = max(i for i, r in enumerate(rows) if r.get("type") == "user")
    return "\n".join(c["text"] for r in rows[last + 1:] if r.get("type") == "assistant" for c in r["message"]["content"] if c.get("type") == "text").strip()
def usage(rows):
    """Tokens by billing category and list-price USD for one transcript. Streamed messages repeat their id: keep the largest figure per field."""
    per = {}
    for r in rows:
        if r.get("type") != "assistant": continue
        m = r["message"]; x = m.get("usage") or {}; d = per.setdefault(m.get("id"), {"model": m.get("model"), "in": 0, "out": 0, "cr": 0, "cw": 0})
        for k, f in (("in", "input_tokens"), ("out", "output_tokens"), ("cr", "cache_read_input_tokens"), ("cw", "cache_creation_input_tokens")): d[k] = max(d[k], x.get(f, 0) or 0)
    u = {"in": 0, "out": 0, "cr": 0, "cw": 0, "usd": 0.0}
    for d in per.values():
        pi, po = PRICE[tier(d["model"])]
        for k in ("in", "out", "cr", "cw"): u[k] += d[k]
        u["usd"] += (d["in"] * pi + d["out"] * po + d["cr"] * pi * 0.1 + d["cw"] * pi * 1.25) / 1e6
    return u
def run_cost(transcript):
    """The orchestrator plus every agent spawned under it at any depth (matched by the exact prompt sent), so a council's
    members and anything they spawn are priced. Calls count the orchestrator's own spawns, as in round 4."""
    rows = rows_of(transcript); ts = [r["timestamp"] for r in rows if r.get("timestamp")]
    t0, t1 = (datetime.fromisoformat(x.replace("Z", "+00:00")) for x in (ts[0], ts[-1]))
    index = {}
    for f in glob.glob(os.path.join(os.path.dirname(transcript), "agent-*.jsonl")):
        try: index.setdefault(first_prompt(rows_of(f))[:3000], []).append(f)
        except Exception: pass
    tot = {"in": 0, "out": 0, "cr": 0, "cw": 0, "usd": 0.0}; used = set(); calls = [0]
    def walk(rs, depth):
        u = usage(rs)
        for k in tot: tot[k] += u[k]
        for r in rs:
            if r.get("type") != "assistant": continue
            for c in r["message"]["content"]:
                if c.get("type") == "tool_use" and c["name"] in ("Agent", "Task"):
                    calls[0] += depth == 0
                    for f in index.get((c["input"].get("prompt") or "")[:3000], []):
                        if f in used: continue
                        used.add(f); walk(rows_of(f), depth + 1); break
    walk(rows, 0)
    return {"minutes": (t1 - t0).total_seconds() / 60, "calls": calls[0], "matched": len(used), **tot}

# --- the round's steps ---
def seal():
    """Generate blinding5.yaml once, before any run: a sealed A-I order of the nine arms for every question and judge."""
    assert not os.path.exists(BF), "blinding5.yaml already exists: the order is sealed"
    rng = random.Random(SEED); m = {}
    for q in QIDS:
        m[q] = {}
        for j in JUDGES:
            arms = ARMS[:]; rng.shuffle(arms); m[q][j] = {chr(65 + k): a for k, a in enumerate(arms)}
    yaml.safe_dump({"seed": SEED, "note": "sealed answer order per question and judge, generated before any round-5 run", "map": m}, open(BF, "w"), sort_keys=False)
    print("sealed", len(m), "questions x", len(JUDGES), "judges")

def save(transcript, arm, q, note=""):
    assert arm in ARMS and q in QIDS, (arm, q)
    rows = rows_of(transcript); txt = final_text(rows); red = re.sub(r"\bAli\b", "the user", txt); c = run_cost(transcript)
    head = f"# arm: {HEAD[arm]} | question: {q} | orchestrator: general-purpose/sonnet | run: {rows[0]['timestamp'][:10]} (round 5, PREREG-5 rules)\n"
    head += f"# minutes: {c['minutes']:.1f} | subagent calls: {c['calls']} (transcripts matched: {c['matched']}) | tokens in/out/cache-read/cache-write: {c['in']}/{c['out']}/{c['cr']}/{c['cw']} | list-price USD: {c['usd']:.2f}\n"
    if note: head += f"# note: {note}\n"
    if red != txt: head += "# note: the author's first name (inherited from global config) redacted to \"the user\"\n"
    os.makedirs(os.path.join(H, "raw", q), exist_ok=True); open(os.path.join(H, "raw", q, arm + ".md"), "w").write(head + "\n" + red + "\n")
    print("saved", q, arm, len(red.split()), "words |", f"{c['minutes']:.1f} min, {c['calls']} calls, ${c['usd']:.2f}")

def packet(q, j):
    tpl = open(os.path.join(H, "judge-prompt-r5.txt")).read()
    parts = [f'Response {slot}:\n"""\n{normalize("wise-men" if arm.startswith("wise-men") else arm, open(os.path.join(H, "raw", q, arm + ".md")).read())}\n"""\n' for slot, arm in BLIND[q][j].items()]
    return tpl.replace("{question}", QS[q]["text"]).replace("{responses}", "\n".join(parts))
def blind(q):
    os.makedirs(os.path.join(H, "blinded-v5"), exist_ok=True)
    for j in JUDGES: open(os.path.join(H, "blinded-v5", f"{q}-{j}.md"), "w").write(packet(q, j))
    print("blinded", q, "x3")

def judged(q, j):
    got = {}
    for slot, sc in score_blocks(open(os.path.join(H, "judgments-v5", f"{q}-{j}.md")).read(), set(BLIND[q][j])).items():
        got[BLIND[q][j][slot]] = dict(sc, composite=sum(sc.values()))
    assert set(got) == set(ARMS), (q, j, set(ARMS) - set(got)); return got
def savejudge(transcript, q, j):
    rows = rows_of(transcript); t = final_text(rows); os.makedirs(os.path.join(H, "judgments-v5"), exist_ok=True)
    open(os.path.join(H, "judgments-v5", f"{q}-{j}.md"), "w").write(f"# judge: fresh opus subagent, no skills, Read-only | question: {q} | judge: {j} | run: {rows[0]['timestamp'][:10]} (round 5)\n# blinded input: blinded-v5/{q}-{j}.md (slots per blinding5.yaml)\n\n{t}\n")
    print("judgment", q, j, dict(sorted(((a, v["composite"]) for a, v in judged(q, j).items()), key=lambda x: -x[1])))
def parse(q):
    os.makedirs(os.path.join(H, "parsed-v5"), exist_ok=True); out = {j: judged(q, j) for j in JUDGES}
    yaml.safe_dump({"question_id": q, "judges": out}, open(os.path.join(H, "parsed-v5", q + ".yaml"), "w"), sort_keys=False)
    print("parsed", q, {a: r2(st.mean(out[j][a]["composite"] for j in JUDGES)) for a in ARMS})

# --- analysis ---
def load():
    R = {}
    for f in sorted(glob.glob(os.path.join(H, "parsed-v5", "R*.yaml"))):
        d = yaml.safe_load(open(f)); R[d["question_id"]] = {a: {k: st.mean(d["judges"][j][a][k] for j in JUDGES) for k in AXES + ["composite"]} for a in ARMS}
        R[d["question_id"]]["_sd"] = {a: st.pstdev([d["judges"][j][a]["composite"] for j in JUDGES]) for a in ARMS}
    return R
def costs():
    """Per arm: minutes, calls and USD from the raw headers; runs whose note says they were interrupted are left out of the time figures only."""
    C = {a: {"min": [], "usd": [], "calls": []} for a in ARMS}
    for q in QIDS:
        for a in ARMS:
            p = os.path.join(H, "raw", q, a + ".md")
            if not os.path.exists(p): continue
            h = open(p).read().split("\n\n", 1)[0]; m = re.search(r"minutes: ([\d.]+) \| subagent calls: (\d+).*list-price USD: ([\d.]+)", h)
            if not m: continue
            C[a]["usd"].append(float(m[3])); C[a]["calls"].append(int(m[2]))
            if "interrupted" not in h: C[a]["min"].append(float(m[1]))
    return C
def med(v): return st.median(v) if v else float("nan")
def boot(d, seed=SEED, n=10000):
    rng = random.Random(seed); k = len(d); means = sorted(st.mean(rng.choice(d) for _ in range(k)) for _ in range(n)); return means[int(0.025 * n)], means[int(0.975 * n) - 1]
def compare(R, a, b):
    d = [R[q][b]["composite"] - R[q][a]["composite"] for q in R]; lo, hi = boot(d); m = st.mean(d)
    word = "clearly ahead" if lo > 0 else "ahead" if m > 0 else "level" if m == 0 else "clearly behind" if hi < 0 else "behind, with an interval that includes zero"
    return {"diff": m, "lo": lo, "hi": hi, "w": sum(x > 0 for x in d), "t": sum(x == 0 for x in d), "l": sum(x < 0 for x in d), "word": word}
def table(R): return {a: {"mean": st.mean(R[q][a]["composite"] for q in R), "axes": {x: st.mean(R[q][a][x] for q in R) for x in AXES}} for a in ARMS}

def lines(view="results"):
    """view: 'results' (both heroes, time and cost), 'wise-men' (the wise-men README: quality only), 'flash' (the flash README: quality, time and cost)."""
    R = load(); n = len(R); T = table(R); C = costs(); L = []; timed = view != "wise-men"
    heroes = {"results": HEROES, "wise-men": [WM], "flash": [FL]}[view]
    head = f"| round 5 ({n} of {len(QIDS)} questions) | total /25 | correct | insight | practical | risk | dissent |" + (" median minutes | median calls | median list-price USD |" if timed else "")
    L += [head, "|---|" + "--:|" * (6 + 3 * timed)]
    for a in sorted(ARMS, key=lambda a: -T[a]["mean"]):
        nm = f"**{NAMES[a]}**" if a in heroes else NAMES[a]
        L += [f"| {nm} | {r1(T[a]['mean'])} | " + " | ".join(r1(T[a]["axes"][x]) for x in AXES) + " |" + (f" {r1(med(C[a]['min']))} | {cnt(med(C[a]['calls']))} | {r2(med(C[a]['usd']))} |" if timed else "")]
    for h in heroes:
        L += [""]
        for a in [x for x in ARMS if x != h]:
            c = compare(R, a, h); L += [f"- {NAMES[h]} against {NAMES[a]}: {sg(c['diff'])} [{sg(c['lo'])}, {sg(c['hi'])}], W–T–L {c['w']}–{c['t']}–{c['l']} — {c['word']}."]
        clear = [a for a in RIVALS if compare(R, a, h)["lo"] > 0]
        L += [f"- {NAMES[h]}: " + ("beats every rival — clearly ahead of all seven." if len(clear) == len(RIVALS) else f"clearly ahead of {len(clear)} of the {len(RIVALS)} rivals ({and_join([NAMES[a] for a in clear])}).")]
    L += [""]
    for h in heroes:
        lead = {x: [a for a in ARMS if abs(T[a]["axes"][x] - max(T[z]["axes"][x] for z in ARMS)) < 1e-9] for x in AXES}
        alone = [AXIS_NAME[x] for x in AXES if lead[x] == [h]]; shared = [AXIS_NAME[x] for x in AXES if h in lead[x] and len(lead[x]) > 1]
        above = sum(all(T[h]["axes"][x] > T[a]["axes"][x] for a in RIVALS) for x in AXES)
        L += [f"- Axes, {NAMES[h]}: the highest " + (and_join(alone) if alone else "score on no axis") + " of the nine arms" + (f", tied for the highest {and_join(shared)}" if shared else "") +
              f"; above every rival on {above} of 5 axes."]
    if timed:
        for h in heroes:
            fast = [NAMES[a] for a in COUNCILS if med(C[h]["min"]) < med(C[a]["min"])]; cheap = [NAMES[a] for a in COUNCILS if med(C[h]["usd"]) < med(C[a]["usd"])]
            L += [f"- Time and cost, {NAMES[h]}: median {r1(med(C[h]['min']))} min and ${r2(med(C[h]['usd']))} a question; faster than {and_join(fast) if fast else 'no rival council'}, cheaper than {and_join(cheap) if cheap else 'no rival council'}."]
    sds = [R[q]["_sd"][a] for q in R for a in ARMS]; L += ["", f"Judge agreement: mean SD of the three judges' totals {r2(st.mean(sds))}."]
    return L

def report(): print("\n".join(lines("results")))
def readme(view): print("\n".join(lines(view)))
def results():
    R = load(); todo = [q for q in QIDS if q not in R]
    L = ["# Head-to-head round 5 results", ""] + ([(IN_PROGRESS if STATUS == "in progress" else STOPPED).format(n=len(R), total=len(QIDS), todo=", ".join(q for q in RUN_ORDER if q in todo)), ""] if todo else [])
    L += ["Eight questions written for this round by an author that knew nothing about the arms ([`PREREG-5.md`](PREREG-5.md), [`questions-r5.yaml`](questions-r5.yaml)); nine arms, every answer new; three blind Opus judges per question with sealed orders ([`blinding5.yaml`](blinding5.yaml)) and round 4's error-first judge prompt for nine answers ([`judge-prompt-r5.txt`](judge-prompt-r5.txt)). "
          "Minutes are the orchestrator's first-to-last transcript timestamp; calls are its subagent spawns; USD prices every token the run used — the orchestrator's and every agent spawned under it, input, output, cache reads and cache writes — at 2026-07 list rates. No council can be faster or cheaper than the plain answer; the pre-registered time and cost comparisons are against the rival councils.", ""] + lines("results")
    L += ["", "## Per question (mean of three judges, total /25)", "", "| question | " + " | ".join(NAMES[a] for a in ARMS) + " |", "|---|" + "--:|" * len(ARMS)] + [f"| {q} ({QS[q]['domain']}, {QS[q]['shape']}) | " + " | ".join(r2(R[q][a]["composite"]) for a in ARMS) + " |" for q in QIDS if q in R]
    notes = [f"- {q}, {NAMES[a]}: {l[8:]}" for q in QIDS for a in ARMS if os.path.exists(os.path.join(H, "raw", q, a + ".md")) for l in open(os.path.join(H, "raw", q, a + ".md")).read().split("\n\n", 1)[0].splitlines() if l.startswith("# note: ")]
    L += ["", "## Deviations and disclosures", ""] + DISCLOSURES + notes + ["", "## Reproduce", "",
          "`python3 eval-data/head-to-head/h2h5.py report` prints the table and comparisons; `results` rewrites this file; `verify` rebuilds every blinded packet from the raw answers and re-parses every judgment. "
          "Time and cost were computed from local agent transcripts when each answer was saved and are stored in the raw file headers; the transcripts themselves are not in the repository.", ""]
    out = "\n".join(L)
    if os.environ.get("H2H5_STDOUT"): sys.stdout.write(out); return
    open(os.path.join(H, "RESULTS-V5.md"), "w").write(out); print("wrote RESULTS-V5.md:", len(R), "questions")
def verify():
    """The judges saw exactly the normalized raw answers, and parsed-v5/ holds exactly what the judgments say."""
    packets = parsed = 0
    for q in QIDS:
        if not os.path.exists(os.path.join(H, "parsed-v5", q + ".yaml")): continue
        for j in JUDGES:
            assert open(os.path.join(H, "blinded-v5", f"{q}-{j}.md")).read() == packet(q, j), ("blinded packet differs from a rebuild", q, j); packets += 1
        assert yaml.safe_load(open(os.path.join(H, "parsed-v5", q + ".yaml")))["judges"] == {j: judged(q, j) for j in JUDGES}, ("parsed scores differ from the judgments", q); parsed += 1
    print(f"verify: {packets} blinded packets rebuilt byte-identical from raw/, {parsed} parsed files match their judgments")

if __name__ == "__main__":
    {"seal": seal, "save": save, "savejudge": savejudge, "blind": blind, "parse": parse, "report": report, "results": results, "readme": readme, "verify": verify}[sys.argv[1]](*sys.argv[2:])
