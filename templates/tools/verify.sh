#!/usr/bin/env bash
# Run the ticket's Done criteria. Usage: tools/verify.sh <worktree> <ticket.md>
# Runs each line of the ```verify block inside the worktree; prints the last 25 lines and the exit code of each.
WT="${1:?worktree}"; T="${2:?ticket}"
T="$(cd "$(dirname "$T")" && pwd)/$(basename "$T")"   # absolute: we cd into the worktree below
cd "$WT"
cmds="$(awk '/^```verify/{f=1;next} /^```/{f=0} f' "$T")"
rc=0
while IFS= read -r c; do
  [ -z "$c" ] && continue
  echo "\$ $c"
  out="$(bash -c "$c" 2>&1)"; e=$?
  echo "$out" | tail -n 25
  echo "exit=$e"
  [ "$e" -eq 0 ] || rc=1
done <<< "$cmds"
exit "$rc"
