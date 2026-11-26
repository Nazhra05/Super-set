#!/usr/bin/env bash
# Report which production tools are installed, with the install command for this OS.
# Usage: bash tools/tools-check.sh [--preset vox|none] [--agent claude-code|antigravity|codex]
# Prints one row per tool: status (ok, MISSING, OLD), version, what it is for, and how to install it.
# It never installs anything; the agent asks the owner first and runs the printed command.
# Exit 0 when every tool marked "required" for the preset is ok, 1 otherwise.
PRESET=none
AGENT=codex
while [ $# -gt 0 ]; do
  case "$1" in
    --preset) PRESET="${2:-none}"; shift 2 ;;
    --agent) AGENT="${2:-codex}"; shift 2 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) OS=windows ;;
  Darwin) OS=macos ;;
  Linux)
    if command -v apt-get >/dev/null 2>&1; then OS=linux-apt
    elif command -v dnf >/dev/null 2>&1; then OS=linux-dnf
    else OS=linux; fi ;;
  *) OS=unknown ;;
esac

# install <windows> <macos> <apt> <dnf> <other>
install_cmd() {
  case "$OS" in
    windows) echo "$1" ;; macos) echo "$2" ;; linux-apt) echo "$3" ;; linux-dnf) echo "$4" ;; *) echo "$5" ;;
  esac
}

# major version as an integer, or 0
major() { echo "$1" | sed -E 's/^[^0-9]*([0-9]+).*/\1/;t;s/.*/0/'; }

fail=0
row() { # name status version need purpose install
  printf '%-18s %-8s %-14s %-12s %s\n' "$1" "$2" "$3" "$4" "$5"
  [ "$2" = ok ] || printf '%-18s %-8s %s\n' "" "" "install: $6"
  if [ "$4" = required ] && [ "$2" != ok ]; then fail=1; fi
}

if [ "$PRESET" = vox ]; then REC=required; else REC=optional; fi
echo "tools-check: os=$OS preset=$PRESET agent=$AGENT"
printf '%-18s %-8s %-14s %-12s %s\n' TOOL STATUS VERSION NEED PURPOSE

# git
if command -v git >/dev/null 2>&1; then v="$(git --version | awk '{print $3}' | cut -d. -f1-3)"; s=ok; else v=-; s=MISSING; fi
row git "$s" "$v" required "scope check, history" \
  "$(install_cmd 'winget install --id Git.Git -e' 'brew install git' 'sudo apt-get install -y git' 'sudo dnf install -y git' 'https://git-scm.com/downloads')"

# node (22+ for HyperFrames; 18+ for the status line)
if command -v node >/dev/null 2>&1; then
  v="$(node -v)"; if [ "$(major "$v")" -ge 22 ]; then s=ok; else s=OLD; fi
else v=-; s=MISSING; fi
row node "$s" "$v" required "status line; HyperFrames needs 22+" \
  "$(install_cmd 'winget install --id OpenJS.NodeJS.LTS -e' 'brew install node' 'Node.js 22+ from https://nodejs.org/en/download (distribution packages are often older)' 'Node.js 22+ from https://nodejs.org/en/download' 'https://nodejs.org/en/download')"

# ffmpeg and ffprobe
FF="${FFMPEG:-$(command -v ffmpeg 2>/dev/null)}"
if [ -n "$FF" ] && command -v ffprobe >/dev/null 2>&1; then v="$("$FF" -version | head -1 | awk '{print $3}' | cut -d- -f1)"; s=ok; else v=-; s=MISSING; fi
row ffmpeg "$s" "$v" "$REC" "frame grabs, contact sheets, loudness, delivery check" \
  "$(install_cmd 'winget install --id Gyan.FFmpeg -e' 'brew install ffmpeg' 'sudo apt-get install -y ffmpeg' 'sudo dnf install -y ffmpeg (Fedora: enable RPM Fusion first)' 'https://ffmpeg.org/download.html')"

# HyperFrames: run through npx at the npm "latest" tag (stable channel), never pinned
if command -v npm >/dev/null 2>&1; then
  latest="$(npm view hyperframes version 2>/dev/null)"
  if [ -n "$latest" ] && [ "$(major "$(node -v 2>/dev/null)")" -ge 22 ]; then s=ok; v="latest=$latest"; else s=MISSING; v="${latest:-offline}"; fi
else s=MISSING; v=-; fi
row hyperframes "$s" "$v" "$REC" "video tool (HTML + GSAP), run as npx hyperframes@latest" \
  "needs node 22+ and npm; first run downloads it: npx --yes hyperframes@latest --help"

# HyperFrames official agent skills, project level
case "$AGENT" in claude-code) SK="$ROOT/.claude/skills" ;; *) SK="$ROOT/.agents/skills" ;; esac
if [ -d "$SK/hyperframes" ]; then s=ok; v=installed; else s=MISSING; v=-; fi
row hyperframes-skills "$s" "$v" "$REC" "official HyperFrames skills for the agent" \
  "npx --yes skills@latest add heygen-com/hyperframes -a $AGENT -y   (project level; review what it adds)"

# agent-browser
if command -v agent-browser >/dev/null 2>&1; then v="$(agent-browser --version 2>/dev/null | head -1 | awk '{print $NF}')"; s=ok; else v=-; s=MISSING; fi
row agent-browser "$s" "${v:-?}" "$REC" "browse references, capture pages, check HTML in a real browser" \
  "npm i -g agent-browser && agent-browser install   (global npm package plus a browser download)"

# python 3.9+
PY=""
for c in python3 python py; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; then PY="$c"; break; fi
done
if [ -n "$PY" ]; then v="$("$PY" -c 'import platform; print(platform.python_version())')"; s=ok; else v=-; s=MISSING; fi
row python "$s" "$v" "$REC" "audio kit (word timing, mastering, delivery check)" \
  "$(install_cmd 'winget install --id Python.Python.3.12 -e' 'brew install python' 'sudo apt-get install -y python3 python3-venv' 'sudo dnf install -y python3' 'https://www.python.org/downloads/')"

# audio kit venv
VPY="$ROOT/.venv/bin/python"; [ -x "$VPY" ] || VPY="$ROOT/.venv/Scripts/python.exe"
if [ -x "$VPY" ] && "$VPY" -c 'import faster_whisper, numpy' >/dev/null 2>&1; then s=ok; v=".venv"; else s=MISSING; v=-; fi
case "$OS" in windows) VBIN=".venv/Scripts/python" ;; *) VBIN=".venv/bin/python" ;; esac
row audio-venv "$s" "$v" "$REC" "faster-whisper + numpy for tools/audio/timing.py" \
  "${PY:-python} -m venv .venv && $VBIN -m pip install -r tools/audio/requirements.txt"

# gh (researcher reads repositories)
if command -v gh >/dev/null 2>&1; then v="$(gh --version | head -1 | awk '{print $3}')"; s=ok; else v=-; s=MISSING; fi
row gh "$s" "$v" optional "researcher reads GitHub repositories" \
  "$(install_cmd 'winget install --id GitHub.cli -e' 'brew install gh' 'https://github.com/cli/cli#installation' 'sudo dnf install -y gh' 'https://github.com/cli/cli#installation')"

# yt-dlp (reference videos the owner points to; check the source's terms first)
if command -v yt-dlp >/dev/null 2>&1; then v="$(yt-dlp --version)"; s=ok; else v=-; s=MISSING; fi
row yt-dlp "$s" "$v" optional "download a reference video the owner names, to watch frames" \
  "$(install_cmd 'winget install --id yt-dlp.yt-dlp -e' 'brew install yt-dlp' 'pipx install yt-dlp' 'pipx install yt-dlp' 'https://github.com/yt-dlp/yt-dlp#installation')"

[ "$OS" = windows ] && echo "note: after a winget install, restart the terminal or the agent app so PATH picks up the new tool."
if [ "$fail" = 0 ]; then echo "tools-check: OK"; else echo "tools-check: required tools missing"; fi
exit "$fail"
