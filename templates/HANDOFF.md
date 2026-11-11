# HANDOFF: state of the last session

Start here when opening a new session. Open Claude Code from the project root `{{PROJECT_ROOT}}` so `CLAUDE.md`, the agents, and the project skills load.
Updated: {{SETUP_DATE}} (workflow setup). This file holds only the current state; history is in the Done log of `TODO.md` and `git log`.

## Current state (checked by command, {{SETUP_DATE}})
{{CURRENT_STATE}}

## Next step
{{NEXT_STEP}}

## How to work
- Ticket flow: `WORKFLOW.md`. Router: `claude --agent router --model {{ROUTER_MODEL}} --effort high` from the root in a terminal, or router mode in `.claude/settings.local.json` for the desktop app (`WORKFLOW.md`, "Starting a router session"). Discussion or doc sessions may run without the router.
- Session reports for the owner: `{{SESSION_REPORT_DIR}}`.

## Waiting for the owner
{{WAITING_OWNER}}

## Not checked in a browser
UI changes not yet seen in a real browser. Remove a line once it has been checked.
