# Changelog

## 0.2.0 (2026-11-14)
- Token efficiency for the producer and visual-reviewer: added lightweight `frame-prep` subagent (`haiku` default) and `tools/verify.sh --with-scope` to run scope/verify checks, extract review frames and downscaled contact sheets into `.review/`, and measure pixel hex/audio before `visual-reviewer` runs; the producer opens frames only at approval gates and asks for `/compact` at every gate boundary.
- Owner replies and Terms: concise 8-to-10-line summary format (Done, Next / Gate, Needs your decision) that always writes `<ID> (<short title>)` instead of bare IDs; expanded `## Terms` in `CLAUDE.md` so standard motion graphics, video, graphic design, and software terms stay in English when replying in another language.

## 0.1.2 (2026-11-11)
- README: what it looks like (example output from a test setup), when not to use it, cost, and status. No change in behaviour.

## 0.1.1 (2026-11-11)
- README and plugin description rewritten for new users: who it is for, the problems it solves, and how a project runs. No change in behaviour.

## 0.1.0 (2026-11-11)
- First version: adopt and bootstrap skills; brief (`PRD.md`), `STYLE.md`, and `REFERENCES.md`; approval gates; producer, asset-builder, visual-reviewer, researcher, and Explore agents; knowledge skills `content-fundamentals`, `motion-principles`, `design-basics`, `character-design`; `tools/scope.sh`, `tools/verify.sh`, `tools/statusline.js`; English and Indonesian docs.
