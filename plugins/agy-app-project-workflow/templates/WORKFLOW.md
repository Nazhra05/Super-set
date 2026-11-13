# WORKFLOW.md: ticket flow for {{PROJECT_NAME}}

In force since setup ({{SETUP_DATE}}, W-04). Project rules in `AGENTS.md` still apply in full; this file only adds how work is split. The board is `TODO.md`, one file per ticket in `tickets/`.

## Starting a router session
The router skill is `.agents/skills/router/SKILL.md`. The flow is the same on every Antigravity surface (Antigravity 2.0 desktop app, Antigravity IDE, and Antigravity CLI `agy`):
- Invoke the `router` skill (`/router` or ask the agent to "start the router session and work through `TODO.md`"). Use your chosen main-session model (`{{ROUTER_MODEL}}` recommended). An ordinary session without invoking `router` keeps working as before for discussion or one-off tasks.

## Roles
| Role | Model tier (`invoke_subagent`) | Task | Limits |
|---|---|---|---|
| router (main session) | {{ROUTER_MODEL}} | plan, brief, dispatch, verify, merge, write `TODO.md` | only writer of `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `tickets/`; in `PRD.md` only the Status and Evidence of a requirement |
| worker | {{WORKER_MODEL}} | implement one ticket in a worktree | only files in Allow, no commit |
| tester | {{TESTER_MODEL}} | red-green tests, mutation checks | only test files |
| reviewer | `pro` or `flash`, by risk tier (below) | read-only review of ticket + diff | no writes, no test runs |
| Explore | {{EXPLORE_MODEL}} | locate (`path:line`) | not for judging logic or security |

## Ticket lifecycle
`Ready` → `In progress` (worktree created) → `Review` (worker/tester done) → `Verified` (guard, verify, reviewer clean) → `Merged` → `Done`. Two failures: the router takes over, splits the ticket, or diagnoses and writes a new fix brief (raising the worker model to `pro` if needed); no third identical attempt without a diagnosis, and the router does not stop to wait for the owner (W-06).

### Queue, merge, and push (W-06)
- The router runs the "Execution order" in `TODO.md` until it is empty, without `Ready` per ticket. Inbox or `Proposed` items may be promoted to the next ticket when they need no owner decision and are not irreversible; the reason goes in one line in the queue.
- Merge `--no-ff` into the working branch without approval after guard, verify, and reviewer are clean. A merge counts as successful when the suite after the merge is green, the worktree is removed, and test data is cleaned; only then is another ticket in the same repo merged or started.
- Push automatically after a ticket when the repo has a remote. Small tickets may share a push with the next one; no unpushed working-branch commits at session end. Docs are committed at the end of each ticket.
- Report to the owner: one summary per ticket pair, and one when the queue is empty.

### Reviewer risk tier (W-05)
| Ticket type | Reviewer (`Model`) |
|---|---|
| Auth, session, authorization, security | `pro` |
| E2E, tests, ordinary logic | `flash` |
| Text or docs only | none |

One round of fixes for reviewer findings may be verified by the router without a second review, as long as each finding gets evidence (command output or code line). Exception: auth, session, authorization, and security tickets are always reviewed again.

### Test evidence
- The router weighs test depth per ticket (W-06): text, docs, or config with no logic need no new test, only the relevant suite; new tests only where behaviour can be wrong. The reason goes in one line in the ticket.
- Auth/security logic: red-green and a mutation check (rule 5 in `AGENTS.md`).
- E2E: every new assertion is proven red by briefly breaking the flow; the test must fail. Green alone is not evidence (vacuous assertions pass).

## Tools (`tools/`)
On Windows, `run_command` runs in PowerShell; always invoke shell scripts with `bash tools/<script>.sh ...`.
- `workflow.conf`: repos (alias, path, working branch), files copied into worktrees, install command, guard patterns.
- `wt.sh add|rm <repo-alias> <ID>`: worktree in `_wt/<ID>-<alias>`, branch `t/<ID>` from the working branch, copies `COPY_FILES` without reading them, runs `INSTALL_CMD`. `rm` refuses a worktree with uncommitted changes (`WT_DISCARD=1` to discard on purpose), then removes it and runs `branch -d` (refuses if unmerged).
- `guard.sh <wt> <base> <ticket>`: fails on a file outside Allow, a deleted test, an added skip/only/todo marker, fewer assertion lines, or any commit on the ticket branch above base (subagents must not commit). So the router runs guard **before** it commits.
- `verify.sh <wt> <ticket>`: runs the ticket's `verify` block, prints the last 25 lines and the exit code of each line.
- `env-guard.js`: `PreToolUse` hook script configured in `.agents/hooks.json` that blocks reading, editing, writing, or printing `.env` files.

## Parallel limits and shared resources
- Max 2 subagents at once, only for truly independent tickets. Small tickets (text, one line) are done by the router directly (`Executor: router`).
- Shared resources (only one ticket at a time may use each): {{SHARED_RESOURCES}}
- The final verification (full suite before merge) runs only when no other ticket is running.
- A failure that disappears on rerun goes to the Inbox in `TODO.md`; it is not ignored.

## Checks before starting
Add a line here for every pre-condition proven by a failed run; delete it once the cause is fixed.
- Always run shell tools via `bash tools/<script>.sh`. Do not `cd` into a worktree and stay there; use `git -C <wt>` or `bash -c "cd ... && ..."`. A process still inside the folder makes `wt.sh rm` fail (folder locked on Windows).
- Commit the ticket and run `bash tools/wt.sh rm` as separate commands; check `git -C <wt> log` first.

## Context and tokens
- The router reads `TODO.md`, the active ticket, and subagent reports (max 40 lines). It does not read transcripts or full diffs.
- Live state is in the ticket files, so `/compact` at a ticket boundary loses nothing.
- Subagents do not see the conversation; all context is in the ticket.
- Budget per ticket is in the ticket (`maxTurns`, retry max 2). Ticket size follows W-07: fits in about 60% of the agent's turn limit (tester max 6 to 8 mutations, worker about 8 files, reviewer 5 explicit check items); the brief names the tool-call limit for the report.
- **Stop-ready boundaries (W-06):** keep every ticket boundary compact-ready (`TODO.md`, the ticket, and `HANDOFF.md` current; docs committed; no subagent running). When the conversation grows long, ask the owner to run `/compact`. When the platform shows a quota or usage-limit notice, finish only the piece in hand, update the ticket, `TODO.md`, and `HANDOFF.md`, commit docs, and stop with a report of what is left.
- **Session report:** at session end the router writes `{{SESSION_REPORT_DIR}}/Session_<date>_<topic>.md`: tickets finished, decisions, Inbox findings, and spawn/retry counts per ticket (W-07).

## Still needs owner approval
{{IRREVERSIBLE_ACTIONS}}, `reset --hard`, force-push, bulk deletes beyond your own test data, deleting or weakening tests, global installs, costs, and any item with status `Waiting decision`. Merging into the working branch and pushing are done by the router. Subagents never commit, push, or merge.

## Known limits
- `.agents/hooks.json` blocks `read_file`, `edit_file`, `write_file`, and `run_command` calls that reference `.env` files via `tools/env-guard.js`. Commits by subagents are caught by `guard.sh`, not by a global deny, because a global deny would also block commits the owner orders in the main session.
- The router's `edit_file`/`write_file` tools cannot be limited per path by the platform; the discipline lives in the prompt.

