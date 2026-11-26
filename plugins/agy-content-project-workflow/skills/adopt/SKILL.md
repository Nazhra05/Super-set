---
name: adopt
description: Use this skill when the user asks to adopt, set up, or initialize the Content Project Workflow (producer skill, asset-builder, visual-reviewer, researcher, Explore subagents, approval gates, brief, art direction, reference inventory) in an existing video, motion graphics, or content project that already has scripts, assets, renders, or its own agent setup. Starts with the style preset (none or Vox editorial collage), surveys first, inventories every reference, asks instead of guessing, merges instead of overwriting, then offers to install the production tools.
---

# Adopt the content workflow into an existing project

Setup material lives in the plugin folder (two directories above this `SKILL.md` file: `<plugin-root>`). Copy it into the project once with `bash "<plugin-root>/scripts/stage.sh" .` (run from the project root, at the step named below). It creates `.workflow-setup/` with `templates/`, `reference/`, and `README.md`; read everything from there. Delete `.workflow-setup/` at the end of the setup, also when the setup stops early.

Rules for this whole skill:
- Reply in the owner's language. Documents go into the project in the document language chosen in the interview (English or Indonesian); code, identifiers, comments, and commits are always English.
- Never guess a name, command, number, or what an image shows. Read it from the project or ask with `ask_question`. A found value is offered as the first option to confirm, marked `(Recommended)`, not written silently.
- Never open `.env` files or print secrets. Never change, move, or re-export scripts, recordings, assets, or renders. Never commit, push, or change branches unless the owner asks.
- Software is installed only in the tools step of the install (`tools.md`), after the owner says yes. Tools the project already uses are kept; a different version is reported, not replaced.
- On Windows, `run_command` runs in PowerShell; always prefix shell scripts with `bash ` (for example `bash tools/scope.sh ...`).
- Before claiming any step done, run the command and quote its output (`verification-before-completion`).

## Execution discipline (follow literally)
This setup has many steps and several of them wait for the owner. Work like a checklist:
1. Do one numbered step at a time, in order. Never merge two steps into one turn and never skip a step because it "looks done".
2. After each step write one line `Step <n> done: <evidence>`, where the evidence is the command you ran and the last lines of its real output, or the owner's answer. No evidence means the step is not done.
3. After every `ask_question`, stop and wait for the answer. Do not continue on an assumed answer, and do not answer for the owner.
4. Before each step, re-read its section in `.workflow-setup/reference/` instead of working from memory; the files are short.
5. Install nothing outside the tools step, and there only what the owner selected, one command at a time, quoting the output of each.
6. If a command fails, quote the error, say what you will do, and do it once; never retry the same command blindly.

## 1. Stage the setup material
Confirm the project root with the owner, then run the stage script (`bash "<plugin-root>/scripts/stage.sh" .`). It is the only file this skill adds before the owner approves the file list.

## 2. Style preset
Ask the style preset question as `.workflow-setup/reference/style-presets.md` describes. Its answer sets the defaults of the interview and of the tools step.

## 3. Survey (read-only)
Collect, with evidence (`path` or command output):
- **Folders and files:** a tree of the project two or three levels deep, with file counts and sizes per folder . Mark which folders hold originals (scripts, recordings, source art) and which hold generated output (renders, caches).
- **References:** every file in folders named like reference, inspiration, moodboard, or assets, and every link in the project's notes. Each one is a candidate row for `REFERENCES.md`; none is skipped.
- **Script and audio:** the script or dialogue file, voice-over files, music, whether the text on screen must match the recording, whether a word-timing file already exists (for example a `timing.js` or captions file), and whether the script is in the JSON form `tools/audio/timing.py` reads (converting it is a first ticket, not a setup step).
- **Tool and commands:** the video or design tool (for example a `package.json` with Remotion or HyperFrames, an After Effects or Figma file), its check, preview, render, and frame-grab commands, and which ones exist (`package.json` scripts, a README, the existing `AGENTS.md` / `CLAUDE.md`).
- **Existing agent setup:** `AGENTS.md` (root and nested), `GEMINI.md`, `CLAUDE.md`, `.agents/`, `.claude/`. List name clashes with the subagents (`asset-builder`, `visual-reviewer`, `researcher`, `Explore`) and the seven skills (`producer` plus the six bundled skills; eight with the preset `vox`).
- **Git:** `git rev-parse --show-toplevel`, `git status --short`. Not a repo is a finding, not a blocker.

## 4. Baseline (read-only commands)
Run the project's check command once, if one exists, and record the real result with the date. Grab one frame from the latest render or preview if a command exists, and describe it with the rule in `AGENTS.md` ("seen" and "inferred"). A failing or slow check is a finding, not a blocker. Do not fix anything.

## 5. Interview
Follow `.workflow-setup/reference/setup-interview.md`. Offer what the survey found as the first option of each question, prefixed with `(Recommended)`. Also ask:
- For each clash found in step 3: which version wins, or how to merge.
- Which existing rules in the current `AGENTS.md` / `GEMINI.md` / `CLAUDE.md` must stay as they are.
- Whether existing to-do items should be imported into the `TODO.md` Inbox (default: yes, imported as Inbox, never executed).

## 6. Brief, art direction, references
Follow `.workflow-setup/reference/brief-and-style.md`, section "Adopt": keep an existing brief or draft one from the script and the project, draft `STYLE.md` from what is already made and from the references, and write `REFERENCES.md` with every reference found in step 3. The owner confirms each part.

## 7. Map existing content into the templates
- Existing instructions: each rule goes to the matching section of `AGENTS.md`. A rule that conflicts with the workflow becomes a question for the owner, or a project decision `D-01...` in `DECISIONS.md` that overrides a C-xx entry, with the reason.
- Existing tasks: Inbox entries in `TODO.md` with a link to the source. Gates already passed are marked with the evidence the owner confirms.
- Proven pitfalls: only facts from the survey that a command proved.
- `HANDOFF.md`: current state from steps 3 and 4, next step agreed with the owner.

## 8. Install and tools
Follow `.workflow-setup/reference/install-steps.md` in full: file list approval, merge rules, placeholders, `.gitignore`, smoke test, report. An existing `STYLE.md` is merged with the preset seed, never replaced; conflicts become questions. The tools step (`tools.md`) runs inside the install: `bash tools/tools-check.sh --preset <preset> --agent antigravity`, one question, install what the owner chose, re-check, record.

## 9. Report
In the owner's language, plain words: the preset, what was installed, what was merged and where, the references found and any that have no clear use yet, what was found (failing check, no git, mismatches between script and recording), the smoke test output, what is not verified, the tools check before and after, decisions waiting for the owner, and how to start the producer session (`producer` skill).
