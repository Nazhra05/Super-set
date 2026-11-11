# App Project Workflow

**Make Claude Code a careful teammate on your software project.** This plugin sets up a project so Claude plans before it builds, proves its work with real test runs, stays inside the task you gave it, and leaves notes for the next session.

Part of the [Super-set](../../README.md) marketplace.

## Is it for you?
Use it if you build an app, website, API, or any code project with Claude Code, alone or in a small team, and you have seen things like:
- Claude changing files when you only asked a question.
- "All tests pass" when they did not, or tests quietly weakened or deleted.
- Edits far outside what you asked for, or code nobody needed.
- Every new session starting from zero.

**When not to use it:** a one-off script or a quick experiment (the setup and the ticket flow are more process than you need), or a folder that is not a git repository and will not become one (the worktrees and the guard need git). For videos, animation, or motion graphics, use `content-project-workflow` instead.

## What it does for you
| Problem | What the plugin sets up |
|---|---|
| Unclear what to build | `PRD.md`: what and why, each requirement with an ID, a status, and evidence. Setup writes it with you. |
| Lost context between sessions | `HANDOFF.md` (where things stand), `TODO.md` (one work board), `DECISIONS.md` (why) |
| Claims without proof | Rules that "done" needs command output just run; new tests must fail first; security logic gets a mutation check |
| Scope creep and weakened tests | Each job is a ticket with an Allow list; `tools/guard.sh` fails on files outside it, deleted tests, skip markers, or fewer assertions |
| Big jobs in one long run | A planning agent (the router) splits work into tickets; worker, tester, and reviewer agents each do one ticket in its own git worktree; the router re-checks before merging |

## How a job runs
1. You put work on the board (`TODO.md`), or ask the router to plan it.
2. The router writes a ticket: goal, files allowed, checks to run.
3. A worker (and a tester for risky logic) does the ticket in a separate worktree.
4. The router runs the guard and the checks itself; a reviewer looks at risky changes.
5. Only then is it merged, and the board and notes are updated.

You can also skip the router and talk to Claude as usual; the rules in `CLAUDE.md` still apply.

## What it looks like
From a test setup of a sample book-club app. The PRD that `bootstrap` wrote from the interview (excerpt):

```
| ID    | Requirement                                                                               | Status  | Evidence |
|-------|-------------------------------------------------------------------------------------------|---------|----------|
| FR-02 | A member can propose a book in an open voting round                                        | Planned | -        |
| FR-03 | A member has one vote per voting round and can change it until the round is closed         | Planned | -        |
| FR-09 | When a closed round ends in a tie, an organizer picks the winner from the tied books       | Planned | -        |

## 7. Open questions
- Sign-in: email link or password? (affects FR-01)
- Is there a limit on proposals per member per round? (affects FR-02)
```

The guard catching a file outside the ticket, from the setup's own smoke test:

```
$ tools/guard.sh _wt/SMOKE-app main tickets/SMOKE.md
OUT-OF-SCOPE: OUTSIDE.txt          (exit 1)
```

Things the setup did not know went to "Open questions" instead of being made up.

## Setup
| Skill | Use when | What it does |
|---|---|---|
| `/app-project-workflow:adopt` | The project already has code, docs, or its own Claude Code setup | Reads the project first, records a test baseline, keeps an existing PRD or drafts one from what is built, asks instead of guessing, merges existing rules and tasks, never overwrites |
| `/app-project-workflow:bootstrap` | New or empty folder | Interviews you, writes a first PRD of what will be built, sets up the repo layout and the docs, no app scaffolding |

Both explain the defaults below and ask which to change, show the list of files before writing, smoke-test the tools, and end with a plain-language report. Nothing is committed unless you ask. The PRD methods are in `reference/prd.md`.

Install: `claude plugin install app-project-workflow@super-set` after adding the marketplace (see the [Super-set README](../../README.md#quick-start)). After setup the project is self-contained, so the plugin can be removed without breaking it.

## Daily use
The flow is the same on every surface; only starting the router differs.
- **Terminal:** `claude --agent router --model <router model> --effort high` from the project root.
- **Desktop app:** router mode is a few keys in `.claude/settings.local.json`; the project's `WORKFLOW.md` has the exact block. Every new session in that project then starts as the router until you remove the keys.

| | Terminal | Desktop app |
|---|---|---|
| Start the router | `--agent router` flag | router mode in `.claude/settings.local.json` |
| Usage guard | reads `.claude/usage.json` from the status line; above 90% of the 5-hour or 7-day limit it stops dispatching | no status line there, so the router keeps every ticket boundary ready and stops cleanly at the app's usage-limit notice |

## Cost
- Always loaded: about 170 tokens per session for the two setup skills (`claude plugin details`).
- During work: the router uses the strongest model you pick; workers and testers use `sonnet`; reviewers use `opus` for security work and `sonnet` otherwise; Explore uses `haiku`. Each spawned agent re-reads its ticket and files (roughly 20k to 25k tokens), so the router does small jobs itself. You can change every model at setup.

## Opinionated defaults (and how to change them)
Setup explains these and asks which to change; afterwards, change them in the files named. To override a decision (W-xx), add a project decision (D-xx) in `DECISIONS.md` with the reason.

| Default | Why | Where |
|---|---|---|
| A question gets an answer, not file changes | Prevents unasked edits | `CLAUDE.md` rule 1 |
| Approval only for irreversible actions; the router merges and pushes on its own | Waiting for a yes on reversible steps adds friction, not safety | `WORKFLOW.md`, W-06 |
| Claims need fresh command output; tests prove red before green; mutation checks for security logic | "Passing" was reported for work that was not | `CLAUDE.md` rule 5, W-01 |
| YAGNI: every line needs a user today | Code nobody calls | `CLAUDE.md` rule 3, W-02 |
| Subagents never commit; the guard enforces the ticket's Allow list | Scope creep, silent test weakening | `tools/guard.sh` |
| Reviewer model by risk | Reviews cost most of what they review | `WORKFLOW.md`, W-05 |
| Tickets sized to about 60% of the agent turn limit | Cut-off agents leave no report | `tickets/_TEMPLATE.md`, W-07 |
| Docs in English or Bahasa Indonesia; code and commits in English; common terms in one form | Readable docs, one language for code | `CLAUDE.md` rule 8, "Terms" |
| Guard patterns for Jest, Vitest, Playwright, PHPUnit skip | Only patterns proven to catch weakened tests | `tools/workflow.conf` |

## What lands in the project
- Docs: `PRD.md`, `CLAUDE.md`, `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `tickets/_TEMPLATE.md`, in English or Indonesian.
- `.claude/agents/`: router, worker, tester, reviewer, Explore.
- `.claude/skills/`: `verification-before-completion`, `systematic-debugging`, `test-driven-development`, `receiving-code-review`, `writing-plans`.
- `.claude/settings.json`: Read deny for `.env` files, status line.
- `tools/`: `workflow.conf`, `wt.sh` (worktrees), `guard.sh`, `verify.sh`, `statusline.js`.

## Requirements
- Git and Node.js.
- Bash: built in on macOS and Linux; on Windows, Git for Windows (Git Bash), which Claude Code already uses.
- One repo or several: `tools/workflow.conf` lists each repo with its alias, path, and working branch.

## Status
Version 0.3. Setup (`adopt`, `bootstrap`) tested end to end on sample projects on Windows (Git Bash). The rules and the router flow come from daily use in a real project before they became a plugin. Not yet tested: macOS, Linux, router mode inside the desktop app, a full interactive setup with the real question cards. Reports welcome: see [Contributing](../../CONTRIBUTING.md).

## Layout of this plugin
```
.claude-plugin/   plugin.json
skills/           adopt, bootstrap
reference/        setup-interview.md, prd.md, install-steps.md
scripts/          stage.sh (copies setup material into the project during setup)
templates/        everything copied into a project (English docs)
templates/id/     the docs in Indonesian
```

## License
MIT, see `LICENSE`. The five skills in `templates/.claude/skills/` are adapted from [obra/superpowers](https://github.com/obra/superpowers) (MIT); attribution and changes are in `templates/.claude/skills/NOTICE`.
