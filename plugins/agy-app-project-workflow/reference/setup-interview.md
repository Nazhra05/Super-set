# Setup interview

Shared by the `adopt` and `bootstrap` skills. Ask with the `ask_question` tool, at most 4 questions per call. Never guess an answer: when the owner has not given it and it cannot be read from the project, ask. In `adopt`, propose answers found in the project as the first option, prefixed with `(Recommended)`, so the owner only confirms.

Reply to the owner in the language they write in. Documents are written in the document language chosen below; code, identifiers, comments, and commits are always English.

Start by explaining the defaults in `.workflow-setup/README.md`, section "Opinionated defaults (and how to change them)", in the owner's language and in plain words, then ask which ones to change. Record each change as a project decision (D-xx) in `DECISIONS.md` with the reason, and apply it to the files named in that table.

## Answers to collect, and the placeholder each one fills

| Placeholder | Question | Notes |
|---|---|---|
| `{{PROJECT_NAME}}` | Project name | Short name used in docs and agent prompts. |
| `{{PROJECT_ROOT}}`, `{{PROJECT_ROOT_FWD}}` | Project root | Absolute path; `_FWD` is the same path with forward slashes. Never assume; confirm the current directory with the owner. |
| `{{PROJECT_SUMMARY}}` | What the project is, for whom, and why | Two to four sentences. |
| `{{OWNER_ROLE}}` | Who the owner is | For example "single developer", "small team lead". |
| `{{OWNER_LANGUAGE}}` | Language for replies to the owner | Default: the language the owner writes in. |
| (no placeholder) | Document language: English or Bahasa Indonesia | Recommended default: Bahasa Indonesia when the owner writes in Indonesian, otherwise English. Decides the source of the core docs in `install-steps.md` step 1. Agent prompts, skills, and tools stay English in both. |
| `{{PROJECT_TERMS}}` | Project terms: words of the app's domain or UI that stay in one form (for example "link", not "tautan") | Asked when replies or documents are not in English; rows `\| use \| do not mix with \|`. Offer terms seen in the project or the interview as options. None: one row `\| None yet. \| \|`. |
| `{{REPOS}}`, `{{REPO_TABLE}}` | Repos: alias, path from root, working branch, stack | Single repo: one line `app|.|main`. Multi-repo (docs root plus app repos): one line per app repo. `REPOS` lines go to `tools/workflow.conf` as `alias|path|branch`; `REPO_TABLE` rows go to `AGENTS.md`. |
| `{{INSTALL_CMD}}` | Dependency install inside a fresh worktree | For example `npm ci --no-audit --no-fund`, `composer install`, `pip install -r requirements.txt`. Empty if none. If the commands differ per repo, ask how to handle it and record the answer as a pitfall; the template supports one command. |
| `{{COMMANDS}}` | Test, lint, type-check, build, dev commands per repo | Run each once before writing it down (rule 5); write only the ones that ran, with the date. |
| `{{DEFAULT_VERIFY}}` | Default `verify` block for tickets | Usually the fast test and type-check commands. |
| `{{TEST_LOCATIONS}}`, `{{TEST_RULES}}` | Where business-logic tests live; project test rules | For example import style inside tests, test files that must not come back. |
| `{{SOURCE_OF_TRUTH}}` | Files that define names (schema, types, routes) | Agents must verify names there. |
| `{{SHARED_RESOURCES}}` | Resources two tickets must not use at once | For example a local database, a dev-server port, an upload folder. "None" is a valid answer. |
| `{{IRREVERSIBLE_ACTIONS}}` | Project-specific actions that always need approval | For example deploy, production data, merge into the release branch. |
| `{{SESSION_REPORT_DIR}}` | Folder for router session reports | Default `docs/sessions` inside the project (committed). May be a folder outside the repo, such as a notes vault. |
| `{{ROUTER_MODEL}}`, `{{WORKER_MODEL}}`, `{{TESTER_MODEL}}`, `{{EXPLORE_MODEL}}` | Model tier per role | Offer the defaults below with the recommendation, then ask whether to change any. |
| `{{EXTRA_DOCS}}` | Other project documents to list in the document map | `adopt`: existing docs found. `bootstrap`: usually none at first. |
| `{{PITFALLS}}` | Proven pitfalls | Only facts proven by command output. Empty list is fine: write "None yet." |
| `{{SETUP_DATE}}` | Today's date | ISO format. |
| (no placeholder) | Where the owner works: Antigravity 2.0 desktop app, Antigravity IDE, Antigravity CLI (`agy`), or several | All surfaces use the same files and the same flow (`router` skill). |

The remaining placeholders (`{{CURRENT_STATE}}`, `{{NEXT_STEP}}`, `{{WAITING_OWNER}}`, `{{EXECUTION_ORDER}}`, `{{TASKS}}`, `{{INBOX}}`, `{{PROJECT_DECISIONS}}`, `{{WAITING_DECISIONS}}`) are filled by the skill from what it found and agreed with the owner. When there is nothing, write "None yet." rather than inventing content. The `{{PRD_*}}` placeholders in `PRD.md` are filled as described in `prd.md`, and the `{{DESIGN_*}}` placeholders in `DESIGN.md` are filled as described in `design.md`.

## Model defaults and recommendation

Show this table, explain it in one or two sentences, then ask "Keep the defaults or change a role?". Subagent models in Antigravity are passed via `invoke_subagent`'s `Model` parameter (`pro`, `flash`, `flash_lite`, or `inherit`).

| Role | Default | Why |
|---|---|---|
| router | `pro` (the recommended default for the main session; ask, never assume, which model the owner prefers) | Plans, writes briefs, judges security findings, merges. A weak router costs more in retries than it saves. |
| designer | `flash` (`{{WORKER_MODEL}}`) | Explores visual references via `agent-browser`, crafts 3 contrasting HTML mockups in `references/mockups/`, and locks `DESIGN.md` at 99.99% proportional fidelity. |
| worker | `flash` | Works inside a strict Allow list with a detailed brief. Raise to `pro` for a ticket that failed twice. |
| tester | `flash` | Red-green and mutation checks need care but follow a fixed procedure. |
| reviewer | `pro` for auth, session, authorization, security; `flash` for tests and ordinary logic; none for text-only | Matches W-05. The router passes `Model: "pro"` or `Model: "flash"` when calling `invoke_subagent`. |
| Explore, scoper | `flash_lite` | Only locates `path:line` and prepares read-only ticket drafts (`scoper`); never judges. |

Adjust the recommendation to what the owner says about their quota: on a plan with tight quota limits, `flash` for the router with `pro` kept for security reviews is the cheaper option; say so as a trade-off, not as the default. When a model changes, update the Roles table in `WORKFLOW.md` and the `router` skill instructions.

