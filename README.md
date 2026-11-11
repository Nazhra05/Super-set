# Super-set

A Claude Code marketplace. Each plugin lives in its own folder under `plugins/` and is installed on its own.

| Plugin | For | Docs |
|---|---|---|
| `app-project-workflow` | Application development: ticket flow with router and subagents, one git worktree per ticket, scope and test-integrity guard, PRD, evidence-first verification | [plugins/app-project-workflow/README.md](plugins/app-project-workflow/README.md) |

## Install
From any terminal (macOS, Linux, or Windows):
```
claude plugin marketplace add Nazhra05/Super-set
claude plugin install <plugin>@super-set
```
Or inside a Claude Code session: `/plugin marketplace add Nazhra05/Super-set`, then `/plugin install <plugin>@super-set`.

## License
MIT, see `LICENSE`. Each plugin carries its own copy and any third-party notices.
