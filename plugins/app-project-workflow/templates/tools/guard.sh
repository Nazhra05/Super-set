#!/usr/bin/env bash
# Deterministic scope and test-integrity check. Usage: tools/guard.sh <worktree> <base-branch> <ticket.md>
# Fails (exit 1) on: a file outside the ticket "## Allow" globs, deleted test files,
# skip/only/todo markers added, fewer assertion lines than the base,
# or any commit on the branch above the base (subagents must not commit; run guard before the router commits).
# Patterns come from tools/workflow.conf.
set -f
. "$(cd "$(dirname "$0")" && pwd)/workflow.conf"
WT="${1:?worktree}"; BASE="${2:?base branch}"; T="${3:?ticket}"
T="$(cd "$(dirname "$T")" && pwd)/$(basename "$T")"   # absolute: we cd into the worktree below
cd "$WT"
MB="$(git merge-base "$BASE" HEAD)"
allow="$(awk '/^## Allow/{f=1;next} /^## /{f=0} f && /^- `/{sub(/^- `/,"");sub(/`.*$/,"");print}' "$T")"
fail=0
changed="$( { git diff --name-only "$MB"; git ls-files --others --exclude-standard; } | sort -u)"
while IFS= read -r f; do
  [ -z "$f" ] && continue
  ok=0
  while IFS= read -r g; do
    [ -z "$g" ] && continue
    case "$f" in $g) ok=1 ;; esac
  done <<< "$allow"
  if [ "$ok" = 0 ]; then echo "OUT-OF-SCOPE: $f"; fail=1; fi
done <<< "$changed"
while IFS= read -r f; do
  [ -z "$f" ] && continue
  echo "$f" | grep -Eq "$TEST_PATH_RE" && { echo "TEST-DELETED: $f"; fail=1; }
done <<< "$(git diff --diff-filter=D --name-only "$MB")"
d="$(git diff -U0 "$MB")"
if echo "$d" | grep -E '^\+[^+]' | grep -Eq "$SKIP_RE"; then
  echo "TEST-WEAKENED: skip/only/todo marker added"; fail=1
fi
rem="$(echo "$d" | grep -E '^-[^-]' | grep -Ec "$ASSERT_RE" || true)"
add="$(echo "$d" | grep -E '^\+[^+]' | grep -Ec "$ASSERT_RE" || true)"
if [ "$rem" -gt "$add" ]; then echo "ASSERTIONS-REDUCED: removed $rem assertion lines, added $add"; fail=1; fi
n="$(git rev-list --count "$MB"..HEAD)"
if [ "$n" -gt 0 ]; then echo "COMMITTED: $n commit(s) above base; subagents must not commit"; fail=1; fi
[ "$fail" = 0 ] && echo "guard: OK"
exit "$fail"
