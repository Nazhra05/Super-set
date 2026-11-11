# Install steps

Shared by the `adopt` and `bootstrap` skills, after the interview in `setup-interview.md`. `TEMPLATES` below means `.workflow-setup/templates/`, staged into the project by `scripts/stage.sh`.

## 1. Plan the file list before writing
List every file the setup will create or change in the project, marked `new` or `merge`. Show the list to the owner in plain language and continue after a yes. Nothing in the project is overwritten silently.

| Project path | Source |
|---|---|
| `CLAUDE.md`, `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md` | `TEMPLATES/<same name>`, or `TEMPLATES/id/<same name>` when the document language is Indonesian |
| `PRD.md` | `TEMPLATES/PRD.md` or `TEMPLATES/id/PRD.md`; not installed when `adopt` keeps an existing PRD (`reference/prd.md`) |
| `tickets/_TEMPLATE.md` | `TEMPLATES/tickets/_TEMPLATE.md` or `TEMPLATES/id/tickets/_TEMPLATE.md` |
| `tools/wt.sh`, `tools/guard.sh`, `tools/verify.sh`, `tools/statusline.js`, `tools/workflow.conf` | `TEMPLATES/tools/` |
| `.claude/agents/{router,worker,tester,reviewer,Explore}.md` | `TEMPLATES/.claude/agents/` |
| `.claude/skills/` (5 skills, `NOTICE`, `LICENSE-superpowers`) | `TEMPLATES/.claude/skills/`, copied unchanged |
| `.claude/settings.json` | `TEMPLATES/.claude/settings.json` |
| `.gitattributes` | `TEMPLATES/.gitattributes` |
| `.gitignore` | lines below |

If a file with the same path already exists, never replace it. Merge instead:
- Markdown docs: keep every existing rule and fact, place it in the matching section of the template, and show the owner what moved where. Conflicting rules are listed as questions, not resolved by you.
- `.claude/settings.json`: merge JSON keys. Add the three `deny` entries if missing. If a `statusLine` already exists, ask before replacing it.
- `.claude/agents/<name>.md` with one of the five names: show both and ask which one wins.
- `.claude/skills/<name>`: if the same skill exists in a different version, ask.
- `.gitattributes`, `.gitignore`: append missing lines only.

## 2. Copy and fill
1. Copy the files. Use `cp` for the skills folder so it stays byte-identical to the plugin copy.
2. Replace every `{{PLACEHOLDER}}` with the interview answers.
3. Check none is left: `grep -rn "{{" CLAUDE.md AGENTS.md WORKFLOW.md TODO.md HANDOFF.md DECISIONS.md PRD.md tickets/_TEMPLATE.md tools/ .claude/agents/ .claude/settings.json` must print nothing.
4. Ensure LF line endings and execute bits on scripts: `chmod +x tools/*.sh`, and `grep -c $'\r' tools/*.sh tools/workflow.conf` must print 0 for each file. On Windows the file system does not store the execute bit, so when the scripts are committed also run `git update-index --chmod=+x tools/*.sh`; otherwise macOS and Linux clones get non-executable scripts.
5. Create `{{SESSION_REPORT_DIR}}` if it does not exist.

## 3. `.gitignore` lines (in the repo that contains the project root)
```
_wt/
.workflow-setup/
.claude/settings.local.json
.claude/usage.json
.env*
```
For `.env*`, check first that no tracked file matches (`git ls-files | grep -E '(^|/)\.env'`); if one does, report it and ask, because ignoring a tracked secret file hides the real problem.

## 4. Smoke test (proves the tools work here; reversible)
Run with Bash from the project root, with a throwaway ticket. Use a repo alias from `tools/workflow.conf`; `<base>` is that repo's working branch.

1. Write `tickets/SMOKE.md` from the template with `## Allow` = one harmless path, for example `` - `SMOKE.txt` ``, and a `verify` block containing `test -f SMOKE.txt`.
2. `tools/wt.sh add <alias> SMOKE` must print `worktree: ...`.
3. Create `SMOKE.txt` in the worktree; `tools/guard.sh _wt/SMOKE-<alias> <base> tickets/SMOKE.md` must print `guard: OK`.
4. Create `OUTSIDE.txt` in the worktree; guard must print `OUT-OF-SCOPE: OUTSIDE.txt` and exit 1. Delete `OUTSIDE.txt`.
5. `tools/verify.sh _wt/SMOKE-<alias> tickets/SMOKE.md` must print `exit=0`.
6. `tools/wt.sh rm <alias> SMOKE` must refuse (uncommitted `SMOKE.txt`). Then `WT_DISCARD=1 tools/wt.sh rm <alias> SMOKE` must print `Deleted branch t/SMOKE` (the branch has no commits, so `branch -d` succeeds).
7. Delete `tickets/SMOKE.md`. Confirm `git worktree list` no longer shows it and `_wt/` is empty.

Quote the real output of each step in the report. If a step fails, use `systematic-debugging`; do not edit the tools to make the smoke test pass without telling the owner why.

## 5. Surface check
- **Terminal:** ask the owner to restart Claude Code in the project root. After one reply, `.claude/usage.json` must exist with a fresh `savedAt`. If the user-level settings already define a status line, the project one wins; say so.
- **Desktop app:** the status line does not run there, so skip the `usage.json` check and say so. If the owner wants router mode now, write the keys from `WORKFLOW.md` ("Starting a router session") into `.claude/settings.local.json` (merge, never replace the file), ask them to open a new session in the project, and confirm the router answers by naming `WORKFLOW.md` as its first read. Until that has been seen, report router mode as not verified on this machine.

## 6. Report and stop
Delete `.workflow-setup/` first and confirm with `ls -A` that it is gone.
In plain language in the owner's language: what was created or merged, what was found (for `adopt`), the smoke test result, what was not verified, and the decisions waiting for the owner. Do not commit unless the owner asks. Name how to start the router on the owner's surface: `claude --agent router --model <router model> --effort high` in a terminal, or router mode in `.claude/settings.local.json` for the desktop app.
