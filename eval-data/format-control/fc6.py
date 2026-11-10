#!/usr/bin/env python3
"""Round 6 (PREREG-6.md): a format-matched control for round 5's plain answer, at two lengths (Part A), and wise-men-flash's
one fresh checker on and off (Part B). Claude models only. No judge runs before every rewrite, audit, draft, run and packet is committed.
  seal | rewrite-prompt Q | save-control T Q | check Q | audit-prompt Q [copy-dir] | save-audit T Q | extract | save-run T Q | blind
  savejudge T part Q j | parse | classify-input | report | results | verify
  helpers: run-prompt Q skills-dir scratch-dir (prints round 5's flash arm prompt) | save-classify T n | spotcheck (writes SPOTCHECK.md)
T is an agent transcript: the path of its .jsonl, or the agent id (looked up under ~/.claude/projects/). part is M, P, S, B1 or B2.
normalize(), score_blocks(), boot(), rows_of(), run_cost() and final_text() are imported unchanged from ../head-to-head/h2h5.py.
No local path enters a repository file: headers record session and agent ids and SHA-256 hashes only."""
import os, re, sys, glob, json, math, random, hashlib, statistics as st, yaml

H = os.path.dirname(os.path.abspath(__file__)); EV = os.path.dirname(H)
HH = os.path.join(EV, "head-to-head"); CC = os.path.join(EV, "consistency-check")
sys.path.insert(0, HH)
import h2h5  # noqa: E402  (the round-5 questions, and its helpers, unchanged)
from h2h5 import normalize, score_blocks, boot, rows_of, run_cost, final_text  # noqa: E402

QS, QIDS, AXES = h2h5.QS, h2h5.QIDS, h2h5.AXES
SEED = 20261104; PREREG_COMMIT = "f7bba85"; ROUND = "round 6, PREREG-6 rules"
FL, WM, PL, PM, PS = "wise-men-flash", "wise-men-3.14", "direct", "plain-memo", "plain-memo-short"
CONTROLS = [PM, PS]; TYPES = {"M": PM, "P": PL, "S": PS}; PARTS = ["M", "P", "S", "B1", "B2"]
NAMES = {FL: "flash 0.1.0", WM: "wise-men 3.14.0", PL: "plain answer", PM: "plain-memo", PS: "plain-memo-short", "draft": "draft", "shipped": "shipped memo"}
FLASH_WORDS = {"R501": 1717, "R502": 1430, "R503": 1617, "R504": 1470, "R505": 2000, "R506": 1579, "R507": 1903, "R508": 1581}  # PREREG-6; checked at seal
HEADERS = ["## Recommendation", "## Why", "## What to do", "## Risks of this plan", "## Strongest counter-position", "## Confidence"]
FIXED = {"## Risks of this plan": "No further risks are named.",
         "## Strongest counter-position": "No case against this recommendation is made beyond the risks above.",
         "## Confidence": "No unknowns are named."}
JUDGES = ["j1", "j2", "j3"]
B1Q = list(QIDS); B2Q = ["R503", "R505", "R507", "R508"]; B2_TIES = ["R501", "R502", "R504", "R506"]; NEW_RUNS = ["R501", "R503", "R505", "R507"]
VER = {"B1": "0.2.0", "B2": "0.1.0"}
AMEND2 = ["R502", "R507", "R508"]; AMEND2_COMMIT = "191188c"  # PREREG-6 Amendment 2: plain-memo's one length-only retry (attempt 3); plain-memo-short's band dropped
STORED = {  # PREREG-6 Part B: the checker agents whose first prompt holds each stored draft
    ("0.2.0", "R502"): ("9adc81fe-890f-46b2-a03e-059fac726935", "a4b33fef412b2ff86"), ("0.2.0", "R504"): ("9adc81fe-890f-46b2-a03e-059fac726935", "aaa7e67bfd9247418"),
    ("0.2.0", "R506"): ("9adc81fe-890f-46b2-a03e-059fac726935", "a40fc420212bdbc0c"), ("0.2.0", "R508"): ("9adc81fe-890f-46b2-a03e-059fac726935", "a3de0644c5ffd71eb"),
    ("0.1.0", "R501"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "a287e44b3f073d195"), ("0.1.0", "R502"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "a99a6cbca9add8005"),
    ("0.1.0", "R503"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "a9379b375d2458bd1"), ("0.1.0", "R504"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "a5dbb7d30985e9039"),
    ("0.1.0", "R505"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "aa28d20743e2bd947"), ("0.1.0", "R506"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "a815e3ce94d94c7be"),
    ("0.1.0", "R507"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "a96a0a9a730dceb32"), ("0.1.0", "R508"): ("e0ff67b0-e729-4db6-beb1-684d997142d1", "ad18fe96b0b72aba8")}
CHECKER_TESTS = ["DISSENT", "DISCLOSURE", "CLAIMS", "COVERAGE", "CONSISTENCY"]
D = {k: os.path.join(H, k) for k in ("prompts", "rewrites", "checks", "audits", "drafts", "runs", "packets", "judgments", "parsed", "classify")}
SEAL = os.path.join(H, "seal6.yaml")
FLASH_HEAD = "wise-men-flash (Ali-expandings/wise-men-flash SKILL.md v0.2.0, aaabd74, unchanged at 1d6a552)"

# --- small helpers ---
def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write(s)
def sha(s): return hashlib.sha256(s if isinstance(s, bytes) else s.encode("utf-8")).hexdigest()
def fsha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def words(t): return len(t.split())
def rel(p): return os.path.relpath(p, H)
def r1(x): return h2h5.r1(x)
def r2(x): return h2h5.r2(x)
def sg(x): return h2h5.sg(x)
def seal_map(): return yaml.safe_load(rd(SEAL))
def source(q): return normalize("direct", rd(os.path.join(HH, "raw", q, "direct.md")))
def body(p): return normalize("wise-men", rd(p))
def header_lines(p): return [l[2:] for l in rd(p).split("\n\n", 1)[0].split("\n") if l.startswith("# ")]
def hfield(p, key):
    for l in header_lines(p):
        for part in l.split(" | "):
            if part.startswith(key + ": "): return part[len(key) + 2:]
    return None
def band(arm, q):
    w = FLASH_WORDS[q] if arm == PM else words(source(q))
    return -(-9 * w // 10), 11 * w // 10, w  # +-10%, integer arithmetic

def transcript(T):
    if os.path.exists(T): return T
    f = glob.glob(os.path.join(os.path.expanduser("~/.claude/projects"), "*", "*", "subagents", f"agent-{T}.jsonl"))
    assert len(f) == 1, ("transcript not found, or not unique", T, len(f)); return f[0]
def tinfo(T):
    f = transcript(T); rows = rows_of(f); mp = f[: -len(".jsonl")] + ".meta.json"
    tools = [(c["name"], c.get("input", {})) for r in rows if r.get("type") == "assistant" for c in r["message"]["content"] if c.get("type") == "tool_use"]
    models = sorted({r["message"].get("model") for r in rows if r.get("type") == "assistant" and r["message"].get("model") not in (None, "<synthetic>")})
    ts = [r["timestamp"] for r in rows if r.get("timestamp")]
    return {"file": f, "rows": rows, "meta": json.load(open(mp)) if os.path.exists(mp) else {}, "tools": tools, "models": models, "date": ts[0][:10],
            "session": next((r["sessionId"] for r in rows if r.get("sessionId")), "?"), "agent": os.path.basename(f)[len("agent-"): -len(".jsonl")],
            "sha": fsha(f), "prompt": h2h5.first_prompt(rows)}
def cost_line(f):
    c = run_cost(f)
    return c, f"minutes: {c['minutes']:.1f} | subagent calls: {c['calls']} (transcripts matched: {c['matched']}) | tokens in/out/cache-read/cache-write: {c['in']}/{c['out']}/{c['cr']}/{c['cw']} | list-price USD: {c['usd']:.2f}"
def tree(f):
    """The transcript and every agent spawned under it at any depth, matched by the exact prompt sent (run_cost's rule)."""
    index = {}
    for g in glob.glob(os.path.join(os.path.dirname(f), "agent-*.jsonl")):
        try: index.setdefault(h2h5.first_prompt(rows_of(g))[:3000], []).append(g)
        except Exception: pass
    out, used = [], set()
    def walk(g, depth):
        out.append((g, depth))
        for r in rows_of(g):
            if r.get("type") != "assistant": continue
            for c in r["message"]["content"]:
                if c.get("type") == "tool_use" and c["name"] in ("Agent", "Task"):
                    for h in index.get((c["input"].get("prompt") or "")[:3000], []):
                        if h in used: continue
                        used.add(h); walk(h, depth + 1); break
    walk(f, 0); return out

def sections(name):
    out, cur = {}, None
    for line in rd(os.path.join(H, name)).split("\n"):
        m = re.fullmatch(r"### (.+)", line)
        if m: cur = m[1].strip(); out[cur] = []
        elif cur is not None: out[cur].append(line)
    return {k: "\n".join(v).strip("\n") for k, v in out.items()}
def fill(t, vals): return re.sub(r"\{(\w+)\}", lambda m: vals[m[1]] if m[1] in vals else m[0], t)  # one pass: inserted text is never re-scanned

# --- sentence units: every rewrite and source sentence gets a number ---
ABBR = {"vs", "e.g", "i.e", "etc", "cf", "approx", "al", "mr", "mrs", "ms", "dr", "st", "no", "inc", "ltd", "jr", "sr", "fig", "u.s", "u.k"}
LIST = re.compile(r"^(\s*(?:[-*+]|\d+[.)])\s+)")
RULE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
TSEP = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{0,}:?\s*\|?\s*$")
def split_sentences(text):
    masked = re.sub(r"`[^`]*`", lambda m: "x" * len(m[0]), text)  # never split inside inline code
    cuts = [0]
    for m in re.finditer(r"[.!?…][)\]\"'”’*_]*(\s+)(?=[A-Z0-9\"“‘'(\[*$_])", masked):
        if masked[m.start()] == ".":
            tok = re.search(r"(\S+)$", masked[: m.start()])
            if tok and tok[1].lower().lstrip("(\"'“‘*_").rstrip(".") in ABBR: continue
        cuts.append(m.end())
    cuts.append(len(text))
    return [text[a:b].strip() for a, b in zip(cuts, cuts[1:]) if text[a:b].strip()]
def units(text):
    """One unit per line: blank, heading ('#'), rule or table separator, or a block (paragraph, list item, table row) split into sentences."""
    out = []
    for line in text.split("\n"):
        if not line.strip(): out.append({"kind": "blank", "line": line})
        elif re.match(r"^#{1,6}\s", line): out.append({"kind": "head", "line": line})
        elif RULE.match(line) or TSEP.match(line): out.append({"kind": "rule", "line": line})
        else:
            m = LIST.match(line); pre = m[1] if m else ""
            out.append({"kind": "block", "line": line, "pre": pre, "sents": split_sentences(line[len(pre):])})
    return out
def sentences(text): return [s for u in units(text) if u["kind"] == "block" for s in u["sents"]]
def numbered(text, letter):
    k, L = 0, []
    for u in units(text):
        if u["kind"] == "blank":
            if L and L[-1] != "": L.append("")
        elif u["kind"] in ("head", "rule"): L.append(u["line"])
        else:
            for i, s in enumerate(u["sents"]):
                k += 1; L.append(f"[{letter}{k}] " + (u["pre"].strip() + " " if i == 0 and u["pre"] else "") + s)
    return "\n".join(L).strip(), k
def section_of(text):
    """For each rewrite sentence number, the header of the section it sits in."""
    cur, out = None, {}
    k = 0
    for u in units(text):
        if u["kind"] == "head": cur = u["line"].strip()
        elif u["kind"] == "block":
            for _ in u["sents"]: k += 1; out[k] = cur
    return out

# --- Part A: the script checks ---
NUM = re.compile(r"(?<![\w.])(\$?)(\d+(?:,\d{3})*(?:\.\d+)?)(%?)")
RANGE = re.compile(r"(?<![\w.])(\$?)(\d+(?:,\d{3})*(?:\.\d+)?)(%?)\s*(?:–|—|-|to)\s*(\$?)(\d+(?:,\d{3})*(?:\.\d+)?)(%?)")
URL = re.compile(r"https?://[^\s)\]>]+|www\.[^\s)\]>]+|\b[\w-]+(?:\.[\w-]+)*\.(?:com|org|net|io|gov|edu|ai|dev)\b(?:/[^\s)\]>]*)?")
CITE = re.compile(r"\(\s*(?:19|20)\d{2}\b[^)]*\)|\bet al\b\.?|\[\d+\]|\bdoi:\s*\S+", re.I)
def nolist(t): return "\n".join(LIST.sub("", l, count=1) for l in t.split("\n"))
def numtokens(t):
    t = nolist(t); vals, dol, pct = set(), set(), set()
    for m in NUM.finditer(t):
        v = m[2].replace(",", ""); vals.add(v)
        if m[1]: dol.add(v)
        if m[3]: pct.add(v)
    for m in RANGE.finditer(t):  # "30–45%" or "$3–5k": the sign of one end covers both
        a, b = m[2].replace(",", ""), m[5].replace(",", "")
        if m[1] or m[4]: dol.update((a, b))
        if m[3] or m[6]: pct.update((a, b))
    return vals, dol, pct
def numbers_not_in(t, src):
    sv, sd, sp = numtokens(src); bad = []
    for m in NUM.finditer(nolist(t)):
        v = m[2].replace(",", "")
        if v not in sv or (m[1] and v not in sd) or (m[3] and v not in sp): bad.append(m[0])
    return sorted(set(bad), key=bad.index)
def strip_header(raw):
    lines = raw.split("\n")
    while lines and (lines[0].startswith("# ") or lines[0].strip() == ""): lines.pop(0)
    return "\n".join(lines).strip()
def script_check(q, arm, raw):
    text = normalize("wise-men", raw); src = source(q); lo, hi, _ = band(arm, q); L = text.split("\n"); res = []
    heads = [l.strip() for l in L if re.match(r"^#{1,6}\s", l)]; first = next((l for l in L if l.strip()), ""); rules = [l for l in L if RULE.match(l)]
    ok = heads == HEADERS and first.strip() == HEADERS[0] and not rules
    res.append(("headers", ok, "the six headers in order, nothing before the first, no other heading, no rule" if ok else f"headings {heads}; first line {first[:60]!r}; rules {len(rules)}"))
    w = words(text); res.append(("words", lo <= w <= hi, f"{w:,} words; band {lo:,}–{hi:,}"))
    bad = numbers_not_in(text, src); res.append(("numbers", not bad, "every number appears in the source" if not bad else "not in the source: " + ", ".join(bad)))
    urls = [u.rstrip(".,;:") for u in URL.findall(text)]; badu = [u for u in urls if u not in src]
    res.append(("links", not badu, "no link the source lacks" if not badu else "links not in the source: " + ", ".join(badu)))
    flat = " ".join(src.split()); badc = [c for c in CITE.findall(text) if " ".join(c.split()) not in flat]
    res.append(("citations", not badc, "no citation the source lacks" if not badc else "citations not in the source: " + ", ".join(badc)))
    nu, ns = len(re.findall(r"\(unverified", text, re.I)), len(re.findall(r"\(unverified", src, re.I))
    res.append(("unverified-tag", nu == 0 or ns > 0, f"{nu} '(unverified' tag(s); the source has {ns}"))
    res.append(("first-name", not re.search(r"\bAli\b", text), "the author's first name is absent" if not re.search(r"\bAli\b", text) else "the author's first name appears"))
    res.append(("normalize", text == strip_header(raw), "normalize() removes nothing but the provenance header" if text == strip_header(raw) else "normalize() removes more than the header"))
    return res
def check_text(res): return "\n".join(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}" for name, ok, detail in res) + "\n"
def check_ok(res): return all(ok for _, ok, _ in res)
def retried(q): return q in AMEND2 and audit_of(q, PM, 3) is not None
def gating_fails(q, arm, res):
    """The failed script checks that keep a final rewrite out of the packets. Amendment 2: plain-memo-short's band is dropped, and a
    plain-memo final still outside its band once its length-only retry has been audited is judged as it is."""
    return [name for name, ok, _ in res if not ok and not (name == "words" and (arm == PS or (arm == PM and retried(q))))]

# --- Part A: files ---
def f_prompt(q, arm, kind, n): return os.path.join(D["prompts"], f"{q}-{arm}-{kind}-{n}.txt")
def f_rewrite(q, arm, n=None): return os.path.join(D["rewrites"], f"{q}-{arm}" + (f"-{n}" if n else "") + ".md")
def f_check(q, arm, n): return os.path.join(D["checks"], f"{q}-{arm}-{n}.txt")
def f_audit(q, arm, n, ext): return os.path.join(D["audits"], f"{q}-{arm}-{n}.{ext}")
def audit_of(q, arm, n):
    p = f_audit(q, arm, n, "yaml"); return yaml.safe_load(rd(p)) if os.path.exists(p) else None
def attempt_state(q, arm, n):
    """None (not run), 'unaudited', 'pass' or 'fail' for one rewrite attempt."""
    if not os.path.exists(f_rewrite(q, arm, n)): return None
    a = audit_of(q, arm, n)
    if a is None: return "unaudited"
    return "pass" if a["pass"] and check_ok(script_check(q, arm, rd(f_rewrite(q, arm, n)))) else "fail"

def problems(q, arm, n):
    """The audit's list (and the script checks' failures) sent to the one retry."""
    L = [f"- Script check failed: {name}: {detail}." for name, ok, detail in script_check(q, arm, rd(f_rewrite(q, arm, n))) if not ok and name != "normalize"]
    a = audit_of(q, arm, n); src = sentences(source(q))
    for x in a["flagged"]:
        if x["label"] == "NEW": L.append(f'- This sentence adds something the source does not state ({x["note"]}): "{x["text"]}"')
        else:
            what = "more" if x["label"] == "STRONGER" else "less"
            L.append(f'- This sentence states a claim with {what} certainty than the source ({x["note"]}): "{x["text"]}" (source: ' + " ".join(f'"{src[s - 1]}"' for s in x["refs"]) + ")")
    for d in a["dropped"]: L.append(f'- This source sentence is not carried into the memo: "{d["text"]}"')
    return "\n".join(L) if L else "- none listed"
def rewrite_prompt_text(q, arm, n):
    S = sections("rewrite-prompt.txt"); lo, hi, target = band(arm, q); src = source(q)
    length = fill(S["LENGTH " + arm], {"lo": f"{lo:,}", "hi": f"{hi:,}", "target": f"{target:,}", "src": f"{words(src):,}"})
    retry = "" if n == 1 else "\n" + fill(S["RETRY"], {"problems": problems(q, arm, 1), "previous": body(f_rewrite(q, arm, 1))}).strip() + "\n"
    return fill(S["TEMPLATE"], {"question": QS[q]["text"], "source": src, "length_rule": length, "retry": retry})
def rewrite_prompt(q):
    """Write the prompt each arm needs next: attempt 1, or the one retry after a failed first attempt."""
    for arm in CONTROLS:
        s1, s2 = attempt_state(q, arm, 1), attempt_state(q, arm, 2)
        n = 1 if s1 is None else 2 if s1 == "fail" and s2 is None else None
        if n is None: print(q, arm, "nothing to send:", f"attempt 1 {s1}, attempt 2 {s2}"); continue
        p = f_prompt(q, arm, "rewrite", n); t = rewrite_prompt_text(q, arm, n)
        if os.path.exists(p): assert rd(p) == t, ("a stored prompt differs from a rebuild", p)
        else: wr(p, t)
        print(q, arm, f"attempt {n}:", rel(p), f"({words(t)} words; send verbatim to a fresh wise-men-flash:wise-member on sonnet)")

def length_retry(q):
    """Amendment 2: plain-memo's one length-only retry, for R502, R507 and R508 only: attempt 2's prompt, byte for byte, plus the target."""
    assert q in AMEND2, ("Amendment 2 allows the length-only retry only for", AMEND2)
    assert attempt_state(q, PM, 1) == "fail" and attempt_state(q, PM, 2) in ("pass", "fail"), (q, "attempt 2 must be saved and audited first")
    lo, hi, target = band(PM, q); w = words(body(f_rewrite(q, PM, 2)))
    t = rd(f_prompt(q, PM, "rewrite", 2)) + "\n\n" + fill(sections("rewrite-prompt.txt")["LENGTH RETRY"], {"w": f"{w:,}", "side": "under" if w < lo else "over", "lo": f"{lo:,}", "hi": f"{hi:,}", "target": f"{target:,}"})
    p = f_prompt(q, PM, "rewrite", 3)
    if os.path.exists(p): assert rd(p) == t, ("a stored prompt differs from a rebuild", p); return t
    assert not (lo <= w <= hi), (q, "attempt 2 is inside its band: Amendment 2 retries only rewrites outside it")
    assert [nm for nm, ok, _ in script_check(q, PM, rd(f_rewrite(q, PM))) if not ok] == ["words"], (q, "Amendment 2's retry is for a final that fails its band and nothing else")
    wr(p, t); print(q, PM, "attempt 3 (Amendment 2, length only):", rel(p), f"({words(t)} words; send verbatim to a fresh wise-men-flash:wise-member on sonnet)"); return t
def save_control(T, q):
    i = tinfo(T); got = i["prompt"]
    hits = [(arm, n) for arm in CONTROLS for n in (1, 2, 3) if os.path.exists(f_prompt(q, arm, "rewrite", n)) and rd(f_prompt(q, arm, "rewrite", n)).strip() == got.strip()]
    assert len(hits) == 1, ("the transcript's prompt matches no stored rewrite prompt for", q, "exactly"); arm, n = hits[0]
    assert not os.path.exists(f_rewrite(q, arm, n)), ("already saved", rel(f_rewrite(q, arm, n)))
    tools = ", ".join(f"{a} {json.dumps(b)[:80]}" for a, b in i["tools"]) or "none"
    txt = final_text(i["rows"]); c, cl = cost_line(i["file"])
    head = (f"# arm: {arm} (round 5's plain answer rewritten into flash's memo format, no new analysis; PREREG-6 Part A) | question: {q} | attempt: {n} | run: {i['date']} ({ROUND})\n"
            f"# rewriter: fresh {i['meta'].get('agentType', '?')}/{i['meta'].get('model', '?')} = {', '.join(i['models'])} | tools used: {tools} | prompt: {rel(f_prompt(q, arm, 'rewrite', n))} (sha256 {sha(rd(f_prompt(q, arm, 'rewrite', n)))[:16]})\n"
            f"# session: {i['session']} | agent: {i['agent']} | transcript sha256: {i['sha']}\n# {cl}\n")
    wr(f_rewrite(q, arm, n), head + "\n" + txt + "\n")
    print("saved", rel(f_rewrite(q, arm, n)), words(normalize("wise-men", txt)), "words |", "tools:", tools, "| models:", i["models"])
    if i["tools"]: print("WARNING: the rewriter used a tool; it was told to use none")

def check(q):
    for arm in CONTROLS:
        for n in (1, 2, 3, "final"):
            p = f_rewrite(q, arm, None if n == "final" else n)
            if not os.path.exists(p): continue
            res = script_check(q, arm, rd(p)); wr(f_check(q, arm, n), f"# script checks (fc6.py check, PREREG-6 Part A rule 1) | {rel(p)} | question: {q} | arm: {arm}\n\n" + check_text(res))
            print(q, arm, n, "PASS" if check_ok(res) else "FAIL", "|", "; ".join(f"{a}: {c}" for a, ok, c in res if not ok) or "all checks pass")

def audit_packet(q, arm, n):
    S = sections("audit-prompt.txt"); src_n, _ = numbered(source(q), "S"); rw_n, nR = numbered(body(f_rewrite(q, arm, n)), "R")
    return fill(S["PACKET"], {"n": str(nR), "question": QS[q]["text"], "source": src_n, "rewrite": rw_n}) + "\n"
def audit_prompt(q, copy_dir=None):
    for arm in CONTROLS:
        for n in (1, 2, 3):
            if not os.path.exists(f_rewrite(q, arm, n)) or audit_of(q, arm, n) is not None: continue
            p = f_prompt(q, arm, "audit", n); t = audit_packet(q, arm, n)
            if os.path.exists(p): assert rd(p) == t, ("a stored audit prompt differs from a rebuild", p)
            else: wr(p, t)
            path = p
            if copy_dir:  # a neutral name, so the auditor's path says nothing about the arm
                os.makedirs(copy_dir, exist_ok=True); path = os.path.join(copy_dir, sha(t)[:12] + ".txt"); wr(path, t)
            print(q, arm, f"attempt {n}:", rel(p), "\n  spawn (fresh wise-member on opus):", fill(sections("audit-prompt.txt")["SPAWN"], {"path": path}))

AREF = r"S\d+(?:\s*[-–]\s*S?\d+)?"; AREFS = rf"{AREF}(?:\s*(?:,|and|&)\s*{AREF})*"
def arefs(s, nS):
    out = []
    for a, b in re.findall(r"S(\d+)(?:\s*[-–]\s*S?(\d+))?", s):
        out += list(range(int(a), int(b) + 1)) if b else [int(a)]
    assert out and all(1 <= x <= nS for x in out), ("source sentence number out of range", s); return sorted(set(out))
def is_fixed(s):
    """A fixed sentence, word for word, allowing quotes, list markers and a short label before it ("Unknowns: No unknowns are named.")."""
    s = re.sub(r"^[-*+]\s+", "", s.strip()).strip('"*_ ')
    return any(s == f or re.fullmatch(r"[\w ]{1,30}:\s*" + re.escape(f), s) for f in FIXED.values())
def parse_audit(text, rw_sents, nS):
    blocks = re.findall(r"```audit\s*\n(.*?)```", text, re.S); nR = len(rw_sents)
    lines = blocks[0].splitlines() if len(blocks) == 1 else [l for l in text.splitlines() if re.match(r"^\s*R\d+:", l)]
    m = {}
    for line in (l.strip().strip("`") for l in lines if l.strip()):
        x = re.fullmatch(r"R(\d+):\s*(.+)", line); assert x, ("unparseable audit line", line)
        k, b = int(x[1]), x[2].strip().replace("**", ""); assert 1 <= k <= nR and k not in m, ("rewrite sentence number", k)
        y = re.fullmatch(rf"({AREFS})(?:\s*[—–-]+\s*(.*))?", b)
        if y: m[k] = {"label": "RESTATES", "refs": arefs(y[1], nS), "note": (y[2] or "").strip()}; continue
        y = re.fullmatch(r"(CONNECTIVE|FIXED)(?:\s*[—–-]+\s*(.*))?", b)
        if y:
            if y[1] == "FIXED": assert is_fixed(rw_sents[k - 1]), ("FIXED on a sentence that is not a fixed sentence", k)
            m[k] = {"label": y[1], "refs": [], "note": (y[2] or "").strip()}; continue
        y = re.fullmatch(r"(NEW|STRONGER|WEAKER)\s*[—–:-]+\s*(.+)", b, re.S); assert y, ("unknown audit label", line)
        z = re.match(rf"({AREFS})\s*(?:[—–-]+\s*(.*))?$", y[2], re.S)
        if z: m[k] = {"label": y[1], "refs": arefs(z[1], nS), "note": (z[2] or "").strip()}
        else:
            assert y[1] == "NEW", ("STRONGER/WEAKER must name the source sentence", line); m[k] = {"label": "NEW", "refs": [], "note": y[2].strip()}
    assert set(m) == set(range(1, nR + 1)), ("audit misses rewrite sentences", sorted(set(range(1, nR + 1)) - set(m))[:10]); return m
def audit_summary(m, rw_sents, src_sents, keep=None):
    """DROPPED: every source sentence that no (kept) rewrite sentence cites."""
    keep = set(m) if keep is None else keep; cited = set(s for k in keep for s in m[k]["refs"])
    dropped = [{"S": s, "text": src_sents[s - 1]} for s in range(1, len(src_sents) + 1) if s not in cited]
    flagged = [{"R": k, "label": m[k]["label"], "refs": m[k]["refs"], "note": m[k]["note"], "text": rw_sents[k - 1]} for k in sorted(keep) if m[k]["label"] in ("NEW", "STRONGER", "WEAKER")]
    reuse = [sum(1 for k in keep if m[k]["label"] == "RESTATES" and s in m[k]["refs"]) for s in range(1, len(src_sents) + 1)]
    counts = {x: sum(1 for f in flagged if f["label"] == x) for x in ("NEW", "STRONGER", "WEAKER")}; counts["DROPPED"] = len(dropped)
    return {"counts": counts, "pass": not any(counts.values()), "flagged": flagged, "dropped": dropped,
            "reuse": {"source_sentences": len(src_sents), "cited_once_or_more": sum(1 for r in reuse if r), "cited_twice_or_more": sum(1 for r in reuse if r >= 2),
                      "max": max(reuse) if reuse else 0, "mean": round(st.mean(reuse), 2) if reuse else 0},
            "labels": {x: sum(1 for k in keep if m[k]["label"] == x) for x in ("RESTATES", "CONNECTIVE", "FIXED", "NEW", "STRONGER", "WEAKER")}}
def save_audit(T, q):
    i = tinfo(T); reads = [x.get("file_path", "") for nm, x in i["tools"] if nm == "Read"]; others = [nm for nm, _ in i["tools"] if nm != "Read"]
    hits = [(arm, n) for arm in CONTROLS for n in (1, 2, 3) if os.path.exists(f_prompt(q, arm, "audit", n))
            and reads and all(os.path.basename(r) in (sha(rd(f_prompt(q, arm, "audit", n)))[:12] + ".txt", os.path.basename(f_prompt(q, arm, "audit", n))) for r in reads)]
    assert len(hits) == 1, ("the auditor's Read matches no stored audit prompt for", q, reads); arm, n = hits[0]; p = f_prompt(q, arm, "audit", n)
    for r in reads:
        if os.path.exists(r): assert fsha(r) == sha(rd(p)), ("the file the auditor read differs from the stored audit prompt", r)
    txt = final_text(i["rows"]); rw_s = sentences(body(f_rewrite(q, arm, n))); src_s = sentences(source(q)); c, cl = cost_line(i["file"])
    head = (f"# audit: {arm} attempt {n} | question: {q} | auditor: fresh {i['meta'].get('agentType', '?')}/{i['meta'].get('model', '?')} = {', '.join(i['models'])} | run: {i['date']} ({ROUND})\n"
            f"# input: {rel(p)} (sha256 {sha(rd(p))[:16]}), read under a neutral file name | tools used: Read x{len(reads)}" + (f", others: {others}" if others else "") + "\n"
            f"# session: {i['session']} | agent: {i['agent']} | transcript sha256: {i['sha']}\n# {cl}\n")
    err = None
    try:
        assert not others, ("the auditor used a tool other than Read", others)
        m = parse_audit(txt, rw_s, len(src_s))
    except AssertionError as e: err = str(e)
    if err:
        k = 1 + len(glob.glob(f_audit(q, arm, n, "invalid-*.md")))
        wr(f_audit(q, arm, n, f"invalid-{k}.md"), head + f"# invalid: {err}\n\n" + txt + "\n"); print("INVALID audit", q, arm, n, err, "-> re-run once with a fresh auditor"); return
    wr(f_audit(q, arm, n, "md"), head + "\n" + txt + "\n")
    s = audit_summary(m, rw_s, src_s); chk = script_check(q, arm, rd(f_rewrite(q, arm, n)))
    out = {"question": q, "arm": arm, "attempt": n, "rewrite_sentences": len(rw_s), "source_sentences": len(src_s), **s,
           "script_checks_pass": check_ok(chk), "map": {f"R{k}": (m[k]["label"] if m[k]["label"] != "RESTATES" else ", ".join(f"S{x}" for x in m[k]["refs"])) + (f" — {', '.join('S' + str(x) for x in m[k]['refs'])}" if m[k]["label"] in ("NEW", "STRONGER", "WEAKER") and m[k]["refs"] else "") for k in sorted(m)}}
    wr(f_audit(q, arm, n, "yaml"), yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=200))
    print("audit", q, arm, n, s["counts"], "| script checks", "pass" if check_ok(chk) else "FAIL", "| attempt", "PASSES" if s["pass"] and check_ok(chk) else "fails")
    finalize(q, arm)

def _build(q, arm, n):
    """One audited attempt as it would enter the packets: if it does not pass outright, every sentence its audit marks NEW, STRONGER
    or WEAKER deleted (a section left empty gets its fixed sentence), and the source sentences then cited nowhere recomputed."""
    raw = rd(f_rewrite(q, arm, n)); text = normalize("wise-men", raw); a = audit_of(q, arm, n)
    kill = set() if attempt_state(q, arm, n) == "pass" else {f["R"] for f in a["flagged"]}
    out, k, inserted = [], 0, []
    for u in units(text):
        if u["kind"] != "block": out.append(u["line"]); continue
        keep = []
        for s in u["sents"]:
            k += 1
            if k not in kill: keep.append(s)
        if len(keep) == len(u["sents"]): out.append(u["line"])
        elif keep: out.append(u["pre"] + " ".join(keep))
    secs, cur = {}, None
    for l in out:
        if l.strip() in HEADERS: cur = l.strip(); secs[cur] = []
        elif cur and l.strip(): secs[cur].append(l)
    final = []
    for h in HEADERS:
        if not secs.get(h):
            assert h in FIXED, ("deletion emptied a section that has no fixed sentence", q, arm, h)
            secs[h] = [FIXED[h]]; inserted.append(h)
    if kill:  # rebuild with single blank lines between blocks
        lines = []
        for h in HEADERS: lines += [h, ""] + [x for b in secs[h] for x in (b, "")]
        final = "\n".join(l for l in lines).strip()
        final = re.sub(r"\n{3,}", "\n\n", final)
    else: final = text
    src_s = sentences(source(q)); rw_s = sentences(text)
    m = {int(r[1:]): None for r in a["map"]}
    keep = set(m) - kill
    refs = {}
    for r, v in a["map"].items():
        lab = v.split(" — ")[0]
        refs[int(r[1:])] = {"label": "RESTATES" if lab.startswith("S") else lab, "refs": [int(x) for x in re.findall(r"S(\d+)", v)], "note": ""}
    after = audit_summary(refs, rw_s, src_s, keep)
    hdr = header_lines(f_rewrite(q, arm, n))
    fails = [nm for nm, ok, _ in script_check(q, arm, "".join(f"# {l}\n" for l in hdr) + "\n" + final + "\n") if not ok]
    info = {"question": q, "arm": arm, "from_attempt": n, "deleted": [f for f in a["flagged"] if f["R"] in kill], "inserted_fixed_sentence_in": inserted,
            "dropped": after["dropped"], "counts_after": after["counts"], "reuse": after["reuse"], "words": words(final)}
    return {"final": final, "info": info, "kill": kill, "inserted": inserted, "after": after, "hdr": hdr, "fails": fails}
def final_build(q, arm):
    """The rewrite that enters the packets: the first passing attempt; otherwise attempt 2 with every sentence still marked NEW,
    STRONGER or WEAKER deleted (a section left empty gets its fixed sentence) and the source sentences then cited nowhere disclosed.
    Amendment 2 (2026-11-10): for plain-memo R502, R507 and R508, the one length-only retry (attempt 3), under the same deletion rule,
    replaces that rewrite if it is then clean (no source sentence left uncited) and passes every script check, its band included;
    otherwise the earlier rewrite is judged as it is. plain-memo-short's band is dropped, so its finals are judged as they are."""
    s1, s2 = attempt_state(q, arm, 1), attempt_state(q, arm, 2)
    if s1 == "pass": n = 1
    elif s1 == "fail" and s2 in ("pass", "fail"): n = 2
    else: return None
    b = _build(q, arm, n); why3 = None; r3 = None
    if arm == PM and q in AMEND2 and attempt_state(q, arm, 3) in ("pass", "fail"):
        b3 = _build(q, arm, 3)
        r3 = {"words": b3["info"]["words"], "deleted": [dict(x) for x in b3["info"]["deleted"]], "dropped": [dict(x) for x in b3["info"]["dropped"]], "script_check_failures": list(b3["fails"]), "used": not b3["info"]["dropped"] and not b3["fails"]}
        if r3["used"]: b, n = b3, 3
        else: why3 = " and ".join(x for x in (f"failed the script check(s) {', '.join(b3['fails'])}" + (f" at {b3['info']['words']:,} words" if "words" in b3["fails"] else "") if b3["fails"] else "",
                                               f"left {len(b3['info']['dropped'])} source sentence(s) cited nowhere" if b3["info"]["dropped"] else "") if x)
    final, info, kill, inserted, after, hdr, fails = (b[k] for k in ("final", "info", "kill", "inserted", "after", "hdr", "fails"))
    lo, hi, _ = band(arm, q); w = info["words"]; a2 = ", Amendment 2's length-only retry," if n == 3 else ""
    if not kill: note = f"final: attempt {n}{a2[:-1] if a2 else ''}, which passed the script checks and the audit" if not fails else f"final: attempt {n}; it passed the audit"
    else: note = (f"final: attempt {n}{a2} with {len(kill)} sentence(s) deleted under PREREG-6 Part A rule 3 ({', '.join(f'R{x}' for x in sorted(kill))})"
                  + (f"; fixed sentence inserted in {', '.join(inserted)}" if inserted else "") + f"; {after['counts']['DROPPED']} source sentence(s) cited nowhere, disclosed in {rel(f_audit(q, arm, 'final', 'yaml'))}")
    if fails == ["words"] and arm == PS:
        note += f"{' and every other script check' if not kill else ''}; at {w:,} words it is outside its band ({lo:,}–{hi:,}), which Amendment 2 (2026-11-10) drops for plain-memo-short, so it is judged as it is"
    elif fails == ["words"] and arm == PM and why3:
        note += f"{' and every other script check' if not kill else ''}; at {w:,} words it is outside its band ({lo:,}–{hi:,}), and Amendment 2's length-only retry (attempt 3) {why3}, so this rewrite is judged as it is, its word count disclosed"
    elif fails: note += f"{' but' if not kill else '; it'} still fails the script check(s) {', '.join(fails)} after the one retry, which PREREG-6 gives no rule for (see DEVIATIONS.md)"
    raw_final = "".join(f"# {l}\n" for l in hdr) + f"# {note}\n\n" + final + "\n"
    if r3: info["amendment_2_retry"] = r3
    return raw_final, info
def finalize(q, arm):
    b = final_build(q, arm)
    if b is None:
        st1 = attempt_state(q, arm, 1)
        if st1 == "fail": print(q, arm, "attempt 1 fails: the one retry is next (fc6.py rewrite-prompt", q + ")")
        return
    raw_final, info = b; wr(f_rewrite(q, arm), raw_final)
    wr(f_audit(q, arm, "final", "yaml"), yaml.safe_dump(info, sort_keys=False, allow_unicode=True, width=200))
    res = script_check(q, arm, raw_final); wr(f_check(q, arm, "final"), f"# script checks (fc6.py check, PREREG-6 Part A rule 1) | {rel(f_rewrite(q, arm))} | question: {q} | arm: {arm}\n\n" + check_text(res))
    print("final", q, arm, "from attempt", info["from_attempt"], "| deleted", len(info["deleted"]), "| dropped", len(info["dropped"]), "| script checks", "pass" if check_ok(res) else "FAIL")

# --- Part B: drafts and new runs ---
def draft_of(prompt):
    """The memo inside a checker's prompt: from '## Recommendation' to the end of its '## Confidence' section, i.e. to the close of the
    block that holds it (the <draft> block in 0.2.0; in 0.1.0 the triple-quoted block, or, where the Chairman did not quote it, up to
    the check instructions)."""
    L = prompt.split("\n"); i = next(k for k, l in enumerate(L) if l.startswith("## Recommendation"))
    j = next(k for k in range(i + 1, len(L)) if L[k].strip() == "## Confidence")
    op = next((L[k].strip() for k in range(i - 1, -1, -1) if L[k].strip()), "")
    cl = {'"""': '"""', "<draft>": "</draft>"}.get(op)
    if cl: k = next(k for k in range(j + 1, len(L)) if L[k].strip() == cl); how = f"the {op} block"
    else: k = next(k for k in range(j + 1, len(L)) if re.match(r"^Run .*checks?", L[k])); how = f"unquoted, after the line {op!r}, up to the check instructions"
    return "\n".join(L[i:k]).strip(), how, L[i - 1].strip() if L[i - 1].strip() else L[i - 2].strip()
def verdict(rows):
    t = final_text(rows); v = {}
    for k in CHECKER_TESTS:
        m = re.search(rf"{k}\**\s*:\s*\**\s*(PASS|FAIL)", t)
        if m: v[k] = m[1]
    return v
def shipped_file(q, ver):
    if ver == "0.1.0": return os.path.join(HH, "raw", q, "wise-men-flash.md")
    return os.path.join(CC, "answers", f"{q}-new.md") if ("0.2.0", q) in STORED else os.path.join(D["runs"], f"{q}-flash-0.2.0.md")
def f_draft(q, ver): return os.path.join(D["drafts"], f"{q}-{ver}.md")
def is_checker(p): return "## Recommendation" in p and all(k in p for k in CHECKER_TESTS[:4])  # 0.1.0 ran four checks, 0.2.0 five
def first_checker(orch_file):
    """The first checker call an orchestrator made, and the agent transcript it started."""
    calls = [c["input"].get("prompt") or "" for r in rows_of(orch_file) if r.get("type") == "assistant" for c in r["message"]["content"]
             if c.get("type") == "tool_use" and c["name"] in ("Agent", "Task") and is_checker(c["input"].get("prompt") or "")]
    if not calls: return None, 0
    for g in sorted(glob.glob(os.path.join(os.path.dirname(orch_file), "agent-*.jsonl"))):
        if h2h5.first_prompt(rows_of(g))[:3000] == calls[0][:3000]: return g, len(calls)
    return None, len(calls)
def extract():
    todo = [(v, q, s, a) for (v, q), (s, a) in sorted(STORED.items())]
    for q in NEW_RUNS:
        rf = os.path.join(D["runs"], f"{q}-flash-0.2.0.md")
        if not os.path.exists(rf): print("no saved run yet for", q, "(0.2.0)"); continue
        g, n = first_checker(transcript(hfield(rf, "orchestrator agent")))
        assert g, ("the run has no checker call", q); todo.append(("0.2.0", q, hfield(rf, "session"), os.path.basename(g)[6:-6]))
    for ver, q, sess, ag in todo:
        i = tinfo(ag); assert i["session"] == sess, (q, ver, "session id differs", i["session"])
        assert QS[q]["text"] in i["prompt"], (q, ver, "the checker prompt does not hold this question")
        try: d, how, intro = draft_of(i["prompt"])
        except StopIteration:
            print(f"draft {q} {ver}: NO extractable draft in the checker's first prompt (agent {ag}): the pair is dropped and disclosed (PREREG-6 exclusions)"); continue
        if ver == "0.2.0": assert how == "the <draft> block", (q, how)
        n = normalize("wise-men", d); red = re.sub(r"\bAli\b", "the user", n)
        sp = shipped_file(q, ver); sh = normalize("wise-men", rd(sp)); v = verdict(i["rows"])
        parent = i["meta"].get("parentAgentId"); first = "?"
        if parent:
            try: g, nchk = first_checker(transcript(parent)); first = "yes" if g and os.path.basename(g) == os.path.basename(i["file"]) else "NO"
            except AssertionError: first = "parent transcript not found"
        head = (f"# draft: wise-men-flash {ver} | question: {q} | the decision memo the checker was given, extracted from the checker's first prompt ({how}) by fc6.py extract (PREREG-6 Part B)\n"
                f"# source: session {sess} | checker agent {ag} ({i['meta'].get('agentType', '?')}/{', '.join(i['models'])}) | transcript sha256: {i['sha']} | run: {i['date']} | first checker call of its run: {first}\n"
                f"# checker verdict: " + ", ".join(f"{k} {v.get(k, '?')}" for k in CHECKER_TESTS if k in v or ver == "0.2.0") + "\n"
                f"# shipped memo: {os.path.relpath(sp, H)} | words: draft {words(red)}, shipped {words(sh)} | identical after normalization: {'yes' if red == sh else 'no'}\n")
        if n != d: head += "# note: normalize() changed the extracted text\n"
        if red != n: head += "# note: the author's first name (inherited from global config) redacted to \"the user\"\n"
        wr(f_draft(q, ver), head + "\n" + red + "\n")
        print(f"draft {q} {ver}: {words(red)} words, shipped {words(sh)}, identical {red == sh}, verdict {v}, first checker {first}")
    for q in B2_TIES:
        if os.path.exists(f_draft(q, "0.1.0")): assert body(f_draft(q, "0.1.0")) == normalize("wise-men", rd(shipped_file(q, "0.1.0"))), ("B2 tie is not an identical pair", q)

def arm_prompt(q, skills, scratch):
    sec = re.search(r"^## wise-men-flash\n\n(.*?)\n\n## ", rd(os.path.join(HH, "arm-prompts-r5.md")), re.S | re.M)[1].strip()
    return sec.replace("<skills>", skills).replace("<scratch>", scratch).replace("<Q>", q) + "\n\nThe user's question:\n\"\"\"\n" + QS[q]["text"] + "\n\"\"\""
def run_prompt(q, skills, scratch): print(arm_prompt(q, skills.rstrip("/"), scratch.rstrip("/")))
def save_run(T, q):
    assert q in NEW_RUNS, q
    i = tinfo(T); p = i["prompt"]
    sk = re.search(r"Read the skill file (\S+)/wise-men-flash/SKILL\.md", p); sc = re.search(r"the only place you may write files is (\S+)/R50\d/flash/", p)
    same = bool(sk and sc) and p.strip() == arm_prompt(q, sk[1], sc[1]).strip()
    txt = final_text(i["rows"]); red = re.sub(r"\bAli\b", "the user", txt); n = normalize("wise-men", red)
    hs = [l.strip() for l in n.split("\n") if l.startswith("## ")]
    g, nchk = first_checker(i["file"]); fin = n.startswith("## Recommendation") and all(h in hs for h in HEADERS) and g is not None
    c, cl = cost_line(i["file"]); kids = tree(i["file"])[1:]
    seats = {}
    for f, dpt in kids:
        ki = tinfo(f); key = f"{ki['meta'].get('agentType', '?')}/{ki['meta'].get('model', '?')} = {', '.join(ki['models'])}"; seats[key] = seats.get(key, 0) + 1
    other = {}
    for f, dpt in tree(i["file"]):
        for nm, _ in tinfo(f)["tools"]:
            if nm not in ("Agent", "Task", "Read"): other[nm] = other.get(nm, 0) + 1
    web = {k: v for k, v in other.items() if re.search(r"web|fetch|search|firecrawl|curl", k, re.I)}
    head = (f"# arm: {FLASH_HEAD} | question: {q} | orchestrator: general-purpose/sonnet | run: {i['date']} ({ROUND})\n# {cl}\n"
            f"# session: {i['session']} | orchestrator agent: {i['agent']} | orchestrator model: {i['meta'].get('agentType', '?')}/{', '.join(i['models'])} | transcript sha256: {i['sha']}\n"
            f"# arm prompt: round 5's flash arm prompt (arm-prompts-r5.md), verbatim apart from local paths: {'yes' if same else 'NO'} | spawned: " + "; ".join(f"{k} x{v}" for k, v in sorted(seats.items())) + f" | checker calls: {nchk}\n")
    head += f"# note: tools beyond Read and Agent, across the run: {', '.join(f'{k} x{v}' for k, v in sorted(other.items()))}" + (" (step-6 verification, which the skill allows)" if web else "") + "\n" if other else "# note: no tool beyond Read and Agent anywhere in the run, so no web check at step 6\n"
    if red != txt: head += "# note: the author's first name (inherited from global config) redacted to \"the user\"\n"
    if not fin:
        k = 1 + len(glob.glob(os.path.join(D["runs"], f"{q}-flash-0.2.0-failed-*.md")))
        wr(os.path.join(D["runs"], f"{q}-flash-0.2.0-failed-{k}.md"), head + "# failed: no finished memo with the six headers, or no checker call\n\n" + red + "\n")
        print("FAILED run", q, "-> re-run once (PREREG-6 exclusions)"); return
    out = os.path.join(D["runs"], f"{q}-flash-0.2.0.md"); assert not os.path.exists(out), ("already saved", rel(out))
    wr(out, head + "\n" + red + "\n")
    print("saved run", q, words(n), "words |", f"{c['minutes']:.1f} min, {c['calls']} calls, ${c['usd']:.2f} | prompt verbatim: {same} | seats {seats} | other tools {other}")

# --- packets ---
def answer(arm, q, part):
    if arm == FL: return normalize("wise-men", rd(os.path.join(HH, "raw", q, "wise-men-flash.md")))
    if arm == WM: return normalize("wise-men", rd(os.path.join(HH, "raw", q, "wise-men-3.14.md")))
    if arm == PL: return normalize("direct", rd(os.path.join(HH, "raw", q, "direct.md")))
    if arm in CONTROLS: return normalize("wise-men", rd(f_rewrite(q, arm)))
    if arm == "draft": return normalize("wise-men", rd(f_draft(q, VER[part])))
    if arm == "shipped": return normalize("wise-men", rd(shipped_file(q, VER[part])))
    raise KeyError(arm)
def slots(part, q, j):
    S = seal_map(); return S["A"][q][part][j] if part in TYPES else S[part][q][j]
def f_packet(part, q, j): return os.path.join(D["packets"], "A", f"{q}-{part}-{j}.md") if part in TYPES else os.path.join(D["packets"], part, f"{q}-{j}.md")
def packet(part, q, j):
    tpl = rd(os.path.join(H, "judge-prompt-r6-3.txt" if part in TYPES else "judge-prompt-r6-2.txt"))
    parts = [f'Response {slot}:\n"""\n{answer(arm, q, part)}\n"""\n' for slot, arm in slots(part, q, j).items()]
    return tpl.replace("{question}", QS[q]["text"]).replace("{responses}", "\n".join(parts))
def packet_list():
    return [(t, q, j) for q in QIDS for t in TYPES for j in JUDGES] + [("B1", q, j) for q in B1Q for j in JUDGES] + [("B2", q, j) for q in B2Q for j in JUDGES]
def inputs_ready(part, q):
    need = {"M": [f_rewrite(q, PM)], "S": [f_rewrite(q, PS)], "P": [], "B1": [f_draft(q, "0.2.0"), shipped_file(q, "0.2.0")], "B2": [f_draft(q, "0.1.0")]}[part]
    miss = [p for p in need if not os.path.exists(p)]
    if part in ("M", "S") and not miss:
        bad = gating_fails(q, TYPES[part], script_check(q, TYPES[part], rd(f_rewrite(q, TYPES[part]))))
        if bad: miss.append(f_rewrite(q, TYPES[part]) + f" (fails the script check(s) {', '.join(bad)}; see DEVIATIONS.md)")
    return miss
def blind():
    made, missing = 0, {}
    for arm in CONTROLS:
        for q in QIDS:
            p = f_rewrite(q, arm)
            if os.path.exists(p): assert normalize("wise-men", rd(p)) == strip_header(rd(p)), ("normalize() removes more than the provenance header", rel(p))
    for q in B2_TIES:
        assert body(f_draft(q, "0.1.0")) == normalize("wise-men", rd(shipped_file(q, "0.1.0"))), ("B2 tie is not an identical pair", q)
    for part, q, j in packet_list():
        miss = inputs_ready(part, q)
        if miss: missing[(part, q)] = [rel(m) for m in miss]; continue
        wr(f_packet(part, q, j), packet(part, q, j)); made += 1
    print("blinded", made, "packets of", len(packet_list()))
    for k, v in missing.items(): print("  not built (input missing):", k, v)

# --- judges (step 6) ---
def f_judgment(part, q, j, suffix=""): return os.path.join(D["judgments"], part, f"{q}-{j}{suffix}.md")
def savejudge(T, part, q, j):
    assert part in PARTS and j in JUDGES, (part, j)
    i = tinfo(T); pk = f_packet(part, q, j); reads = [x.get("file_path", "") for nm, x in i["tools"] if nm == "Read"]; others = [nm for nm, _ in i["tools"] if nm != "Read"]
    assert i["models"] == ["claude-opus-5-5"], ("judge model is not claude-opus-5-5: the opus alias may have moved; stop and ask the owner", i["models"])
    tools_ok = not others and reads and all(os.path.realpath(r) == os.path.realpath(pk) for r in reads)
    txt = final_text(i["rows"]); letters = set(slots(part, q, j)); err = None if tools_ok else f"tools beyond one Read of the packet: Read {reads}, others {others}"
    if not err:
        try:
            if set(score_blocks(txt, letters)) != letters: err = "scores blocks missing for some letters"
        except AssertionError as e: err = f"parse: {e}"
    head = (f"# judge: fresh opus subagent ({i['meta'].get('agentType', '?')}, Read-only), no skills | part: {part} | question: {q} | judge: {j} | run: {i['date']} ({ROUND})\n"
            f"# blinded input: {rel(pk)} (slots per seal6.yaml) | model: {', '.join(i['models'])} | session: {i['session']} | agent: {i['agent']} | transcript sha256: {i['sha']}\n")
    if err:
        k = 1 + len(glob.glob(f_judgment(part, q, j, "-invalid-*")))
        wr(f_judgment(part, q, j, f"-invalid-{k}"), head + f"# invalid: {err}\n\n{txt}\n"); print("INVALID judgment", part, q, j, err, "-> re-run once" if k == 1 else "-> dropped and disclosed"); return
    assert not os.path.exists(f_judgment(part, q, j)), "already saved"
    wr(f_judgment(part, q, j), head + "\n" + txt + "\n"); print("judgment", part, q, j, {slots(part, q, j)[k]: sum(v.values()) for k, v in score_blocks(txt, letters).items()})
def judged(part, q, j):
    got = {}
    for slot, sc in score_blocks(rd(f_judgment(part, q, j)), set(slots(part, q, j))).items():
        got[slots(part, q, j)[slot]] = dict(sc, composite=sum(sc.values()))
    assert set(got) == set(slots(part, q, j).values()), (part, q, j); return got
def parse_all():
    out = {}
    for part in PARTS:
        for q in (QIDS if part in TYPES or part == "B1" else B2Q):
            js = [j for j in JUDGES if os.path.exists(f_judgment(part, q, j))]
            if not js: continue
            out[(part, q)] = {"question_id": q, "part": part, "judges": {j: judged(part, q, j) for j in js}}
    return out
def parse():
    for (part, q), d in parse_all().items():
        wr(os.path.join(D["parsed"], part, q + ".yaml"), yaml.safe_dump(d, sort_keys=False))
        print("parsed", part, q, len(d["judges"]), "judges", {a: r2(st.mean(d["judges"][j][a]["composite"] for j in d["judges"])) for a in next(iter(d["judges"].values()))})

# --- the contradiction classifier (step 7) ---
CLASSIFY = """You are classifying errors that blind graders listed. Each section below is one grader's PASS 0 error list for two responses, labelled only A and B. Classify every listed error as INTERNAL (it contradicts another part of the same response, the question's stated facts, or the response's own numbers) or OTHER (any other factual or logical error). "none found" lists no error. Count only the errors the grader listed; add none, merge none.

Return only this. For every section, in order, one line:
<section id>: A internal=<n> other=<n> | B internal=<n> other=<n>
Then a blank line, then one line per INTERNAL error: <section id> <letter>: <the error, in under 15 words>
"""
def pass0(t):
    m = re.search(r"PASS 0(.*?)(?=PASS 1)", t, re.S); return m[1].strip() if m else t.strip()
def classify_input():
    secs = [(f"{part}-{q}-{j}", pass0(rd(f_judgment(part, q, j)).split("\n\n", 1)[1])) for part in ("B1", "B2") for q in (B1Q if part == "B1" else B2Q) for j in JUDGES if os.path.exists(f_judgment(part, q, j))]
    chunks, cur = [], []
    for s in secs:
        if cur and sum(len(x[1]) for x in cur) + len(s[1]) > 60000: chunks.append(cur); cur = []
        cur.append(s)
    if cur: chunks.append(cur)
    for n, ch in enumerate(chunks, 1):
        wr(os.path.join(D["classify"], f"input-{n}.md"), CLASSIFY + "\n" + "\n\n".join(f"=== {sid} ===\n{t}" for sid, t in ch) + "\n")
        print(f"classify/input-{n}.md: {len(ch)} sections; spawn a fresh wise-member on sonnet: Read the file classify/input-{n}.md and follow it; return only what it asks for.")
def save_classify(T, n):
    i = tinfo(T); txt = final_text(i["rows"])
    wr(os.path.join(D["classify"], f"output-{n}.md"), f"# classifier: fresh {i['meta'].get('agentType', '?')}/{', '.join(i['models'])}, Read-only, sees only the letters A and B | input: classify/input-{n}.md | run: {i['date']} ({ROUND})\n"
       f"# session: {i['session']} | agent: {i['agent']} | transcript sha256: {i['sha']}\n\n{txt}\n"); print("saved classify output", n, len(classified()), "sections parsed")
def classified():
    out = {}
    for p in sorted(glob.glob(os.path.join(D["classify"], "output-*.md"))):
        for m in re.finditer(r"^(B[12]-R50\d-j\d): A internal=(\d+) other=(\d+) \| B internal=(\d+) other=(\d+)\s*$", rd(p), re.M):
            part, q, j = m[1].split("-"); sl = slots(part, q, j)
            out[(part, q, j)] = {sl["A"]: {"internal": int(m[2]), "other": int(m[3])}, sl["B"]: {"internal": int(m[4]), "other": int(m[5])}}
    return out

# --- analysis ---
def load(part):
    """Question means over the valid judges; a question with fewer than two valid judges in this packet type is left out."""
    R = {}
    for q in QIDS:
        p = os.path.join(D["parsed"], part, q + ".yaml")
        if not os.path.exists(p): continue
        d = yaml.safe_load(rd(p)); js = list(d["judges"])
        if len(js) < 2: continue
        R[q] = {a: {k: st.mean(d["judges"][j][a][k] for j in js) for k in AXES + ["composite"]} for a in d["judges"][js[0]]}
    return R
def summ(d):
    v = [d[q] for q in sorted(d)]
    if not v: return None
    lo, hi = boot(v, seed=SEED); return {"n": len(v), "mean": st.mean(v), "lo": lo, "hi": hi, "per": d}
def dif(R, a, b, key="composite"): return {q: R[q][a][key] - R[q][b][key] for q in R}
def boot_ratio(num, den, seed=SEED, n=10000):
    """Percentile bootstrap of mean(num)/mean(den), resampling questions jointly (boot()'s scheme, for a ratio)."""
    rng = random.Random(seed); k = len(num); out = []
    for _ in range(n):
        s = [rng.randrange(k) for _ in range(k)]; dn = st.mean(den[i] for i in s)
        if dn: out.append(st.mean(num[i] for i in s) / dn)
    out.sort(); return out[int(0.025 * len(out))], out[int(0.975 * len(out)) - 1]
def iv(s): return f"{sg(s['mean'])} [{sg(s['lo'])}, {sg(s['hi'])}] over {s['n']} questions" if s else "not computable (no questions)"
def a1_word(dc, dp):
    if not dc or not dp: return "not computable"
    if dp["lo"] <= 0: return "inconclusive"
    if dc["lo"] > 0: return "holds" if dc["mean"] >= 0.5 * dp["mean"] else "holds, but smaller"
    return "does not hold"
def b1_word(c):
    if not c: return "not computable"
    if c["lo"] > 0: return "clearly improves"
    if c["hi"] < 0: return "clearly worse"
    return "ahead, not clearly" if c["mean"] > 0 else "no measured benefit"
def measures():
    M, P, S, B1, B2 = (load(x) for x in PARTS); out = {"R": {"M": M, "P": P, "S": S, "B1": B1, "B2": B2}}
    for hero, tag in ((FL, "flash"), (WM, "wise-men")):
        dc, dp, ds = summ(dif(M, hero, PM)), summ(dif(P, hero, PL)), summ(dif(S, hero, PS))
        both = sorted(set(M) & set(P)); F = {q: (P[q][hero]["composite"] - P[q][PL]["composite"]) - (M[q][hero]["composite"] - M[q][PM]["composite"]) for q in both}
        sb = sorted(set(P) & set(S)); Ffmt = {q: (P[q][hero]["composite"] - P[q][PL]["composite"]) - (S[q][hero]["composite"] - S[q][PS]["composite"]) for q in sb}
        sl = sorted(set(S) & set(M)); Flen = {q: (S[q][hero]["composite"] - S[q][PS]["composite"]) - (M[q][hero]["composite"] - M[q][PM]["composite"]) for q in sl}
        share = None
        if dp and dp["lo"] > 0 and both:
            num = [F[q] for q in both]; den = [P[q][hero]["composite"] - P[q][PL]["composite"] for q in both]
            share = {"S": st.mean(num) / st.mean(den), "ci": boot_ratio(num, den)}
        out[tag] = {"D_ctrl": dc, "D_plain": dp, "D_short": ds, "F": summ(F), "F_fmt": summ(Ffmt), "F_len": summ(Flen), "share": share,
                    "word": a1_word(dc, dp), "word_short": a1_word(ds, dp),
                    "corr_M": summ({q: M[q][PM]["correctness"] - M[q][hero]["correctness"] for q in M}), "corr_P": summ({q: P[q][PL]["correctness"] - P[q][hero]["correctness"] for q in P}),
                    "corr_S": summ({q: S[q][PS]["correctness"] - S[q][hero]["correctness"] for q in S})}
    out["B1"] = {"C": summ(dif(B1, "shipped", "draft")), "axes": {x: summ(dif(B1, "shipped", "draft", x)) for x in AXES}}
    out["B1"]["word"] = b1_word(out["B1"]["C"])
    c2 = dif(B2, "shipped", "draft"); c2.update({q: 0.0 for q in B2_TIES}); out["B2"] = {"C": summ(c2), "C_judged": summ(dif(B2, "shipped", "draft"))}
    cl = classified(); out["contradictions"] = {}
    for part in ("B1", "B2"):
        per = {}
        for (p, q, j), v in cl.items():
            if p != part: continue
            for a in ("draft", "shipped"):
                per.setdefault(q, {}).setdefault(a, {"internal": 0, "other": 0, "judges": 0})
                per[q][a]["internal"] += v[a]["internal"]; per[q][a]["other"] += v[a]["other"]; per[q][a]["judges"] += 1
        out["contradictions"][part] = per
    out["words"] = {}
    for part in PARTS:
        for q in (B2Q if part == "B2" else QIDS):
            if inputs_ready(part, q): continue
            for a in set(slots(part, q, "j1").values()): out["words"].setdefault(part, {}).setdefault(a, {})[q] = words(answer(a, q, part))
    return out
def lines():
    m = measures(); R = m["R"]; L = []
    corr = []
    for part in ("M", "P", "S"):
        if R[part]: corr.append(f"{part} packets: " + ", ".join(f"{NAMES[a]} {r2(st.mean(R[part][q][a]['correctness'] for q in R[part]))}" for a in (FL, WM, TYPES[part])))
    for part in ("B1", "B2"):
        if R[part]: corr.append(f"{part}: " + ", ".join(f"{NAMES[a]} {r2(st.mean(R[part][q][a]['correctness'] for q in R[part]))}" for a in ("draft", "shipped")))
    L += ["Correctness first. In round 5 a plain answer scored higher on correctness than flash and wise-men (4.3 against 3.8 for both). In this round, correctness out of 5 (mean of three judges, then of questions), by packet type: " + "; ".join(corr) + ".", ""]
    L += ["The caveat. Every answer, rewrite, audit, judge and classifier here is a Claude model, there are no human grades, and this tests one known bias of LLM judges with LLM judges. It cannot answer whether AI validating AI can be trusted; only human blind ratings can, and they are a separate step. "
          "The owner's spot check of two rewrites before judging (Part A, rule 4) was skipped: he left the call to the analyst (Amendment 2), so the blind audits are the only check that the rewrites add nothing to the answer they restate.", ""]
    f = m["flash"]; b = m["B1"]
    L += [f"**A1 (primary): the win over the plain answer survives format matching — {f['word']}.** Flash − plain-memo (`D_ctrl`, M packets): {iv(f['D_ctrl'])}; flash − plain answer (`D_plain`, P packets): {iv(f['D_plain'])}."
          + (" The 3-answer sitting did not reproduce round 5's gap (the `D_plain` interval is not above zero), so A1 is inconclusive and `S` is not reported." if f["word"] == "inconclusive" else ""), "",
          "Read A1 with this: the control is a faithful rewrite of the plain answer under the pre-registered rules, not a format-only twin of it. The rewriters carried the prompt's word \"the source\" into every long rewrite and half the short ones, and most judges of those packets named it as a fault; both rewrites scored below the plain answer they restate. So this round rules out length as the driver of the gap (long and short rewrites scored alike) more firmly than it rules out format. Details under Honest limits.", ""]
    L += [f"**B1 (primary): the checker improves the memo (0.2.0) — {b['word']}.** Shipped − draft (`C`, total /25): {iv(b['C'])}. "
          "B1 measured wise-men-flash 0.2.0, whose practitioner anchor and Devil's Advocate ran on `opus` (`claude-opus-5-5`); 0.3.0, released on 2026-11-10, routes those two seats to `fable` (falling back to `opus`), which no round has measured.", ""]
    L += ["## Part A: the format-matched control", ""]
    for tag, hero in (("flash", FL), ("wise-men", WM)):
        x = m[tag]; nm = NAMES[hero]
        L += [f"- {'A1' if tag == 'flash' else 'A2'} ({nm}): {x['word']}. `D_ctrl` {iv(x['D_ctrl'])}; `D_plain` {iv(x['D_plain'])}."]
        L += [f"- A3 ({nm}): format effect `F` = `D_plain` − `D_ctrl` {iv(x['F'])}" + (f"; share of the gap format and length explain, `S` = {s2(x['share']['S'])} [{s2(x['share']['ci'][0])}, {s2(x['share']['ci'][1])}]." if x["share"] else "; `S` not reported (the replication guard failed or no question has both packet types).")
              + (" Both are negative: next to the same anchor, the format-matched rewrite scored below the plain answer it restates, so format and length explain none of the gap, and the stated prediction (`F` > 0) did not hold." if x["F"] and x["F"]["mean"] < 0 else "")]
        L += [f"- A5 ({nm}): `D_short` {iv(x['D_short'])} ({x['word_short']} by A1's rule); format only `F_fmt` = `D_plain` − `D_short` {iv(x['F_fmt'])}; length `F_len` = `D_short` − `D_ctrl` {iv(x['F_len'])}."
              + (" `D_short` holds while `D_ctrl` does not: the stretched rewrite, not the format, closed the gap." if x["word_short"].startswith("holds") and not x["word"].startswith("holds") else "")]
        L += [f"- A4 ({nm}): correctness, plain-memo − {nm} (M) {iv(x['corr_M'])}; plain answer − {nm} (P) {iv(x['corr_P'])}; plain-memo-short − {nm} (S) {iv(x['corr_S'])}.", ""]
    for part in ("M", "P", "S"):
        if not R[part]: continue
        arms = [FL, WM, TYPES[part]]
        L += [f"| {part} packets ({len(R[part])} questions) | total /25 | correct | insight | practical | risk | dissent | words |", "|---|--:|--:|--:|--:|--:|--:|--:|"]
        for a in arms:
            w = m["words"].get(part, {}).get(a, {}); L += [f"| {NAMES[a]} | {r2(st.mean(R[part][q][a]['composite'] for q in R[part]))} | " + " | ".join(r2(st.mean(R[part][q][a][x] for q in R[part])) for x in AXES) + f" | {round(st.mean(w.values())) if w else '–'} |"]
        L += [""]
    L += ["## Part B: the checker on and off", ""]
    for part in ("B1", "B2"):
        if not R[part]: continue
        L += [f"| {part} ({VER[part]}, {len(R[part])} questions judged) | total /25 | correct | insight | practical | risk | dissent | words |", "|---|--:|--:|--:|--:|--:|--:|--:|"]
        for a in ("draft", "shipped"):
            w = m["words"].get(part, {}).get(a, {}); L += [f"| {NAMES[a]} | {r2(st.mean(R[part][q][a]['composite'] for q in R[part]))} | " + " | ".join(r2(st.mean(R[part][q][a][x] for q in R[part])) for x in AXES) + f" | {round(st.mean(w.values())) if w else '–'} |"]
        L += [""]
    L += ["- B1 per axis, shipped − draft: " + "; ".join(f"{h2h5.AXIS_NAME[x]} {iv(b['axes'][x])}" for x in AXES) + "."]
    L += [f"- B2 (0.1.0, secondary): `C` over all 8 questions, the four identical pairs entering as ties: {iv(m['B2']['C'])}; over the four judged questions only: {iv(m['B2']['C_judged'])}."]
    for part in ("B1", "B2"):
        per = m["contradictions"].get(part)
        if per: L += [f"- B3 ({part}): internal contradictions the judges listed, summed over judges, draft → shipped: " + "; ".join(f"{q} {per[q]['draft']['internal']} → {per[q]['shipped']['internal']}" for q in sorted(per))
                      + f"; all PASS 0 errors: {sum(per[q]['draft']['internal'] + per[q]['draft']['other'] for q in per)} → {sum(per[q]['shipped']['internal'] + per[q]['shipped']['other'] for q in per)}."]
    for part in ("B1", "B2"):
        w = m["words"].get(part)
        if w and "draft" in w: L += [f"- Words, {part}, shipped − draft: " + ", ".join(f"{q} {w['shipped'][q] - w['draft'][q]:+d}" for q in sorted(w["draft"])) + "."]
    L += ["", "## Per question (mean of the valid judges, total /25)", ""]
    for part in PARTS:
        if not R[part]: continue
        arms = [FL, WM, TYPES[part]] if part in TYPES else ["draft", "shipped"]
        L += [f"| {part} | " + " | ".join(NAMES[a] for a in arms) + " |", "|---|" + "--:|" * len(arms)] + [f"| {q} | " + " | ".join(r2(R[part][q][a]["composite"]) for a in arms) + " |" for q in sorted(R[part])] + [""]
    L += ["## The rewrites: audit results", "", "NEW / STRONGER / WEAKER / DROPPED as each audit found them, before the deletion rule. Attempt 3 is Amendment 2's length-only retry (`plain-memo` R502, R507, R508). Words and band are the final's.", "",
          "| question | arm | from attempt | attempt 1 | attempt 2 | attempt 3 | deleted | dropped, disclosed | words | band |", "|---|---|--:|---|---|---|--:|--:|--:|---|"]
    for q in QIDS:
        for arm in CONTROLS:
            fy = f_audit(q, arm, "final", "yaml")
            if not os.path.exists(fy): continue
            fi = yaml.safe_load(rd(fy)); a1, a2, a3 = audit_of(q, arm, 1), audit_of(q, arm, 2), audit_of(q, arm, 3)
            fmt = lambda a: "/".join(str(a["counts"][x]) for x in ("NEW", "STRONGER", "WEAKER", "DROPPED")) if a else "–"
            r3 = fi.get("amendment_2_retry"); lo, hi, _ = band(arm, q)
            t3 = fmt(a3) + (f" ({r3['words']:,} words, {'used' if r3['used'] else 'not used'})" if r3 else "")
            bd = f"{lo:,}–{hi:,}, " + ("in" if lo <= fi["words"] <= hi else "out") + (" (band dropped)" if arm == PS else "")
            L += [f"| {q} | {arm} | {fi['from_attempt']} | {fmt(a1)} | {fmt(a2)} | {t3} | {len(fi['deleted'])} | {len(fi['dropped'])} | {fi['words']:,} | {bd} |"]
    L += ["", "## Judges", ""] + judge_lines()
    dv = os.path.join(H, "DEVIATIONS.md")
    L += ["", "## Deviations and disclosures", ""] + ([l for l in rd(dv).split("\n") if l.startswith("- ")] if os.path.exists(dv) else ["- none recorded"])
    L += ["", "## Reproduce", "", "`python3 eval-data/format-control/fc6.py report` prints this page; `results` rewrites it; `verify` rebuilds every packet from the stored answers, rewrites and drafts, every final rewrite from its attempt and audit, and re-parses every judgment. "
          "The drafts and the new runs were taken from local agent transcripts, which are not in the repository; their headers carry each transcript's SHA-256, so the owner's machine can re-check them.", ""]
    return L
def s2(x): return ("−" if x < 0 else "") + r2(abs(x))
SRC_QUOTE = re.compile(r"[\"“]the source[\"”]|\"the source|the source says|“the source")
def judge_lines():
    """Counts from the stored judgments: valid ones by part, re-runs, the models in every judge header."""
    L, valid, models = [], {}, {}
    for part in PARTS:
        valid[part] = len(glob.glob(os.path.join(D["judgments"], part, "R50?-j?.md")))
    inval = sorted(glob.glob(os.path.join(D["judgments"], "*", "*-invalid-*.md")))
    for p in glob.glob(os.path.join(D["judgments"], "*", "*.md")):
        m = re.search(r"\| model: ([\w.-]+)", rd(p)); models[m[1] if m else "?"] = models.get(m[1] if m else "?", 0) + 1
    L += [f"- {sum(valid.values())} valid judgments (" + ", ".join(f"{p} {valid[p]}" for p in PARTS) + "), each by a fresh `wise-member` agent on `opus` that read its packet and nothing else."
          + (f" {len(inval)} judgment(s) failed and were re-run once by a fresh judge on the same packet: " + "; ".join(f"{rel(p)} ({re.search(r'# invalid: (.*)', rd(p))[1]})" for p in inval) + "." if inval else " None failed.")
          + " Model in every judge transcript, re-runs included: " + ", ".join(f"`{k}` ×{v}" for k, v in sorted(models.items())) + "."]
    q = {part: sum(1 for qq in QIDS for j in JUDGES if os.path.exists(f_judgment(part, qq, j)) and SRC_QUOTE.search(rd(f_judgment(part, qq, j)).split("\n\n", 1)[1])) for part in TYPES}
    n = {arm: sum(1 for qq in QIDS if re.search(r"\bthe source\b", body(f_rewrite(qq, arm)), re.I)) for arm in CONTROLS}
    L += [f"- What the control carried besides format. The rewrite rules let the Strongest counter-position and Confidence sections hold only what the plain answer says, so where it raised no objection the section says so, and Confidence follows a fixed hedge-word rule. "
          f"The rewrite prompt calls the plain answer \"the source\", and the rewriters carried that word into {n[PM]} of 8 `plain-memo` and {n[PS]} of 8 `plain-memo-short` finals (the audits check content, not this label, so none flagged it); "
          f"{q['M']} of 24 M-packet and {q['S']} of 24 S-packet judgments quote \"the source\" as a fault ({q['P']} of 24 P-packet judgments, whose packets hold no rewrite). "
          "Both rewrites scored below the plain answer on every axis. These are part of what A1 measured: the control is a faithful rewrite under the pre-registered rules, not a format-only twin of the plain answer, and the verdicts above stand as pre-registered."]
    return L
def report(): print("\n".join(lines()))
def results():
    L = ["# Round 6 results: a format-matched control and the checker on and off", "", f"Pre-registration: [`PREREG-6.md`](PREREG-6.md), committed as `{PREREG_COMMIT}` before any rewrite, run or judgment, and amended before any judge ran (Amendment 2, `{AMEND2_COMMIT}`, 2026-11-10).", ""] + lines()
    wr(os.path.join(H, "RESULTS-6.md"), "\n".join(L)); print("wrote RESULTS-6.md")

def verify():
    n_pk = n_fin = n_par = 0
    for part, q, j in packet_list():
        p = f_packet(part, q, j)
        if os.path.exists(p): assert rd(p) == packet(part, q, j), ("packet differs from a rebuild", rel(p)); n_pk += 1
    for q in QIDS:
        for arm in CONTROLS:
            if os.path.exists(f_rewrite(q, arm)):
                b = final_build(q, arm); assert b and b[0] == rd(f_rewrite(q, arm)), ("final rewrite differs from a rebuild", q, arm); n_fin += 1
    for (part, q), d in parse_all().items():
        p = os.path.join(D["parsed"], part, q + ".yaml"); assert os.path.exists(p) and yaml.safe_load(rd(p)) == d, ("parsed scores differ from the judgments", part, q); n_par += 1
    print(f"verify: {n_pk} packets rebuilt byte-identical, {n_fin} final rewrites rebuilt from their attempts and audits, {n_par} parsed files match their judgments")

def spotcheck():
    q2 = seal_map()["spotcheck"]
    L = ["# Spot check: two rewrites to read before any judging", "",
         f"The owner reads these before any judge runs (PREREG-6 Part A, step 4 of \"How nothing new is enforced\"). The two questions, {q2[0]} and {q2[1]}, were drawn in `seal6.yaml` before any rewrite existed.", "",
         "For each question there are three texts, one after the other: the plain answer from round 5 (the source), with every sentence numbered S1, S2, …; then the two rewrites of it, the long one (`plain-memo`, stretched to flash's length) and the short one (`plain-memo-short`, at the plain answer's own length). "
         "After every rewrite sentence, in brackets, are the source sentences it restates, as the blind auditor mapped them. CONNECTIVE means the auditor found it only links or introduces; FIXED is one of the three set sentences for an empty section.", "",
         "What to look for: any rewrite sentence that says something the source does not say (a new fact, number, example, step, risk or argument), or that sounds more certain or less certain than the source. "
         "Note it by question, arm and R number (for example \"R503 plain-memo R14: adds a new step\"). Anything marked is deleted the same way the audit's findings are, and listed in the results.", ""]
    for q in q2:
        L += [f"## {q}", "", "**The question.** " + QS[q]["text"], "", "### The source: round 5's plain answer, numbered", ""]
        k = 0
        for u in units(source(q)):
            if u["kind"] == "block":
                parts = []
                for i, s in enumerate(u["sents"]): k += 1; parts.append(f"**S{k}** {s}")
                L += [(u["pre"] if u["pre"] else "") + " ".join(parts), ""]
        for arm in CONTROLS:
            fy = f_audit(q, arm, "final", "yaml")
            if not os.path.exists(fy): L += [f"### {arm}: not finished yet", ""]; continue
            fi = yaml.safe_load(rd(fy)); n = fi["from_attempt"]; a = audit_of(q, arm, n); dele = {d["R"] for d in fi["deleted"]}
            L += [f"### {'The long rewrite' if arm == PM else 'The short rewrite'} (`{arm}`, attempt {n}, {fi['words']} words)", ""]
            k = 0
            for u in units(body(f_rewrite(q, arm, n))):
                if u["kind"] == "head": L += [f"**{u['line'].lstrip('#').strip()}**", ""]
                elif u["kind"] == "block":
                    parts = []
                    for s in u["sents"]:
                        k += 1; v = a["map"][f"R{k}"]
                        parts.append(("~~" + s + "~~" if k in dele else s) + f" [R{k}: {v}" + ("; DELETED" if k in dele else "") + "]")
                    L += [(u["pre"] if u["pre"] else "") + " ".join(parts), ""]
            if fi["inserted_fixed_sentence_in"]: L += ["Fixed sentence inserted after deletion in: " + ", ".join(fi["inserted_fixed_sentence_in"]), ""]
            lo, hi, _ = band(arm, q); inb = lo <= fi["words"] <= hi
            L += [f"Length: {fi['words']:,} words; its pre-registered band is {lo:,}–{hi:,}" + (" (inside)." if inb else " (outside the band, which the plan's rules could not repair; the owner decides how it is used, see DEVIATIONS.md)."), ""]
            L += [f"Audit result for this version{' (after the one retry' + (' and the deletions' if fi['deleted'] else '') + ')' if n == 2 else ''}: NEW {fi['counts_after']['NEW']}, STRONGER {fi['counts_after']['STRONGER']}, WEAKER {fi['counts_after']['WEAKER']}, DROPPED {fi['counts_after']['DROPPED']}."
                  + (" Deleted: " + "; ".join(f"R{d['R']} ({d['label']}: {d['note']})" for d in fi["deleted"]) + "." if fi["deleted"] else " Nothing deleted.")
                  + (" Source sentences carried nowhere (disclosed, not put back): " + ", ".join(f"S{d['S']}" for d in fi["dropped"]) + "." if fi["dropped"] else ""), ""]
    wr(os.path.join(H, "SPOTCHECK.md"), "\n".join(L)); print("wrote SPOTCHECK.md for", q2)

def seal():
    """seal6.yaml, once, before any rewrite or run: the answer order for every packet and judge, and the two spot-check questions."""
    assert not os.path.exists(SEAL), "seal6.yaml already exists: the order is sealed"
    for q in QIDS: assert words(normalize("wise-men", rd(os.path.join(HH, "raw", q, "wise-men-flash.md")))) == FLASH_WORDS[q], ("flash word count differs from PREREG-6", q)
    rng = random.Random(SEED); A = {}
    for q in QIDS:  # three-answer packets: a seeded base order, rotated across j1-j3, so every answer sits in every slot once per question
        A[q] = {}
        for t in TYPES:
            base = [FL, WM, TYPES[t]]; rng.shuffle(base)
            A[q][t] = {j: {chr(65 + s): base[(s + r) % 3] for s in range(3)} for r, j in enumerate(JUDGES)}
    B = {}
    for part, qs in (("B1", B1Q), ("B2", B2Q)):  # two-answer packets: j1 seeded, j2 its reverse, j3 seeded
        B[part] = {}
        for q in qs:
            o1 = ["draft", "shipped"]; rng.shuffle(o1); o3 = ["draft", "shipped"]; rng.shuffle(o3)
            B[part][q] = {"j1": {"A": o1[0], "B": o1[1]}, "j2": {"A": o1[1], "B": o1[0]}, "j3": {"A": o3[0], "B": o3[1]}}
    spot = sorted(rng.sample(QIDS, 2))
    yaml.safe_dump({"seed": SEED, "note": "sealed answer order per packet and judge, and the owner's two spot-check questions, generated by fc6.py seal before any round-6 rewrite or run (PREREG-6)",
                    "spotcheck": spot, "A": A, "B1": B["B1"], "B2": B["B2"]}, open(SEAL, "w"), sort_keys=False)
    print("sealed: Part A", len(A), "questions x 3 packet types x 3 judges; B1", len(B["B1"]), "; B2", len(B["B2"]), "; spot check", spot)

if __name__ == "__main__":
    cmd = {"seal": seal, "rewrite-prompt": rewrite_prompt, "save-control": save_control, "check": check, "audit-prompt": audit_prompt, "save-audit": save_audit,
           "length-retry": length_retry, "extract": extract, "run-prompt": run_prompt, "save-run": save_run, "blind": blind, "savejudge": savejudge, "parse": parse, "classify-input": classify_input,
           "save-classify": save_classify, "report": report, "results": results, "verify": verify, "spotcheck": spotcheck}
    cmd[sys.argv[1]](*sys.argv[2:])
