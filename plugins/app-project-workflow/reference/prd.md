# PRD: two ways to write it

Shared by the `adopt` and `bootstrap` skills. The template is `TEMPLATES/PRD.md` (`.workflow-setup/templates/PRD.md`). It is one template with two ways to fill it: `bootstrap` writes what will be built, from the owner's answers; `adopt` writes what is already built, from the code, and the owner confirms it.

## Rules for both
- Write only what the owner said or what the project proves. Anything unknown goes to "Open questions"; never invent a requirement, user, or number.
- Ask with AskUserQuestion, at most 4 questions per call. Reply in the owner's language; the PRD is in the chosen document language. Section and column names below are those of the English template; `TEMPLATES/id/PRD.md` has the same sections in the same order.
- One line per requirement, phrased as behaviour a user can see or a rule the system enforces. IDs `FR-01`, `FR-02`, ... in order; group rows by feature area when there are many.
- Status values are the four in the template. `Met` needs evidence: a `path:line`, a test file, or a command that can be rerun. A claim from a README or old document alone is `Not checked`.
- Non-functional rows only for aspects the owner names or the project proves (for example security, performance, supported platforms, where it runs). "None yet." is a valid answer.
- Show the full draft to the owner in plain language before the install file list, and continue after a yes. Changes asked for are applied first.
- Fill the placeholders: `{{PRD_PROBLEM}}` (problem, goals, signs of success), `{{PRD_USERS}}` (roles and what each may do), `{{PRD_SCOPE}}` (in scope, and out of scope for now), `{{PRD_REQUIREMENTS}}` and `{{PRD_NON_FUNCTIONAL}}` (table rows), `{{PRD_DEPENDENCIES}}`, `{{PRD_OPEN_QUESTIONS}}`, `{{PRD_HISTORY}}` (one line: date, first version, and how it was written).

## Bootstrap: write what will be built
Build on the answers from the project interview, then ask what is still missing:
1. The problem, who has it, and the goals. How the owner will know it works (signs of success).
2. Users or roles, and what each may do.
3. What is in scope for the first version, and what is out of scope for now.
4. The first features. Each becomes a requirement with status `Planned` and evidence `-`.
5. Non-functional needs the owner already knows; dependencies and assumptions (hosting, external services).

Keep it small: the first version holds what the first tickets build. The first `TODO.md` tasks name the requirement they serve.

## Adopt: write what is already built
1. **The project already has a PRD or spec** (found in the survey): do not rewrite it. Ask the owner, with this as the first option: "Keep the existing document as the PRD (Recommended)". Then the template is not installed, `PRD.md` in the document map of `CLAUDE.md` is replaced by the existing path, and the other option is to restructure it into the template with the original linked in History. Either way the original file stays where it is.
2. **No PRD:** draft one from the survey: README, routes or endpoints, pages or screens, CLI commands, database schema, and tests. Each behaviour found becomes a candidate requirement with its evidence path. Status `Met` only when a test or the code path shows it, `Partial` when a gap is visible, `Not checked` otherwise. Do not run or change application code for this.
3. **Problem, goals, users, scope:** the code does not show why the app exists. Ask the owner; offer what the README or other docs say as the first option "(found in project)".
4. **Owner confirms each candidate:** keep as a requirement, drop it, or unsure. Dropped behaviour that still exists in the code goes to the `TODO.md` Inbox as a YAGNI candidate (W-02), never removed during setup. Unsure items go to "Open questions".
5. Every `Partial` requirement gets an Inbox entry in `TODO.md` that names its ID.
