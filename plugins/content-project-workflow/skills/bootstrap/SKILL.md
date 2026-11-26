---
name: bootstrap
description: Set up the Content Project Workflow (producer, asset-builder, visual-reviewer, researcher, Explore agents, approval gates, brief, art direction, reference inventory) in a new or empty folder for a video, motion graphics, or other content project. Starts with the style preset (none or Vox editorial collage), interviews the owner, writes the first brief and style guide, smoke-tests the tools, then offers to install the production tools.
disable-model-invocation: true
allowed-tools:
  - Bash(bash "${CLAUDE_PLUGIN_ROOT}/scripts/stage.sh" *)
---

# Bootstrap the content workflow in a new or empty folder

Setup material lives in the plugin folder, outside the project. Copy it into the project once with `bash "${CLAUDE_PLUGIN_ROOT}/scripts/stage.sh" .` (run from the project root, at the step named below). It creates `.workflow-setup/` with `templates/`, `reference/`, and `README.md`; read everything from there. Delete `.workflow-setup/` at the end of the setup, also when the setup stops early.

Rules for this whole skill:
- Reply in the owner's language. Documents go into the project in the document language chosen in the interview (English or Indonesian); code, identifiers, comments, and commits are always English.
- Never guess. Ask for anything the owner has not said. A recommendation is offered as the first option, marked "(Recommended)".
- Do not build scenes, characters, or assets. Software is installed only in the tools step of the install (`tools.md`), after the owner says yes. Production is the first tickets.
- Before claiming any step done, run the command and quote its output (`verification-before-completion`).

## 1. Check the folder
Confirm the project root with the owner. List what is there (`ls -la`). If it already has scripts, assets, renders, a framework project, or a `CLAUDE.md`, stop and suggest `/content-project-workflow:adopt` instead.

## 2. Stage the setup material
Run the stage script (see the top of this skill).

## 3. Style preset
Follow `.workflow-setup/reference/style-presets.md`: ask the preset question first (no preset, or Vox editorial collage). Its answer sets the defaults of the interview and of the tools step.

## 4. Interview
Follow `.workflow-setup/reference/setup-interview.md`. Ask what the content is, for whom, on which platform, and the first outcome that matters, then the rest of the table there. Tools that are not installed yet are written as "Not set up yet" until the tools step, never invented.

## 5. Brief, art direction, references
Follow `.workflow-setup/reference/brief-and-style.md`, section "Bootstrap": the brief (`PRD.md`), the first `STYLE.md` (seeded by the preset when it is not `none`), and `REFERENCES.md` from what the owner hands over. Every reference the owner names gets an ID.

## 6. Repo
Recommend `git init` (reversible; mention it): the scope check needs git. Ask which large or generated folders to ignore (renders, caches); never ignore original assets without asking. If the owner declines git, say that `tools/scope.sh` will not run.

## 7. Install and tools
Follow `.workflow-setup/reference/install-steps.md` in full, including its tools step (`tools.md`: run `tools/tools-check.sh` with the preset, ask once which missing tools to install, with the preset `vox` the required ones recommended and pre-marked, install what the owner chose, re-check, record). In a new project the file list is all `new`. Fill the docs for this project:
- `TODO.md`: the gates table, and the first tickets agreed with the owner (for example "set up the video tool", "script to JSON for the audio kit", "style frames for scene 1"), status `Proposed` unless the owner says `Ready`. A ticket that builds a deliverable names its requirement ID and its reference IDs.
- `DECISIONS.md`: section B with the decisions made in the interview (the first is the style preset), each with date and reason; section C with what is still open.
- `HANDOFF.md`: current state and the next step.
- `CLAUDE.md` pitfalls: "None yet."

## 8. Report
In the owner's language, plain words: the preset, what was created, the brief's open questions, the references and what each is for, the smoke test output (or why parts were skipped), the tools check before and after, what is waiting for the owner, the first ticket, and how to start the producer.
