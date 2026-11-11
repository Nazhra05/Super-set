# Setup interview

Shared by the `adopt` and `bootstrap` skills. Ask with the AskUserQuestion tool, at most 4 questions per call. Never guess an answer: when the owner has not given it and it cannot be read from the project, ask. In `adopt`, propose answers found in the project as the first option ("(found in project)") so the owner only confirms.

Reply to the owner in the language they write in. Everything written into the project is in English.

Start by explaining the defaults in `<plugin root>/README.md`, section "Opinionated defaults (and how to change them)", in the owner's language and in plain words, then ask which ones to change. Record each change as a project decision (D-xx) in `DECISIONS.md` with the reason, and apply it to the files named in that table.

## Answers to collect, and the placeholder each one fills

| Placeholder | Question | Notes |
|---|---|---|
| `{{PROJECT_NAME}}` | Project name | Short name used in docs and agent prompts. |
| `{{PROJECT_ROOT}}`, `{{PROJECT_ROOT_FWD}}` | Project root | Absolute path; `_FWD` is the same path with forward slashes (for `settings.json`). Never assume; confirm the current directory with the owner. |
| `{{PROJECT_SUMMARY}}` | What the project is, for whom, and why | Two to four sentences. |
| `{{OWNER_ROLE}}` | Who the owner is | For example "single developer", "small team lead". |
| `{{OWNER_LANGUAGE}}` | Language for replies to the owner | Default: the language the owner writes in. Documents stay English. |
| `{{REPOS}}`, `{{REPO_TABLE}}` | Repos: alias, path from root, working branch, stack | Single repo: one line `app|.|main`. Multi-repo (docs root plus app repos): one line per app repo. `REPOS` lines go to `tools/workflow.conf` as `alias|path|branch`; `REPO_TABLE` rows go to `CLAUDE.md`. |
| `{{INSTALL_CMD}}` | Dependency install inside a fresh worktree | For example `npm ci --no-audit --no-fund`, `composer install`, `pip install -r requirements.txt`. Empty if none. If the commands differ per repo, ask how to handle it and record the answer as a pitfall; the template supports one command. |
| `{{COMMANDS}}` | Test, lint, type-check, build, dev commands per repo | Run each once before writing it down (rule 5); write only the ones that ran, with the date. |
| `{{DEFAULT_VERIFY}}` | Default `verify` block for tickets | Usually the fast test and type-check commands. |
| `{{TEST_LOCATIONS}}`, `{{TEST_RULES}}` | Where business-logic tests live; project test rules | For example import style inside tests, test files that must not come back. |
| `{{SOURCE_OF_TRUTH}}` | Files that define names (schema, types, routes) | Agents must verify names there. |
| `{{SHARED_RESOURCES}}` | Resources two tickets must not use at once | For example a local database, a dev-server port, an upload folder. "None" is a valid answer. |
| `{{IRREVERSIBLE_ACTIONS}}` | Project-specific actions that always need approval | For example deploy, production data, merge into the release branch. |
| `{{SESSION_REPORT_DIR}}` | Folder for router session reports | Default `docs/sessions` inside the project (committed). May be a folder outside the repo, such as a notes vault. |
| `{{ROUTER_MODEL}}`, `{{WORKER_MODEL}}`, `{{TESTER_MODEL}}`, `{{EXPLORE_MODEL}}` | Model per role | Offer the defaults below with the recommendation, then ask whether to change any. |
| `{{EXTRA_DOCS}}` | Other project documents to list in the document map | `adopt`: existing docs found. `bootstrap`: usually none at first. |
| `{{PITFALLS}}` | Proven pitfalls | Only facts proven by command output. Empty list is fine: write "None yet." |
| `{{SETUP_DATE}}` | Today's date | ISO format. |
| (no placeholder) | Where the owner works: terminal, desktop app, IDE extension, or several | Decides the surface check in `install-steps.md` step 5. All surfaces use the same files and the same flow. |

The remaining placeholders (`{{CURRENT_STATE}}`, `{{NEXT_STEP}}`, `{{WAITING_OWNER}}`, `{{EXECUTION_ORDER}}`, `{{TASKS}}`, `{{INBOX}}`, `{{PROJECT_DECISIONS}}`, `{{WAITING_DECISIONS}}`) are filled by the skill from what it found and agreed with the owner. When there is nothing, write "None yet." rather than inventing content.

## Model defaults and recommendation

Show this table, explain it in one or two sentences, then ask "Keep the defaults or change a role?".

| Role | Default | Why |
|---|---|---|
| router | strongest model available to the owner, effort high | Plans, writes briefs, judges security findings, merges. A weak router costs more in retries than it saves. |
| worker | `sonnet`, effort low | Works inside a strict Allow list with a detailed brief. Raise to `opus` for a ticket that failed twice. |
| tester | `sonnet`, effort medium | Red-green and mutation checks need care but follow a fixed procedure. |
| reviewer | `opus` for auth, session, authorization, security; `sonnet` for tests and ordinary logic; none for text-only | Matches W-05. The router passes `model: sonnet` for the lower tier. |
| Explore | `haiku`, effort low | Only locates `path:line`; never judges. |

Adjust the recommendation to what the owner says about their plan: on a plan with tight usage limits, a `sonnet` router with `opus` kept for security reviews is the cheaper option; say so as a trade-off, not as the default. When a model changes, edit the `model:` line in that agent file and the Roles table in `WORKFLOW.md`.
