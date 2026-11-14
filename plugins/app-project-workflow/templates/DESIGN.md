# DESIGN.md: UI and design system for {{PROJECT_NAME}}

Last updated: {{SETUP_DATE}}. Status: **{{DESIGN_STATUS}}**.
The router and designer update this file at the 3-mockup design gate; once status is `Locked`, workers must use the locked tokens and components below and never invent new hex colors, font families, or card styles per ticket.

## 1. Product archetype and workspace mode
{{DESIGN_ARCHETYPE}}

## 2. Numerical quality bar (99.99% proportional fidelity)
Every mockup and UI ticket is judged against hard numbers, not vague adjectives:
- **Color ratio:** 92% to 95% neutral surfaces (`--bg`, `--surface`, `--surface-subtle`), 4% to 6% ink and hairlines (`1px solid` at 10% to 14% ink opacity), and at most 3% accent (`--accent`, used only on the primary action and active state indicator). Never use default AI violet/lavender (OKLCH hue 270 to 330) unless the owner's brand logo requires it.
- **Spacing scale:** only `4, 8, 12, 16, 24, 32, 48, 64px` (`--s-1` to `--s-8`). Equal left and right container edges at every viewport.
- **Typography and contrast:** body and data text `14px` to `16px` (`line-height: 1.5`, contrast `>= 7:1`), muted labels and metadata `12px` to `13px` (`font-weight: 500`, contrast `>= 4.5:1`), reading width `<= 65ch`, interactive controls `40px` to `44px` tall.
- **Floor and ceiling target:** every screen shows realistic domain records from `PRD.md` (5 to 8 rows or items, never `Lorem ipsum`), at most 4 distinct component groups per screen, at most 2 levels of box nesting, and 0 unrequested decorative widgets.

## 3. Locked design tokens
{{DESIGN_TOKENS}}

## 4. Locked layout shell and base components
{{DESIGN_COMPONENTS}}

## 5. Reference and mockup inventory (`references/`)
Files live in `references/brand/` (logos, brand assets), `references/inspiration/` (user references or screenshots captured by `designer` via `agent-browser`), and `references/mockups/` (`option-1.html`, `option-2.html`, `option-3.html` and their browser screenshots).

| ID | Path or URL | Kind | What to take / status |
|---|---|---|---|
{{DESIGN_REFERENCES}}
