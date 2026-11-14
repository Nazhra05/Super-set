# Changelog

## 0.2.0 (2026-11-14)
- Token efficiency for the router: added lightweight `scoper` subagent (`flash_lite` default) so the router prepares ticket drafts without reading raw source files into its own context; added composite `tools/wt.sh check` and `tools/wt.sh land` subcommands; earlier `/compact` cadence after every completed ticket pair.
- Owner replies and Terms: concise 8-to-10-line summary format (Done, Next, Needs your decision) that always writes `<ID> (<short title>)` instead of bare IDs; expanded `## Terms` in `AGENTS.md` so standard software engineering terms stay in English when replying in another language.

## 0.1.0 (2026-11-13)
- First version for Google Antigravity (Gemini): native `plugin.json` manifest, `adopt` and `bootstrap` skills using `ask_question`, `.agents/agents/` (`worker`, `tester`, `reviewer`, `Explore`) mapped to Antigravity tools and Gemini model tiers (`pro`, `flash`, `flash_lite`), `.agents/skills/router/` entry skill, `.agents/hooks.json` with `tools/env-guard.js` `PreToolUse` `.env` protection, consolidated `AGENTS.md` project rules (English and Bahasa Indonesia in `templates/id/`), and PowerShell-safe `bash tools/*.sh` invocations.

