# Tools step

Shared by the `adopt` and `bootstrap` skills. Runs **after** the install step (`install-steps.md`), when the docs and `tools/` are in place, and before the final report. It is the only place where the setup installs software, and only after the owner says yes.

## 1. Check
Run from the project root:
```
bash tools/tools-check.sh --preset <none|vox> --agent antigravity
```
It prints one row per tool (status `ok`, `MISSING`, or `OLD`, version, required or optional, purpose) and, for anything not `ok`, the install command for this operating system. It never installs. Quote its output in the report.

| Tool | Why | `none` | `vox` |
|---|---|---|---|
| git | `tools/scope.sh`, history | required | required |
| Node.js 22+ | status line; HyperFrames needs 22+ | required | required |
| ffmpeg + ffprobe | frame grabs, contact sheets, loudness, delivery check | optional | required |
| HyperFrames (`npx hyperframes@latest`) | the video tool | optional | required |
| HyperFrames official skills | the agent knows the tool's rules | optional | required |
| agent-browser | look at reference sites, capture pages, check HTML in a real browser | optional | required |
| Python 3.9+ | audio kit | optional | required |
| audio venv (`faster-whisper`, `numpy`) | `tools/audio/timing.py` | optional | required |
| gh | researcher reads GitHub repositories | optional | optional |
| yt-dlp | download a reference video the owner names, to look at its frames | optional | optional |

## 2. Ask once
Ask with `ask_question`, one multi-select question listing only the tools that are not `ok`, each with its purpose and the exact command:
- Preset `vox`: every required tool is pre-marked and labelled "(Recommended)". Say in one sentence why: the preset's skill, kit, and checks depend on them.
- Preset `none`: nothing is pre-marked; git and Node.js are labelled "(Recommended)".
- Say which commands are global (winget, brew, apt, `npm i -g`) and which stay in the project (`.venv`, project-level skills), and that a global install changes the machine, not only this project.
- `sudo` commands (Linux) are never run by the agent: print them for the owner to run, then re-check.

## 3. Install what the owner selected
One command per `run_command` call; prefix shell scripts with `bash ` on Windows. After each call, quote its last lines before running the next one.
Run the printed commands one at a time, in this order: system packages (git, Node.js, Python, ffmpeg, gh, yt-dlp), then `agent-browser`, then the HyperFrames download, then the HyperFrames skills, then the audio venv. After each, quote the last lines of its output. A command that fails is not retried blindly: report the error, skip it, and continue with the rest.
- Windows: after a winget install the current shell does not see the new PATH. Ask the owner to restart the terminal or the app, then re-run the check; do not edit PATH yourself.
- HyperFrames skills: `npx --yes skills@latest add heygen-com/hyperframes -a antigravity -y` installs into `.agents/skills/` of this project (where the `skills` installer puts Antigravity skills). List what it added (`ls .agents/skills`) and tell the owner that the skills come from a third party (HeyGen) and that the `skills` installer sends an install event (its `--help` names "install telemetry").
- Audio venv: `python -m venv .venv`, then `.venv/Scripts/python` (Windows) or `.venv/bin/python` (macOS, Linux) `-m pip install -r tools/audio/requirements.txt`. Add `.venv/` to `.gitignore` (append only). The first `timing.py` run downloads a speech model (a few hundred MB for `small`); say so.
- yt-dlp: only for a video the owner names; downloading is subject to the source's terms. Never download on your own initiative.

## 4. Re-check and record
Run `tools/tools-check.sh` again and quote it. Then:
- `AGENTS.md` "Commands": the commands that ran, with the date (for `vox`, the HyperFrames and audio lines in `style-presets.md`, and the HyperFrames version that ran, as information).
- `HANDOFF.md`: which tools are missing and why (declined, failed, waiting for a restart).
- `TODO.md`: a missing required tool becomes a task for the owner, status `Waiting decision`.

Nothing in this step is committed unless the owner asks.
