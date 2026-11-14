#!/usr/bin/env bash
# Manage a ticket worktree. Usage: tools/wt.sh add|rm|check|land <repo-alias> <TICKET-ID> [args...]
# Repos and working branches come from tools/workflow.conf. Worktree: <root>/_wt/<ID>-<alias>, branch t/<ID>.
# Files in COPY_FILES are copied by name only (never read).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/tools/workflow.conf"
usage() { echo "usage: wt.sh add|rm|check|land <repo-alias> <ID> [commit-msg] [ticket-path]; aliases: $(echo "$REPOS" | awk -F'|' 'NF>=3{printf "%s ", $1}')" >&2; exit 2; }
ACTION="${1:-}"; ALIAS="${2:-}"; ID="${3:-}"
[ -n "$ALIAS" ] && [ -n "$ID" ] || usage
line="$(echo "$REPOS" | awk -F'|' -v a="$ALIAS" 'NF>=3 && $1==a')"
[ -n "$line" ] || usage
REPO="$ROOT/$(echo "$line" | cut -d'|' -f2)"
BASE="$(echo "$line" | cut -d'|' -f3 | tr -d '[:space:]')"
WT="$ROOT/_wt/$ID-$ALIAS"; BR="t/$ID"
case "$ACTION" in
  add)
    git -C "$REPO" worktree add -b "$BR" "$WT" "$BASE"
    for f in $COPY_FILES; do
      if [ -f "$REPO/$f" ]; then cp "$REPO/$f" "$WT/$f"; fi
    done
    if [ -n "$INSTALL_CMD" ]; then (cd "$WT" && bash -c "$INSTALL_CMD"); fi
    echo "worktree: $WT  branch: $BR  base: $BASE"
    ;;
  check)
    TICKET="${4:-$ROOT/tickets/$ID.md}"
    bash "$ROOT/tools/guard.sh" "$WT" "$BASE" "$TICKET"
    bash "$ROOT/tools/verify.sh" "$WT" "$TICKET"
    git -C "$WT" diff --stat "$BASE"
    ;;
  land)
    MSG="${4:?commit message required for wt.sh land}"
    TICKET="${5:-$ROOT/tickets/$ID.md}"
    bash "$ROOT/tools/guard.sh" "$WT" "$BASE" "$TICKET"
    git -C "$WT" add -A
    git -C "$WT" commit -m "$MSG"
    git -C "$REPO" merge --no-ff "$BR" -m "Merge branch '$BR' ($ID)"
    git -C "$REPO" worktree remove --force "$WT"
    git -C "$REPO" branch -d "$BR"
    bash "$ROOT/tools/verify.sh" "$REPO" "$TICKET"
    echo "landed: $ID on $BASE"
    ;;
  rm)
    # `worktree remove --force` discards uncommitted work. Refuse unless the tree is clean
    # (ignored files such as .env and node_modules do not count) or WT_DISCARD=1.
    dirty="$(git -C "$WT" status --porcelain 2>/dev/null)"
    if [ -n "$dirty" ] && [ "${WT_DISCARD:-0}" != 1 ]; then
      echo "wt.sh rm: $WT has uncommitted changes; commit them or rerun with WT_DISCARD=1:" >&2
      echo "$dirty" >&2
      exit 1
    fi
    git -C "$REPO" worktree remove --force "$WT"
    git -C "$REPO" branch -d "$BR"   # refuses if unmerged; use branch -D by hand after deciding
    ;;
  *) usage ;;
esac
