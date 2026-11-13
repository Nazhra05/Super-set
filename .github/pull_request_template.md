## What and why
<!-- What does this change, and what problem from real use does it solve? Link the issue if there is one. -->

## Plugin and version
<!-- Which plugin. If behaviour changed: new version in plugin.json (and marketplace.json for Claude Code plugins), and a CHANGELOG line. -->

## How it was tested
<!-- Commands you ran and their output. Operating system and terminal/CLI or desktop app/IDE. -->

## Not tested
<!-- Say plainly what you did not test (for example macOS, Linux, desktop app, an interactive setup). -->

## Checklist
- [ ] Manifest validation passes (`claude plugin validate` for Claude Code plugins; JSON validation for Antigravity `plugin.json`)
- [ ] A changed rule has a reason in `templates/DECISIONS.md`
- [ ] Changes to `templates/` docs are mirrored in `templates/id/` (or I asked the maintainer to add them)
- [ ] Shared material is changed in all matching plugins
- [ ] No company, product, or personal names and no local paths inside the plugins
- [ ] No em dashes in documents; LF line endings; `.sh` files executable in git
