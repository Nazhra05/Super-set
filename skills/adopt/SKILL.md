---
name: adopt
description: Set up the App Project Workflow (router, worker, tester, reviewer, Explore agents, ticket board, worktree guard tools) in a project that already exists and has code, docs, or its own Claude Code setup. Surveys the project first, asks instead of guessing, merges instead of overwriting.
disable-model-invocation: true
allowed-tools:
  - Bash(bash "${CLAUDE_PLUGIN_ROOT}/scripts/stage.sh" *)
---

# Adopt the workflow into an existing project

Setup material lives in the plugin folder, outside the project. Copy it into the project once with `bash "${CLAUDE_PLUGIN_ROOT}/scripts/stage.sh" .` (run from the project root, at the step named below). It creates `.workflow-setup/` with `templates/`, `reference/`, and `README.md`; read everything from there. Delete `.workflow-setup/` at the end of the setup, also when the setup stops early.

Rules for this whole skill:
- Reply in the owner's language; write everything into the project in English.
- Never guess a name, command, branch, or number. Read it from the project or ask. A found value is offered as an option to confirm, not written silently.
- Never open `.env` files or print secrets. Never change application code. Read setup material only from `.workflow-setup/`. Never commit, push, or change branches unless the owner asks.
- Before claiming any step done, run the command and quote its output (`verification-before-completion`).

## 1. Survey (read-only)
Confirm the project root with the owner, then collect, with evidence (`path` or command output):
- **Repos:** `git rev-parse --show-toplevel`, `git status --short`, `git branch -a`, `git remote -v`, and nested repos (`find . -maxdepth 3 -name .git -not -path '*/node_modules/*'`). Note dirty trees; do not touch them.
- **Existing Claude setup:** `CLAUDE.md` (root and nested), `AGENTS.md`, `.claude/settings.json`, `.claude/agents/`, `.claude/skills/`, `.claude/commands/`, hooks. List name clashes with the five agents (`router`, `worker`, `tester`, `reviewer`, `Explore`) and the five skills.
- **Work tracking and decisions:** any TODO, backlog, roadmap, changelog, ADR, or decision files.
- **Stack and commands:** `package.json` scripts, `composer.json`, `pyproject.toml`, `Makefile`, CI config. Candidate test, lint, type-check, build, install commands per repo.
- **Source of truth for names:** database schema files, type definitions, API specs.
- **Shared resources:** local database, fixed dev-server ports, upload folders used by tests.

## 2. Stage the setup material
Run the stage script (see the top of this skill). It is the only file this skill adds before the owner approves the file list.

## 3. Baseline (read-only commands)
Run the test command of each repo once and record the real result with the date. A failing or slow suite is a finding, not a blocker: record it for `HANDOFF.md` and the Inbox. Do not fix anything. State that existing tests are not yet proven genuine (W-01).

## 4. Interview
Follow `.workflow-setup/reference/setup-interview.md`. Offer what the survey found as the first option of each question. Also ask:
- For each clash found in step 1: which version wins, or how to merge.
- Which existing rules in the current `CLAUDE.md`/`AGENTS.md` must stay as they are.
- Whether existing TODO items should be imported into the `TODO.md` Inbox (default: yes, imported as Inbox, never executed).
- Which existing docs to list in the document map.

## 5. Map existing content into the templates
- Existing instructions: each rule goes to the matching section of `CLAUDE.md` or `AGENTS.md`. A rule that conflicts with the workflow becomes a question for the owner, or a project decision `D-01...` in `DECISIONS.md` that overrides a W-xx entry, with the reason.
- Existing tasks: Inbox entries in `TODO.md` with a link to the source. The execution order stays empty unless the owner names tickets.
- Existing decisions: summarized under "B. Project decisions" with a pointer to the original file; the original stays where it is.
- Proven pitfalls: only facts from the survey that a command proved (for example "suite needs local MySQL running", shown by a failing run).
- `HANDOFF.md`: current state from step 1 and 2, next step agreed with the owner.

## 6. Install
Follow `.workflow-setup/reference/install-steps.md` in full: file list approval, merge rules, placeholders, `.gitignore`, smoke test, status line, report.

## 7. Report
In the owner's language, plain words: what was installed, what was merged and where, what was found (dirty trees, failing tests, clashes, secrets risk), the smoke test output, what is not verified, decisions waiting for the owner, and the router launch command.
