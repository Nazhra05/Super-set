# Super-set

**Stop Claude Code, Google Antigravity, and OpenAI Codex from guessing, overreaching, and saying "done" without proof.**

Super-set is a small collection of workflow plugins for **Claude Code**, **Google Antigravity (Gemini)**, and **OpenAI Codex**. Each one sets up your project with a way of working that a careful teammate would follow: answer questions before touching files, look things up instead of inventing them, show proof before claiming success, split big jobs into checked tickets, and leave notes so the next session starts where the last one stopped.

You run one setup command in your project. It interviews you, writes a few plain Markdown documents for that project, and installs helper agents and tools. Then you keep using your coding agent as usual, with fewer surprises.

## Which plugin do I need?

| You are making... | Claude Code | Google Antigravity | OpenAI Codex | What you get |
|---|---|---|---|---|
| An app, website, API, or any software project | [`app-project-workflow`](plugins/app-project-workflow/README.md) | [`agy-app-project-workflow`](plugins/agy-app-project-workflow/README.md) | [`codex-app-project-workflow`](plugins/codex-app-project-workflow/README.md) | A requirements document (PRD), a work board, session notes, and a ticket flow where a planning agent hands work to builder, tester, and reviewer agents, with a guard that catches deleted tests and edits outside the ticket |
| A video, animation, or motion graphic | [`content-project-workflow`](plugins/content-project-workflow/README.md) | [`agy-content-project-workflow`](plugins/agy-content-project-workflow/README.md) | [`codex-content-project-workflow`](plugins/codex-content-project-workflow/README.md) | A brief, a style guide, a list of every reference, approval steps from storyboard to final render, agents that build, check frames, and research sources, and built-in knowledge about content, motion, and design |

If the result is code that runs, pick the app plugin. If the result is something people watch, pick the content plugin. You can install both; each project uses one.

## What changes for you

| Without a plugin | With a plugin |
|---|---|
| The agent starts editing when you only asked a question | A question gets an answer; files change only when you ask for work |
| "Done" or "all tests pass" without proof | "Done" comes with the output of a command just run (and, for content, the frames it looked at) |
| Each new session starts from zero | `HANDOFF.md` says where things stand; `CLAUDE.md` / `AGENTS.md` holds the rules and the pitfalls already found |
| One long run that drifts and fills the context | Work is cut into tickets; each result is checked before it counts |
| Guesses about names, numbers, or what a screenshot shows | Names and numbers are looked up; what is seen is kept apart from what is guessed; unknowns become questions for you |

## Why trust it

The rules were not designed on paper. Each one was added after something went wrong in real projects, and the reason is written next to it in each plugin's `templates/DECISIONS.md`. A few examples:

- **A test suite stayed green with signature verification switched off entirely.** Since then, every new test must be shown to fail before the fix, and security checks get a mutation test (break the check on purpose, the test must fail).
- **On one measured day, 36% of subagent tokens were wasted on runs cut off at their turn limit.** Since then, tickets are sized to about 60% of an agent's limit and every brief says when the report is due.
- **Reviews cost 56% to 80% of the work they reviewed.** Since then, the reviewer model is chosen by risk: the strongest model for security, a cheaper one for ordinary logic, none for text-only changes.
- **A feedback screenshot was "fixed" based on a wrong reading, and a character was made by recoloring an existing mascot.** Since then, the content plugin separates what is seen from what is inferred, measures instead of estimating, and asks before basing a design on someone else's.

You can read every rule, change it for your project, and record why.

## Quick start

### For Claude Code
1. **Install** (once per computer, from any terminal):
   ```
   claude plugin marketplace add Nazhra05/Super-set
   claude plugin install app-project-workflow@super-set
   ```
   For video or content projects, install `content-project-workflow@super-set`. Inside a Claude Code session you can use `/plugin marketplace add Nazhra05/Super-set` and `/plugin install <plugin>@super-set`. The terminal and the desktop app share the same installation.
2. **Restart Claude Code** and open it in your project folder.
3. **Run the setup:**
   - Existing project: `/<plugin>:adopt` (for example `/app-project-workflow:adopt`). It reads what is there first and never overwrites your files.
   - New or empty folder: `/<plugin>:bootstrap`.

### For Google Antigravity (Gemini)
1. **Install** (once per computer, or per workspace):
   Copy `plugins/agy-app-project-workflow` (or `plugins/agy-content-project-workflow`) into `~/.gemini/config/plugins/<plugin-name>/`, or register its path in your project's `.agents/plugins.json`.
2. **Open Antigravity** (Antigravity 2.0 desktop app, Antigravity IDE, or Antigravity CLI `agy`) in your project folder.
3. **Run the setup:**
   - Existing project: invoke the `adopt` skill (`/adopt` or click the starter prompt on the plugin card).
   - New or empty folder: invoke the `bootstrap` skill (`/bootstrap`).

### For OpenAI Codex
1. **Install** (once per computer):
   Copy the setup skills from `plugins/codex-app-project-workflow/skills/` (or `plugins/codex-content-project-workflow/skills/`) into `~/.codex/skills/`, and set `CODEX_APP_WORKFLOW_ROOT` / `CODEX_CONTENT_WORKFLOW_ROOT` to the plugin folder path (or run `bash "<path-to-plugin>/scripts/stage.sh" .` in your project folder).
2. **Open Codex** (`codex` CLI or Codex desktop/IDE) in your project folder.
3. **Run the setup:**
   - Existing project: invoke `$codex-app-adopt` (or `$codex-content-adopt`).
   - New or empty folder: invoke `$codex-app-bootstrap` (or `$codex-content-bootstrap`).

Setup asks its questions, shows the list of files it will add, and waits for your yes. Nothing is committed unless you ask.

4. **Work as usual**, or start the planning agent for bigger jobs (the router for apps, the producer for content). Each plugin's README shows how.

## What lands in your project

Plain Markdown files you can read and edit, plus an agent customization folder (`.claude/` for Claude Code, `.agents/` for Antigravity, `.codex/` for OpenAI Codex):

- `CLAUDE.md` / `AGENTS.md`: how the agent works with you in this project, commands that are proven to work, pitfalls already found.
- `HANDOFF.md`: where the last session stopped. A new session reads it first.
- `TODO.md`: the one work board.
- `DECISIONS.md`: why things are the way they are.
- `PRD.md`: what you are making and why (for content: the brief).
- `.claude/`, `.agents/`, or `.codex/`: the helper subagents/role prompts and skills.

Documents can be in English or Bahasa Indonesia; setup asks. Code and commits stay in English. After setup the project is self-contained, so removing the plugin later does not break it.

## Status

All plugins are in version 0.x. What has been tested, and what not yet:

| | Claude Code (`app-*`, `content-*`) | Google Antigravity (`agy-*`) | OpenAI Codex (`codex-*`) |
|---|---|---|---|
| Setup (`adopt`, `bootstrap`) | Tested end to end on sample projects (`content:bootstrap` not yet) | Validated (manifest, placeholder parity, hook guard); interactive runs not yet tested | Validated (manifest, placeholder parity, `stage.sh`); interactive runs not yet tested |
| Daily flow (planning agent with helpers) | App flow used in a real project; content flow not yet | Adapted from the proven flow; not yet tried in a real project | Adapted from the proven flow (`codex exec`); not yet tried in a real project |
| Windows, terminal / shell tools | Tested (Git Bash) | Tested (`env-guard.js` and `bash` tool wrappers) | Tested (`stage.sh` and `bash` tool wrappers) |
| macOS, Linux | Not yet tested (scripts are written for them) | Not yet tested | Not yet tested |
| Desktop app / IDE | Partly tested | Not yet tested | Not yet tested |

Reports from any of the untested cases are very welcome (see Contributing).

## Questions

- **Does it change my code or assets?** Setup only adds workflow files after you approve the list. Existing files are merged, never overwritten. Original assets and recordings are never touched without your approval.
- **Does it work in the desktop app?** Yes. Each plugin's README explains how to run the planning session in both the terminal and the desktop app.
- **Does it cost extra tokens?** An installed plugin adds only its two setup skill descriptions to every session: about 170 to 200 tokens. The helper subagents cost tokens only when the planning agent sends them work; each plugin's README lists which model tiers they use.
- **Can I change the rules?** Yes. Edit the project's files and record why in `DECISIONS.md`, so later sessions follow the new rule.

## Contributing

Help is welcome, and you do not need to write code to give it. The most useful contributions right now:

- **Try it and tell us what happened**, especially on macOS, Linux, the desktop app, Google Antigravity, or the content plugins on a real video project. Open an issue with the "Bug report" or "Field report" form.
- **Suggest a rule or a fix** with the "Feature request" form: what went wrong without it, and what would have prevented it.
- **Add guard patterns** for more test frameworks (pytest, Go, Rust, `node:test`, Pest), each proven by a guard run that must fail.
- **Improve the knowledge skills** of the content plugins, with sources.

Questions go to [Discussions, Q&A](https://github.com/Nazhra05/Super-set/discussions/categories/q-a), early ideas to [Discussions, Ideas](https://github.com/Nazhra05/Super-set/discussions/categories/ideas), and bugs and field reports to [Issues](https://github.com/Nazhra05/Super-set/issues/new/choose). Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License
MIT, see `LICENSE`. Each plugin carries its own copy and any third-party notices. The bundled discipline skills (`verification-before-completion`, `systematic-debugging`, `test-driven-development`, `receiving-code-review`, `writing-plans`) are adapted from [obra/superpowers](https://github.com/obra/superpowers) by Jesse Vincent (MIT); see each plugin's `NOTICE` and `LICENSE-superpowers`.
