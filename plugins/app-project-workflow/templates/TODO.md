# TODO.md: the single work board for {{PROJECT_NAME}}

The only live work list. Decisions are in `DECISIONS.md`, session state in `HANDOFF.md`.

## Rules of use
1. **New findings go to the Inbox first, they are not executed directly.** Enough detail: what, evidence, impact. The router may triage items that need no owner decision and are not irreversible (W-06); the rest is discussed with the owner.
2. **The router runs the "Execution order" until it is empty** without `Ready` per ticket (W-06), then adds suitable Inbox or `Proposed` items to the order with a one-line reason. `In progress` max two, per the parallel limits in `WORKFLOW.md`. Items with an open `Blocked by` or `Waiting decision` are skipped.
3. **Status:** `Inbox` · `Proposed` (recommended; the router may promote it when no owner decision is needed) · `Ready` · `In progress` · `Done` · `Waiting decision` (needs the owner's answer) · `Blocked` (waits for another task).
4. **Scope limit.** A finding in the middle of a task stops at the task boundary, goes to the Inbox, and work continues. No silent scope growth, no dependency installs or config changes not written in the task.
5. **Every task has Done criteria as a verification command.** Claim done only with command output (rule 5 in `CLAUDE.md`). Irreversible changes always ask for separate approval (`WORKFLOW.md`).
6. **Owner:** `Owner` (actions on servers, accounts, external services) or `Claude`.
7. **Ticket execution** follows `WORKFLOW.md`. Tasks run by worker/tester get `tickets/<ID>.md` from `tickets/_TEMPLATE.md`; this board stays the only list.

## Execution order
| # | Task | Owner | Why this order |
|---|---|---|---|
{{EXECUTION_ORDER}}

## Tasks
Group by track when the board grows (for example Security, Tests, Product, Hygiene, Deploy). ID prefix = track letter.
| ID | Task | Owner | Status | Blocked by | Done criteria |
|---|---|---|---|---|---|
{{TASKS}}

## Inbox (not triaged; do not execute)
{{INBOX}}

## Done log
Newest first: date, ID, one line, commit.
