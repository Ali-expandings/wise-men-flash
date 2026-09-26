#!/usr/bin/env python3
"""Regenerate the README charts and the banner as hand-authored SVG.

Run: python3 scripts/make_charts.py   (needs PyYAML only)

Every chart is written twice, <name>.svg for GitHub's light theme and <name>-dark.svg for dark; the README picks one
with <picture>. The numbers come from eval-data/head-to-head/ through flash4.py, the same code that writes RESULTS.md,
so a chart cannot disagree with the results file. Text always uses neutral ink, never a series colour: identity comes
from the mark beside the text. Drawing helpers and banner sprites follow the wise-men repository's, so the two
projects read as one family: flash is marked in amber, the full wise-men council in its own dark red."""
import os, sys, math, statistics as st
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "eval-data", "head-to-head"))
import flash4 as F

OUT = os.environ.get("CHARTS_OUT") or os.path.join(ROOT, "assets")  # check.sh renders into a temp dir and diffs against assets/
AXES = F.AXES
AXIS_NAME = {"correctness": "Correctness", "insight": "Insight", "practical": "Practical use", "risk": "Risk awareness", "dissent": "Dissent quality"}
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
THEMES = {
    "light": dict(ACCENT="#b8740c", SIB="#9e1b24", INK="#1f2328", TXT="#59636e", MUTE="#818b98", GRID="#d8dee4", SURF="#ffffff", BAR2="#8c959f", OTHER="#8c959f"),
    "dark": dict(ACCENT="#e2a336", SIB="#b8323a", INK="#e6edf3", TXT="#9198a1", MUTE="#6e7681", GRID="#262c36", SURF="#0d1117", BAR2="#7d8590", OTHER="#6e7681"),
}
C = dict(THEMES["light"])  # active theme
HERO, SIB = F.HERO, F.SIB
NAME = {HERO: "wise-men-flash", SIB: "wise-men full council", "warp-council": "Warp council", "llm-council": "llm-council", "direct": "plain answer"}
SRC = {HERO: "measured as wise-men 3.13 --fast", SIB: "wise-men 3.13 · members, review, debate", "warp-council": "warpdotdev · 24.5k installs",
       "llm-council": "aiwithremy · 1.0k installs", "direct": "no skill"}
TOPIC = {"R401": "Postgres search or a dedicated engine?", "R402": "A pipeline that fails every few weeks", "R403": "A target for halving onboarding drop-off",
         "R404": "A vendor's 30% case study", "R405": "How far to trust a natural experiment"}

def num(v): return f"{v:.1f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)
r1, sg = F.r1, F.sg
def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def svg(w, h, body, title): return f'<svg viewBox="0 0 {num(w)} {num(h)}" width="{num(w)}" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">\n<title>{esc(title)}</title>\n{body}</svg>\n'
def t(x, y, s, size=12, fill=None, weight=400, anchor="start", extra=""):
    return f'<text x="{num(x)}" y="{num(y)}" font-size="{size}" font-weight="{weight}" fill="{fill or C["TXT"]}" text-anchor="{anchor}" {extra}>{esc(s)}</text>\n'
def line(x1, y1, x2, y2, col, w=1, extra=""): return f'<line x1="{num(x1)}" y1="{num(y1)}" x2="{num(x2)}" y2="{num(y2)}" stroke="{col}" stroke-width="{w}" {extra}/>\n'
def hbar(x, y, w, h, fill, r=4):  # grows right from the baseline; rounded data end, square at the baseline
    if w <= 0: return ""
    r = min(r, w, h / 2)
    return f'<path d="M{num(x)},{num(y)}h{num(w - r)}a{num(r)},{num(r)} 0 0 1 {num(r)},{num(r)}v{num(h - 2 * r)}a{num(r)},{num(r)} 0 0 1 -{num(r)},{num(r)}h-{num(w - r)}z" fill="{fill}"/>\n'
def hbar_outline(x, y, w, h, col, r=4):  # the plain answer: same shape as hbar, outline only
    if w <= 0: return ""
    x, y, w, h = x + 0.75, y + 0.75, w - 1.5, h - 1.5; r = min(r, w, h / 2)
    return f'<path d="M{num(x)},{num(y)}h{num(w - r)}a{num(r)},{num(r)} 0 0 1 {num(r)},{num(r)}v{num(h - 2 * r)}a{num(r)},{num(r)} 0 0 1 -{num(r)},{num(r)}h-{num(w - r)}z" fill="none" stroke="{col}" stroke-width="1.5"/>\n'
def dot(cx, cy, r, fill): return f'<circle cx="{num(cx)}" cy="{num(cy)}" r="{r}" fill="{fill}" stroke="{C["SURF"]}" stroke-width="2"/>\n'
def ring(cx, cy, r, col, w=1.6): return f'<circle cx="{num(cx)}" cy="{num(cy)}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}"/>\n'
def band(y, h, x=32, w=816): return f'<rect x="{num(x)}" y="{num(y)}" width="{num(w)}" height="{num(h)}" rx="6" fill="{C["ACCENT"]}" fill-opacity="0.10"/>\n'
def colour(a): return C["ACCENT"] if a == HERO else C["SIB"] if a == SIB else C["BAR2"]
def bar(a, x, y, w, h, r=4): return hbar_outline(x, y, w, h, C["TXT"], r) if a == "direct" else hbar(x, y, w, h, colour(a), r)
def by_total(T): return sorted(F.ARMS, key=lambda a: (-T[a]["mean"], F.ARMS.index(a)))

def chart_round4(R):
    n = len(R); T = F.table(R); x0, sc, top, rh = 250, 15.6, 112, 46; arms = by_total(T); bottom = top + rh * len(arms) - 6
    b = t(40, 32, f"Round 4: total score on new questions — {n} of 8 questions run, three blind judges each", 16, C["INK"], 600)
    b += t(40, 52, "Sum of 5 rubric axes (1–5 each, max 25), mean of 3 judges, averaged over the questions. Right: flash's lead, 95% bootstrap interval.", 12, C["TXT"])
    b += t(40, 68, "Questions written by an author that knew nothing about the arms; a stricter judge that lists every error before it scores.", 12, C["TXT"])
    b += t(840, top - 12, "flash ahead by [95%]", 11, C["MUTE"], anchor="end")
    for g in range(0, 26, 5):
        x = x0 + g * sc; b += line(x, top - 4, x, bottom, C["GRID"]) + t(x, bottom + 16, g, 11, C["MUTE"], anchor="middle")
    for i, a in enumerate(arms):
        y = top + i * rh; m = T[a]["mean"]; hero = a == HERO
        if hero: b += band(y - 3, rh - 2)
        b += t(x0 - 14, y + 15, NAME[a], 13, C["INK"], 700 if hero else 500, "end") + t(x0 - 14, y + 30, SRC[a], 11, C["MUTE"], anchor="end")
        b += bar(a, x0, y + 6, m * sc, 22) + t(x0 + m * sc + 8, y + 22, r1(m), 13, C["INK"], 700 if hero else 500)
        if hero: b += t(840, y + 22, "—", 12, C["MUTE"], anchor="end"); continue
        c = F.compare(R, a); b += t(840, y + 22, f"{sg(c['diff'])}  [{sg(c['lo'])}, {sg(c['hi'])}]", 12, C["INK"] if c["lo"] > 0 else C["TXT"], 600 if c["lo"] > 0 else 400, "end")
    fy = bottom + 42; clear = sum(F.compare(R, a)["lo"] > 0 for a in F.RIVALS); s = F.compare(R, SIB)
    b += t(40, fy, f"An interval above zero is the pre-registered bar for \"clearly ahead\": met against {clear} of {len(F.RIVALS)} rivals. Against the full wise-men council,", 11, C["MUTE"])
    b += t(40, fy + 16, f"flash is {r1(abs(s['diff']))} behind with an interval that includes zero. Flash was measured as the --fast arm of wise-men 3.13, the profile this skill ships.", 11, C["MUTE"])
    b += t(40, fy + 32, "Pre-registered at eight questions and stopped at five at the owner's request, after three questions' scores were known; the writing,", 11, C["MUTE"])
    b += t(40, fy + 48, "ethics and personal-decision questions were not run. Intervals resample the five questions (10,000 draws), not judges.", 11, C["MUTE"])
    b += t(40, fy + 64, f"N = {n} · one top-level model ran every arm · Warp's council on Claude models only · three fresh Opus judges per question · PREREG-4.md", 11, C["MUTE"])
    return svg(860, fy + 78, b, f"Round 4 mean total score out of 25 on {n} new questions, three blind judges each: " + ", ".join(f"{NAME[a]} {r1(T[a]['mean'])}" for a in arms))

def chart_questions(R):
    qs = sorted(R); n = len(qs); lo = min(10, int(min(R[q][a]["composite"] for q in qs for a in F.ARMS)))
    x0, x1, hi = 300, 640, 25; sc = (x1 - x0) / (hi - lo); top, rh = 112, 32; bottom = top + rh * (n - 1) + 16
    short = {"llm-council": "llm-council", "warp-council": "Warp", "direct": "plain answer"}
    b = t(40, 32, "Round 4, question by question", 16, C["INK"], 600)
    b += t(40, 52, "Mean of three blind judges' totals (max 25) for flash, the full wise-men council, two rival councils and a plain answer", 12, C["TXT"])
    b += t(660, top - 22, "flash vs the best rival", 11, C["MUTE"])
    for g in range(lo, 26, 5):
        x = x0 + (g - lo) * sc; b += line(x, top - 16, x, bottom, C["GRID"]) + t(x, bottom + 16, g, 11, C["MUTE"], anchor="middle")
    won = tied = lost = 0; sib_up = []
    for i, q in enumerate(qs):
        y = top + i * rh; r = R[q]; fl = r[HERO]["composite"]; vals = [r[a]["composite"] for a in F.ARMS]
        b += t(40, y + 4, q, 11, C["MUTE"]) + t(84, y + 4, TOPIC[q], 12, C["INK"])
        b += line(x0 + (min(vals) - lo) * sc, y, x0 + (max(vals) - lo) * sc, y, C["GRID"], 2) + ring(x0 + (r["direct"]["composite"] - lo) * sc, y, 7, C["TXT"])
        for a in F.COUNCILS: b += dot(x0 + (r[a]["composite"] - lo) * sc, y, 4.5, C["OTHER"])
        b += ring(x0 + (r[SIB]["composite"] - lo) * sc, y, 6, C["SIB"], 2) + dot(x0 + (fl - lo) * sc, y, 6.5, C["ACCENT"])
        bv = max(r[a]["composite"] for a in F.RIVALS); best = [short[a] for a in F.RIVALS if abs(r[a]["composite"] - bv) < 1e-9]
        rel = "ahead" if fl > bv + 1e-9 else "tied" if abs(fl - bv) < 1e-9 else "behind"; won += rel == "ahead"; tied += rel == "tied"; lost += rel == "behind"
        b += t(660, y + 4, rel, 12, C["INK"]) + t(712, y + 4, f"{', '.join(best)} {r1(bv)}", 11, C["MUTE"])
        if r[SIB]["composite"] > fl + 1e-9: sib_up.append(r[SIB]["composite"] - fl)
    ly = bottom + 44
    b += dot(46, ly - 4, 6.5, C["ACCENT"]) + t(58, ly, "wise-men-flash", 11) + ring(170, ly - 4, 6, C["SIB"], 2) + t(182, ly, "full wise-men council", 11)
    b += dot(318, ly - 4, 4.5, C["OTHER"]) + t(328, ly, "the rival councils", 11) + ring(446, ly - 4, 7, C["TXT"]) + t(458, ly, "plain answer", 11)
    b += t(40, ly + 22, f"Against the best rival on each question: ahead {won}, tied {tied}, behind {lost}. The full council scored higher on {len(sib_up)} of {n}"
                        + (f", by {r1(min(sib_up))}–{r1(max(sib_up))} points." if sib_up else "."), 11, C["MUTE"])
    b += t(40, ly + 38, "Five of the eight pre-registered questions were run before the round was stopped. Three fresh Opus judges per question.", 11, C["MUTE"])
    return svg(860, ly + 54, b, f"Round 4 per-question scores over {n} questions: wise-men-flash versus the best rival ahead {won}, tied {tied}, behind {lost}; the full wise-men council higher on {len(sib_up)}")

def chart_axes(R):
    n = len(R); T = F.table(R); arms = by_total(T); top, rh = 118, 34
    cols = [("composite", "Total /25", 25, 222, 80)] + [(x, AXIS_NAME[x], 5, 364 + k * 94, 46) for k, x in enumerate(AXES)]
    val = lambda a, k: T[a]["mean"] if k == "composite" else T[a]["axes"][k]
    b = t(40, 32, "Round 4 scoreboard — the total and each rubric axis", 16, C["INK"], 600)
    b += t(40, 52, f"Mean of three judges over the {n} questions run · total out of 25, each axis 1–5 · sorted by total · the plain answer is the outlined bar", 12, C["TXT"])
    for key, title, mx, x, w in cols: b += t(x, top - 14, title, 11, C["INK"], 600)
    best = {key: max(val(a, key) for a in arms) for key, *_ in cols}
    for i, a in enumerate(arms):
        y = top + i * rh; yc = y + rh / 2; hero = a == HERO
        if hero: b += band(y + 2, rh - 4)
        b += t(206, yc + 4, NAME[a], 13, C["INK"], 700 if hero else 500, "end")
        for key, title, mx, x, w in cols:
            v = val(a, key); top_v = abs(v - best[key]) < 1e-9
            b += f'<rect x="{num(x)}" y="{num(yc - 5)}" width="{num(w)}" height="10" rx="3" fill="{C["GRID"]}" fill-opacity="0.6"/>\n' + bar(a, x, yc - 5, v / mx * w, 10, 3)
            b += t(x + w + 8, yc + 4, r1(v), 12, C["INK"] if top_v else C["TXT"], 700 if top_v else 400)
    lead = {x: [a for a in arms if abs(val(a, x) - best[x]) < 1e-9] for x in AXES}
    alone = [AXIS_NAME[x].lower() for x in AXES if lead[x] == [HERO]]; shared = [AXIS_NAME[x].lower() for x in AXES if HERO in lead[x] and len(lead[x]) > 1]
    above = sum(all(val(HERO, x) > val(a, x) for a in F.RIVALS) for x in AXES); fy = top + rh * len(arms) + 28
    b += t(40, fy, "Bold = highest in the column (ties bolded together). wise-men-flash had the top " + F.and_join(alone) + (f" and shared the top {F.and_join(shared)};" if shared else ";"), 11, C["MUTE"])
    b += t(40, fy + 16, f"it scored above every rival on {above} of 5 axes, and the full wise-men council led the rest. Warp's council ran on Claude models only.", 11, C["MUTE"])
    b += t(40, fy + 32, f"N = {n} of 8 pre-registered questions, three blind judges each, means shown.", 11, C["MUTE"])
    return svg(860, fy + 46, b, f"Round 4 scoreboard, means over {n} questions: " + "; ".join(f"{NAME[a]}: total {r1(T[a]['mean'])}, " + ", ".join(f"{AXIS_NAME[x].lower()} {r1(T[a]['axes'][x])}" for x in AXES) for a in arms))

def chart_speed(R):
    T = F.table(R); Cs = F.costs(); m = {a: F.med(Cs[a]["min"]) for a in F.ARMS}; usd = {a: F.med(Cs[a]["usd"]) for a in F.ARMS}
    px0, px1, py0, py1, xmax, ylo, yhi = 90, 540, 100, 360, 40, 15, 25
    X = lambda v: px0 + v / xmax * (px1 - px0); Y = lambda s: py1 - (s - ylo) / (yhi - ylo) * (py1 - py0)
    b = t(40, 32, "Round 4: score against time — how much of the council's quality arrives how fast", 16, C["INK"], 600)
    b += t(40, 52, "Mean of three blind judges' totals (max 25) against the median minutes per question. Cost: every token of the run and its subagents, list price.", 12, C["TXT"])
    for g in range(0, xmax + 1, 10): b += line(X(g), py0, X(g), py1, C["GRID"]) + t(X(g), py1 + 16, g, 11, C["MUTE"], anchor="middle")
    for g in range(ylo, yhi + 1): b += line(px0, Y(g), px1, Y(g), C["GRID"], 1, 'stroke-opacity="0.5"' if g % 5 else "") + (t(px0 - 8, Y(g) + 4, g, 11, C["MUTE"], anchor="end") if g % 5 == 0 else "")
    b += t((px0 + px1) / 2, py1 + 36, "median minutes per question", 11, C["TXT"], anchor="middle")
    b += t(px0 - 34, (py0 + py1) / 2, "total /25", 11, C["TXT"], anchor="middle", extra=f'transform="rotate(-90 {num(px0 - 34)} {num((py0 + py1) / 2)})"')
    place = {HERO: (14, 4, "start"), SIB: (-14, 4, "end"), "warp-council": (12, 4, "start"), "llm-council": (12, 4, "start"), "direct": (12, 4, "start")}
    for a in sorted(F.ARMS, key=lambda a: a == HERO):
        x, y = X(m[a]), Y(T[a]["mean"]); dx, dy, anc = place[a]
        b += (ring(x, y, 7, C["TXT"]) if a == "direct" else dot(x, y, 7.5 if a == HERO else 6, colour(a))) + t(x + dx, y + dy, NAME[a], 12, C["INK"], 700 if a == HERO else 500, anc)
    tx, ty = 580, 118; b += t(tx, ty, "arm", 11, C["MUTE"], 600) + t(tx + 172, ty, "score", 11, C["MUTE"], 600, "end") + t(tx + 216, ty, "min", 11, C["MUTE"], 600, "end") + t(tx + 262, ty, "cost", 11, C["MUTE"], 600, "end")
    for i, a in enumerate(by_total(T)):
        y = ty + 26 + i * 26; hero = a == HERO
        if hero: b += band(y - 17, 24, tx - 8, 280)
        w, col = (700, C["INK"]) if hero else (400, C["TXT"])
        b += t(tx, y, NAME[a], 12, col, w) + t(tx + 172, y, r1(T[a]["mean"]), 12, col, w, "end") + t(tx + 216, y, r1(m[a]), 12, col, w, "end") + t(tx + 262, y, f"${F.r2(usd[a])}", 12, col, w, "end")
    frac_t, frac_c = m[HERO] / m[SIB], usd[HERO] / usd[SIB]; fy = py1 + 66
    b += t(40, fy, f"wise-men-flash scored {r1(T[SIB]['mean'] - T[HERO]['mean'])} below the full wise-men council in {round(frac_t * 100)}% of its time and {round(frac_c * 100)}% of its cost, and "
                   f"{r1(T[HERO]['mean'] - T['warp-council']['mean'])} above Warp's council,", 11, C["MUTE"])
    b += t(40, fy + 16, f"which answered {r1(m[HERO] - m['warp-council'])} minutes sooner for ${F.r2(usd[HERO] - usd['warp-council'])} less. Time: the orchestrator's first-to-last transcript timestamp, median over runs the usage", 11, C["MUTE"])
    b += t(40, fy + 32, "limit did not interrupt (it stopped every council arm once, on R402). N = 5 questions · PREREG-4.md · no council can beat a plain answer on time or cost.", 11, C["MUTE"])
    return svg(860, fy + 46, b, "Round 4 score against median minutes per question: " + ", ".join(f"{NAME[a]} {r1(T[a]['mean'])} in {r1(m[a])} min at ${F.r2(usd[a])}" for a in by_total(T)))

# ---------- round 5 (PREREG-5): wise-men-flash and wise-men 3.14.0 against every rival at its latest version ----------
import h2h5 as G
G_NAME = {G.FL: "wise-men-flash", G.WM: "wise-men full council", "warp-council": "Warp council", "llm-council": "llm-council", "lifeos-council": "LifeOS Council",
          "ecc-council": "ECC council", "brainstorming": "brainstorming", "grilling": "grilling", "direct": "plain answer"}
G_SRC = {G.FL: "this repo · v0.1.0, three members", G.WM: "wise-men 3.14.0 · sibling skill", "warp-council": "warpdotdev", "llm-council": "aiwithremy", "lifeos-council": "danielmiessler/LifeOS",
         "ecc-council": "affaan-m/ECC", "brainstorming": "obra/superpowers", "grilling": "mattpocock/skills", "direct": "no skill"}
TOPIC.update({"R501": "Row-level security or app-layer checks?", "R502": "Outages every January after a freeze", "R503": "Build or buy an automation builder?",
              "R504": "A $15,000 lifetime value, 3 years in", "R505": "A records study linking a drug to dementia", "R506": "Correcting the error behind a closure",
              "R507": "An unverifiable tip about a candidate", "R508": "Buying the business I work for"})
def g_load(): R = G.load(); return {q: {a: R[q][a] for a in G.ARMS} for q in G.RUN_ORDER if q in R}
def g_mean(rows, a, k="composite"): return st.mean(r[a][k] for r in rows.values())
def g_bar(a, x, y, w, h, r=4): return hbar_outline(x, y, w, h, C["TXT"], r) if a == "direct" else hbar(x, y, w, h, C["ACCENT"] if a == G.FL else C["SIB"] if a == G.WM else C["BAR2"], r)
def g_arms(rows): return sorted(G.ARMS, key=lambda a: (-g_mean(rows, a), G.ARMS.index(a)))
def g_note(n): return f"In progress: {n} of 8 pre-registered questions judged; the rest are being run in the pre-registered order, and these charts are regenerated as each is judged." if n < 8 else ""

def chart_round5(R):
    n = len(R); x0, sc, top, rh = 250, 15.6, 112, 44; arms = g_arms(R); bottom = top + rh * len(arms) - 6
    b = t(40, 32, f"Round 5{', in progress' if n < 8 else ''}: every rival at its latest version — {n} of 8 new questions, three blind judges each", 16, C["INK"], 600)
    b += t(40, 52, "Sum of 5 rubric axes (1–5 each, max 25), mean of 3 judges, averaged over the questions. Right: flash's lead, 95% bootstrap interval.", 12, C["TXT"])
    b += t(40, 68, "Nine arms judged together under the error-first judge; questions from a blind author; every answer new, this skill run as installed.", 12, C["TXT"])
    b += t(840, top - 12, "flash ahead by [95%]", 11, C["MUTE"], anchor="end")
    for g in range(0, 26, 5):
        x = x0 + g * sc; b += line(x, top - 4, x, bottom, C["GRID"]) + t(x, bottom + 16, g, 11, C["MUTE"], anchor="middle")
    for i, a in enumerate(arms):
        y = top + i * rh; m = g_mean(R, a); hero = a == G.FL
        if hero: b += band(y - 3, rh - 2)
        b += t(x0 - 14, y + 15, G_NAME[a], 13, C["INK"], 700 if hero else 500, "end") + t(x0 - 14, y + 30, G_SRC[a], 11, C["MUTE"], anchor="end")
        b += g_bar(a, x0, y + 6, m * sc, 22) + t(x0 + m * sc + 8, y + 22, r1(m), 13, C["INK"], 700 if hero else 500)
        if hero: b += t(840, y + 22, "—", 12, C["MUTE"], anchor="end"); continue
        c = G.compare(R, a, G.FL); b += t(840, y + 22, f"{sg(c['diff'])}  [{sg(c['lo'])}, {sg(c['hi'])}]", 12, C["INK"] if c["lo"] > 0 else C["TXT"], 600 if c["lo"] > 0 else 400, "end")
    fy = bottom + 42; clear = sum(G.compare(R, a, G.FL)["lo"] > 0 for a in G.RIVALS)
    b += t(40, fy, f"An interval above zero is the pre-registered bar for \"clearly ahead\": met against {clear} of {len(G.RIVALS)} rivals{' so far' if n < 8 else ''}. The red bar is the full wise-men council.", 11, C["MUTE"])
    b += t(40, fy + 16, g_note(n) or "Intervals resample questions (10,000 draws), not judges.", 11, C["MUTE"])
    b += t(40, fy + 32, f"N = {n} · Warp's council on Claude models only · LifeOS and brainstorming given the files their skills name · three fresh Opus judges per question · PREREG-5.md", 11, C["MUTE"])
    return svg(860, fy + 46, b, f"Round 5{' (in progress)' if n < 8 else ''} mean total score out of 25 on {n} new questions, three blind judges each: " + ", ".join(f"{G_NAME[a]} {r1(g_mean(R, a))}" for a in arms))

def chart_round5_questions(R):
    qs = list(R); n = len(qs); lo = min(10, int(min(r[a]["composite"] for r in R.values() for a in r)))
    x0, x1, hi = 300, 640, 25; sc = (x1 - x0) / (hi - lo); top, rh = 112, 32; bottom = top + rh * (n - 1) + 16
    others = [a for a in G.RIVALS if a != "direct"]; short = dict(G_NAME, **{"warp-council": "Warp", "lifeos-council": "LifeOS", "ecc-council": "ECC"})
    b = t(40, 32, f"Round 5{', in progress' if n < 8 else ''}, question by question", 16, C["INK"], 600)
    b += t(40, 52, "Mean of three blind judges' totals (max 25): flash, the full wise-men council, six rival skills and a plain answer", 12, C["TXT"])
    b += t(660, top - 22, "flash vs the best rival", 11, C["MUTE"])
    for g in range(lo, 26, 5):
        x = x0 + (g - lo) * sc; b += line(x, top - 16, x, bottom, C["GRID"]) + t(x, bottom + 16, g, 11, C["MUTE"], anchor="middle")
    won = tied = lost = 0
    for i, q in enumerate(qs):
        y = top + i * rh; r = R[q]; fl = r[G.FL]["composite"]; vals = [r[a]["composite"] for a in G.ARMS]
        b += t(40, y + 4, q, 11, C["MUTE"]) + t(84, y + 4, TOPIC[q], 12, C["INK"])
        b += line(x0 + (min(vals) - lo) * sc, y, x0 + (max(vals) - lo) * sc, y, C["GRID"], 2) + ring(x0 + (r["direct"]["composite"] - lo) * sc, y, 7, C["TXT"])
        for a in others: b += dot(x0 + (r[a]["composite"] - lo) * sc, y, 4.5, C["OTHER"])
        b += ring(x0 + (r[G.WM]["composite"] - lo) * sc, y, 6, C["SIB"], 2) + dot(x0 + (fl - lo) * sc, y, 6.5, C["ACCENT"])
        bv = max(r[a]["composite"] for a in G.RIVALS); best = [short[a] for a in G.RIVALS if abs(r[a]["composite"] - bv) < 1e-9]
        rel = "ahead" if fl > bv + 1e-9 else "tied" if abs(fl - bv) < 1e-9 else "behind"; won += rel == "ahead"; tied += rel == "tied"; lost += rel == "behind"
        b += t(660, y + 4, rel, 12, C["INK"]) + t(712, y + 4, f"{', '.join(best)} {r1(bv)}", 11, C["MUTE"])
    ly = bottom + 44
    b += dot(46, ly - 4, 6.5, C["ACCENT"]) + t(58, ly, "wise-men-flash", 11) + ring(170, ly - 4, 6, C["SIB"], 2) + t(182, ly, "full wise-men council", 11)
    b += dot(318, ly - 4, 4.5, C["OTHER"]) + t(328, ly, "the six rival skills", 11) + ring(456, ly - 4, 7, C["TXT"]) + t(468, ly, "plain answer", 11)
    b += t(40, ly + 22, f"Against the best rival on each question: ahead {won}, tied {tied}, behind {lost}. Questions in the pre-registered run order.", 11, C["MUTE"])
    b += t(40, ly + 38, g_note(n) or "Eight new questions from a blind author, one per slot. Three fresh Opus judges per question.", 11, C["MUTE"])
    return svg(860, ly + 54, b, f"Round 5{' (in progress)' if n < 8 else ''} per-question scores over {n} questions: wise-men-flash versus the best rival ahead {won}, tied {tied}, behind {lost}")

def chart_round5_axes(R):
    n = len(R); arms = g_arms(R); top, rh = 118, 32
    cols = [("composite", "Total /25", 25, 222, 80)] + [(x, AXIS_NAME[x], 5, 364 + k * 94, 46) for k, x in enumerate(AXES)]
    b = t(40, 32, f"Round 5 scoreboard{', in progress' if n < 8 else ''} — the total and each rubric axis", 16, C["INK"], 600)
    b += t(40, 52, f"Mean of three judges over the {n} questions judged · total out of 25, each axis 1–5 · sorted by total · the plain answer is the outlined bar", 12, C["TXT"])
    for key, title, mx, x, w in cols: b += t(x, top - 14, title, 11, C["INK"], 600)
    best = {key: max(g_mean(R, a, key) for a in arms) for key, *_ in cols}
    for i, a in enumerate(arms):
        y = top + i * rh; yc = y + rh / 2; hero = a == G.FL
        if hero: b += band(y + 2, rh - 4)
        b += t(206, yc + 4, G_NAME[a], 13, C["INK"], 700 if hero else 500, "end")
        for key, title, mx, x, w in cols:
            v = g_mean(R, a, key); top_v = abs(v - best[key]) < 1e-9
            b += f'<rect x="{num(x)}" y="{num(yc - 5)}" width="{num(w)}" height="10" rx="3" fill="{C["GRID"]}" fill-opacity="0.6"/>\n' + g_bar(a, x, yc - 5, v / mx * w, 10, 3)
            b += t(x + w + 8, yc + 4, r1(v), 12, C["INK"] if top_v else C["TXT"], 700 if top_v else 400)
    above = sum(all(g_mean(R, G.FL, x) > g_mean(R, a, x) for a in G.RIVALS) for x in AXES); fy = top + rh * len(arms) + 28
    b += t(40, fy, f"Bold = highest in the column (ties bolded together). wise-men-flash scored above every rival on {above} of the 5 axes{' so far' if n < 8 else ''}.", 11, C["MUTE"])
    b += t(40, fy + 16, g_note(n) or f"N = {n} questions, three blind judges each, means shown.", 11, C["MUTE"])
    return svg(860, fy + 30, b, f"Round 5 scoreboard{' (in progress)' if n < 8 else ''}, means over {n} questions: " + "; ".join(f"{G_NAME[a]}: total {r1(g_mean(R, a))}, " + ", ".join(f"{AXIS_NAME[x].lower()} {r1(g_mean(R, a, x))}" for x in AXES) for a in arms))

def chart_round5_speed(R):
    n = len(R); Cs = G.costs(); sc = {a: g_mean(R, a) for a in G.ARMS}; m = {a: G.med(Cs[a]["min"]) for a in G.ARMS}; usd = {a: G.med(Cs[a]["usd"]) for a in G.ARMS}
    xlo = 0.5 if min(m.values()) < 1 else 1; xhi = 100 if max(m.values()) > 50 else 50; ylo, yhi = min(14, int(min(sc.values())) - 1), 25
    px0, px1, py0, py1 = 90, 540, 100, 360  # time on a log scale: seven of the nine arms answer inside ten minutes
    X = lambda v: px0 + math.log(v / xlo) / math.log(xhi / xlo) * (px1 - px0); Y = lambda s: py1 - (s - ylo) / (yhi - ylo) * (py1 - py0)
    b = t(40, 32, f"Round 5{', in progress' if n < 8 else ''}: score against time — every arm, median minutes per question", 16, C["INK"], 600)
    b += t(40, 52, "Mean of three blind judges' totals (max 25) against the median minutes per question. Cost: every token of the run and its subagents, list price.", 12, C["TXT"])
    for g in (0.5, 1, 2, 5, 10, 20, 50, 100):
        if xlo <= g <= xhi: b += line(X(g), py0, X(g), py1, C["GRID"]) + t(X(g), py1 + 16, num(float(g)), 11, C["MUTE"], anchor="middle")
    for g in range(ylo, yhi + 1): b += line(px0, Y(g), px1, Y(g), C["GRID"], 1, 'stroke-opacity="0.5"' if g % 5 else "") + (t(px0 - 8, Y(g) + 4, g, 11, C["MUTE"], anchor="end") if g % 5 == 0 else "")
    b += t((px0 + px1) / 2, py1 + 36, "median minutes per question (log scale)", 11, C["TXT"], anchor="middle")
    b += t(px0 - 34, (py0 + py1) / 2, "total /25", 11, C["TXT"], anchor="middle", extra=f'transform="rotate(-90 {num(px0 - 34)} {num((py0 + py1) / 2)})"')
    pts = {a: (X(m[a]), Y(sc[a])) for a in G.ARMS}; boxes = [(x - 8, y - 8, x + 8, y + 8) for x, y in pts.values()]; labels = ""
    def free(bx): return px0 - 4 <= bx[0] and bx[2] <= px1 + 30 and py0 - 14 <= bx[1] and bx[3] <= py1 + 2 and not any(bx[0] < o[2] and o[0] < bx[2] and bx[1] < o[3] and o[1] < bx[3] for o in boxes)
    for a in sorted(G.ARMS, key=lambda a: (a not in (G.FL, G.WM), -sc[a])):  # the two wise-men arms place their labels first
        x, y = pts[a]; name = G_NAME[a]; w = len(name) * 6.6 + 4
        for dx, dy, anc in ((11, 4, "start"), (-11, 4, "end"), (0, -12, "middle"), (0, 20, "middle"), (11, -9, "start"), (11, 16, "start"), (-11, -9, "end"), (-11, 16, "end")):
            x0 = x + dx if anc == "start" else x + dx - w if anc == "end" else x - w / 2; bx = (x0, y + dy - 11, x0 + w, y + dy + 3)
            if free(bx): break
        boxes.append(bx); labels += t(x + dx, y + dy, name, 12, C["INK"], 700 if a == G.FL else 500, anc)
    for a in sorted(G.ARMS, key=lambda a: a == G.FL):
        x, y = pts[a]; b += ring(x, y, 7, C["TXT"]) if a == "direct" else dot(x, y, 7.5 if a == G.FL else 6, C["ACCENT"] if a == G.FL else C["SIB"] if a == G.WM else C["OTHER"])
    b += labels
    tx, ty = 580, 118; b += t(tx, ty, "arm", 11, C["MUTE"], 600) + t(tx + 172, ty, "score", 11, C["MUTE"], 600, "end") + t(tx + 216, ty, "min", 11, C["MUTE"], 600, "end") + t(tx + 262, ty, "cost", 11, C["MUTE"], 600, "end")
    for i, a in enumerate(g_arms(R)):
        y = ty + 26 + i * 26; hero = a == G.FL
        if hero: b += band(y - 17, 24, tx - 8, 280)
        w, col = (700, C["INK"]) if hero else (400, C["TXT"])
        b += t(tx, y, G_NAME[a], 12, col, w) + t(tx + 172, y, r1(sc[a]), 12, col, w, "end") + t(tx + 216, y, r1(m[a]), 12, col, w, "end") + t(tx + 262, y, f"${G.r2(usd[a])}", 12, col, w, "end")
    best = max(G.RIVALS, key=lambda a: (sc[a], -G.ARMS.index(a))); fy = max(py1 + 66, ty + 26 * 10 + 20)
    dw, dt, dc = sc[G.FL] - sc[G.WM], m[G.FL] - m[best], usd[G.FL] - usd[best]
    b += t(40, fy, f"wise-men-flash scored {r1(abs(dw))} {'below' if dw < 0 else 'above'} the full wise-men council in {round(m[G.FL] / m[G.WM] * 100)}% of its time and {round(usd[G.FL] / usd[G.WM] * 100)}% of its cost, and "
                   f"{r1(sc[G.FL] - sc[best])} above the best-scoring rival, {G_NAME[best]},", 11, C["MUTE"])
    b += t(40, fy + 16, f"taking {r1(abs(dt))} minutes {'longer' if dt > 0 else 'less'} and ${G.r2(abs(dc))} {'more' if dc > 0 else 'less'} a question. Time: the orchestrator's first-to-last transcript timestamp, median over runs the usage limit did not interrupt.", 11, C["MUTE"])
    b += t(40, fy + 32, g_note(n) or f"N = {n} questions · PREREG-5.md · no council can beat a plain answer on time or cost.", 11, C["MUTE"])
    return svg(860, fy + 46, b, f"Round 5{' (in progress)' if n < 8 else ''} score against median minutes per question: " + ", ".join(f"{G_NAME[a]} {r1(sc[a])} in {r1(m[a])} min at ${G.r2(usd[a])}" for a in g_arms(R)))

# ---------- banner: three council members and a bolt in the wise-men pixel style, one 5 px grid, three-tone shading ----------
BU, B_OUTLINE = 5, "#120b09"
B_RAMP = {  # material: highlight, base, shadow
    "O": ("#e89272", "#d97757", "#a6563b"), "L": ("#a6563b", "#8c4730", "#6e3624"), "C": ("#474d57", "#30353d", "#1f2329"),
    "R": ("#b3303a", "#8e1b24", "#5e1117"), "A": ("#e5b04e", "#c48a22", "#8a5e12"), "Z": ("#ffe08a", "#f2b632", "#b97f12")}
B_FIXED = {"k": "#16100e", "l": "#4a505a", "r": "#8e1b24", "x": "#5e1117", "Y": "#d4a72c", "N": "#9fb0c2"}
LEGS = ["..L.L..L.L..", "..L.L..L.L.."]
FACE, BLANK = ".OOOOOOOOOO.", "............"
def _at(ch, *cells): return {rc: ch for rc in cells}
SPRITES = {
    "devils-advocate": ([".R........R.", ".RR......RR.", "..RR....RR..", FACE, FACE, FACE, FACE, "RRRRRRRRRRRR", "RRRRRRRRRRRR", ".RRRRRRRRRR.", *LEGS],
                        {**_at("k", (3, 2), (3, 3), (4, 4), (3, 9), (3, 8), (4, 7), (5, 3), (6, 3), (5, 8), (6, 8)), **_at("x", (7, 5), (7, 6))}),
    "anchor": (["...AAAAAA...", "..AAAAAAAA..", "AAAAAAAAAAAA", FACE, FACE, FACE, FACE, "CCCCCCCCCCCC", "CCCCCCCCCCCC", ".CCCCCCCCCC.", *LEGS],
               {**_at("k", (3, 2), (3, 3), (3, 4), (3, 7), (3, 8), (3, 9), (5, 3), (6, 3), (5, 8), (6, 8)), **_at("Y", (8, 1), (8, 10))}),
    "domain": ([BLANK, BLANK, BLANK, FACE, FACE, FACE, FACE, "CCCCCCCCCCCC", "CCCCCCCCCCCC", ".CCCCCCCCCC.", *LEGS],
               {**_at("k", (4, 2), (4, 3), (4, 4), (4, 7), (4, 8), (4, 9), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (5, 9), (6, 2), (6, 3), (6, 4), (6, 7), (6, 8), (6, 9)),
                **_at("N", (5, 3), (5, 8)), **_at("l", (7, 4), (8, 4), (7, 7), (8, 7)), **_at("x", (7, 5), (7, 6)), **_at("r", (8, 5), (8, 6), (9, 5), (9, 6))}),
    "bolt": (["......ZZZZ", ".....ZZZZ.", ".....ZZZ..", "....ZZZZ..", "....ZZZ...", "...ZZZZ...", "...ZZZZZZZ", "..ZZZZZZZ.",
              "......ZZZ.", ".....ZZZ..", ".....ZZ...", "....ZZZ...", "....ZZ....", "...ZZ.....", "...Z......", "..Z......."], {}),
}

def _sprite(name, x0, y0):
    grid, marks = SPRITES[name]
    g = [list(row) for row in grid]
    for (r, c), ch in marks.items(): g[r][c] = ch
    h, w = len(g), len(g[0])
    solid = lambda r, c: 0 <= r < h and 0 <= c < w and g[r][c] != "."
    px = lambda r, c, col: f'<rect x="{x0 + c * BU}" y="{y0 + r * BU}" width="{BU}" height="{BU}" fill="{col}"/>'
    out = [px(r, c, B_OUTLINE) for r in range(-1, h + 1) for c in range(-1, w + 1)
           if not solid(r, c) and any(solid(r + a, c + b) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
    for r in range(h):
        for c in range(w):
            m = g[r][c]
            if m == ".": continue
            if m in B_RAMP:
                hi, base, sh = B_RAMP[m]
                col = hi if not solid(r - 1, c) or not solid(r, c - 1) else sh if not solid(r + 1, c) or not solid(r, c + 1) else base
            else:
                col = B_FIXED[m]
            out.append(px(r, c, col))
    return "".join(out)

def banner():
    mw, gap, x0 = 12 * BU, 8, 22
    xs = [x0, x0 + mw + gap, x0 + 2 * (mw + gap)]; tier_top = [158, 144]
    b = '<rect width="860" height="190" rx="14" fill="#0d1117"/>\n'
    for tier, left, right in ((0, xs[0] - 10, xs[2] + mw + 10), (1, xs[1] - 6, xs[1] + mw + 6)):
        b += (f'<rect x="{left}" y="{tier_top[tier]}" width="{right - left}" height="{178 - tier_top[tier]}" fill="#161b22"/>'
              f'<rect x="{left}" y="{tier_top[tier]}" width="{right - left}" height="3" fill="{"#b8740c" if tier == 1 else "#262c34"}"/>\n')
    b += '<g shape-rendering="crispEdges">' + _sprite("devils-advocate", xs[0], tier_top[0] - 12 * BU) + _sprite("anchor", xs[1], tier_top[1] - 12 * BU)
    b += _sprite("domain", xs[2], tier_top[0] - 12 * BU) + _sprite("bolt", xs[2] + mw + 22, 34) + "</g>\n"
    tx = xs[2] + mw + 96
    b += f'<rect x="{tx + 2}" y="50" width="14" height="4" fill="#e2a336"/>'
    b += t(tx + 24, 56, "FAST COUNCIL · FOUR CALLS", 11, "#8b949e", 700, extra='letter-spacing="3"')
    b += (f'<text x="{tx}" y="106" font-size="50" font-weight="800" fill="#f0f6fc" text-anchor="start" letter-spacing="-1.5">wise-men-'
          f'<tspan fill="#e2a336">flash</tspan></text>\n')
    b += t(tx + 2, 134, "Three Claude subagents down three reasoning paths, one checked", 15, "#9198a1")
    b += t(tx + 2, 154, "decision memo, dissent intact — in a third of the full council's time.", 15, "#9198a1")
    return svg(860, 190, b, "wise-men-flash: a pixel-art council of three, a Devil's Advocate, a practitioner in a hard hat and an analyst, beside a lightning bolt")

if __name__ == "__main__":
    R = F.load(); R5 = g_load(); os.makedirs(OUT, exist_ok=True); wrote = []
    charts = [("round4", chart_round4, R), ("round4-questions", chart_questions, R), ("round4-axes", chart_axes, R), ("round4-speed", chart_speed, R),
              ("round5", chart_round5, R5), ("round5-questions", chart_round5_questions, R5), ("round5-axes", chart_round5_axes, R5), ("round5-speed", chart_round5_speed, R5)]
    for theme, suffix in (("light", ""), ("dark", "-dark")):
        C.clear(); C.update(THEMES[theme])
        for name, fn, data in charts:
            open(os.path.join(OUT, name + suffix + ".svg"), "w").write(fn(data)); wrote.append(name + suffix)
    open(os.path.join(OUT, "banner.svg"), "w").write(banner()); wrote.append("banner")
    print("wrote", ", ".join(wrote))
