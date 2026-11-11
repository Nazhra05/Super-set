# WORKFLOW.md: gates and ticket flow for {{PROJECT_NAME}}

In force since setup ({{SETUP_DATE}}). Project rules in `CLAUDE.md` still apply in full; this file adds the production gates and how work is split. The board is `TODO.md`, one file per ticket in `tickets/`.

## Starting a producer session
The producer profile is `.claude/agents/producer.md`. The flow is the same on every surface; only the way to start it differs.
- **Terminal (macOS, Linux, Windows):** from the project root, `claude --agent producer --model {{PRODUCER_MODEL}} --effort high`. An ordinary `claude` session keeps working as before.
- **Desktop app** (or any surface that cannot pass `--agent`): put these keys in `.claude/settings.local.json` (personal, not committed), then open a new session in the project folder:
  ```json
  {
    "agent": "producer",
    "model": "{{PRODUCER_MODEL}}",
    "effortLevel": "high",
    "env": { "WORKFLOW_SURFACE": "desktop" }
  }
  ```
  While the keys are there, every new session in this project on this machine starts as the producer. Remove the four keys to go back to ordinary sessions.

## Roles
| Role | Model / effort | Task | Limits |
|---|---|---|---|
| producer (main session) | {{PRODUCER_MODEL}} / high | plan gates and tickets, brief, dispatch, verify, report to the owner | only writer of `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `REFERENCES.md`, `tickets/`; in `PRD.md` only Status and Evidence; `STYLE.md` only after a gate the owner approved |
| asset-builder | {{BUILDER_MODEL}} / medium | build one ticket: art, characters, scenes, audio cues | only files in Allow, no commit; one builder at a time |
| visual-reviewer | {{REVIEWER_MODEL}} / high | read-only review of frames and files against the ticket, `STYLE.md`, `PRD.md`, and the listed references | no edits to project files; frame grabs go to `.review/` |
| researcher | {{RESEARCHER_MODEL}} / medium | read external sources and write one cited note | writes only `docs/research/<topic>.md` and clones under `.research/` |
| Explore | {{EXPLORE_MODEL}} / low | locate files and lines | no judgement |

## Gates
Production moves through these gates in order. A gate marked **approval** stops the producer until the owner says yes, with the evidence in front of them (frames, sheets, a rough cut). Status of each gate lives in `TODO.md`, "Gates".

| Gate | Output | Owner |
|---|---|---|
| Brief | `PRD.md` agreed | **approval** |
| Script and storyboard | script locked to the recording; one panel per shot with time code, framing, action, text on screen | report |
| Style frames | 2 to 4 full-color still frames of key shots, shown next to the references they answer | **approval** |
| Character sheets | per character: turnaround, expression sheet, mouth chart, pose sheet, colors (skill `character-design`) | **approval** |
| Animatic | timed rough cut with the real audio | **approval** |
| Shots | each shot built and reviewed per ticket | report per pair of tickets |
| Final | full render, audio measured, captions checked, watched with sound by the owner | **approval** |

A gate may be skipped only by a project decision (D-xx) with the reason, for example "no characters in this project".

## Ticket loop
1. Take the next item from "Execution order" in `TODO.md`. Skip anything with an open `Blocked by` or `Waiting decision`, or behind a gate that is not approved.
2. Fill the ticket from `tickets/_TEMPLATE.md`: goal, the requirement (`R-xx`), the references (`REF-xx`) and what to take from each, Allow globs, verify commands, the frames the reviewer must check. Size it to one shot, one asset, or one sheet.
3. Dispatch one `asset-builder` with the ticket path. The builder works in the project folder (no worktrees: renders and art are large), so only one builder runs at a time; the researcher, visual-reviewer, and Explore may run beside it.
4. When it returns, its report is a claim. Run `tools/scope.sh <ticket>` (git only) and `tools/verify.sh <ticket>` yourself.
5. Dispatch `visual-reviewer` with the ticket path. It grabs the frames named in the ticket and reports per check item `seen` or `inferred`, with the frame files.
6. Fix rounds: at most two; then diagnose (`systematic-debugging`) or split the ticket. Never a third blind retry.
7. Done: update the ticket, `TODO.md`, the requirement's Status and Evidence in `PRD.md`, and "Used in" in `REFERENCES.md`. In a git repo, commit the ticket's files and the docs. Push only with the owner's approval unless a project decision allows it.
8. Report to the owner once per gate and once per pair of shot tickets, with the frames.

## Images from the owner (C-01)
When the owner sends a screenshot or frame: write what is seen (`seen`), what you infer (`inferred`), and the request in one sentence. If the image could mean two different fixes, ask before building. Locate the problem with a measurement or a frame grab at the exact time, not by eye.

## Research (C-05)
A source is read, not summarized from its front page.
- **Repository:** shallow clone into `.research/<name>` (`git clone --depth 1`), or list and read files with `gh api repos/<owner>/<repo>/contents/<path>`. Read the README, the folder tree, and the files that matter.
- **Web page:** fetch it; for long pages read on with an offset until the relevant part is read.
- **Note:** `docs/research/<topic>.md` lists the files or pages read, what is taken (with path or URL), what is not taken and why, and what could not be read. A source that could not be read is reported as such, never filled in.
- Licenses: copying code or art needs a license check and the owner's approval; reading for ideas does not.

## Context and tokens
- The producer reads `TODO.md`, the active ticket, and subagent reports (max 40 lines). It does not read transcripts or full diffs.
- Images are expensive. Look at downscaled contact sheets first; open a full frame only where a detail matters.
- One ticket per dispatch, one gate per stretch of work: report at the gate instead of running on for hours.
- **Usage (terminal):** read `.claude/usage.json` (written by `tools/statusline.js`) before a dispatch. Above 90% of the 5-hour or 7-day limit, or file missing or older than 10 minutes: only work that surely finishes cleanly; otherwise stop, update the ticket, `TODO.md`, and `HANDOFF.md`, and report. Context at 60% or more: prepare compact at the ticket boundary and ask the owner to `/compact`.
- **Desktop app:** the status line does not run there (`WORKFLOW_SURFACE=desktop`). Keep every ticket boundary compact-ready, and when the app shows a usage-limit notice, finish only the piece in hand, update the files above, and stop with a report.
- **Session report:** at session end write `{{SESSION_REPORT_DIR}}/Session_<date>_<topic>.md`: tickets finished, gates passed, decisions, Inbox findings, and cost (tokens per agent, cut-off runs).

## Frame checks
Frame grab: {{FRAME_COMMAND}}. Frames for review go to `.review/` (not committed). Every shot ticket names the time codes to check: the first frame, each text change, each character expression change, and the last frame.

## Still needs owner approval
{{IRREVERSIBLE_ACTIONS}}, the gates marked **approval**, changing dialogue or facts, using a third-party asset (license), basing a new character or design on an existing character, mascot, or brand asset, sending project material to an external AI service, deleting files beyond your own test output, global installs, costs, and any item with status `Waiting decision`. Subagents never commit, push, or publish.

## Known limits
- Without git, `tools/scope.sh` cannot check which files a builder changed; the producer then lists changed files by modification time and says the check was skipped.
- The producer's Edit/Write tools cannot be limited per path; the discipline lives in the prompt.
- Claude reads images with limited precision for exact positions, sizes, and counts; rule 5 in `CLAUDE.md` is the answer, not a guarantee.
