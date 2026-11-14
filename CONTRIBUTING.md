# Contributing to Super-set

Thank you for helping. This project is small and maintained by one person, so clear, focused contributions help most. You do not need to write code to contribute.

## Ways to help

| Help | How | Where |
|---|---|---|
| **Question** | How do I, does it, why does it... | [Discussions, Q&A](https://github.com/Nazhra05/Super-set/discussions/categories/q-a) |
| **Early idea** | Not sure yet whether it should become a rule or a feature | [Discussions, Ideas](https://github.com/Nazhra05/Super-set/discussions/categories/ideas) |
| **Field report** | Use a plugin on a real project and tell us what worked, what confused you, and what went wrong. Most wanted: macOS, Linux, the desktop app, Google Antigravity, OpenAI Codex, and the content plugins on a real video. | Issue form "Field report" |
| **Bug report** | Something failed: a setup step, a script, an instruction the agent misread. | Issue form "Bug report" |
| **Rule or feature idea** | What went wrong without it, and what would have prevented it. | Issue form "Feature request" |
| **Guard patterns** | Patterns for more test frameworks in `app-project-workflow`, `agy-app-project-workflow`, and `codex-app-project-workflow` (pytest, Go, Rust, `node:test`, Pest), each proven by a guard run that must fail. | Pull request |
| **Knowledge skills** | Better or more content, motion, and design guidance in `content-project-workflow`, `agy-content-project-workflow`, and `codex-content-project-workflow`, with sources. | Pull request |
| **Translations** | Core docs in another language, as a new `templates/<lang>/` folder that mirrors `templates/id/`. | Pull request |

For anything bigger than a small fix, please open an issue (or an Ideas discussion) first so we can agree on the approach before you spend time on it.

## How a pull request works (short version)
1. Fork the repository on GitHub and create a branch.
2. Make your change and run the checks below.
3. Open a pull request against `main` and fill in the template.
4. The maintainer reviews it, may ask for changes, and merges it when it is ready.

## Rules for changes
These keep the plugins trustworthy. A pull request that breaks one of them will be asked to change.

- **Every rule needs a reason from real use.** A new or changed rule comes with what went wrong without it, and an entry in the plugin's `templates/DECISIONS.md` (W-xx for the app plugins, C-xx for the content plugins).
- **Do not invent platform behaviour.** Keys, flags, frontmatter fields, and tool behaviour must be in the official docs (https://code.claude.com/docs for Claude Code, https://antigravity.google/docs for Google Antigravity) or shown by a test. Say which in the pull request.
- **Prove it.** Describe what you ran and paste the output. Say plainly what you did not test (for example macOS or the desktop app).
- **Keep it generic.** No company, product, or personal names, and no local paths, inside the plugins.
- **Both languages.** A change to a document in `templates/` is made in `templates/id/` too, with the same placeholders. If you cannot write Indonesian, say so in the pull request and the maintainer will add it.
- **Shared parts stay in sync.** Material that exists across plugins (`scripts/stage.sh`, `tools/statusline.js`, `tools/env-guard.js`, the shared skills, the common rules) is changed in all matching plugins.
- **Style:** English in the repository (except `templates/id/`), no em dashes in documents, LF line endings, shell scripts executable in git (`git update-index --chmod=+x <file>`), Conventional Commits with a subject of at most 72 characters.
- **Licenses:** do not copy text or code from other projects unless their license allows it, and keep the attribution (see each plugin's `NOTICE`).

## Checks before you open a pull request
Run from the repository root:

```
claude plugin validate .
claude plugin validate plugins/app-project-workflow
claude plugin validate plugins/content-project-workflow
node -e "JSON.parse(require('fs').readFileSync('plugins/agy-app-project-workflow/plugin.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('plugins/agy-content-project-workflow/plugin.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('plugins/codex-app-project-workflow/plugin.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('plugins/codex-content-project-workflow/plugin.json','utf8'))"
git ls-files --eol | grep -c 'i/crlf'
git ls-files -s | grep '\.sh$'
```

The validations must pass, the CRLF count must be `0`, and every `.sh` file must show `100755`.

To try your working copy in Claude Code without installing it, open an empty folder and run:

```
claude --plugin-dir /path/to/Super-set/plugins/<plugin>
```

then `/<plugin>:bootstrap` in that session. For Google Antigravity, register the plugin folder in `.agents/plugins.json` or copy it into `~/.gemini/config/plugins/`.

If you changed a plugin's behaviour, also bump its `version` in its `plugin.json` (and in `.claude-plugin/marketplace.json` for Claude Code plugins), and add a line to `plugins/<plugin>/CHANGELOG.md`.

## Code of conduct
Be kind and assume good intent. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
