# Brief, art direction, and references

Shared by the `adopt` and `bootstrap` skills. Three documents, each from a template in `TEMPLATES/` (or `TEMPLATES/id/` for Indonesian; same sections in the same order):
- `PRD.md`: the brief. What the content must achieve and why. Requirements with IDs `R-01`, `R-02`, ...
- `STYLE.md`: art direction. How it must look, move, and sound.
- `REFERENCES.md`: every reference with an ID `REF-01`, `REF-02`, ..., what it shows, what to take from it, and where it is used.

## Rules for all three
- Write only what the owner said or what the project proves. Anything unknown goes to "Open questions"; never invent a fact, number, character trait, or brand rule.
- Facts and numbers shown on screen come only from the script or a source the owner names; each gets its source in the brief.
- Describing a reference image follows the rule in `CLAUDE.md`: what is seen, then what is inferred, and ask when it matters. Do not claim exact colors or positions from looking; measure them (for example sample pixel colors with a script) or ask.
- Ask with AskUserQuestion, at most 4 questions per call. Show each draft in plain language before the install file list, and continue after a yes.
- Placeholders: `{{PRD_GOAL}}` (purpose, audience, sign of success), `{{PRD_FORMAT}}` (platform, aspect ratio, resolution, duration, language, captions, delivery file), `{{PRD_MESSAGE}}` (key message, call to action, facts with source), `{{PRD_REQUIREMENTS}}` (table rows), `{{PRD_CONSTRAINTS}}` (brand rules, legal, accessibility), `{{PRD_OPEN_QUESTIONS}}`, `{{PRD_HISTORY}}`; `{{STYLE_LOOK}}`, `{{STYLE_PALETTE}}`, `{{STYLE_TYPE}}`, `{{STYLE_MOTION}}`, `{{STYLE_SOUND}}`, `{{STYLE_CHARACTERS}}`, `{{STYLE_DO}}`, `{{STYLE_DONT}}`; `{{REFERENCE_ROWS}}`.

## Requirements in the brief
One line per requirement, phrased as something a viewer sees or hears, or a rule the content follows (for example "Scene 1 shows the unemployment rate with its source on screen"). Status values: `Planned`, `Met` (seen in a frame or measured, with evidence), `Partial`, `Not checked`. Evidence is a frame file, a time code in a render, or a command.

## References
- Every reference counts: files in the project's reference and asset folders, links the owner gives, repositories, style examples. None is left out of `REFERENCES.md`; one with no clear use gets "Use for: ask owner".
- Columns: ID, path or URL, what it shows (seen), what to take from it (agreed with the owner), used in (ticket IDs, filled later).
- A repository or web page is not "read" from a summary of its front page. The researcher agent reads it as described in `WORKFLOW.md`, "Research", and writes a note in `docs/research/`.

## Bootstrap: from the owner
1. The goal, audience, platform, and the first outcome that matters; how the owner will know it worked.
2. Format: platform, aspect ratio, resolution, duration, language, captions.
3. Message: the key message, call to action, and any facts with their source.
4. Requirements: the scenes or deliverables the owner already knows. Each becomes `R-xx` with status `Planned`.
5. References the owner has: collect them into `REFERENCES.md` and ask what to take from each.
6. Style: a first `STYLE.md` from the owner's words and the references; empty parts say "To be set at the style-frame gate".

## Adopt: from what exists
1. **An existing brief or spec** (found in the survey): keep it; ask whether to keep it as the brief (Recommended; `PRD.md` in the document map then points to it) or to restructure it into the template with the original linked in History.
2. **No brief:** draft one from the script, the voice-over, and the project notes. Scenes and on-screen facts found become candidate requirements with evidence. The owner confirms each: keep, drop, or unsure (to Open questions).
3. **Style:** draft `STYLE.md` from what is already made (fonts, colors, characters, motion found in the project files) and from the references. Colors are read from files or measured, not estimated from a screenshot.
4. **References:** one row per reference found in the survey, no exceptions. Ask the owner what to take from each.
