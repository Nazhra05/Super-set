#!/usr/bin/env bash
# Scope check for one ticket, in a git repo without worktrees. Usage: tools/scope.sh <ticket.md>
# Fails (exit 1) when a changed, added, or deleted file (git status against HEAD) is outside the ticket's "## Allow" globs.
# Run it with no other ticket's changes in the working tree; commit or stash the previous ticket first.
set -f
T="${1:?ticket}"
T="$(cd "$(dirname "$T")" && pwd)/$(basename "$T")"
cd "$(cd "$(dirname "$0")/.." && pwd)"
git rev-parse --git-dir >/dev/null 2>&1 || { echo "scope: not a git repo, check skipped"; exit 2; }
allow="$(awk '/^## Allow/{f=1;next} /^## /{f=0} f && /^- `/{sub(/^- `/,"");sub(/`.*$/,"");print}' "$T")"
fail=0
changed="$(git status --porcelain --untracked-files=all | sed -E 's/^.. //; s/^.* -> //; s/^"(.*)"$/\1/')"
ticket_rel="${T#"$(pwd)/"}"
while IFS= read -r f; do
  [ -z "$f" ] && continue
  [ "$f" = "$ticket_rel" ] && continue
  case "$f" in TODO.md|HANDOFF.md|DECISIONS.md|PRD.md|STYLE.md|REFERENCES.md|tickets/*|docs/research/*) continue ;; esac
  ok=0
  while IFS= read -r g; do
    [ -z "$g" ] && continue
    case "$f" in $g) ok=1 ;; esac
  done <<< "$allow"
  if [ "$ok" = 0 ]; then echo "OUT-OF-SCOPE: $f"; fail=1; fi
done <<< "$changed"
[ "$fail" = 0 ] && echo "scope: OK"
exit "$fail"
