# Changelog

## 0.3.0 (2026-11-26)
- **Style preset, asked first in `adopt` and `bootstrap`:** "No preset" or "Vox editorial collage". The Vox preset installs the `vox-editorial` skill (look, two clocks, type, 9:16 layout with the clear bands `hyperframes check` measures, rhythm, transitions, no literal metaphors, people as licensed photo cut-outs, captions, sound, review checklist) and `vox-kit.js`, a tested set of deterministic GSAP helpers: ease on twos, paper boil, torn sticker edge, printed-ink filter, object pop, highlighter, whip pan with blur, camera push, words on the spoken syllable, caption karaoke, mouth swaps. Tested with HyperFrames 0.9.97 (`check` passed with 0 errors on a composition using every helper; snapshots identical to 0.9.28). Techniques learned from MIT-licensed projects, credited in the skill and `NOTICE`; no code copied.
- **Tools step at the end of setup:** `tools/tools-check.sh` reports git, Node.js 22+, ffmpeg, HyperFrames (`latest` npm tag, never pinned), the official HyperFrames skills, agent-browser, Python, the audio venv, gh, and yt-dlp, with the install command for Windows (winget), macOS (brew), and Linux (apt, dnf). The agent asks once and installs what the owner selects; with the Vox preset the production tools are required and recommended. `sudo` commands are printed for the owner, never run.
- **Audio kit** (`tools/audio/`), from the owner's own script and recorded voice-over, nothing generated: `timing.py` (faster-whisper word times aligned to the script, edges snapped to the audible speech, per-speaker mouth tracks, `window.TIMING`), `master_audio.py` (loudnorm plus an oversampled true-peak limiter, corrected until -14 LUFS and the true-peak target hold), `delivery_check.py` (codec, pixel format, size, frame rate, audio, loudness, true peak, faststart; one PASS or FAIL per item).
- **Lessons from a full production run:** C-10 character art comes from a human artist, an owned or licensed asset, or photo cut-outs, with a ticket budget for hard body parts (skill `character-design`); C-11 delegation never skips the animatic, the new **Vertical slice** gate, or the final, and motion is shown as clips with sound; Report and research-note skeletons within the first 3 tool calls; light mode for slow machines; lean documents (overwritten `HANDOFF.md`, archived Done log and superseded decisions).

## 0.2.0 (2026-11-14)
- Token efficiency for the producer and visual-reviewer: added lightweight `frame-prep` subagent (`haiku` default) and `tools/verify.sh --with-scope` to run scope/verify checks, extract review frames and downscaled contact sheets into `.review/`, and measure pixel hex/audio before `visual-reviewer` runs; the producer opens frames only at approval gates and asks for `/compact` at every gate boundary.
- Owner replies and Terms: concise 8-to-10-line summary format (Done, Next / Gate, Needs your decision) that always writes `<ID> (<short title>)` instead of bare IDs; expanded `## Terms` in `CLAUDE.md` so standard motion graphics, video, graphic design, and software terms stay in English when replying in another language.

## 0.1.2 (2026-11-11)
- README: what it looks like (example output from a test setup), when not to use it, cost, and status. No change in behaviour.

## 0.1.1 (2026-11-11)
- README and plugin description rewritten for new users: who it is for, the problems it solves, and how a project runs. No change in behaviour.

## 0.1.0 (2026-11-11)
- First version: adopt and bootstrap skills; brief (`PRD.md`), `STYLE.md`, and `REFERENCES.md`; approval gates; producer, asset-builder, visual-reviewer, researcher, and Explore agents; knowledge skills `content-fundamentals`, `motion-principles`, `design-basics`, `character-design`; `tools/scope.sh`, `tools/verify.sh`, `tools/statusline.js`; English and Indonesian docs.
