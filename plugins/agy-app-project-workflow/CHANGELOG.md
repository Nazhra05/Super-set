# Changelog

## 0.3.0 (2026-11-14)
- UI design flow and 3-mockup gate (W-10): added `DESIGN.md` (`templates/DESIGN.md` and `templates/id/DESIGN.md`), automatic `references/{brand,inspiration,mockups}/` directory setup, `reference/design.md`, the `designer` subagent, and the `ui-design` skill.
- Adapted numerical art-direction and layout discipline from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (99.99% proportional fidelity bar, 92% to 95% neutral / <=3% accent color ratio, strict spacing scale, floor and ceiling screen anatomy, unhurried studio craftsmanship mindset) and integrated browser discovery and verification workflows for [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser).
- Compact visual briefing: the router briefs `designer` in 6 to 8 lines pointing to `PRD.md` and `references/` rather than writing long prose descriptions; `designer` inspects reference images directly and builds 3 contrasting HTML mockups (`references/mockups/option-1..3.html`) verified at `1440x900` and `390x844` before locking `DESIGN.md`.

## 0.2.0 (2026-11-14)
- Token efficiency for the router: added lightweight `scoper` subagent (`flash_lite` default) so the router prepares ticket drafts without reading raw source files into its own context; added composite `tools/wt.sh check` and `tools/wt.sh land` subcommands; earlier `/compact` cadence after every completed ticket pair.
- Owner replies and Terms: concise 8-to-10-line summary format (Done, Next, Needs your decision) that always writes `<ID> (<short title>)` instead of bare IDs; expanded `## Terms` in `AGENTS.md` so standard software engineering terms stay in English when replying in another language.

## 0.1.0 (2026-11-13)
- First version for Google Antigravity (Gemini): native `plugin.json` manifest, `adopt` and `bootstrap` skills using `ask_question`, `.agents/agents/` (`worker`, `tester`, `reviewer`, `Explore`) mapped to Antigravity tools and Gemini model tiers (`pro`, `flash`, `flash_lite`), `.agents/skills/router/` entry skill, `.agents/hooks.json` with `tools/env-guard.js` `PreToolUse` `.env` protection, consolidated `AGENTS.md` project rules (English and Bahasa Indonesia in `templates/id/`), and PowerShell-safe `bash tools/*.sh` invocations.

