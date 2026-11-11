# HANDOFF: state of the last session

Start here when opening a new session. Open Claude Code from the project root `{{PROJECT_ROOT}}` so `CLAUDE.md`, the agents, and the project skills load.
Updated: {{SETUP_DATE}} (workflow setup). This file holds only the current state; history is in the Done log of `TODO.md`.

## Current state (checked by command, {{SETUP_DATE}})
{{CURRENT_STATE}}

## Next step
{{NEXT_STEP}}

## How to work
- Gates and ticket flow: `WORKFLOW.md`. Producer: `claude --agent producer --model {{PRODUCER_MODEL}} --effort high` from the root in a terminal, or producer mode in `.claude/settings.local.json` for the desktop app (`WORKFLOW.md`, "Starting a producer session"). Discussion sessions may run without the producer.
- Session reports for the owner: `{{SESSION_REPORT_DIR}}`.

## Waiting for the owner
{{WAITING_OWNER}}

## Not yet seen or heard by the owner
Frames, renders, or audio changes the owner has not looked at or listened to. Remove a line once they have.
