# Changelog

## 0.2.0 (2026-11-14)
- Token efficiency for the producer and visual-reviewer: added lightweight `frame-prep` subagent (`flash_lite` default) and `tools/verify.sh --with-scope` to run scope/verify checks, extract review frames and downscaled contact sheets into `.review/`, and measure pixel hex/audio before `visual-reviewer` runs; the producer opens frames only at approval gates and asks for `/compact` at every gate boundary.
- Owner replies and Terms: concise 8-to-10-line summary format (Done, Next / Gate, Needs your decision) that always writes `<ID> (<short title>)` instead of bare IDs; expanded `## Terms` in `AGENTS.md` so standard motion graphics, video, graphic design, and software terms stay in English when replying in another language.

## 0.1.0 (2026-11-13)
- First version for Google Antigravity (Gemini): native `plugin.json` manifest, `adopt` and `bootstrap` skills using `ask_question`, `.agents/agents/` (`asset-builder`, `visual-reviewer`, `researcher`, `Explore`) mapped to Antigravity tools and Gemini model tiers (`pro`, `flash`, `flash_lite`), `.agents/skills/producer/` entry skill, `.agents/hooks.json` with `tools/env-guard.js` `PreToolUse` `.env` protection, consolidated `AGENTS.md` project rules (English and Bahasa Indonesia in `templates/id/`), and PowerShell-safe `bash tools/*.sh` invocations.

