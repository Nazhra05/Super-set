#!/usr/bin/env bash
# Run a ticket's Done criteria. Usage: tools/verify.sh [--with-scope] <ticket.md>
# With --with-scope, runs tools/scope.sh first. Then runs each line of the ```verify block from the project root; prints the last 25 lines and the exit code of each.
WITH_SCOPE=0
if [ "${1:-}" = "--with-scope" ]; then WITH_SCOPE=1; shift; fi
T="${1:?ticket}"
T="$(cd "$(dirname "$T")" && pwd)/$(basename "$T")"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [ "$WITH_SCOPE" -eq 1 ]; then
  bash "$ROOT/tools/scope.sh" "$T" || exit $?
fi
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
