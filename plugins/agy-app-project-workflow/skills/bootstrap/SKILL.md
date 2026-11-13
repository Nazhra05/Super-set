---
name: bootstrap
description: Use this skill when the user asks to bootstrap, set up, or initialize the App Project Workflow (router skill, worker, tester, reviewer, Explore subagents, ticket board, worktree guard tools) in a new or empty project folder. Interviews the owner about the project, writes a first PRD, creates the git repo layout, fills the core workflow docs for this project, and smoke-tests the tools.
---

# Bootstrap the workflow in a new or empty project

Setup material lives in the plugin folder (two directories above this `SKILL.md` file: `<plugin-root>`). Copy it into the project once with `bash "<plugin-root>/scripts/stage.sh" .` (run from the project root, at the step named below). It creates `.workflow-setup/` with `templates/`, `reference/`, and `README.md`; read everything from there. Delete `.workflow-setup/` at the end of the setup, also when the setup stops early.

Rules for this whole skill:
- Reply in the owner's language. Documents go into the project in the document language chosen in the interview (English or Indonesian); code, identifiers, comments, and commits are always English.
- Never guess. Ask for anything the owner has not said using `ask_question`. A recommendation is offered as the first option, marked `(Recommended)`.
- Do not scaffold application code, install frameworks, or add dependencies. This skill sets up the way of working; building the app is the first tickets.
- On Windows, `run_command` runs in PowerShell; always prefix shell scripts with `bash ` (for example `bash tools/wt.sh ...`).
- Before claiming any step done, run the command and quote its output (`verification-before-completion`).

## 1. Check the folder
Confirm the project root with the owner. List what is there. If it already has code, a git repo with commits, or an `AGENTS.md` / `CLAUDE.md`, stop and suggest the `adopt` skill instead.

## 2. Stage the setup material
Run the stage script (`bash "<plugin-root>/scripts/stage.sh" .`).

## 3. Interview about the project
Ask, with `ask_question` (max 4 questions per call):
- What the app does, for whom, and the first outcome that matters. This becomes `{{PROJECT_SUMMARY}}` and the first `TODO.md` entries.
- Planned stack per part (frontend, backend, database). If undecided, record it as `Waiting decision` in `DECISIONS.md` section C; do not pick for the owner.
- Repo layout: one repo (recommended for a new project) or a docs root with separate app repos. Working branch name per repo.
- Whether the repo will get a remote now or later.
Then follow `.workflow-setup/reference/setup-interview.md` for the remaining answers. Commands that do not exist yet (no test runner installed) are written as "Not set up yet" and added as the first Inbox or Proposed tasks, never invented.

## 4. Product requirements (PRD)
Follow `.workflow-setup/reference/prd.md`, section "Bootstrap": build on the answers above, ask what is missing, every requirement `Planned`.

## 5. Create the repo layout
- `git init` each repo the owner chose (reversible; mention it). Create the working branch name the owner chose.
- `tools/wt.sh` needs a commit to branch from: after the files are installed in step 6, ask the owner whether to make the initial commit. If they decline, skip the smoke test steps that need a worktree and say so.

## 6. Install
Follow `.workflow-setup/reference/install-steps.md` in full. In a new project there is nothing to merge, so the file list is all `new`. Fill the docs for this project:
- `PRD.md`: the draft the owner approved in step 4.
- `TODO.md`: execution order with the first tickets agreed with the owner (for example "set up test runner", "decide stack"), status `Proposed` unless the owner says `Ready`. A task that builds a feature names its requirement ID.
- `DECISIONS.md`: section B with the decisions made in the interview (stack, repo layout), each with date and reason; section C with what is still open.
- `HANDOFF.md`: current state (empty project, workflow installed) and the next step.
- `AGENTS.md` pitfalls: "None yet."

## 7. Report
In the owner's language, plain words: what was created, the PRD's open questions, the smoke test output (or why parts were skipped), what is waiting for the owner, the first ticket, and how to start the router session (`router` skill).

