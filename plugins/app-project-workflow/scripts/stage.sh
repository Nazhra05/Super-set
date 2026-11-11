#!/usr/bin/env bash
# Copy the setup material (templates, reference docs, README) from the plugin into
# <project>/.workflow-setup, so the setup skills read it inside the project folder.
# The plugin cache lives outside the project, where Claude Code does not read freely.
# Usage: bash "${CLAUDE_PLUGIN_ROOT}/scripts/stage.sh" <project-dir>
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?project dir}/.workflow-setup"
if [ -e "$DEST" ]; then
  echo "stage.sh: $DEST already exists; finish or delete the previous setup first" >&2
  exit 1
fi
mkdir -p "$DEST"
cp -R "$SRC/templates" "$SRC/reference" "$DEST/"
cp "$SRC/README.md" "$DEST/README.md"
echo "staged: $DEST"
