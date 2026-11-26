# Style presets

Shared by the `codex-content-adopt` and `codex-content-bootstrap` skills. The preset is the **first question** of the setup, before the interview, because it changes the defaults of the questions that follow and the tools step at the end. Ask it as one numbered question, options in this order:

| Option | Label shown | What it means |
|---|---|---|
| `none` | No preset (Recommended unless the owner asks for a style) | The workflow as before: the owner names the video tool, the style is built from the owner's references at the style-frame gate. |
| `vox` | Vox editorial collage | Paper-collage explainer: printed photo cut-outs, documents with highlighter, stamps, hand annotations, camera always moving, caption karaoke from the owner's recorded voice-over. Built in HyperFrames with GSAP. |

In `adopt`, when the survey found a style already in use, offer it as "(found in project)" text in the question and keep `none` as the safe default; a preset never overwrites an existing `STYLE.md` (it is merged, and conflicts become questions).

Record the answer as a project decision in `DECISIONS.md` (the next free D-xx; D-01 in a new project): "Style preset: <label>", date, reason the owner gave, and fill `{{PRESET_SKILLS}}` in `AGENTS.md`.

## What `none` changes
Nothing beyond the earlier behaviour. `{{PRESET_SKILLS}}` = `None.` The tools step (`tools.md`) still runs; every tool is offered as optional, git and Node.js as required.

## What `vox` changes
1. **Interview defaults** (`setup-interview.md`): `{{TOOLCHAIN}}` is offered as "HyperFrames, latest stable release (npm tag `latest`), HTML + GSAP (Recommended)"; the owner may still pick another tool, in which case say plainly that `vox-kit.js` is written for HTML and GSAP. `{{TOOL_SKILLS}}` is offered as the official HyperFrames skills, installed in the tools step. `{{COMMANDS}}` gets the HyperFrames lines below once they have run.
2. **Skill:** install `.codex/skills/vox-editorial/` (`SKILL.md` and `vox-kit.js`) from `TEMPLATES/.codex/skills/vox-editorial/`. `{{PRESET_SKILLS}}` = `` `vox-editorial` (style preset Vox editorial collage; `vox-kit.js` holds the tested helpers) ``.
3. **Audio kit:** install `tools/audio/` (`timing.py`, `master_audio.py`, `delivery_check.py`, `requirements.txt`). Ask where the script and the voice-over are; the kit only uses what the owner recorded and wrote, it never generates speech or text. When the script is not yet in the JSON form `timing.py` reads (`{"lang", "lines": [{"id", "scene", "speaker", "text"}]}`), make converting it the first ticket, not part of the setup.
4. **`STYLE.md` seed** (each line marked "Preset default, to confirm at the style-frame gate"):
   - Look: paper world in three layers; printed photo cut-outs with torn edge, shadow, tilted color block; something drawn on every shot; documents and data inside the scene (`vox-editorial` sections 1 and 4).
   - Palette: cream ground, charcoal ink, one saturated accent per frame. No hex values are invented: they are chosen with the owner or read from the references, and stay "To be set at the style-frame gate" until then.
   - Type: heavy grotesque in caps plus an italic serif accent; display type with the ink filter; open-license fonts bundled with `@font-face`. Font names stay "To be set" until chosen.
   - Motion: two clocks (collage on twos, smooth camera), overshoot for objects only, text never flies in, 3 to 5 transition kinds (`vox-editorial` sections 2, 3, 6).
   - Sound: few effects with a cause on screen; -14 LUFS, true peak -3 dBTP.
   - Characters: people as licensed photo cut-outs; drawn characters only from a human artist, an owned asset, or a licensed asset (`character-design`).
   - Do / Do not: from `vox-editorial` sections 5 and 7 (no literal metaphors, no repeated voice-over on screen, no three cards in a row).
5. **Gates:** unchanged, with one addition the preset makes concrete: at the animatic gate the owner approves the visual concept of every script line (`vox-editorial` section 7).
6. **Tools step:** `tools.md` runs with `--preset vox`, so HyperFrames, its official skills, ffmpeg, agent-browser, Python, and the audio kit's packages are **required** and offered as "(Recommended)".

## HyperFrames lines for `{{COMMANDS}}` (vox, after they ran once)
Write them with the project's HyperFrames folder and the date they ran. HyperFrames is not pinned: `latest` is the stable npm tag (the others, such as `alpha`, are pre-releases). Record in `AGENTS.md` the version that ran at setup, as information.
- Check: `npx --yes hyperframes@latest check`
- Frames: `npx --yes hyperframes@latest snapshot --at <t1>,<t2> --no-end -o .review/<ID>`
- Render: `npx --yes hyperframes@latest render -o renders/<name>.mp4`
- Preview (run by the owner): `npx --yes hyperframes@latest preview`
- Word timing: `<venv python> tools/audio/timing.py --audio <voice-over> --script <script.json> --out <composition data folder>`
- Mastering: `<venv python> tools/audio/master_audio.py <render> <mastered>`; delivery check: `<venv python> tools/audio/delivery_check.py <mastered>`

If a new `latest` release breaks a check that passed before, record it as a proven pitfall with the two version numbers, and run the previous version explicitly (`hyperframes@<previous>`) until a fixed release is out.
