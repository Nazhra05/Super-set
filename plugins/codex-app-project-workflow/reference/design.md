# UI design flow, `DESIGN.md`, and `references/`

Shared by the `codex-app-adopt` and `codex-app-bootstrap` skills. Every project gets `DESIGN.md` (from `TEMPLATES/DESIGN.md` or `TEMPLATES/id/DESIGN.md`) and the `references/` directory tree (`references/brand/`, `references/inspiration/`, `references/mockups/`).

## Rules
- Never invent design tokens, font names, or hex colors during setup unless they are read from existing project files (in `adopt`) or explicitly handed over by the owner.
- When the owner has no visual references or says "up to you", do **not** force them to pick fonts or hex codes in text. Record the status as `Proposed (awaiting 3-mockup gate)` and note that the `designer` subagent will gather inspiration via `agent-browser` and build 3 live HTML mockups (`references/mockups/option-1.html` to `option-3.html`) for the owner to compare visually before anything is locked.
- When the project has no user interface at all (for example a pure CLI tool, backend API, or library), set `{{DESIGN_STATUS}}` to `Not applicable (no UI)` and write `None (no UI in scope).` in the remaining placeholders.

## Placeholders in `DESIGN.md`
- `{{DESIGN_STATUS}}`: `Not applicable (no UI)`, `Proposed (awaiting 3-mockup gate)`, or `Locked`.
- `{{DESIGN_ARCHETYPE}}`: 2 to 4 lines naming the product category (for example SaaS dashboard, POS workspace, developer tool, consumer web app, public portal), information density (`high-density tool` vs `spacious consumer/editorial`), primary viewport (`desktop-first 1440x900`, `mobile-first 390x844`, or both), and theme polarity (`light`, `dark`, or `both`).
- `{{DESIGN_TOKENS}}`: in `bootstrap` (before the 3-mockup gate), write `To be locked after the owner selects from the 3 mockups in references/mockups/ (plus any fixed brand colors from references/brand/).` In `adopt`, list the CSS variables, Tailwind theme tokens, font families, and radius scale actually found in the codebase (with file paths).
- `{{DESIGN_COMPONENTS}}`: in `bootstrap`, write `To be locked at the 3-mockup gate and implemented in the first UI foundation ticket.` In `adopt`, list existing layout shells and shared UI primitives found in the codebase.
- `{{DESIGN_REFERENCES}}`: table rows `| REF-01 | <path or URL> | <brand / inspiration / mockup> | <what to take or status> |`. If the owner has provided none yet, write one row: `| REF-01 | references/inspiration/ | inspiration | To be populated by designer via agent-browser before the 3-mockup gate |`.

## Bootstrap: 3 questions for UI projects
Ask (combined with the PRD interview, max 4 numbered questions per turn):
1. **Visual benchmark / references:** "Do you have 1 or 2 real apps/websites, screenshots, or URLs whose look and feel you like, or should the `designer` agent search for inspiration and show you 3 visual mockups first (Recommended if you have none)?"
2. **Workspace density and mode:** "Is this UI used for intensive daily work (compact tables, high data density, quiet surfaces) or occasional consumer/public flows (larger type, generous whitespace), and should it start in Light or Dark mode?"
3. **Fixed brand assets:** "Do you already have a logo or fixed brand colors to drop into `references/brand/`, or is the palette open for the 3 mockups?"

Also check whether `agent-browser` is installed (`bash -c "command -v agent-browser >/dev/null 2>&1"`). If it is missing, mention in the setup report that installing it (`npm i -g agent-browser && agent-browser install`) is strongly recommended so `designer` and `tester` can research inspiration sites and verify UI mockups in a real headless browser.

## Adopt: surveying an existing UI
1. Check whether the codebase already has a frontend or UI layer. If not, set `{{DESIGN_STATUS}}` to `Not applicable (no UI)`.
2. If a UI exists, inspect the actual CSS/theme files (for example `tailwind.config.*`, `globals.css`, `tokens.css`, component library files) and any files in `references/`.
3. Ask the owner whether the current visual design is already locked (`Locked`: document the existing tokens and components in `DESIGN.md` so workers follow them) or needs a redesign / new direction (`Proposed (awaiting 3-mockup gate)`: the `designer` agent will generate 3 mockups before new UI tickets run).
