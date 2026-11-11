# Super-set

**Ready-made ways of working for Claude Code.** Each plugin sets up a project so Claude works the way a careful teammate would: it asks before it guesses, shows proof before it says "done", keeps notes so the next session can pick up where the last one stopped, and splits big jobs into small, checked pieces.

You run one setup command in your project. It interviews you, writes a small set of documents for that project, and installs helper agents and tools. After that you keep using Claude Code as usual, with fewer surprises.

## Which plugin do I need?

| You are making... | Use | What you get |
|---|---|---|
| An app, website, API, or any software project | [`app-project-workflow`](plugins/app-project-workflow/README.md) | A requirements document (PRD), a work board, a ticket flow where one agent plans and others build, test, and review in separate git worktrees, and a guard that catches deleted tests and edits outside the ticket |
| A video, animation, motion graphic, or other content | [`content-project-workflow`](plugins/content-project-workflow/README.md) | A brief, a style guide, a list of every reference, approval steps from storyboard to final render, agents that build, check frames, and research sources, and built-in knowledge about content, motion, and design |

Not sure? If the result is code that runs, pick the app plugin. If the result is something people watch or look at, pick the content plugin. You can install both; each project uses one.

## What changes for you

| Without a plugin | With a plugin |
|---|---|
| Claude starts editing when you only asked a question | A question gets an answer; files change only when you ask for work |
| "Done" or "fixed" without proof | "Done" comes with the output of a command just run (and, for content, the frames it looked at) |
| Each new session starts from zero | `HANDOFF.md` says where things stand; `CLAUDE.md` holds the rules and proven pitfalls |
| Long, unchecked runs | Work is cut into tickets; every result is checked before it counts |
| Guesses about names, numbers, or what a screenshot shows | Names and numbers are looked up; unknowns become questions for you |

Every rule exists because something went wrong without it. The reasons are written in each plugin's `templates/DECISIONS.md`, so you can see why and change what does not fit you.

## Quick start

1. **Install** (once per computer, from any terminal on macOS, Linux, or Windows):
   ```
   claude plugin marketplace add Nazhra05/Super-set
   claude plugin install app-project-workflow@super-set
   ```
   For content projects, install `content-project-workflow@super-set` instead (or as well). Inside a Claude Code session you can use `/plugin marketplace add Nazhra05/Super-set` and `/plugin install <plugin>@super-set`. The terminal and the desktop app share the same installation.
2. **Restart Claude Code**, then open it in your project folder.
3. **Run the setup:**
   - Existing project: `/<plugin>:adopt` (for example `/app-project-workflow:adopt`). It reads what is there first and never overwrites your files.
   - New or empty folder: `/<plugin>:bootstrap`.

   Setup asks its questions, shows you the list of files it will add, and waits for your yes. Nothing is committed unless you ask.
4. **Work as usual**, or start the planning agent for bigger jobs (the router for apps, the producer for content). Each plugin's README shows how.

## What lands in your project

Plain Markdown files you can read and edit, plus a `.claude/` folder:

- `CLAUDE.md`: how Claude should work with you in this project, the commands that are proven to work, and pitfalls already found.
- `HANDOFF.md`: where the last session stopped. A new session reads it first.
- `TODO.md`: the one work board.
- `DECISIONS.md`: why things are the way they are.
- `PRD.md`: what you are making and why (for content: the brief).
- `.claude/agents/` and `.claude/skills/`: the helper agents and skills.

Documents can be written in English or Bahasa Indonesia; setup asks. Code and commits stay in English. After setup the project is self-contained, so removing the plugin later does not break it.

## Questions

- **Does it change my code or assets?** Setup only adds workflow files after you approve the list. Existing files are merged, never overwritten. Original assets and recordings are never touched without your approval.
- **Does it work in the desktop app?** Yes. Some details differ (the desktop app has no status line); each plugin's README explains them.
- **Does it cost extra tokens?** A little: an installed plugin adds its skill descriptions to every session (about 250 tokens for `app-project-workflow`). The helper agents run only when the planning agent sends them work.
- **Can I change the rules?** Yes. Edit the project's files; record why in `DECISIONS.md` so later sessions follow the new rule.

## License
MIT, see `LICENSE`. Each plugin carries its own copy and any third-party notices.
