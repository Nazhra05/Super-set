# WORKFLOW.md: ticket flow for {{PROJECT_NAME}}

In force since setup ({{SETUP_DATE}}, W-04). Project rules in `CLAUDE.md` still apply in full; this file only adds how work is split. The board is `TODO.md`, one file per ticket in `tickets/`.

## Starting a router session
The router profile is `.claude/agents/router.md`. The flow is the same on every surface; only the way to start the router differs.
- **Terminal (macOS, Linux, Windows):** from the project root, `claude --agent router --model {{ROUTER_MODEL}} --effort high`. An ordinary `claude` session keeps working as before.
- **Desktop app** (or any surface that cannot pass `--agent`): Turn router mode on by putting these keys in `.claude/settings.local.json` (personal, not committed), then open a new session in the project folder:
  ```json
  {
    "agent": "router",
    "model": "{{ROUTER_MODEL}}",
    "effortLevel": "high",
    "env": { "WORKFLOW_SURFACE": "desktop" }
  }
  ```
  While the keys are there, every new session in this project on this machine starts as the router. Remove the four keys to go back to ordinary sessions. Ask Claude in an ordinary session to switch it on or off; it is a one-file change.

## Roles
| Role | Model / effort | Task | Limits |
|---|---|---|---|
| router (main session) | {{ROUTER_MODEL}} / high | plan, brief, dispatch, verify, merge, write `TODO.md` | only writer of `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `tickets/`; in `PRD.md` only the Status and Evidence of a requirement |
| worker | {{WORKER_MODEL}} / low | implement one ticket in a worktree | only files in Allow, no commit |
| tester | {{TESTER_MODEL}} / medium | red-green tests, mutation checks | only test files |
| reviewer | opus or sonnet / high, by risk tier (below) | read-only review of ticket + diff | no writes, no test runs |
| Explore | {{EXPLORE_MODEL}} / low | locate (`path:line`) | not for judging logic or security |

## Ticket lifecycle
`Ready` → `In progress` (worktree created) → `Review` (worker/tester done) → `Verified` (guard, verify, reviewer clean) → `Merged` → `Done`. Two failures: the router takes over, splits the ticket, or diagnoses and writes a new fix brief (raising the model if needed); no third identical attempt without a diagnosis, and the router does not stop to wait for the owner (W-06).

### Queue, merge, and push (W-06)
- The router runs the "Execution order" in `TODO.md` until it is empty, without `Ready` per ticket. Inbox or `Proposed` items may be promoted to the next ticket when they need no owner decision and are not irreversible; the reason goes in one line in the queue.
- Merge `--no-ff` into the working branch without approval after guard, verify, and reviewer are clean. A merge counts as successful when the suite after the merge is green, the worktree is removed, and test data is cleaned; only then is another ticket in the same repo merged or started.
- Push automatically after a ticket when the repo has a remote. Small tickets may share a push with the next one; no unpushed working-branch commits at session end. Docs are committed at the end of each ticket.
- Report to the owner: one summary per ticket pair, and one when the queue is empty.

### Reviewer risk tier (W-05)
| Ticket type | Reviewer |
|---|---|
| Auth, session, authorization, security | opus |
| E2E, tests, ordinary logic | sonnet |
| Text or docs only | none |

One round of fixes for reviewer findings may be verified by the router without a second review, as long as each finding gets evidence (command output or code line). Exception: auth, session, authorization, and security tickets are always reviewed again.

### Test evidence
- The router weighs test depth per ticket (W-06): text, docs, or config with no logic need no new test, only the relevant suite; new tests only where behaviour can be wrong. The reason goes in one line in the ticket.
- Auth/security logic: red-green and a mutation check (rule 5 in `CLAUDE.md`).
- E2E: every new assertion is proven red by briefly breaking the flow; the test must fail. Green alone is not evidence (vacuous assertions pass).

## Tools (`tools/`)
- `workflow.conf`: repos (alias, path, working branch), files copied into worktrees, install command, guard patterns.
- `wt.sh add|rm <repo-alias> <ID>`: worktree in `_wt/<ID>-<alias>`, branch `t/<ID>` from the working branch, copies `COPY_FILES` without reading them, runs `INSTALL_CMD`. `rm` refuses a worktree with uncommitted changes (`WT_DISCARD=1` to discard on purpose), then removes it and runs `branch -d` (refuses if unmerged).
- `guard.sh <wt> <base> <ticket>`: fails on a file outside Allow, a deleted test, an added skip/only/todo marker, fewer assertion lines, or any commit on the ticket branch above base (subagents must not commit). So the router runs guard **before** it commits.
- `verify.sh <wt> <ticket>`: runs the ticket's `verify` block, prints the last 25 lines and the exit code of each line.
- `statusline.js`: status line that saves Claude Code's status JSON to `.claude/usage.json` for the usage checks below. Runs in the terminal only.

## Parallel limits and shared resources
- Max 2 subagents at once, only for truly independent tickets. Small tickets (text, one line) are done by the router directly (`Executor: router`).
- Shared resources (only one ticket at a time may use each): {{SHARED_RESOURCES}}
- The final verification (full suite before merge) runs only when no other ticket is running.
- A failure that disappears on rerun goes to the Inbox in `TODO.md`; it is not ignored.

## Checks before starting
Add a line here for every pre-condition proven by a failed run; delete it once the cause is fixed.
- Do not `cd` into a worktree in the main shell; use a subshell `( cd ... && ... )` or `git -C`. A shell still inside the folder makes `wt.sh rm` fail (folder locked on Windows).
- Commit the ticket and run `wt.sh rm` as separate commands; check `git log` in the worktree first.

## Context and tokens
- The router reads `TODO.md`, the active ticket, and subagent reports (max 40 lines). It does not read transcripts or full diffs.
- Live state is in the ticket files, so compact or `/clear` at a ticket boundary loses nothing.
- Subagents do not see the conversation; all context is in the ticket.
- Budget per ticket is in the ticket (`maxTurns`, retry max 2). Ticket size follows W-07: fits in about 60% of the agent's turn limit (tester max 6 to 8 mutations, worker about 8 files, reviewer 5 explicit check items); the brief names the tool-call limit for the report.
- **Usage and context (W-06):** in the terminal, read `.claude/usage.json` (written by `tools/statusline.js`) before starting a ticket and before dispatch, for example `node -e "const u=require('./.claude/usage.json');console.log(u.savedAt,u.context_window?.used_percentage,u.rate_limits)"`.
  - 5-hour or 7-day usage above 90%: only work that will surely finish cleanly, no new dispatches and no long runs. If none: stop, prepare the handoff, report the reset time. File missing or older than 10 minutes = unknown, treat it as above 90%.
  - Context at 60% or more: prepare compact at the ticket boundary (ticket, `TODO.md`, `HANDOFF.md` current; docs committed; no subagent running), then ask the owner to `/compact`.
  - **The desktop app does not run the status line** (checked 2026-11-11: a desktop session left `usage.json` untouched), so the file is not updated there (`WORKFLOW_SURFACE=desktop`). The router then does not treat the stale file as "above 90%". Instead: it keeps every ticket boundary compact-ready (the files above current, docs committed), and when the app shows a usage-limit notice it finishes only the piece in hand, updates the ticket, `TODO.md`, and `HANDOFF.md`, commits docs, and stops with a report of what is left.
- **Session report:** at session end the router writes `{{SESSION_REPORT_DIR}}/Session_<date>_<topic>.md`: tickets finished, decisions, Inbox findings, and cost details (tokens per agent from completion notices, USD cost from `.claude/usage.json` or `/cost`), including tokens of cut-off runs and the number of spawns per ticket (W-07).

## Still needs owner approval
{{IRREVERSIBLE_ACTIONS}}, `reset --hard`, force-push, bulk deletes beyond your own test data, deleting or weakening tests, global installs, costs, and any item with status `Waiting decision`. Merging into the working branch and pushing are done by the router. Subagents never commit, push, or merge.

## Known limits
- `.claude/settings.json` denies the Read tool on `.env`, `.env.local`, `.env.production`. This does not cover `cat` through Bash; that still prompts. Commits by subagents are caught by `guard.sh`, not by a global deny, because a global deny would also block commits the owner orders in the main session.
- The router's Edit/Write tools cannot be limited per path; the discipline lives in the prompt.
- `effort` in agent frontmatter is not documented to apply to the main session, so `--effort high` is part of the launch command.
