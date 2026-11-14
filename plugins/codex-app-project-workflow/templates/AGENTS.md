# AGENTS.md: {{PROJECT_NAME}}

Short on purpose. Details live in the documents it points to; do not copy them here.
Last verified: {{SETUP_DATE}}. **New session or after compact: read `HANDOFF.md` first.** Status numbers (test counts, versions) are not written here; take them from command output.

## What this is
{{PROJECT_SUMMARY}}

| Repo alias | Path | Stack | Working branch |
|---|---|---|---|
{{REPO_TABLE}}

Source of truth for names (tables, columns, routes, types): {{SOURCE_OF_TRUTH}}.

## How to work with me (owner: {{OWNER_ROLE}})
1. **Discussion vs execution.** Default is discussion: when I ask, discuss, or compare, answer only and do not change files. Execute only after a clear work order. Unsure? Ask in one sentence.
2. **Clear, reversible tasks: do them, do not ask for approval per step.** Approval only for what cannot be undone: see "Still needs owner approval" in `WORKFLOW.md`. In the router flow, merging into the working branch and pushing is done by the router itself (W-06).
3. **Change only what was asked.** Report other findings, do not act on them. **Replace** old code, do not stack a new version beside it; delete what becomes dead. **YAGNI:** every line needs a real user today (a requirement in `PRD.md` or a caller in the code); no features, abstractions, options, or fallbacks "for later". The same question applies when reviewing existing code (W-02).
4. **Do not invent** table, column, function, file names, or numbers. Verify them in the source of truth above and in the code.
5. **Verify through tools, not reports.** Claim "done" or "passing" only with output of a command just run (skill `verification-before-completion`). Agent reports and old documents are not evidence. Do not weaken or skip tests to make them pass. **Existing tests are not assumed genuine (W-01).** For each change: (a) prove red-green: a new test must fail on the code before the fix; (b) for authorization or security logic, run a mutation check (break the check briefly, the test must fail), then restore and compare with the backup; (c) clean up test leftovers; (d) run the full suite at the end. Text, docs, or config changes without logic need no new test, only the relevant suite.
6. **Do not commit or push unless asked**, except the router in the ticket flow (W-06). Conventional Commits, subject max 72 characters. Check `git status` first; do not touch local changes outside the task.
7. **Concise summaries for me in plain language (max 8 to 10 lines)**: always write `<ID> (<short title>)` instead of a bare ID (`T-xx`, `FR-xx`, `D-xx`). State what changed, the risk, and what decision you need from me (no command log dumps or long file lists). If a UI change was not checked in a browser, say so.
8. Language: reply to me in {{OWNER_LANGUAGE}}, following "Terms" below. Code, identifiers, comments, commits, and documents in English. No em dashes in documents.

## Code and test rules (apply to every agent)
- **Anti-bloat:** write only what was asked. No extra UI elements, speculative features, custom event listeners, or state nobody asked for. No premature abstraction: no single-use wrapper functions, single-use subcomponents, or `variant` props not used in more than one real place.
- **Tests:** focus on business logic. Test locations: {{TEST_LOCATIONS}}. No negative tests for features or labels that were removed (for example asserting that a deleted text is absent). No brittle UI-rendering tests that only snapshot markup.{{TEST_RULES}}
- **Documents:** read only the documents relevant to the task (map below). No duty to read all of them or to report skills in every reply; mention a skill or document only when it affected the result.

## Terms
Applies to replies, reports, and documents written in a language other than English. Keep all workflow terms and all standard software engineering terms in English (never translate them into stiff local equivalents): ticket, task, worktree, branch, commit, merge, push, router, scoper, worker, tester, reviewer, guard, verify, Inbox, Allow, done criteria, blocked by, the status values (`Ready`, `In progress`, `Planned`, `Met`, and so on), PRD, IDs (`FR-01`, `W-01`, `D-01`), section names (for example "Execution order"), and technical software terms such as endpoint, route, middleware, payload, request, response, query, schema, migration, index, state, props, component, hook, context, render, build, bundle, lint, type-check, runtime, auth, session, token, mock, assertion, regression, and refactor. Project terms agreed with the owner:

| Use | Do not mix with |
|---|---|
{{PROJECT_TERMS}}

## Commands (verified {{SETUP_DATE}})
{{COMMANDS}}

## Proven pitfalls (do not re-guess)
Add an entry only after it has been proven by command output, with the date.
{{PITFALLS}}

## Skills and role prompts
- In `.codex/skills/`: `router`, `verification-before-completion`, `systematic-debugging`, `test-driven-development`, `receiving-code-review`, `writing-plans`. Reasons: `DECISIONS.md` W-08; license: `.codex/skills/NOTICE`.
- Role prompts in `.codex/agents/`: `scoper.md`, `worker.md`, `tester.md`, `reviewer.md`, `Explore.md` (dispatched via `codex exec`).
- TDD only for business logic (locations above).
- Do not add skills or hooks that force a ritual before every reply, or separate worktree or subagent skills; the ticket flow covers them (W-04, W-08).
- **Ticket flow (W-04):** splitting work into worktrees and subagents happens only through `WORKFLOW.md`, in a router session (`$router` or `router` skill). Outside that flow, subagents are run only when I ask. Rules 1 to 8 apply to every agent.

## Document map (read what the task needs, not everything)
`PRD.md` (what and why) · `WORKFLOW.md` (ticket flow) · `TODO.md` (the only work board) · `HANDOFF.md` (last session state, start here) · `DECISIONS.md` (decisions and what is waiting) · `AGENTS.md` (working, code, and test rules for any agent){{EXTRA_DOCS}}

