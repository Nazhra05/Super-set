# DECISIONS: decision log for {{PROJECT_NAME}}

Two series. **W-xx** are workflow decisions inherited from the App Project Workflow plugin; they explain why the rules in `CLAUDE.md`, `WORKFLOW.md`, and the agents look the way they do. Change them only by writing a new project decision that overrides one, with the reason. **D-xx** are this project's own decisions, starting at D-01.

Format per entry: title with status and date, then Reason, Decision, Consequence (files that changed).

## A. Workflow decisions (inherited at setup, {{SETUP_DATE}})
Each rule was added after a concrete failure in real use. The evidence is kept short so the reason is not argued again.

### W-01 Verify through tools; tests are not assumed genuine
- **Reason:** agents reported "done" and "passing" for work that was not. In real use, turning off signature verification entirely left the whole suite green, and a tester twice reported an escape string that was not in the file.
- **Decision:** a claim needs output of a command just run. Agent reports and old documents are not evidence. Status numbers are quoted from command output with a date, or not written. Every new test is proven red before the fix; authorization and security logic also gets a mutation check (break the check, the test must fail, restore, compare with the backup). Existing tests are audited step by step as they become relevant.

### W-02 YAGNI for new and existing code
- **Reason:** earlier agents added many lines nobody used. Auditing tests alone does not touch excess code that still runs.
- **Decision:** every line needs a real user today: a requirement or a caller in the code. Three questions per candidate: (1) who calls or uses it (proven by grep or a test)? (2) which requirement does it serve? (3) what breaks when it is removed (proven by a green suite)? No answer to (1) and (2) makes it a removal candidate. No big refactor in the name of YAGNI. Lists of "unreferenced functions" from tools are a starting point only (many false positives from templates and framework entry points).

### W-03 Legacy code: lock behaviour first; TDD for new logic
- **Decision:** before changing old code of unknown quality: understand the important behaviour, lock it with tests proven honest by mutation (W-01), change in small steps, review the diff with YAGNI (W-02), run the full suite. New logic with clear rules: pure TDD (failing test first). Tests do not replace code review: tests answer "is the behaviour right", review answers "is this code worth keeping".

### W-04 Ticket flow with router, worktree, and subagents
- **Reason:** working one item at a time is slow once the board is ticket-shaped, but unsupervised agents made many mistakes.
- **Decision:** a router main session plans and verifies; worker, tester, reviewer, and Explore subagents work one ticket each in a git worktree created by `tools/wt.sh`. `tools/guard.sh` checks scope and test integrity deterministically; `tools/verify.sh` runs the ticket's Done criteria. Subagent reports are claims; the router reruns guard and verify. Outside the router flow, subagents are created only when the owner asks. The superpowers skills for subagents and worktrees are not installed; `WORKFLOW.md`, `tools/`, and `.claude/agents/` replace them.

### W-05 Reviewer by risk tier
- **Reason:** in real use a reviewer used 56% to 80% of the tokens of the agent it reviewed, and a sonnet reviewer was sharp enough for test tickets.
- **Decision:** opus for auth, session, authorization, security; sonnet for E2E, tests, ordinary logic; no reviewer for text-only changes. One round of fixes may be verified by the router with evidence, except security tickets, which are always reviewed again. This only measures mistakes that were caught; mistakes that pass every layer are not measured.

### W-06 The router runs on its own; approval only for the irreversible
- **Reason:** asking the owner to approve merges, pushes, and doc commits added friction without adding safety, because all of them can be undone.
- **Decision:** the router works through the execution order without `Ready` per ticket, merges `--no-ff` into the working branch after guard, verify, and reviewer are clean, pushes after each ticket, and promotes Inbox items that need no owner decision. After two failures it diagnoses or takes over instead of waiting. Test depth is weighed per ticket. Still needs approval: the list in `WORKFLOW.md`. Usage guard: above 90% of the 5-hour or 7-day limit (or unknown), only work that surely finishes cleanly; at 60% context, prepare compact at the ticket boundary. Reports once per ticket pair, plus a session report with cost details.

### W-07 Tickets are sized to fit the agent turn limit
- **Reason:** agents stopped at `maxTurns` without a report; on one measured day 36% of subagent tokens were wasted on cut-off runs. Raising the limit only makes failed runs larger.
- **Decision:** budget in the ticket equals the agent's `maxTurns`; work is sized to about 60% of it (tester max 6 to 8 mutations, worker about 8 files, reviewer 5 explicit check items). Every brief names the tool call by which the report must be sent (limit minus 8). Each spawn costs about 20k to 25k tokens of re-reading, so small work is done by the router directly. Session reports record tokens per agent, cut-off runs, and spawns per ticket so the sizes can be tuned with data.

### W-08 Five discipline skills, project scope, no hooks
- **Decision:** the project ships five skills in `.claude/skills/`: `verification-before-completion` (evidence before claims), `systematic-debugging` (root cause, not guesses), `test-driven-development` (business logic only), `receiving-code-review` (no reflexive agreement), `writing-plans` (small steps, executed through the ticket flow or inline). Kept out on purpose: any skill or SessionStart hook that forces a ritual before every reply (it burns context and collides with "discussion vs execution"), review-request skills that duplicate the built-in `/code-review` and `/security-review`, and separate subagent or worktree skills (the ticket flow in W-04 covers them). License and changes: `.claude/skills/NOTICE`.

### W-09 One place for status; short instruction files
- **Decision:** work status lives only in `TODO.md` and `HANDOFF.md`; other documents hold no status numbers. `CLAUDE.md` and `AGENTS.md` stay short and point to documents instead of copying them. No rule obliges an agent to read every document or to report skills in each reply; such rituals were ignored or burned context in real use.

## B. Project decisions
{{PROJECT_DECISIONS}}

## C. Waiting for the owner
{{WAITING_DECISIONS}}
