# Content Project Workflow (Antigravity)

**Run your video or animation project with Google Antigravity like a small studio.** This plugin sets up a project so Antigravity follows a brief and a style guide, uses every reference you give it, shows you designs for approval before building on them, checks its own frames instead of guessing, and keeps each step short.

Part of the [Super-set](../../README.md) repository.

## Is it for you?
Use it if you make explainer videos, social reels, animations, or motion graphics with Google Antigravity (for example with HyperFrames or Remotion), and you have seen things like:
- The agent reading your screenshot wrong and "fixing" the wrong thing.
- Characters or designs made with little care, or copied from an existing mascot.
- References you supplied being ignored, or "I checked that repository" with nothing to show.
- One request turning into an hour-long run that fills the context.
- Missing basics: a weak hook, text under the app buttons, captions that do not match the voice-over.

**When not to use it:** a single graphic or a one-off clip with no script (the gates are more process than you need), or software projects (use `agy-app-project-workflow`).

## What it does for you
| Problem | What the plugin sets up |
|---|---|
| No shared picture of the goal | `PRD.md` (the brief): goal, audience, format, message, facts with sources |
| Inconsistent look | `STYLE.md`: palette (measured hex values), type, motion, sound, characters, do and don't |
| Ignored references | `REFERENCES.md`: every file and link with an ID, what it shows, what to take from it, where it was used |
| Misread screenshots | A rule in `AGENTS.md` to write what is seen, then what is inferred, and to measure instead of estimating; ask when it matters |
| Work built on unapproved designs | Approval gates: brief, style frames, character sheets, animatic, final |
| Shallow research | A `researcher` subagent that reads the actual files and writes a cited note |
| Low-effort characters | A `character-design` skill: options side by side, turnaround, expressions, mouth shapes, poses, rig, and an originality rule |
| Long runs | A `producer` skill that hands one shot at a time to builders and reviewers and stops at every gate |
| Missing craft knowledge | Skills for content basics (hook, pacing, safe zones, captions, loudness), motion (the 12 principles, easing), and design (hierarchy, type, color, contrast) |

## How a project runs
1. Setup writes the brief, style guide, and reference list with you.
2. The producer plans the next gate: storyboard, style frames, character sheets, animatic, shots, final.
3. An `asset-builder` makes one piece; a `visual-reviewer` grabs the frames and checks them with `read_file` against the brief, style, script, and references.
4. At each approval gate the producer shows you the frames or sheets and waits for your yes.

You can also skip the producer and talk to Antigravity as usual; the rules in `AGENTS.md` still apply automatically.

## Setup
| Skill | Use when | What it does |
|---|---|---|
| `adopt` | The project already has a script, recordings, assets, renders, or its own agent setup | Reads everything first, lists every reference, keeps or drafts the brief and style from what exists, merges existing rules, never overwrites originals |
| `bootstrap` | New or empty folder | Interviews you with `ask_question`, writes the first brief, style guide, and reference list; no production yet |

Both explain the defaults below and ask which to change, show the list of files before writing, smoke-test the tools, and end with a plain-language report. Nothing is committed unless you ask.

### Installing the plugin in Antigravity
Copy `Super-set/plugins/agy-content-project-workflow` into `~/.gemini/config/plugins/agy-content-project-workflow/`, or reference it from your project's `.agents/plugins.json`. After setup the project is self-contained, so disabling or removing the plugin later does not break the project.

## Daily use
The flow is identical across Antigravity 2.0 desktop app, Antigravity IDE, and Antigravity CLI (`agy`):
- Invoke the **`producer`** skill (`/producer` or ask the agent to "start the producer session and work through `TODO.md`").
- The producer works through the gates and tickets in `TODO.md`, stops at every approval gate, and sends heavy work (building assets, reviewing frames, research) to subagents via `invoke_subagent` so its own turns stay short.

## Cost and model tiers
- During work: the `producer`, `asset-builder`, and `visual-reviewer` default to `pro`, because design and visual judgement are where lighter settings fail; `researcher` uses `flash` and `Explore` uses `flash_lite`. Images cost many tokens, so frames are checked as small contact sheets first. On a plan with tight quota limits, setup can set the `asset-builder` to `flash` for routine tickets.

## Opinionated defaults (and how to change them)
Setup explains these and asks which to change; afterwards, change them in the files named. To override a decision (C-xx), add a project decision (D-xx) in `DECISIONS.md` with the reason.

| Default | Why | Where |
|---|---|---|
| A question or an image alone gets an answer, not file changes | Prevents unasked edits | `AGENTS.md` rule 1 |
| For every image: what is seen, then what is inferred; measure, do not estimate; ask when it matters | Screenshots were misread | `AGENTS.md` rule 5, C-01 |
| "Done" needs a check just run and the frames looked at; say what was not watched or heard | "Done" without looking | `AGENTS.md` rule 6, C-02 |
| Approval gates: brief, style frames, character sheets, animatic, final | Work built on unapproved designs | `WORKFLOW.md`, C-03 |
| Every reference is listed and accounted for | References ignored | `REFERENCES.md`, C-04 |
| Research reads the source and writes a cited note | A repository "check" read only its front page | `WORKFLOW.md`, C-05 |
| One ticket per dispatch; stop at gates; heavy work in subagents | Hour-long turns filled the context | `WORKFLOW.md`, C-06 |
| Design options side by side; character sheets before animation; no copying an existing character or mascot without asking | Low-effort, derivative characters | skill `character-design`, C-07 |
| Facts and dialogue on screen come only from the script or a named source | Invented numbers, text that does not match the recording | `AGENTS.md` rule 4 |
| Originals (script, recordings, source art) are never overwritten without approval | They cannot be recreated | `WORKFLOW.md` |
| Docs in English or Bahasa Indonesia; code and commits in English; common terms in one form | Readable docs, no mixed terms | `AGENTS.md` rule 9, "Terms" |

## What lands in the project
- Docs: `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `PRD.md` (brief), `STYLE.md`, `REFERENCES.md`, `tickets/_TEMPLATE.md`, in English or Indonesian.
- `.agents/agents/`: `asset-builder`, `visual-reviewer`, `researcher`, `Explore`.
- `.agents/skills/`: `producer`, `content-fundamentals`, `motion-principles`, `design-basics`, `character-design`, `verification-before-completion`, `systematic-debugging`.
- `.agents/hooks.json` + `tools/env-guard.js`: `PreToolUse` hook that blocks reading, editing, writing, or running shell commands on `.env` files.
- `tools/`: `scope.sh` (files changed outside a ticket's Allow list; needs git), `verify.sh` (runs a ticket's checks), `env-guard.js`.

## Requirements
- Node.js (`env-guard.js` hook) and Bash (Git Bash on Windows).
- Git is recommended; without it the scope check does not run.
- Frame grabs usually need `ffmpeg` or the video tool's snapshot command.

## Layout of this plugin
```
plugin.json       Antigravity plugin manifest
skills/           adopt, bootstrap
reference/        setup-interview.md, brief-and-style.md, install-steps.md
scripts/          stage.sh (copies setup material into the project during setup)
templates/        everything copied into a project (English docs)
templates/id/     the docs in Indonesian
```

## License
MIT, see `LICENSE`. `verification-before-completion` and `systematic-debugging` are adapted from [obra/superpowers](https://github.com/obra/superpowers) (MIT); attribution and changes are in `templates/.agents/skills/NOTICE`. The knowledge skills list their sources inside each skill.

