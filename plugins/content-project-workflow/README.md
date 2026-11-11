# Content Project Workflow

**Run your video or content project with Claude Code like a small studio.** This plugin sets up a project so Claude follows a brief and a style guide, uses every reference you give it, shows you designs for approval before building on them, checks its own frames instead of guessing, and keeps each step short.

## Is it for you?
Use it if you make explainer videos, social reels, animations, motion graphics, or similar content with Claude Code (for example with HyperFrames or Remotion), and you have seen things like:
- Claude reading your screenshot wrong and "fixing" the wrong thing.
- Characters or designs made with little care, or copied from an existing mascot.
- References you supplied being ignored, or "I checked that repository" with nothing to show.
- One request turning into an hour-long run that fills the context.
- Missing basics: weak hook, text under the app buttons, text that does not match the voice-over.

For software projects, use `app-project-workflow` instead.

## What it does for you
| Problem | What the plugin sets up |
|---|---|
| No shared picture of the goal | `PRD.md` (the brief): goal, audience, format, message, facts with sources |
| Inconsistent look | `STYLE.md`: palette (measured hex values), type, motion, sound, characters, do and don't |
| Ignored references | `REFERENCES.md`: every file and link with an ID, what it shows, what to take from it, where it was used |
| Misread screenshots | A rule to write what is seen, then what is inferred, and to measure instead of estimating; ask when it matters |
| Work built on unapproved designs | Approval gates: brief, style frames, character sheets, animatic, final |
| Shallow research | A researcher agent that reads the actual files and writes a cited note |
| Low-effort characters | A character-design skill: options side by side, turnaround, expressions, mouth shapes, poses, rig, and an originality rule |
| Long runs | A producer agent that hands one shot at a time to builders and reviewers and stops at every gate |
| Missing craft knowledge | Skills for content basics (hook, pacing, safe zones, captions, loudness), motion (the 12 principles, easing), and design (hierarchy, type, color, contrast) |

## How a project runs
1. Setup writes the brief, style guide, and reference list with you.
2. The producer plans the next gate: storyboard, style frames, character sheets, animatic, shots, final.
3. An asset-builder makes one piece; a visual-reviewer grabs the frames and checks them against the brief, style, script, and references.
4. At each approval gate the producer shows you the frames or sheets and waits for your yes.

You can also skip the producer and talk to Claude as usual; the rules in `CLAUDE.md` still apply. The reasons for each rule are in `templates/DECISIONS.md` (C-01 to C-09).

## Two setup paths
| Skill | Use when | What it does |
|---|---|---|
| `/content-project-workflow:adopt` | The project already has a script, recordings, assets, renders, or its own Claude Code setup | Surveys read-only, inventories every reference, keeps or drafts the brief and style from what exists, merges existing rules, never overwrites originals |
| `/content-project-workflow:bootstrap` | New or empty folder | Interviews you, writes the first brief, style guide, and reference list, no production yet |

Both explain the defaults below, ask which to change, smoke-test the tools, and end with a plain-language report. Nothing is committed unless you ask. During setup the skill copies its material into a temporary `.workflow-setup/` folder in the project and deletes it at the end.

## Install
```
claude plugin marketplace add Nazhra05/Super-set
claude plugin install content-project-workflow@super-set
```
Or inside a Claude Code session: `/plugin marketplace add Nazhra05/Super-set`, then `/plugin install content-project-workflow@super-set`. Then open Claude Code in the project (terminal or desktop app) and run one of the two skills. After setup the project is self-contained.

The plugin works with any video or design tool. Setup asks which one you use and recommends its official agent skills (for example HyperFrames or Remotion); you install those yourself.

## Daily use
- **Terminal:** `claude --agent producer --model <producer model> --effort high` from the project root.
- **Desktop app:** producer mode is a few keys in `.claude/settings.local.json`; the project's `WORKFLOW.md` has the exact block.

The producer works through the gates and tickets in `TODO.md`, stops at every gate for your approval, and sends heavy work (building assets, reviewing frames, research) to subagents so its own turns stay short.

## Opinionated defaults (and how to change them)
| Default | Why | Where to change |
|---|---|---|
| Discussion first: a question gets an answer, not file changes | Prevents unasked edits | `CLAUDE.md` rule 1 |
| Look before you interpret: for every image, say what is seen, then what is inferred; measure instead of estimating; ask when it matters | Image reading is weak at exact positions and sizes, and feedback screenshots were misread | `CLAUDE.md` rule 5, C-01 |
| "Done" needs fresh evidence: the project check passes and the frames were looked at; not watched with sound means say so | Claims of "done" without looking | `CLAUDE.md` rule 6, C-02 |
| Approval gates: brief, style frames, character sheets, animatic, final | Costly work started on unapproved designs | `WORKFLOW.md`, C-03 |
| Every reference is listed and accounted for | References were ignored | `REFERENCES.md`, C-04 |
| Research reads the source and writes a cited note | A repository "check" read only a summary of its front page | `WORKFLOW.md` "Research", C-05 |
| Short turns: one ticket per dispatch, stop at gates, heavy work in subagents | Hour-long turns filled the context | `WORKFLOW.md`, C-06 |
| Design effort: options side by side against the references, character sheets before animation, no copying an existing character or brand mascot without asking | Low-effort, derivative characters | skill `character-design`, C-07 |
| Facts and dialogue on screen come only from the script or a named source; changing dialogue needs approval | Invented numbers and text that does not match the recording | `CLAUDE.md` rule 4 |
| Originals (script, recordings, source art) are never overwritten without approval | They cannot be recreated | `WORKFLOW.md` "Still needs owner approval" |
| Documents in English or Bahasa Indonesia (chosen at setup); code and commits English; common terms stay in one form | Readable docs, no mixed terms | `CLAUDE.md` rule 9, "Terms" |
| Models: producer, asset-builder, and visual-reviewer `opus`; researcher `sonnet`; Explore `haiku` | Design and visual judgement need the strongest model | `model:` line in `.claude/agents/*.md` |

To override a C-xx decision in a project, add a project decision (D-xx) in `DECISIONS.md` with the reason, then change the file.

## What lands in the project
- Docs: `CLAUDE.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `PRD.md` (brief), `STYLE.md`, `REFERENCES.md`, `tickets/_TEMPLATE.md`, in English or Indonesian.
- `.claude/agents/`: producer, asset-builder, visual-reviewer, researcher, Explore.
- `.claude/skills/`: `content-fundamentals`, `motion-principles`, `design-basics`, `character-design`, `verification-before-completion`, `systematic-debugging`.
- `.claude/settings.json`: Read deny for `.env` files, status line.
- `tools/`: `scope.sh` (files changed outside a ticket's Allow list, needs git), `verify.sh` (runs a ticket's checks), `statusline.js`.

## Requirements
- Node.js (status line) and Bash (Git Bash on Windows).
- Git is recommended; without it the scope check does not run.
- Frame grabs usually need `ffmpeg` or the video tool's snapshot command.

## Layout of this plugin
In the Super-set repository this plugin lives in `plugins/content-project-workflow/`.
```
.claude-plugin/   plugin.json
skills/           adopt, bootstrap
reference/        setup-interview.md, brief-and-style.md, install-steps.md
scripts/          stage.sh (copies setup material into the project)
templates/        everything copied into a project (English docs)
templates/id/     the docs in Indonesian, same structure
```

## License
MIT, see `LICENSE`. `verification-before-completion` and `systematic-debugging` are adapted from [obra/superpowers](https://github.com/obra/superpowers) (MIT); attribution and changes are in `templates/.claude/skills/NOTICE`.
