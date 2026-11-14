# Changelog

## 0.2.0 (2026-11-14)
- Token efficiency for the router: added lightweight `scoper` role prompt (`codex-mini-latest` default) so the router prepares ticket drafts without reading raw source files into its own context; added composite `tools/wt.sh check` and `tools/wt.sh land` subcommands; earlier `/compact` cadence after every completed ticket pair.
- Owner replies and Terms: concise 8-to-10-line summary format (Done, Next, Needs your decision) that always writes `<ID> (<short title>)` instead of bare IDs; expanded `## Terms` in `AGENTS.md` so standard software engineering terms stay in English when replying in another language.

## 0.1.0 (2026-11-14)
- First version for OpenAI Codex: `plugin.json` manifest, `codex-app-adopt` and `codex-app-bootstrap` setup skills, `.codex/agents/` role prompts (`worker.md`, `tester.md`, `reviewer.md`, `Explore.md`) dispatched via `codex exec` with OpenAI Codex models (`gpt-5-codex`, `codex-mini-latest`), `.codex/skills/router/` entry skill plus five discipline skills, consolidated `AGENTS.md` project rules (English and Bahasa Indonesia in `templates/id/`), and PowerShell-safe `bash tools/*.sh` invocations.

