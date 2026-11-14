# TODO.md: the single work board for {{PROJECT_NAME}}

The only live work list. Decisions are in `DECISIONS.md`, session state in `HANDOFF.md`.

## Rules of use
1. **New findings go to the Inbox first, they are not executed directly.** Enough detail: what, evidence (frame, time code, file), impact.
2. **Gates first.** Work behind a gate that is not approved waits. The producer runs the "Execution order" up to the next gate marked approval, then stops and reports.
3. **Status:** `Inbox` · `Proposed` · `Ready` · `In progress` · `Done` · `Waiting decision` (needs the owner's answer) · `Blocked` (waits for another task).
4. **Scope limit.** A finding in the middle of a task goes to the Inbox and work continues. No silent scope growth, no tool installs not written in the task.
5. **Every task has done criteria as a command or a frame check.** Claim done only with output and the frames looked at (rule 6 in `AGENTS.md`).
6. **Owner:** `Owner` (approvals, recordings, accounts, publishing) or `Agent`.
7. **Ticket execution** follows `WORKFLOW.md`; tickets live in `tickets/`.

## Gates
| Gate | Status | Approved (date) | Evidence |
|---|---|---|---|
{{GATES}}

## Execution order
| # | Task | Owner | Why this order |
|---|---|---|---|
{{EXECUTION_ORDER}}

## Tasks
| ID | Task | Requirement | References | Owner | Status | Blocked by | Done criteria |
|---|---|---|---|---|---|---|---|
{{TASKS}}

## Inbox (not triaged; do not execute)
{{INBOX}}

## Done log
Newest first: date, ID, one line, commit or file.

