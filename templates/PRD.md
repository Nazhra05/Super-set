# PRD: {{PROJECT_NAME}}

Last updated: {{SETUP_DATE}}. This document answers **what and why** only. How it is built: the code and `CLAUDE.md`. Why a decision went one way: `DECISIONS.md`. Next work: `TODO.md`. No status numbers here (W-09); the Evidence column points to a file or a command that can be rerun.

Requirements change only with the owner's agreement, and each change gets a line in History. A removed requirement keeps its ID; IDs are never reused. Code that serves no requirement here and has no caller is a YAGNI candidate (W-02).

## 1. Problem and goals
{{PRD_PROBLEM}}

## 2. Users
{{PRD_USERS}}

## 3. Scope
{{PRD_SCOPE}}

## 4. Functional requirements
Status: `Planned` (not built yet) · `Met` (enforced in code, shown by the evidence) · `Partial` (gap recorded in `TODO.md`) · `Not checked` (claimed, not yet verified in code).

| ID | Requirement | Status | Evidence |
|---|---|---|---|
{{PRD_REQUIREMENTS}}

## 5. Non-functional requirements
| Aspect | Requirement | Status | Evidence |
|---|---|---|---|
{{PRD_NON_FUNCTIONAL}}

## 6. Dependencies and assumptions
{{PRD_DEPENDENCIES}}

## 7. Open questions
Questions that change what is built. Decisions waiting for the owner are in `DECISIONS.md` section C.
{{PRD_OPEN_QUESTIONS}}

## 8. History
{{PRD_HISTORY}}
