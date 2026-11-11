# Changelog

## 0.3.0 (2026-11-11)
- New core doc `PRD.md` (what and why): requirements with IDs, status, and evidence. One template, two ways to fill it, in `reference/prd.md`: `bootstrap` writes what will be built from the interview; `adopt` keeps an existing PRD or drafts one from what is built, and the owner confirms each requirement.
- Document language chosen at setup: English or Bahasa Indonesia (`templates/id/`). Agent prompts, skills, and tools stay English; code, identifiers, comments, and commits always English. New "Terms" section in `CLAUDE.md`: workflow terms and the project's own terms stay in one form in replies, reports, and documents.
- Setup asks which router model to use (`opus` recommended) instead of assuming it.
- Fix: `guard.sh` missed deleted tests in a `tests/`, `test/`, or `e2e/` folder at the repo root (for example Laravel `tests/Feature/`), because `TEST_PATH_RE` required a `/` before the folder name. Now `(^|/)(tests?|e2e)/`.
- YAGNI (rule 3, W-02) now points to the requirements in `PRD.md`. Tickets name the requirement they serve. The router updates only Status and Evidence in `PRD.md`; requirement changes need the owner.

## 0.2.1 (2026-11-11)
- Fix: the setup skills could not read the templates, because the installed plugin lives outside the project folder. `scripts/stage.sh` (pre-approved in the skills' `allowed-tools`) now copies the setup material into `.workflow-setup/` inside the project; the setup deletes it at the end.
- Router reads the surface with `printenv WORKFLOW_SURFACE` (a `$VAR` in a command is blocked by permission checks).

## 0.2.0 (2026-11-11)
- MIT license; author and repository metadata in the manifests; marketplace `super-set`.
- Desktop app support: router mode through `.claude/settings.local.json`, and a usage rule for surfaces without a status line.
- Skills made self-contained: references to skills outside this workflow replaced with the ticket flow; attribution in `templates/.claude/skills/NOTICE`.
- Guard patterns limited to proven ones and written in portable POSIX regex (macOS, Linux, Windows Git Bash).
- README explains the opinionated defaults and where to change them.

## 0.1.0 (2026-11-11)
- First version: adopt and bootstrap skills, templates, agents, and tools.
