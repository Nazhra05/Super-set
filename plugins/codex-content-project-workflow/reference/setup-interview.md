# Setup interview

Shared by the `codex-content-adopt` and `codex-content-bootstrap` skills. Ask at most 4 numbered questions per turn. Never guess an answer: when the owner has not given it and it cannot be read from the project, ask. In `adopt`, propose answers found in the project as the first option, prefixed with `(Recommended)`, so the owner only confirms.

Reply to the owner in the language they write in. Documents are written in the document language chosen below; code, identifiers, comments, and commits are always English.

Start by explaining the defaults in `.workflow-setup/README.md`, section "Opinionated defaults (and how to change them)", in the owner's language and in plain words, then ask which ones to change. Record each change as a project decision (D-xx) in `DECISIONS.md` with the reason, and apply it to the files named in that table.

## Answers to collect, and the placeholder each one fills

| Placeholder | Question | Notes |
|---|---|---|
| `{{PROJECT_NAME}}` | Project name | Short name used in docs and agent prompts. |
| `{{PROJECT_ROOT}}`, `{{PROJECT_ROOT_FWD}}` | Project root | Absolute path; `_FWD` is the same path with forward slashes. Confirm the current directory with the owner. |
| `{{PROJECT_SUMMARY}}` | What the content is, for whom, on which platform, and why | Two to four sentences. |
| `{{OWNER_ROLE}}` | Who the owner is | For example "single creator", "small studio lead". |
| `{{OWNER_LANGUAGE}}` | Language for replies to the owner | Default: the language the owner writes in. |
| (no placeholder) | Document language: English or Bahasa Indonesia | Recommended default: Bahasa Indonesia when the owner writes in Indonesian, otherwise English. Decides the source of the core docs in `install-steps.md` step 1. Agent prompts, skills, and tools stay English in both. |
| `{{PROJECT_TERMS}}` | Project terms that stay in one form (for example "link", not "tautan"; names of characters, segments, brand words) | Asked when replies or documents are not in English, and always for character and brand names. Rows `\| use \| do not mix with \|`. None: one row `\| None yet. \| \|`. |
| `{{FOLDER_TABLE}}` | What lives where: script, recordings, original art, references, the video tool project, renders | Rows `\| part \| path \|`. Mark originals; they are protected (see `{{IRREVERSIBLE_ACTIONS}}`). |
| `{{TOOLCHAIN}}` | The video or design tool and its version (for example HyperFrames, Remotion, After Effects, Figma) | Ask; never pick for the owner. "Not decided" goes to `DECISIONS.md` section C. |
| `{{TOOL_SKILLS}}` | Official agent skills for that tool | Offer what the tool documents (for example HyperFrames: `npx skills add heygen-com/hyperframes`; Remotion: its Agent Skills). Installing them is the owner's step; write the command, do not run it. "None" is a valid answer. |
| `{{COMMANDS}}` | Check, preview, render, frame-grab, audio-measure commands | Run each once before writing it down; write only the ones that ran, with the date. A preview the owner runs is written as "run by the owner". |
| `{{DEFAULT_VERIFY}}` | Default `verify` block for tickets | Usually the project check command plus a frame grab of the shot. |
| `{{FRAME_COMMAND}}` | How to grab a frame at a given time from a render or preview | For example an `ffmpeg -ss <t> -i <file> -frames:v 1 <out>.png` line or the tool's snapshot command. "Not set up yet" is allowed. |
| `{{IRREVERSIBLE_ACTIONS}}` | Actions that always need approval in this project | Always included: overwriting or deleting originals (script, recordings, source art), publishing or uploading, paid services. Ask what else (for example sending material to an external AI service). |
| `{{SESSION_REPORT_DIR}}` | Folder for producer session reports | Default `docs/sessions` inside the project. |
| `{{PRODUCER_MODEL}}`, `{{BUILDER_MODEL}}`, `{{REVIEWER_MODEL}}`, `{{RESEARCHER_MODEL}}`, `{{EXPLORE_MODEL}}` | Model per role | Offer the defaults below with the recommendation, then ask whether to change any. |
| `{{EXTRA_DOCS}}` | Other project documents to list in the document map | `adopt`: existing docs found. `bootstrap`: usually none. |
| `{{PITFALLS}}` | Proven pitfalls | Only facts proven by command output. Empty list: "None yet." |
| `{{SETUP_DATE}}` | Today's date | ISO format. |
| (no placeholder) | Where the owner works: Codex CLI, Codex desktop app / IDE extension, or several | All surfaces use the same files and the same flow (`producer` skill). |

The remaining placeholders (`{{CURRENT_STATE}}`, `{{NEXT_STEP}}`, `{{WAITING_OWNER}}`, `{{GATES}}`, `{{EXECUTION_ORDER}}`, `{{TASKS}}`, `{{INBOX}}`, `{{PROJECT_DECISIONS}}`, `{{WAITING_DECISIONS}}`) are filled by the skill from what it found and agreed with the owner. When there is nothing, write "None yet." rather than inventing content. The `{{PRD_*}}`, `{{STYLE_*}}`, and `{{REFERENCE_ROWS}}` placeholders are filled as described in `brief-and-style.md`.

## Model defaults and recommendation

Show this table, explain it in one or two sentences, then ask "Keep the defaults or change a role?". Subagent runs in Codex CLI use `codex exec -m <model> ...`.

| Role | Default | Why |
|---|---|---|
| producer | `gpt-5-codex` (recommended for the main session; ask) | Plans gates, writes briefs, judges what an image shows, talks to the owner. |
| asset-builder | `gpt-5-codex` | Draws characters and builds scenes in code; lower capability here produced flat, unconvincing art in real use. Lower to `codex-mini-latest` for mechanical tasks (renaming layers, timing data). |
| visual-reviewer | `gpt-5-codex` | Reads frames against the storyboard, style, and references; must separate what it sees from what it infers. |
| researcher | `gpt-5-codex` | Clones and reads sources, writes cited notes; follows a fixed procedure. |
| Explore, frame-prep | `codex-mini-latest` | Only locates files/lines (`Explore`) or runs `verify --with-scope` and extracts frames into `.review/` (`frame-prep`). |

On a plan with tight usage limits, `codex-mini-latest` (or `gpt-5-mini`) for the asset-builder on routine tickets is the cheaper option; say so as a trade-off. When a model changes, update the Roles table in `WORKFLOW.md` and the `producer` skill instructions.

