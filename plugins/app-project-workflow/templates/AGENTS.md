# AGENTS.md: {{PROJECT_NAME}}

Full working rules are in `CLAUDE.md`. This file holds only the code rules that apply to any agent.

## Anti-bloat
1. Write only what was asked. No extra UI elements, speculative features, custom event listeners, or state nobody asked for.
2. No premature abstraction: no single-use wrapper functions, single-use subcomponents, or `variant` props not used in more than one real place.

## Tests
3. Focus on business logic. Test locations: {{TEST_LOCATIONS}}.
4. No negative tests for features or labels that were removed (for example asserting that a deleted text is absent).
5. No brittle UI-rendering tests that only snapshot markup.{{TEST_RULES}}

## Documents
6. Read only the documents relevant to the task (map in `CLAUDE.md`). No duty to read all of them or to report skills in every reply; mention a skill or document only when it affected the result.
