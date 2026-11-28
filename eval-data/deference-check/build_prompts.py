#!/usr/bin/env python3
"""Rebuild the 18 checker prompts of this check.

The memos and the honest closings come from an outside tester's bench,
github.com/mrtooher/fable-mode at commit 26756a9, folder
bench/judgment/qwen-rounds/round7/. That repo has no licence file, so they are
not copied here. Clone it, then run from this folder:

    python3 build_prompts.py /path/to/fable-mode

Prompts are written to prompts/. The checker text comes from SKILL.md at
aa551a7 (0.3.1, "old") and at the 0.3.2 commit ("new"), read with git show,
so the prompts are byte-identical to the ones that ran.
"""
import os, re, subprocess, sys

R7 = os.path.join(sys.argv[1], "bench/judgment/qwen-rounds/round7")
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = {"old": "aa551a7", "new": None}  # new: the commit whose message starts "0.3.2:"

def skill_text(rev):
    if rev is None:
        rev = subprocess.run(["git", "log", "--format=%h", "--grep=^0.3.2:", "-1"], cwd=HERE,
                             capture_output=True, text=True, check=True).stdout.strip()
    return subprocess.run(["git", "show", f"{rev}:SKILL.md"], cwd=HERE,
                          capture_output=True, text=True, check=True).stdout

def checker_parts(s):
    head = re.search(r"```\n(You are checking a decision memo.*?)\n```", s, re.S).group(1)
    checks = re.search(r"The five checks:\n\n(.*?)\n\nReturn format:", s, re.S).group(1)
    ret = re.search(r"Return format:\n```\n(.*?)\n```", s, re.S).group(1)
    return head, checks, ret

qs = {m.group(1): m.group(2) for m in
      (re.match(r"(\d)\. (.*)", l.strip()) for l in open(f"{R7}/case/questions.md")) if m}
calls = {(m.group(1), m.group(2)): m.group(3) for m in
         (re.match(r"Q(\d) Call (\d): (.*)", l.strip()) for l in open(f"{R7}/case/calls.md")) if m}

def split_memo(q):
    lines = open(f"{R7}/out/memo-q{q}.md").read().rstrip().split("\n")
    foot = [l for l in lines if "general-purpose" in l or "requested `fable`" in l]
    body = [l for l in lines if l not in foot]
    while body and body[-1].strip() in ("", "---"):
        body.pop()
    return "\n".join(body), "\n".join(foot)

runs = [(f"q{q}-c{c}-{k}", "new", q, c, f"{HERE}/planted/q{q}-c{c}-{k}.md")
        for q, c, k in [("1","1","blatant"),("1","1","subtle"),("2","2","blatant"),("2","2","subtle"),
                        ("3","2","blatant"),("3","2","subtle"),("1","2","away"),("2","1","away"),("3","1","away")]]
runs += [(f"q{q}-c{c}-honest", "new", q, c, f"{R7}/out/close-q{q}-c{c}.md")
         for q, c in [("1","1"),("1","2"),("2","1"),("2","2"),("3","1"),("3","2")]]
runs += [(f"q{q}-c{c}-honest", "old", q, c, f"{R7}/out/close-q{q}-c{c}.md")
         for q, c in [("1","1"),("2","2"),("3","2")]]

os.makedirs(f"{HERE}/prompts", exist_ok=True)
for name, ver, q, c, closing in runs:
    head, checks, ret = checker_parts(skill_text(SKILL[ver]))
    body, foot = split_memo(q)
    draft = body + "\n\n" + open(closing).read().strip() + "\n\n---\n" + foot
    p = (head.replace("{question verbatim}", qs[q])
             .replace('{the shared brief, or "None needed — the question is self-contained."}',
                      "None needed — the question is self-contained.")
             .replace("{the corrected draft}", draft))
    p = re.sub(r"\{my-call-first mode only:.*?\}", calls[(q, c)], p)
    p += "\n\nThe five checks:\n\n" + checks + "\n\nReturn format:\n```\n" + ret + "\n```\n"
    open(f"{HERE}/prompts/{name}-{ver}.txt", "w").write(p)
print(len(runs), "prompts written to prompts/")
