# <ID>: <short title>

- **Gate:** <gate from WORKFLOW.md, for example Style frames or Shots>
- **Requirement:** <R-xx from PRD.md, or `-` for tooling and docs>
- **References:** <REF-xx from REFERENCES.md, each with what to take from it>
- **Executor:** producer | asset-builder (then visual-reviewer)
- **Model:** (subagent default from `WORKFLOW.md`; write only when different, with the reason)
- **Budget:** maxTurns = agent limit (asset-builder 40, visual-reviewer 30), target about 60%; report no later than tool call (limit - 8); fix rounds max 2
- **Status:** Ready | In progress | Review | Done | Blocked
- **Blocked by:** -

## Goal
One paragraph: what must exist or look different after this ticket, and why.

## Context
Only what the agent needs: file paths, the shot's time range, the script lines, relevant pitfalls from `AGENTS.md`, the `STYLE.md` sections that apply. Subagents do not see the conversation.

## Allow
One glob per line in backticks (relative to the project root). Anything outside is a violation for `tools/scope.sh`.
- `path/to/scene-1.html`
- `path/to/assets/scene-1/*`

## Forbidden
- Do not overwrite or delete originals (script, recordings, source art) or anything in `REFERENCES.md`.
- Do not change dialogue, facts, or text on screen that comes from the script.
- Do not base a design on an existing character, mascot, or brand asset unless this ticket says the owner approved it.
- Do not open or copy `.env`. Other findings: write them in the Report as Inbox candidates.

## Verify
Each line runs from the project root through `bash tools/verify.sh`. Exit 0 = pass.
```verify
{{DEFAULT_VERIFY}}
```

## Review
Frames the visual-reviewer must grab and check (time codes), and what each must show:
- 

## Report (filled by the agent, max 40 lines)
- Files changed:
- Verify output:
- References used and how:
- Frames produced (paths):
- Not done or not checked:
- Inbox findings:

## Producer result
- scope:
- verify (rerun by producer):
- visual-reviewer:
- Owner shown (date):

