# Install steps

Shared by the `adopt` and `bootstrap` skills, after the interview and the brief. `TEMPLATES` below means `.workflow-setup/templates/`, staged into the project by `scripts/stage.sh`.

## 1. Plan the file list before writing
List every file the setup will create or change in the project, marked `new` or `merge`. Show the list to the owner in plain language and continue after a yes. Nothing in the project is overwritten silently.

| Project path | Source |
|---|---|
| `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `PRD.md`, `STYLE.md`, `REFERENCES.md` | `TEMPLATES/<same name>`, or `TEMPLATES/id/<same name>` when the document language is Indonesian. `PRD.md` is not installed when `adopt` keeps an existing brief. |
| `tickets/_TEMPLATE.md` | `TEMPLATES/tickets/_TEMPLATE.md` or `TEMPLATES/id/tickets/_TEMPLATE.md` |
| `tools/scope.sh`, `tools/verify.sh`, `tools/env-guard.js` | `TEMPLATES/tools/` |
| `.agents/agents/{asset-builder,visual-reviewer,researcher,Explore}.md` | `TEMPLATES/.agents/agents/` |
| `.agents/skills/producer/SKILL.md` | `TEMPLATES/.agents/skills/producer/SKILL.md` |
| `.agents/skills/` (6 skills, `NOTICE`, `LICENSE-superpowers`) | `TEMPLATES/.agents/skills/`, copied unchanged |
| `.agents/hooks.json` | `TEMPLATES/.agents/hooks.json` |
| `.gitattributes` | `TEMPLATES/.gitattributes` |
| `.gitignore` | lines below |
| `docs/research/`, `{{SESSION_REPORT_DIR}}` | new folders |

If a file with the same path already exists, never replace it. Merge instead:
- Markdown docs: keep every existing rule and fact, place it in the matching section of the template, and show the owner what moved where. If the project had a `CLAUDE.md` or `GEMINI.md`, merge its rules into `AGENTS.md` (and keep the original file or point it to `AGENTS.md` as agreed with the owner). Conflicting rules are listed as questions, not resolved by you.
- `.agents/hooks.json`: merge JSON keys. Keep existing hooks and add `env-guard` if missing.
- `.agents/agents/<name>.md` with one of the four names: show both and ask which one wins.
- `.agents/skills/<name>`: if the same skill exists in a different version, ask.
- `.gitattributes`, `.gitignore`: append missing lines only.

## 2. Copy and fill
1. Copy the files. Use `cp` for the six bundled skills so they stay byte-identical to the plugin copy.
2. Replace every `{{PLACEHOLDER}}` with the answers.
3. Check none is left: `bash -c 'grep -rn "{{" AGENTS.md WORKFLOW.md TODO.md HANDOFF.md DECISIONS.md PRD.md STYLE.md REFERENCES.md tickets/_TEMPLATE.md tools/ .agents/agents/ .agents/skills/producer/ .agents/hooks.json'` must print nothing.
4. Ensure LF line endings and execute bits: `bash -c "chmod +x tools/*.sh && grep -c $'\r' tools/*.sh"` must print 0 for each file. On Windows also run `git update-index --chmod=+x tools/*.sh` when the scripts are committed.
5. Create `docs/research/` and `{{SESSION_REPORT_DIR}}` if they do not exist.

## 3. `.gitignore` lines (only in a git repo)
```
.workflow-setup/
.review/
.research/
.env*
```
Plus the generated folders the owner chose to ignore (for example renders, caches). Never ignore originals without asking. For `.env*`, check first that no tracked file matches (`git ls-files | grep -E '(^|/)\.env'`); if one does, report it and ask.

## 4. Smoke test (proves the tools work here; reversible)
1. Write `tickets/SMOKE.md` from the template with `## Allow` = `` - `SMOKE.txt` `` and a `verify` block containing `test -f SMOKE.txt`.
2. Create `SMOKE.txt` in the project root. `bash tools/verify.sh tickets/SMOKE.md` must print `exit=0`.
3. In a git repo: scope compares against the last commit, so the setup files must be committed first; ask the owner (if they decline, skip this step and say so). Then `bash tools/scope.sh tickets/SMOKE.md` must print `scope: OK`. Create `OUTSIDE.txt`; `bash tools/scope.sh tickets/SMOKE.md` must print `OUT-OF-SCOPE: OUTSIDE.txt` and exit 1. Not a git repo: scope prints `scope: not a git repo, check skipped`; say so.
4. Delete `SMOKE.txt`, `OUTSIDE.txt`, and `tickets/SMOKE.md`; confirm with `ls`.
5. If `{{FRAME_COMMAND}}` is set and a render or preview exists: grab one frame, open it with `read_file`, and describe it with "seen" and "inferred" as `AGENTS.md` rule 5 asks.

Quote the real output of each step in the report. If a step fails, use `systematic-debugging`; do not edit the tools to make it pass without telling the owner why.

## 5. Report and stop
Delete `.workflow-setup/` first and confirm that it is gone.
In plain language in the owner's language: what was created or merged, what was found, the smoke test result, what was not verified, the decisions waiting for the owner, the recommended tool skills (`{{TOOL_SKILLS}}`, the owner installs them), and how to start the producer on any Antigravity surface (CLI, IDE, or Antigravity 2.0 desktop app): invoke the `producer` skill (`/producer` or ask to "start the producer session"). Do not commit unless the owner asks.

