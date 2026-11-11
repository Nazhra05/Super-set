# App Project Workflow

**Make Claude Code a careful teammate on your software project.** This plugin sets up a project so Claude plans before it builds, proves its work with real test runs, stays inside the task you gave it, and leaves notes for the next session.

## Is it for you?
Use it if you build an app, website, API, or any code project with Claude Code, alone or in a small team, and you have seen things like:
- Claude changing files when you only asked a question.
- "All tests pass" when they did not, or tests quietly weakened or deleted.
- Edits far outside what you asked for, or code nobody needed.
- Every new session starting from zero.

For videos, animation, or other content, use `content-project-workflow` instead.

## What it does for you
| Problem | What the plugin sets up |
|---|---|
| Unclear what to build | `PRD.md`: what and why, each requirement with an ID and its status. Setup writes it with you. |
| Lost context between sessions | `HANDOFF.md` (where things stand), `TODO.md` (one work board), `DECISIONS.md` (why) |
| Claims without proof | Rules that "done" needs command output just run; new tests must fail first, security logic gets a mutation check |
| Scope creep and weakened tests | Each job is a ticket with an Allow list; `tools/guard.sh` fails on files outside it, deleted tests, skip markers, or fewer assertions |
| Big jobs in one long run | A planning agent (the router) splits work into tickets; worker, tester, and reviewer agents each do one ticket in its own git worktree; the router re-checks before merging |

## How a job runs
1. You put work on the board (`TODO.md`), or ask the router to plan it.
2. The router writes a ticket: goal, files allowed, checks to run.
3. A worker (and a tester for risky logic) does the ticket in a separate worktree.
4. The router runs the guard and the checks itself; a reviewer looks at the diff for risky changes.
5. Only then is it merged, and the board and notes are updated.

You can also skip the router and just talk to Claude as usual; the rules in `CLAUDE.md` still apply. Every rule exists because something went wrong without it; the reasons are in `templates/DECISIONS.md` (W-01 to W-09).

## Two setup paths
| Skill | Use when | What it does |
|---|---|---|
| `/app-project-workflow:adopt` | The project already has code, docs, or its own Claude Code setup | Surveys the project read-only, records a test baseline, keeps an existing PRD or drafts one from what is built, asks instead of guessing, merges existing rules and tasks into the templates, never overwrites |
| `/app-project-workflow:bootstrap` | New or empty folder | Interviews you about the project, writes a first PRD of what will be built, sets up the repo layout, fills the core docs for this project, no app scaffolding |

Both write the PRD into one template (`templates/PRD.md`): what and why, requirements with IDs (`FR-01`), a status, and evidence. You confirm every requirement; anything unknown goes to "Open questions". The two methods are in `reference/prd.md`.

Both explain the defaults below, ask which to change, smoke-test the tools, and end with a plain-language report. Nothing is committed unless you ask. During setup the skill copies its material into a temporary `.workflow-setup/` folder in the project (the installed plugin lives outside the project) and deletes it at the end.

## Install
From any terminal (macOS, Linux, or Windows):
```
claude plugin marketplace add Nazhra05/Super-set
claude plugin install app-project-workflow@super-set
```
Or inside a Claude Code session: `/plugin marketplace add Nazhra05/Super-set`, then `/plugin install app-project-workflow@super-set`. Plugins live in your user folder, so the desktop app and the terminal see the same installation.

Then open Claude Code in the target project (terminal or desktop app) and run one of the two skills. After setup the project is self-contained: the agents, skills, and tools are copied into it, so the plugin can be removed without breaking the project.

## Daily use
The flow is the same on every surface; only starting the router differs.
- **Terminal:** `claude --agent router --model <router model> --effort high` from the project root.
- **Desktop app:** router mode is a few keys in `.claude/settings.local.json` (`agent`, `model`, `effortLevel`, and `WORKFLOW_SURFACE=desktop`); the project's `WORKFLOW.md` has the exact block. Every new session in that project then starts as the router until you remove the keys.

The router works through `TODO.md`. Ordinary sessions without the router stay available for discussion and small edits.

### Terminal vs desktop app
| | Terminal | Desktop app |
|---|---|---|
| Start the router | `--agent router` flag | router mode in `.claude/settings.local.json` |
| Usage guard | reads `.claude/usage.json` from the status line; above 90% of the 5-hour or 7-day limit it stops dispatching | the app does not run status lines, so the router keeps every ticket boundary ready for a stop and stops cleanly when the app shows a usage-limit notice |
| Everything else | same files, same agents, same tools | same |

## Opinionated defaults (and how to change them)
These are deliberate. The setup skills explain them and ask which to change; afterwards, change them in the files named.

| Default | Why | Where to change |
|---|---|---|
| Discussion first: a question gets an answer, not file changes | Prevents unasked edits | `CLAUDE.md` rule 1 |
| Approval only for irreversible actions; the router merges into the working branch and pushes on its own | Reversible steps waiting for a yes add friction without safety | `WORKFLOW.md` "Still needs owner approval", W-06 |
| Claims need fresh command output; existing tests are not assumed genuine; red-green and mutation checks for security logic | Agents reported "passing" for work that was not | `CLAUDE.md` rule 5, W-01 |
| YAGNI: every line needs a user today | Agents add code nobody calls | `CLAUDE.md` rule 3, W-02 |
| Subagents never commit; `guard.sh` enforces the ticket's Allow list | Scope creep and silent test weakening | `tickets/_TEMPLATE.md`, `tools/guard.sh` |
| Reviewer model by risk: opus for security, sonnet for ordinary logic, none for text | Reviews cost most of what the reviewed work costs | `WORKFLOW.md`, W-05 |
| Models: router strongest, worker and tester sonnet, Explore haiku | Cost versus judgement per role | `model:` line in `.claude/agents/*.md` |
| Tickets sized to about 60% of the agent turn limit | Agents cut off at the limit leave no report | `tickets/_TEMPLATE.md`, W-07 |
| Documents in English or Bahasa Indonesia (chosen at setup; recommended: Indonesian when you write in Indonesian); code, identifiers, comments, and commits always English; Claude replies in your language; common terms (ticket, worktree, merge, and the project's own terms) stay in one form; Conventional Commits; no em dashes in docs | Readable docs for you, one language for code, no mixed terms | `CLAUDE.md` rules 6 and 8, section "Terms" |
| Guard patterns for Jest, Vitest, Playwright, PHPUnit skip | Only patterns proven to catch weakened tests | `tools/workflow.conf`; prove a new pattern with a guard run that must fail |

To override a W-xx decision in a project, add a project decision (D-xx) in `DECISIONS.md` with the reason, then change the file.

## What lands in the project
- Core docs: `PRD.md`, `CLAUDE.md`, `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `tickets/_TEMPLATE.md`, filled for that project, in English or Indonesian. Agent prompts, skills, and tools are the same in both.
- `.claude/agents/`: router, worker, tester, reviewer, Explore.
- `.claude/skills/`: `verification-before-completion`, `systematic-debugging`, `test-driven-development`, `receiving-code-review`, `writing-plans`.
- `.claude/settings.json`: Read deny for `.env` files, status line.
- `tools/`: `workflow.conf` (repos, branches, install command, guard patterns), `wt.sh`, `guard.sh`, `verify.sh`, `statusline.js`.

## Requirements
- Git and Node.js.
- Bash: built in on macOS and Linux. On Windows, Git for Windows (Git Bash), which Claude Code on Windows already uses for its Bash tool.
- One repo or several: `tools/workflow.conf` lists each repo with its alias, path, and working branch.

## Layout of this plugin
In the Super-set repository this plugin lives in `plugins/app-project-workflow/`.
```
.claude-plugin/   plugin.json
skills/           adopt, bootstrap
reference/        setup-interview.md, prd.md, install-steps.md (shared by both skills)
scripts/          stage.sh (copies setup material into the project)
templates/        everything copied into a project (English core docs)
templates/id/     the core docs in Indonesian, same structure
```

## License
MIT, see `LICENSE`. The five skills in `templates/.claude/skills/` are adapted from [obra/superpowers](https://github.com/obra/superpowers) (MIT); attribution and changes are in `templates/.claude/skills/NOTICE`.
