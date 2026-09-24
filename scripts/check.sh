#!/usr/bin/env bash
# Structural invariants for wise-men-flash. Run from the repo root:
#   PII_TERMS='<pattern>' ./scripts/check.sh
# PII_TERMS is never committed; pass it at call time.
set -u
cd "$(dirname "$0")/.." || exit 2
fail=0
say() { printf '%s %s\n' "$([ "$2" = ok ] && echo '  ok ' || echo 'FAIL')" "$1"; }

# 1. version stamps agree
v_skill=$(sed -n 's/^version: //p' SKILL.md | head -1)
v_plug=$(sed -n 's/.*"version": "\([^"]*\)".*/\1/p' .claude-plugin/plugin.json | head -1)
[ "$v_skill" = "$v_plug" ] && say "version stamps agree ($v_skill)" ok || { say "version mismatch: SKILL $v_skill vs plugin $v_plug" FAIL; fail=1; }

# 2. SKILL.md is self-contained — it must not point at resource files this repo doesn't ship
if grep -Eq 'resources/(personas|prompts|model-routing|council-record)' SKILL.md; then
  say "SKILL.md references resources/ files this skill does not ship" FAIL; fail=1
else say "SKILL.md self-contained (no resources/ references)" ok; fi

# 3. the four synthesis checks are all present
missing=""
for c in DISSENT DISCLOSURE CLAIMS COVERAGE; do grep -q "$c" SKILL.md || missing="$missing $c"; done
[ -z "$missing" ] && say "four synthesis checks present" ok || { say "synthesis check(s) missing:$missing" FAIL; fail=1; }

# 4. flash IS the fast tier — no stray --fast flag or peer-review/debate stage should be described as part of it
if grep -q -- '--fast' SKILL.md; then say "stray --fast flag in SKILL.md (flash is already the fast tier)" FAIL; fail=1
else say "no stray --fast flag" ok; fi
if grep -Eq 'Stage 2|peer review|debate round' SKILL.md && ! grep -q 'no peer review\|no debate\|No peer review\|no peer-review' SKILL.md; then
  say "SKILL.md mentions peer review / debate without marking them absent" FAIL; fail=1
else say "peer review / debate correctly marked absent" ok; fi

# 4b. the member agent's frontmatter must start on line 1 — anything above it (a comment, a blank line) makes the
#     parser skip the block, and the agent then registers WITHOUT its tool restriction, silently
if [ "$(head -1 agents/wise-member.md)" = "---" ] && grep -q '^tools: Read, Grep, Glob$' agents/wise-member.md; then
  say "wise-member.md frontmatter on line 1 with tools: Read, Grep, Glob" ok
else say "wise-member.md frontmatter not on line 1 or tools line wrong (agent would register without its tool restriction)" FAIL; fail=1; fi

# 5. installed agent copy (clone install) matches the shipped file, when present
inst="$HOME/.claude/agents/wise-member.md"
if [ -f "$inst" ]; then
  diff -q agents/wise-member.md "$inst" >/dev/null 2>&1 && say "installed wise-member.md matches shipped copy" ok \
    || say "installed wise-member.md differs from shipped copy (re-copy after edits)" ok  # informational: wise-men may own this file
fi

# 6. PII sweep (pattern supplied at call time, never committed)
if [ -n "${PII_TERMS:-}" ]; then
  files=$(git ls-files 2>/dev/null)   # outside a repo (or before the first add) fall back to the working tree, never to an empty scan
  [ -z "$files" ] && files=$(find . -type f -not -path './.git/*' -not -path './plans/*')
  hits=$(printf '%s\n' "$files" | xargs grep -InE "$PII_TERMS" 2>/dev/null | grep -v '^\./plans/')
  [ -z "$hits" ] && say "PII sweep clean" ok || { say "PII sweep hit:"; printf '%s\n' "$hits"; fail=1; }
else say "PII sweep skipped (set PII_TERMS to run it)" ok; fi

[ "$fail" = 0 ] && echo "ALL CHECKS PASSED" || echo "CHECKS FAILED"
exit $fail
