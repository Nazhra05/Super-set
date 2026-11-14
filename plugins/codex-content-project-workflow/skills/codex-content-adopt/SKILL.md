---
name: codex-content-adopt
description: Adopt the Content Project Workflow (producer skill, asset-builder, visual-reviewer, researcher, Explore role prompts, approval gates, brief, art direction, reference inventory) in an existing video, motion graphics, or content project using OpenAI Codex. Surveys first, inventories every reference, asks instead of guessing, merges instead of overwriting.
---

# Adopt the content workflow into an existing project (Codex)

Setup material lives in the plugin folder (two directories above this `SKILL.md` file: `<plugin-root>`). Copy it into the project once with `bash "<plugin-root>/scripts/stage.sh" .` (run from the project root, at the step named below). It creates `.workflow-setup/` with `templates/`, `reference/`, and `README.md`; read everything from there. Delete `.workflow-setup/` at the end of the setup, also when the setup stops early.

Rules for this whole skill:
- Reply in the owner's language. Documents go into the project in the document language chosen in the interview (English or Indonesian); code, identifiers, comments, and commits are always English.
- Never guess a name, command, number, or what an image shows. Read it from the project or ask the owner (at most 4 numbered questions per turn). A found value is offered as the first option to confirm, marked `(Recommended)`, not written silently.
- Never open `.env` files or print secrets. Never change, move, or re-export scripts, recordings, assets, or renders. Never commit, push, or change branches unless the owner asks.
- Before claiming any step done, run the command and quote its output (`verification-before-completion`).

## 1. Survey (read-only)
Confirm the project root with the owner, then collect, with evidence (`path` or command output):
- **Folders and files:** a tree of the project two or three levels deep, with file counts and sizes per folder (`find`, `du`). Mark which folders hold originals (scripts, recordings, source art) and which hold generated output (renders, caches).
- **References:** every file in folders named like reference, inspiration, moodboard, or assets, and every link in the project's notes. Each one is a candidate row for `REFERENCES.md`; none is skipped.
- **Script and audio:** the script or dialogue file, voice-over files, music, and whether the text on screen must match the recording.
- **Tool and commands:** the video or design tool (for example a `package.json` with Remotion or HyperFrames, an After Effects or Figma file), its check, preview, render, and frame-grab commands, and which ones exist (`package.json` scripts, a README, the existing `AGENTS.md` / `CLAUDE.md`).
- **Existing agent setup:** `AGENTS.md` (root and nested), `CLAUDE.md`, `.codex/`, `.agents/`, `.claude/`. List name clashes with the role prompts (`asset-builder`, `visual-reviewer`, `researcher`, `Explore`) and the seven skills (`producer` plus the six bundled skills).
- **Git:** `git rev-parse --show-toplevel`, `git status --short`. Not a repo is a finding, not a blocker.

## 2. Stage the setup material
Run the stage script (`bash "<plugin-root>/scripts/stage.sh" .`). It is the only file this skill adds before the owner approves the file list.

## 3. Baseline (read-only commands)
Run the project's check command once, if one exists, and record the real result with the date. Grab one frame from the latest render or preview if a command exists, and describe it with the rule in `AGENTS.md` ("seen" and "inferred"). A failing or slow check is a finding, not a blocker. Do not fix anything.

## 4. Interview
Follow `.workflow-setup/reference/setup-interview.md`. Offer what the survey found as the first option of each question, prefixed with `(Recommended)`. Also ask:
- For each clash found in step 1: which version wins, or how to merge.
- Which existing rules in the current `AGENTS.md` / `CLAUDE.md` must stay as they are.
- Whether existing to-do items should be imported into the `TODO.md` Inbox (default: yes, imported as Inbox, never executed).

## 5. Brief, art direction, references
Follow `.workflow-setup/reference/brief-and-style.md`, section "Adopt": keep an existing brief or draft one from the script and the project, draft `STYLE.md` from what is already made and from the references, and write `REFERENCES.md` with every reference found in step 1. The owner confirms each part.

## 6. Map existing content into the templates
- Existing instructions: each rule goes to the matching section of `AGENTS.md`. A rule that conflicts with the workflow becomes a question for the owner, or a project decision `D-01...` in `DECISIONS.md` that overrides a C-xx entry, with the reason.
- Existing tasks: Inbox entries in `TODO.md` with a link to the source. Gates already passed are marked with the evidence the owner confirms.
- Proven pitfalls: only facts from the survey that a command proved.
- `HANDOFF.md`: current state from steps 1 and 3, next step agreed with the owner.

## 7. Install
Follow `.workflow-setup/reference/install-steps.md` in full: file list approval, merge rules, placeholders, `.gitignore`, smoke test, report.

## 8. Report
In the owner's language, plain words: what was installed, what was merged and where, the references found and any that have no clear use yet, what was found (failing check, no git, mismatches between script and recording), the smoke test output, what is not verified, decisions waiting for the owner, the recommended skills for the video tool, and how to start the producer session (`$producer` or ask Codex to use the `producer` skill).

