# Changelog

## 0.2.0 (2026-11-14)
- Token efficiency for the producer and visual-reviewer: added lightweight `frame-prep` role prompt (`codex-mini-latest` default) and `tools/verify.sh --with-scope` to run scope/verify checks, extract review frames and downscaled contact sheets into `.review/`, and measure pixel hex/audio before `visual-reviewer` runs; the producer opens frames only at approval gates and asks for `/compact` at every gate boundary.
- Owner replies and Terms: concise 8-to-10-line summary format (Done, Next / Gate, Needs your decision) that always writes `<ID> (<short title>)` instead of bare IDs; expanded `## Terms` in `AGENTS.md` so standard motion graphics, video, graphic design, and software terms stay in English when replying in another language.

## 0.1.0 (2026-11-14)
- First version for OpenAI Codex: `plugin.json` manifest, `codex-content-adopt` and `codex-content-bootstrap` setup skills, `.codex/agents/` role prompts (`asset-builder.md`, `visual-reviewer.md`, `researcher.md`, `Explore.md`) dispatched via `codex exec` with OpenAI Codex models (`gpt-5-codex`, `codex-mini-latest`), `.codex/skills/producer/` entry skill plus four craft skills and two discipline skills, consolidated `AGENTS.md` project rules (English and Bahasa Indonesia in `templates/id/`), and PowerShell-safe `bash tools/*.sh` invocations.

