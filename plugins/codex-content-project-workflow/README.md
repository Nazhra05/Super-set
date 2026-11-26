# Content Project Workflow (OpenAI Codex)

**Run your video or animation project with OpenAI Codex like a small studio.** This plugin sets up a project so Codex follows a brief and a style guide, uses every reference you give it, shows you designs for approval before building on them, checks its own frames instead of guessing, and keeps each step short.

Part of the [Super-set](../../README.md) repository.

## Is it for you?
Use it if you make explainer videos, social reels, animations, or motion graphics with OpenAI Codex (for example with HyperFrames or Remotion), and you have seen things like:
- The agent reading your screenshot wrong and "fixing" the wrong thing.
- Characters or designs made with little care, or copied from an existing mascot.
- References you supplied being ignored, or "I checked that repository" with nothing to show.
- One request turning into an hour-long run that fills the context.
- Missing basics: a weak hook, text under the app buttons, captions that do not match the voice-over.

**When not to use it:** a single graphic or a one-off clip with no script (the gates are more process than you need), or software projects (use `codex-app-project-workflow`).

## What it does for you
| Problem | What the plugin sets up |
|---|---|
| No shared picture of the goal | `PRD.md` (the brief): goal, audience, format, message, facts with sources |
| Inconsistent look | `STYLE.md`: palette (measured hex values), type, motion, sound, characters, do and don't |
| Ignored references | `REFERENCES.md`: every file and link with an ID, what it shows, what to take from it, where it was used |
| Misread screenshots | A rule in `AGENTS.md` to write what is seen, then what is inferred, and to measure instead of estimating; ask when it matters |
| Work built on unapproved designs | Approval gates: brief, style frames, character sheets, animatic, final |
| Shallow research | A `researcher` role prompt that reads the actual files and writes a cited note |
| Low-effort characters | A `character-design` skill: options side by side, turnaround, expressions, mouth shapes, poses, rig, and an originality rule |
| Long runs | A `producer` skill that hands one shot at a time to builders and reviewers via `codex exec` and stops at every gate |
| Missing craft knowledge | Skills for content basics (hook, pacing, safe zones, captions, loudness), motion (the 12 principles, easing), and design (hierarchy, type, color, contrast) |
| Agent-drawn characters that never look right | A rule on where character art comes from (a human artist painting to the agent's rig spec, an owned or licensed asset, or photo cut-outs) and a ticket budget for hard parts such as hands |
| Finished film rejected for reasons a rough cut would have shown | Delegation never skips the animatic or the new vertical-slice gate; motion is shown as clips with sound |
| A specific look you want without designing it from zero | Optional **Vox editorial collage** preset: a style skill plus `vox-kit.js`, tested HyperFrames + GSAP helpers (paper boil on twos, torn sticker edges, printed ink, highlighter, stamps, whip pans, caption karaoke) |
| Tools missing halfway through | A tools check at the end of setup that lists what production needs, with the install command for your OS, and installs what you select |
| Captions and lip sync that drift from the voice-over | An audio kit: word timing from your own recording and script, mouth tracks, loudness mastering, and a delivery check before upload |

## How a project runs
1. Setup asks for a style preset (none, or Vox editorial collage), writes the brief, style guide, and reference list with you, then checks and offers to install the production tools.
2. The producer plans the next gate: storyboard, style frames, character sheets, animatic, vertical slice, shots, final.
3. An `asset-builder` makes one piece; a `visual-reviewer` grabs the frames and checks them against the brief, style, script, and references.
4. At each approval gate the producer shows you the frames or sheets and waits for your yes.

You can also skip the producer and talk to Codex as usual; the rules in `AGENTS.md` still apply automatically.

## Setup
| Skill | Use when | What it does |
|---|---|---|
| `codex-content-adopt` | The project already has a script, recordings, assets, renders, or its own agent setup | Reads everything first, lists every reference, keeps or drafts the brief and style from what exists, merges existing rules, never overwrites originals |
| `codex-content-bootstrap` | New or empty folder | Interviews you with concise numbered multiple-choice questions, writes the first brief, style guide, and reference list; no production yet |

Both start with the style preset, explain the defaults below and ask which to change, show the list of files before writing, smoke-test the tools, run the tools check and install only what you select, and end with a plain-language report. Nothing is committed unless you ask.

### Style preset: Vox editorial collage
Pick it as the first answer of the setup. It recommends HyperFrames (always the `latest` stable release, never pinned), installs the `vox-editorial` skill with `vox-kit.js`, seeds `STYLE.md` with the preset's defaults (to confirm at the style-frame gate), installs the audio kit, and marks HyperFrames, its official skills, ffmpeg, agent-browser, and Python as required in the tools check. Your script and your recorded voice-over are the input; the plugin generates no speech or text.

### Installing the setup skills in Codex
Copy the two setup skill folders (`skills/codex-content-adopt` and `skills/codex-content-bootstrap`) into `~/.codex/skills/`, and set `CODEX_CONTENT_WORKFLOW_ROOT` to the absolute path of `Super-set/plugins/codex-content-project-workflow` (or run `bash "<path-to>/Super-set/plugins/codex-content-project-workflow/scripts/stage.sh" .` in your project folder before invoking the skill). After setup the project is self-contained, so removing the setup skills later does not break the project.

## Daily use
The flow is identical in the OpenAI Codex CLI (`codex`) and the Codex desktop/IDE experience:
- Invoke the **`producer`** skill (`$producer` or ask Codex to "start the producer session and work through `TODO.md`").
- The producer works through the gates and tickets in `TODO.md`, stops at every approval gate, and sends heavy work (building assets, reviewing frames, research) to isolated `codex exec` runs so its own turns stay short.

## Cost and model tiers
- During work: the `producer`, `asset-builder`, and `visual-reviewer` default to `gpt-5-codex`, because design and visual judgement are where lighter settings fail; `frame-prep`, `researcher`, and `Explore` use `codex-mini-latest`. Images cost many tokens, so `frame-prep` extracts frames and contact sheets first and the producer only opens images at approval gates. On a plan with tight quota limits, setup can set the `asset-builder` to `codex-mini-latest` for routine tickets.

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
| Character art from a human artist, an owned or licensed asset, or photo cut-outs; hard parts get a ticket budget | Agent-drawn characters rejected after many rounds | skill `character-design`, C-10 |
| Delegation never skips the animatic, the vertical slice, or the final | Literal metaphors found only after the full render | `WORKFLOW.md`, C-11 |
| Software is installed only after you say yes, in one question at the end of setup | Installs are machine-wide | `reference/tools.md` |

## What lands in the project
- Docs: `AGENTS.md`, `WORKFLOW.md`, `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `PRD.md` (brief), `STYLE.md`, `REFERENCES.md`, `tickets/_TEMPLATE.md`, in English or Indonesian.
- `.codex/agents/`: `frame-prep.md`, `asset-builder.md`, `visual-reviewer.md`, `researcher.md`, `Explore.md`.
- `.codex/skills/`: `producer`, `content-fundamentals`, `motion-principles`, `design-basics`, `character-design`, `verification-before-completion`, `systematic-debugging`.
- `tools/`: `scope.sh` (files changed outside a ticket's Allow list; needs git), `verify.sh` (runs a ticket's checks), `tools-check.sh` (which production tools are installed, with install commands).
- With the Vox preset or a recorded voice-over: `tools/audio/` (`timing.py`, `master_audio.py`, `delivery_check.py`); with the Vox preset: `.codex/skills/vox-editorial/` (`SKILL.md`, `vox-kit.js`).

## Requirements
- OpenAI Codex CLI (`codex`) and Bash (Git Bash on Windows).
- Git is recommended; without it the scope check does not run.
- The rest is checked at the end of setup by `tools/tools-check.sh` and installed only if you select it: ffmpeg, HyperFrames (Node.js 22+), its official skills, agent-browser, Python 3.9+ with `faster-whisper` for the audio kit, gh, yt-dlp. With the Vox preset the production tools are required.

## Layout of this plugin
```
plugin.json       Plugin manifest
skills/           codex-content-adopt, codex-content-bootstrap
reference/        style-presets.md, setup-interview.md, brief-and-style.md, install-steps.md, tools.md
scripts/          stage.sh (copies setup material into the project during setup)
templates/        everything copied into a project (English docs, tools, audio kit, skills)
templates/id/     the docs in Indonesian
```

## License
MIT, see `LICENSE`. `verification-before-completion` and `systematic-debugging` are adapted from [obra/superpowers](https://github.com/obra/superpowers) (MIT); attribution and changes are in `templates/.codex/skills/NOTICE`. The knowledge skills list their sources inside each skill.
