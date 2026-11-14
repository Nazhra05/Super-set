---
name: ui-design
description: Studio-grade UI design system, 3-mockup exploration gate, and real-browser verification skill. Adapted from Leonxlnx/taste-skill and powered by vercel-labs/agent-browser. Use when exploring visual directions, building the 3 foundation mockups in references/mockups/, locking DESIGN.md, or implementing and verifying UI tickets.
---

# UI Design: 3-Mockup Gate, Numerical Craft, and Browser Verification

This skill governs how `designer` explores and locks visual direction in `DESIGN.md` and how `worker` implements UI tickets. Design choices are made through **visual artifacts, reference images, and hard numerical constraints**, never vague prose.

Adapted from design principles in [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT) and browser automation workflows from [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) (Apache-2.0).

## 1. Mindset: Unhurried Studio Craftsmanship
Work with unhurried studio craftsmanship. Take the full space needed inside your turn to write complete, production-grade HTML and CSS with **99.99% proportional and structural fidelity** to the reference and token scale. Never abbreviate markup with `<!-- more rows -->`, never use `Lorem ipsum` or `"Item 1"`, and never rush visual details such as focus rings, active states, border contrast, or tabular numeral alignment (`font-variant-numeric: tabular-nums`).

## 2. Hard Numerical Rules (The 99.99% Bar)
Every mockup in `references/mockups/` and every UI component in production must satisfy these exact numbers:

1. **Color distribution (92-95 / 4-6 / <=3):**
   - **92% to 95% neutral surfaces:** `--bg` (canvas), `--surface` (cards/panels), `--surface-subtle` (table headers, hover rows). Never pure `#000000` ink on pure `#ffffff` without warmth or tint.
   - **4% to 6% ink and structure:** primary ink `--ink` (`>= 7:1` contrast), secondary `--muted` (`>= 4.5:1` contrast), and crisp hairlines (`1px solid` at `10%` to `14%` of `--ink` opacity).
   - **At most 3% accent (`--accent`):** used only on the primary action button, active navigation indicator, and focus ring.
   - **No generic AI violet/lavender:** never pick an accent or gradient in OKLCH hue `270` to `330` unless the owner's brand logo in `references/brand/` requires it.
2. **Spacing and rhythm scale:**
   - Use only `4, 8, 12, 16, 24, 32, 48, 64px` (`--s-1` to `--s-8`) for all padding, gaps, and margins.
   - Equal left and right container edges at every viewport width (`1440px` desktop and `390px` mobile).
   - Card/panel internal padding: `20px` to `24px` on desktop (`16px` on mobile); gap between cards: `16px` to `24px`.
3. **Typography and sizing:**
   - Body, table cells, and form inputs: `14px` to `16px` (`line-height: 1.5`), never smaller than `14px`.
   - Labels, badges, and table column headers: `12px` to `13px`, `font-weight: 500`, sentence case (no wide-tracked uppercase walls).
   - Running prose measure: `<= 65ch`.
   - Numeric columns, prices, IDs, and timestamps: always set `font-variant-numeric: tabular-nums`.
   - Interactive controls (buttons, inputs, nav rows): `40px` to `44px` height on desktop, `44px` minimum tap target on mobile (`390px`).

## 3. Target Floor and Ceiling (Knowing Exactly When to Stop)

### Floor (Minimum viable anatomy so a design never feels empty)
Every mockup option (`option-1.html`, `option-2.html`, `option-3.html`) must render the **primary workspace screen** from `PRD.md` with:
- Complete navigation shell (sidebar, top bar, or split rail matching the option's archetype).
- Workspace header with screen title, context metadata, and the primary action button (verb + object, for example `Create invoice`, `Record payment`).
- Main data or interaction view populated with **5 to 8 realistic domain records** taken from `PRD.md` terminology (real names, realistic statuses, tabular numbers).
- At least 1 visible interactive state (1 selected/active row, drawer, filter state, or detail panel) and responsive CSS that stacks cleanly at `390px`.

### Ceiling (Hard cap so a design never feels cluttered or over-designed)
- **At most 4 component groups** per screen (for example: Navigation + Header Bar + Primary Data Table/Grid + 1 Summary/Detail Panel).
- **At most 2 levels of box nesting** (a panel inside the main canvas, or a card inside a grid; never a bordered card inside a bordered card inside a bordered panel).
- **One button pair** across the entire screen (`.btn-primary` and `.btn-secondary`), one border-radius family, one shadow or hairline rule.
- **Zero unrequested chrome:** do not invent notification bells, chat bubbles, fake sparkline charts, theme-toggle widgets, or decorative gradients not grounded in `PRD.md`.

## 4. Browser Research and Verification with `agent-browser`

When `agent-browser` is installed (`command -v agent-browser`), load its core guide once per session if needed (`agent-browser skills get core`) and use it for both inspiration discovery and visual verification:

### A. Inspiration discovery (when `references/inspiration/` is empty or has URLs)
1. If the owner provided URLs in `DESIGN.md` or `references/inspiration/`, open each URL with `agent-browser open <url>`, inspect its structure (`agent-browser snapshot -i`), extract computed typography and colors (`agent-browser eval "JSON.stringify({font: getComputedStyle(document.body).fontFamily, bg: getComputedStyle(document.body).backgroundColor})"`), and save a screenshot (`agent-browser screenshot references/inspiration/ref-1.png`).
2. If the owner gave no references ("lazy" mode), pick 1 or 2 reachable inspiration sources matching the `PRD.md` product category:
   - SaaS, developer tools, high-density workspaces: `https://interfaces.dev`, `https://component.gallery`, `https://dark.design`
   - Landing pages, editorial, service, consumer web: `https://minimal.gallery`, `https://godly.website`, `https://saaslandingpage.com`, `https://lapa.ninja`
   Capture 1 or 2 reference screenshots into `references/inspiration/` and view them directly with the `Read` tool so your layout proportions are anchored in real visual frames.
3. Always close the browser when done (`agent-browser close`). If `agent-browser` is not installed or a site is unreachable, do not block: fall back immediately to the curated archetype matrix in Section 5 and state it in your report.

### B. Real-browser check of the 3 mockups (or built UI)
After writing `references/mockups/option-1.html`, `option-2.html`, and `option-3.html`, serve or open each file in `agent-browser` and check both desktop (`1440x900`) and mobile (`390x844`):
```bash
agent-browser open <file-or-local-url>
agent-browser set viewport 1440 900
agent-browser eval "({scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth})"
agent-browser screenshot references/mockups/option-1-desktop.png
agent-browser set viewport 390 844
agent-browser eval "({scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth})"
agent-browser screenshot references/mockups/option-1-mobile.png
```
Read the generated screenshots with the `Read` tool. If `scrollWidth > clientWidth` (horizontal overflow) or elements collide, fix the CSS once and re-shoot before reporting.

## 5. Curated Archetype Matrix (3 Contrasting Directions)
When building the 3 mockups (`option-1.html`, `option-2.html`, `option-3.html`), never make 3 minor color swaps of the same layout. Give each option a distinct **structural layout + font pairing + palette system** (if the owner provided fixed brand colors in `references/brand/`, lock that brand accent across all 3 options and vary the surface polarity, typography, and navigation layout):

| Direction | Best for | Layout & density | Google Fonts pairing (Headings / Body / Mono) | Palette tokens (`--bg` / `--surface` / `--ink` / `--muted` / `--accent`) | Radius |
|---|---|---|---|---|---|
| **Option A: Crisp High-Density Workspace** | Dashboards, POS, fintech, admin, internal tools, analytics | Compact left sidebar (`220px`) + full-height data table + right inspector drawer; `1px solid` hairlines, zero drop shadows | `Plus Jakarta Sans` (600) / `Inter` (400, 500) / `JetBrains Mono` | `#F8F9FA` / `#FFFFFF` / `#111827` / `#4B5563` / `#0F766E` (deep teal) or `#1D4ED8` (cobalt) | Sharp (`4px` controls, `6px` panels) |
| **Option B: Warm Editorial & Spacious Surface** | Consumer apps, booking, education, healthcare, publishing, CRM | Top navigation bar + centered `1200px` container + 2-column asymmetric split (summary cards left, main workflow right) | `Instrument Serif` or `Fraunces` (600) / `DM Sans` (400, 500) / `IBM Plex Mono` | `#F6F4F0` (warm stone) / `#FFFFFF` / `#1C1917` / `#57534E` / `#C2410C` (terracotta) or `#15803D` (forest) | Soft (`8px` controls, `12px` cards) |
| **Option C: Technical Carbon / High-Contrast Split** | Developer tools, AI ops, monitoring, media tools, modern SaaS | Ultra-slim icon/label rail + split command header + bento summary strip above dense log/record list | `Space Grotesk` (600) / `Geist` or `IBM Plex Sans` (400, 500) / `JetBrains Mono` | `#0B0F17` (carbon) or `#F1F5F9` (cool slate) / `#111827` or `#FFFFFF` / `#F8FAFC` or `#0F172A` / `#94A3B8` or `#475569` / `#0284C7` (sky) or `#EA580C` (signal orange) | Crisp (`6px` controls, `8px` panels) |

## 6. Locking the Owner's Choice into Code
Once the owner selects an option (or a hybrid such as "Layout from Option 1 + Palette from Option 2"):
1. Update `DESIGN.md` with Status `Locked`, the exact `:root` CSS variables, font links, spacing/radius tokens, and base component rules.
2. The first UI ticket in `TODO.md` must create the shared token stylesheet (for example `src/styles/tokens.css` or Tailwind theme config) and base layout primitives so every subsequent `worker` ticket imports them directly instead of writing ad-hoc styles.
