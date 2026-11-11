# Super-set

**Stop Claude Code from guessing, overreaching, and saying "done" without proof.**

Super-set is a small collection of Claude Code plugins. Each one sets up your project with a way of working that a careful teammate would follow: answer questions before touching files, look things up instead of inventing them, show proof before claiming success, split big jobs into checked tickets, and leave notes so the next session starts where the last one stopped.

You run one setup command in your project. It interviews you, writes a few plain Markdown documents for that project, and installs helper agents and tools. Then you keep using Claude Code as usual, with fewer surprises.

## Which plugin do I need?

| You are making... | Use | What you get |
|---|---|---|
| An app, website, API, or any software project | [`app-project-workflow`](plugins/app-project-workflow/README.md) | A requirements document (PRD), a work board, session notes, and a ticket flow where a planning agent hands work to builder, tester, and reviewer agents, with a guard that catches deleted tests and edits outside the ticket |
| A video, animation, or motion graphic | [`content-project-workflow`](plugins/content-project-workflow/README.md) | A brief, a style guide, a list of every reference, approval steps from storyboard to final render, agents that build, check frames, and research sources, and built-in knowledge about content, motion, and design |

If the result is code that runs, pick the app plugin. If the result is something people watch, pick the content plugin. You can install both; each project uses one.

## What changes for you

| Without a plugin | With a plugin |
|---|---|
| Claude starts editing when you only asked a question | A question gets an answer; files change only when you ask for work |
| "Done" or "all tests pass" without proof | "Done" comes with the output of a command just run (and, for content, the frames it looked at) |
| Each new session starts from zero | `HANDOFF.md` says where things stand; `CLAUDE.md` holds the rules and the pitfalls already found |
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

   Setup asks its questions, shows the list of files it will add, and waits for your yes. Nothing is committed unless you ask.
4. **Work as usual**, or start the planning agent for bigger jobs (the router for apps, the producer for content). Each plugin's README shows how.

## What lands in your project

Plain Markdown files you can read and edit, plus a `.claude/` folder:

- `CLAUDE.md`: how Claude works with you in this project, commands that are proven to work, pitfalls already found.
- `HANDOFF.md`: where the last session stopped. A new session reads it first.
- `TODO.md`: the one work board.
- `DECISIONS.md`: why things are the way they are.
- `PRD.md`: what you are making and why (for content: the brief).
- `.claude/agents/` and `.claude/skills/`: the helper agents and skills.

Documents can be in English or Bahasa Indonesia; setup asks. Code and commits stay in English. After setup the project is self-contained, so removing the plugin later does not break it.

## Status

Both plugins are young (version 0.x). What has been tested, and what not yet:

| | app-project-workflow | content-project-workflow |
|---|---|---|
| Setup (`adopt`, `bootstrap`) | Tested end to end on sample projects | `adopt` tested end to end on a sample project; `bootstrap` not yet |
| Daily flow (planning agent with helpers) | Used in a real project before it became a plugin | Not yet tried in a real project |
| Windows (Git Bash), terminal | Tested | Tested |
| macOS, Linux | Not yet tested (scripts are written for them) | Not yet tested |
| Desktop app | Partly tested | Not yet tested |

Reports from any of the untested cases are very welcome (see Contributing).

## Questions

- **Does it change my code or assets?** Setup only adds workflow files after you approve the list. Existing files are merged, never overwritten. Original assets and recordings are never touched without your approval.
- **Does it work in the desktop app?** Yes. Some details differ (the desktop app has no status line); each plugin's README explains them.
- **Does it cost extra tokens?** An installed plugin adds its two skill descriptions to every session: about 170 tokens for `app-project-workflow` and 200 for `content-project-workflow`, measured with `claude plugin details`. The helper agents cost tokens only when the planning agent sends them work; each plugin's README lists which models they use.
- **Can I change the rules?** Yes. Edit the project's files and record why in `DECISIONS.md`, so later sessions follow the new rule.

## Contributing

Help is welcome, and you do not need to write code to give it. The most useful contributions right now:

- **Try it and tell us what happened**, especially on macOS, Linux, or the desktop app, and the content plugin on a real video project. Open an issue with the "Bug report" or "Field report" form.
- **Suggest a rule or a fix** with the "Feature request" form: what went wrong without it, and what would have prevented it.
- **Add guard patterns** for more test frameworks (pytest, Go, Rust, `node:test`, Pest), each proven by a guard run that must fail.
- **Improve the knowledge skills** of the content plugin, with sources.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Questions and ideas: [open an issue](https://github.com/Nazhra05/Super-set/issues).

## License
MIT, see `LICENSE`. Each plugin carries its own copy and any third-party notices.
