# App Project Workflow (Antigravity)

**Make Google Antigravity a careful teammate on your software project.** This plugin sets up a project so Antigravity plans before it builds, proves its work with real test runs, stays inside the task you gave it, and leaves notes for the next session.

Part of the [Super-set](../../README.md) repository.

## Is it for you?
Use it if you build an app, website, API, or any code project with Google Antigravity (Antigravity 2.0 desktop app, Antigravity IDE, or Antigravity CLI `agy`), alone or in a small team, and you have seen things like:
- The agent changing files when you only asked a question.
- "All tests pass" when they did not, or tests quietly weakened or deleted.
- Edits far outside what you asked for, or code nobody needed.
- Every new session starting from zero.

**When not to use it:** a one-off script or a quick experiment (the setup and the ticket flow are more process than you need), or a folder that is not a git repository and will not become one (the worktrees and the guard need git). For videos, animation, or motion graphics, use `agy-content-project-workflow` instead.

## What it does for you
| Problem | What the plugin sets up |
|---|---|
| Unclear what to build | `PRD.md`: what and why, each requirement with an ID, a status, and evidence. Setup writes it with you. |
| Lost context between sessions | `HANDOFF.md` (where things stand), `TODO.md` (one work board), `DECISIONS.md` (why) |
| Claims without proof | Rules in `AGENTS.md` that "done" needs command output just run; new tests must fail first; security logic gets a mutation check |
| Scope creep and weakened tests | Each job is a ticket with an Allow list; `tools/guard.sh` fails on files outside it, deleted tests, skip markers, or fewer assertions |
| Big jobs in one long run | The `router` skill plans tickets; `worker`, `tester`, and `reviewer` subagents each do one ticket in its own git worktree; the router re-checks before merging |

## How a job runs
1. You put work on the board (`TODO.md`), or ask the router to plan it.
2. The router writes a ticket: goal, files allowed, checks to run.
3. A `worker` (and a `tester` for risky logic) does the ticket in a separate worktree via `invoke_subagent`.
4. The router runs `bash tools/guard.sh` and `bash tools/verify.sh` itself; a `reviewer` looks at risky changes.
5. Only then is it merged, and the board and notes are updated.

You can also skip the router and talk to Antigravity as usual; the rules in `AGENTS.md` still apply automatically.

## Setup
| Skill | Use when | What it does |
|---|---|---|
| `adopt` | The project already has code, docs, or its own agent setup | Reads the project first, records a test baseline, keeps an existing PRD or drafts one from what is built, asks with `ask_question` instead of guessing, merges existing rules and tasks, never overwrites |
| `bootstrap` | New or empty folder | Interviews you, writes a first PRD of what will be built, sets up the repo layout and the docs, no app scaffolding |

Both explain the defaults below and ask which to change, show the list of files before writing, smoke-test the tools, and end with a plain-language report. Nothing is committed unless you ask.

### Installing the plugin in Antigravity
Copy `Super-set/plugins/agy-app-project-workflow` into `~/.gemini/config/plugins/agy-app-project-workflow/`, or reference it from your project's `.agents/plugins.json`. After setup the project is self-contained, so disabling or removing the plugin later does not break the project.

## Daily use
The flow is identical across Antigravity 2.0 desktop app, Antigravity IDE, and Antigravity CLI (`agy`):
- Invoke the **`router`** skill (`/router` or ask the agent to "start the router session and work through `TODO.md`").
- Every ticket boundary is kept compact-ready (`TODO.md`, the ticket, and `HANDOFF.md` current; docs committed; no subagent running).

## Cost and model tiers
- During work: the router runs in your main session (`pro` recommended); `worker` and `tester` subagents default to `flash`; `reviewer` uses `pro` for security/auth work and `flash` otherwise; `Explore` uses `flash_lite`. Each spawned subagent re-reads its ticket and files, so the router does small jobs itself. You can change every model tier at setup.

## Opinionated defaults (and how to change them)
Setup explains these and asks which to change; afterwards, change them in the files named. To override a decision (W-xx), add a project decision (D-xx) in `DECISIONS.md` with the reason.

| Default | Why | Where |
|---|---|---|
| A question gets an answer, not file changes | Prevents unasked edits | `AGENTS.md` rule 1 |
| Approval only for irreversible actions; the router merges and pushes on its own | Waiting for a yes on reversible steps adds friction, not safety | `WORKFLOW.md`, W-06 |
| Claims need fresh command output; tests prove red before green; mutation checks for security logic | "Passing" was reported for work that was not | `AGENTS.md` rule 5, W-01 |
| YAGNI: every line needs a user today | Code nobody calls | `AGENTS.md` rule 3, W-02 |
| Subagents never commit; the guard enforces the ticket's Allow list | Scope creep, silent test weakening | `tools/guard.sh` |
| Reviewer model by risk (`pro` vs `flash`) | Reviews cost most of what they review | `WORKFLOW.md`, W-05 |
| Tickets sized to about 60% of the agent turn limit | Cut-off agents leave no report | `tickets/_TEMPLATE.md`, W-07 |
| Docs in English or Bahasa Indonesia; code and commits in English; common terms in one form | Readable docs, one language for code | `AGENTS.md` rule 8, "Terms" |
| Guard patterns for Jest, Vitest, Playwright, PHPUnit skip | Only patterns proven to catch weakened tests | `tools/workflow.conf` |

## What lands in the project
- Docs: `PRD.md`, `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `tickets/_TEMPLATE.md`, in English or Indonesian.
- `.agents/agents/`: `worker`, `tester`, `reviewer`, `Explore`.
- `.agents/skills/`: `router`, `verification-before-completion`, `systematic-debugging`, `test-driven-development`, `receiving-code-review`, `writing-plans`.
- `.agents/hooks.json` + `tools/env-guard.js`: `PreToolUse` hook that blocks reading, editing, writing, or running shell commands on `.env` files.
- `tools/`: `workflow.conf`, `wt.sh` (worktrees), `guard.sh`, `verify.sh`, `env-guard.js`.

## Requirements
- Git and Node.js.
- Bash: built in on macOS and Linux; on Windows, Git for Windows (Git Bash). All `.sh` tools are invoked with `bash tools/<script>.sh` so they run cleanly from Windows PowerShell.

## Layout of this plugin
```
plugin.json       Antigravity plugin manifest
skills/           adopt, bootstrap
reference/        setup-interview.md, prd.md, install-steps.md
scripts/          stage.sh (copies setup material into the project during setup)
templates/        everything copied into a project (English docs)
templates/id/     the docs in Indonesian
```

## License
MIT, see `LICENSE`. The five discipline skills in `templates/.agents/skills/` are adapted from [obra/superpowers](https://github.com/obra/superpowers) (MIT); attribution and changes are in `templates/.agents/skills/NOTICE`.

