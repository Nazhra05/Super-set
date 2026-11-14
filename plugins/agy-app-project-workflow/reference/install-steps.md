# Install steps

Shared by the `adopt` and `bootstrap` skills, after the interview in `setup-interview.md`. `TEMPLATES` below means `.workflow-setup/templates/`, staged into the project by `scripts/stage.sh`.

## 1. Plan the file list before writing
List every file the setup will create or change in the project, marked `new` or `merge`. Show the list to the owner in plain language and continue after a yes. Nothing in the project is overwritten silently.

| Project path | Source |
|---|---|
| `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md` | `TEMPLATES/<same name>`, or `TEMPLATES/id/<same name>` when the document language is Indonesian |
| `PRD.md` | `TEMPLATES/PRD.md` or `TEMPLATES/id/PRD.md`; not installed when `adopt` keeps an existing PRD (`reference/prd.md`) |
| `tickets/_TEMPLATE.md` | `TEMPLATES/tickets/_TEMPLATE.md` or `TEMPLATES/id/tickets/_TEMPLATE.md` |
| `tools/wt.sh`, `tools/guard.sh`, `tools/verify.sh`, `tools/env-guard.js`, `tools/workflow.conf` | `TEMPLATES/tools/` |
| `.agents/agents/{scoper,worker,tester,reviewer,Explore}.md` | `TEMPLATES/.agents/agents/` |
| `.agents/skills/router/SKILL.md` | `TEMPLATES/.agents/skills/router/SKILL.md` |
| `.agents/skills/` (5 discipline skills, `NOTICE`, `LICENSE-superpowers`) | `TEMPLATES/.agents/skills/`, copied unchanged |
| `.agents/hooks.json` | `TEMPLATES/.agents/hooks.json` |
| `.gitattributes` | `TEMPLATES/.gitattributes` |
| `.gitignore` | lines below |

If a file with the same path already exists, never replace it. Merge instead:
- Markdown docs: keep every existing rule and fact, place it in the matching section of the template, and show the owner what moved where. If the project had a `CLAUDE.md` or `GEMINI.md`, merge its rules into `AGENTS.md` (and keep the original file or point it to `AGENTS.md` as agreed with the owner). Conflicting rules are listed as questions, not resolved by you.
- `.agents/hooks.json`: merge JSON keys. Keep existing hooks and add `env-guard` if missing.
- `.agents/agents/<name>.md` with one of the four names: show both and ask which one wins.
- `.agents/skills/<name>`: if the same skill exists in a different version, ask.
- `.gitattributes`, `.gitignore`: append missing lines only.

## 2. Copy and fill
1. Copy the files. Use `cp` for the five discipline skills so they stay byte-identical to the plugin copy.
2. Replace every `{{PLACEHOLDER}}` with the interview answers.
3. Check none is left: `bash -c 'grep -rn "{{" AGENTS.md WORKFLOW.md TODO.md HANDOFF.md DECISIONS.md PRD.md tickets/_TEMPLATE.md tools/ .agents/agents/ .agents/skills/router/ .agents/hooks.json'` must print nothing.
4. Ensure LF line endings and execute bits on scripts: `bash -c "chmod +x tools/*.sh && grep -c $'\r' tools/*.sh tools/workflow.conf"` must print 0 for each file. On Windows the file system does not store the execute bit, so when the scripts are committed also run `git update-index --chmod=+x tools/*.sh`; otherwise macOS and Linux clones get non-executable scripts.
5. Create `{{SESSION_REPORT_DIR}}` if it does not exist.

## 3. `.gitignore` lines (in the repo that contains the project root)
```
_wt/
.workflow-setup/
.env*
```
For `.env*`, check first that no tracked file matches (`git ls-files | grep -E '(^|/)\.env'`); if one does, report it and ask, because ignoring a tracked secret file hides the real problem.

## 4. Smoke test (proves the tools work here; reversible)
Run with `bash` from the project root, with a throwaway ticket. Use a repo alias from `tools/workflow.conf`; `<base>` is that repo's working branch.

1. Write `tickets/SMOKE.md` from the template with `## Allow` = one harmless path, for example `` - `SMOKE.txt` ``, and a `verify` block containing `test -f SMOKE.txt`.
2. `bash tools/wt.sh add <alias> SMOKE` must print `worktree: ...`.
3. Create `SMOKE.txt` in the worktree; `bash tools/guard.sh _wt/SMOKE-<alias> <base> tickets/SMOKE.md` must print `guard: OK`.
4. Create `OUTSIDE.txt` in the worktree; `bash tools/guard.sh _wt/SMOKE-<alias> <base> tickets/SMOKE.md` must print `OUT-OF-SCOPE: OUTSIDE.txt` and exit 1. Delete `OUTSIDE.txt`.
5. `bash tools/verify.sh _wt/SMOKE-<alias> tickets/SMOKE.md` must print `exit=0`.
6. `bash tools/wt.sh rm <alias> SMOKE` must refuse (uncommitted `SMOKE.txt`). Then `bash -c "WT_DISCARD=1 ./tools/wt.sh rm <alias> SMOKE"` must print `Deleted branch t/SMOKE` (the branch has no commits, so `branch -d` succeeds).
7. Delete `tickets/SMOKE.md`. Confirm `git worktree list` no longer shows it and `_wt/` is empty.

Quote the real output of each step in the report. If a step fails, use `systematic-debugging`; do not edit the tools to make the smoke test pass without telling the owner why.

## 5. Report and stop
Delete `.workflow-setup/` first and confirm that it is gone.
In plain language in the owner's language: what was created or merged, what was found (for `adopt`), the smoke test result, what was not verified, and the decisions waiting for the owner. Do not commit unless the owner asks. Name how to start the router on any Antigravity surface (CLI, IDE, or Antigravity 2.0 desktop app): invoke the `router` skill (`/router` or ask to "start the router session").

