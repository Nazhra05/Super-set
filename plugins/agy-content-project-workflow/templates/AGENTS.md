# AGENTS.md: {{PROJECT_NAME}}

Short on purpose. Details live in the documents it points to; do not copy them here.
Last verified: {{SETUP_DATE}}. **New session or after compact: read `HANDOFF.md` first.** Status numbers (durations, counts, versions) are not written here; take them from command output.

## What this is
{{PROJECT_SUMMARY}}

| Part | Path |
|---|---|
{{FOLDER_TABLE}}

Tool: {{TOOLCHAIN}}. Brief: `PRD.md`. Look and sound: `STYLE.md`. References: `REFERENCES.md`.

## How to work with me (owner: {{OWNER_ROLE}})
1. **Discussion vs execution.** Default is discussion: when I ask, discuss, compare, or send only an image, answer and do not change files. Execute only after a clear work order. Unsure? Ask in one sentence.
2. **Clear, reversible tasks: do them, do not ask for approval per step.** Approval only for what cannot be undone and at the gates: see "Gates" and "Still needs owner approval" in `WORKFLOW.md`.
3. **Change only what was asked.** Report other findings, do not act on them. **Replace** old versions, do not stack a new one beside them; delete what becomes dead. **YAGNI:** every file and every element on screen needs a reason today (a requirement in `PRD.md`, a line in `STYLE.md`, or a caller in the code).
4. **Do not invent** facts, numbers, dialogue, names, or what a reference shows. Facts on screen come only from the script or a source named in `PRD.md`. Text on screen matches the recording; changing dialogue means re-recording, so ask first.
5. **Look before you interpret (C-01).** For every image (my screenshots, references, frames): first write what you see, marked `seen`, then what you infer, marked `inferred`, and restate what I asked in one sentence. When the meaning decides the work, ask before acting. Never claim exact positions, sizes, or colors from looking; measure them (crop, zoom, pixel samples, frame grabs at a time code).
6. **Verify through tools, not reports (C-02).** Claim "done" only with output of a command just run **and** the frames looked at (skill `verification-before-completion`). Agent reports and old documents are not evidence. Say plainly what was not done: not rendered, not watched with sound, not checked on a phone.
7. **Do not commit or push unless asked**, except the producer committing in the ticket flow (`WORKFLOW.md`). Conventional Commits, subject max 72 characters.
8. **Concise summaries for me in plain language (max 8 to 10 lines)**: always write `<ID> (<short title>)` instead of a bare ID (`T-xx`, `R-xx`, `REF-xx`, `D-xx`). State what changed, how it looks (with the frame), the risk, and what decision you need from me (no command log dumps).
9. Language: reply to me in {{OWNER_LANGUAGE}}, following "Terms" below. Code, identifiers, comments, commits, and documents in English. No em dashes in documents.

## Terms
Applies to replies, reports, and documents written in a language other than English. Keep all workflow terms and all standard motion graphics, video, graphic design, and software terms in English (never translate them into stiff local equivalents): ticket, task, gate, brief, storyboard, style frame, animatic, character sheet, turnaround, expression sheet, mouth chart, pose sheet, rig, render, frame, contact sheet, shot, scene, asset, reference, producer, asset-builder, frame-prep, visual-reviewer, researcher, Inbox, Allow, verify, the status values (`Ready`, `In progress`, `Planned`, `Met`, and so on), IDs (`R-01`, `REF-01`, `C-01`, `D-01`), section names (for example "Execution order"), and craft terms such as keyframe, easing, anticipation, follow-through, overlap, timing, pacing, hook, safe zone, aspect ratio, frame rate, resolution, lower third, rough cut, hierarchy, typography, kerning, leading, contrast, palette, saturation, voice-over, loudness, and caption. Project terms agreed with the owner:

| Use | Do not mix with |
|---|---|
{{PROJECT_TERMS}}

## Commands (verified {{SETUP_DATE}})
{{COMMANDS}}

## Proven pitfalls (do not re-guess)
Add an entry only after it has been proven by command output, with the date.
{{PITFALLS}}

## Skills
- In `.agents/skills/`: `producer`, `content-fundamentals`, `motion-principles`, `design-basics`, `character-design` (knowledge, read when the task needs it), `verification-before-completion`, `systematic-debugging`. License: `.agents/skills/NOTICE`.
- Skills for the video tool: {{TOOL_SKILLS}}.
- **Ticket flow:** splitting work into subagents happens only through `WORKFLOW.md`, in a producer session (`producer` skill). Outside that flow, subagents are created only when I ask. Rules 1 to 9 apply to every agent.

## Document map (read what the task needs, not everything)
`PRD.md` (brief: what and why) · `STYLE.md` (how it looks and sounds) · `REFERENCES.md` (every reference and its use) · `WORKFLOW.md` (gates and ticket flow) · `TODO.md` (the only work board) · `HANDOFF.md` (last session state, start here) · `DECISIONS.md` (decisions and what is waiting) · `docs/research/` (cited research notes){{EXTRA_DOCS}}

