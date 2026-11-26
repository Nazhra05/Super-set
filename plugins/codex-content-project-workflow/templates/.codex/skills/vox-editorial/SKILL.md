---
name: vox-editorial
description: Use when the project's style preset is "Vox editorial collage" - paper-collage explainers with printed photo cut-outs, documents with highlighter, stamps, hand annotations, and caption karaoke, built in HyperFrames with GSAP. Read before storyboard, style frame, animatic, and shot tickets; ships vox-kit.js (tested helpers).
---

# Vox editorial collage

The look of Vox-style explainers: a physical paper world filmed by a camera that never stops, where every claim is shown with a document, a number, or a real object, and something is drawn on every shot. `STYLE.md` of the project always wins over this file; this file is the default the style frames start from.

## 1. The look
- **A paper world.** Cream or kraft paper ground, printed textures, torn strips. Three layers in every frame: the printed world (background), torn paper strips (middle), the subject (front). Never a dark void with small floating objects.
- **One saturated accent per frame.** Everything else cream, charcoal, or flat muted tones. A second saturated color only for a payoff, and small.
- **Printed photos, not screen images.** Photos are cut out, printed (grayscale or duotone, clean fine halftone; coarse dots turn dark photos to mud), with a torn white paper edge, a soft drop shadow, and a tilted color block behind them.
- **Something drawn on every shot:** highlighter on a document, a strike-through, a circle, an arrow that draws itself, a stamp, a handwritten note.
- **Documents and data inside the scene**, not floating cards: the number sits on the paper, the source line sits under it.

## 2. Two clocks
- **Collage clock, on twos:** paper, cut-outs, stamps, strips, and type move at 12 poses per second (`Vox.onTwos`). Paper boils (a small wobble, `Vox.boil`) while it holds.
- **Camera clock, smooth:** the camera wrapper moves every frame (`Vox.cameraPush`, 2 to 5% per about 5 seconds, stopping only at a cut).
- **Photos of people never boil.** The paper around them does.

## 3. Type
- One typeface per text element. Variation comes from color chips and angle, not from mixing fonts in one element.
- Two voices in one line: plain words in a heavy grotesque, all caps; one or two key words in an italic serif, lower case, accent color.
- Elements that appear later start hidden **outside** the timeline (CSS `visibility: hidden` or `gsap.set` before the timeline): a zero-duration `tl.set` at position 0 does not render at frame 0 (`check`: `gsap_timeline_set_initial_hide`).
- Text never flies in. It types, is stamped word by word on the spoken syllable (`Vox.wordsOn` with times from `window.TIMING`), or jumps between two or three poses.
- **Overshoot is for objects only** (`Vox.slap`), never for text.
- Display type looks printed: the ink filter (`url(#vox-ink)`, re-seeded by `Vox.inkReseed`) roughens its edges.
- Headlines: 4 to 9% of frame height, one or two lines; a stacked headline is one paper strip per phrase, each landing on the first word of its phrase.
- Fonts are bundled with `@font-face` (HyperFrames replaces system fonts); use fonts with an open license (OFL, Apache) and record them in `REFERENCES.md`.

## 4. Layout for 9:16
- **Text lives between 15% and 65% of the height** (y 288 to 1248 px on 1080x1920) and away from the side edges. These are the clear bands `hyperframes check` measures (`outside_safe_zone`): Instagram Reels y 14 to 65%, x 6 to 94%; YouTube Shorts y 15 to 65%; TikTok also narrows the lower right. The bottom third belongs to the platform's buttons and caption bar, so captions sit just above the 65% line, not at the bottom.
- Pictures may run to the edges and past them; only text and faces must stay inside.
- A camera push crops the edges: check the **last** frame of every shot, not only the first.
- One idea per frame, one focal point. No three cards in a row, no bullet slides, no side-by-side panels instead of a scene.

## 5. Rhythm
- Average shot 2 to 3 seconds, with motion inside it. A treatment goes stale after about 6 seconds: change the world (background, scale, light) per beat, and never show the same background twice in a row.
- In a busy beat, one new element about every half second. Hold 0.3 to 0.75 seconds before a payoff.
- The screen does not repeat the voice-over word for word. On-screen text is a number, a term, a label, or a document quote; the caption carries the transcript.

## 6. Transitions
- 3 to 5 kinds per film, each with a reason: hard cut between arguments; whip pan with motion blur (`Vox.whip`) to change world; object becomes the world (an element grows past the frame and its texture is the next background); carry across (a result shrinks and lands in the next world). Dissolve only between two states of the same layout.

## 7. Metaphors and visual concepts
- Decide one visual concept per script line at the storyboard gate, and write for each: the claim, the evidence shown, and why this image. The owner approves them in the animatic.
- **Never translate figurative language literally.** A line that says the numbers "mirror" reality does not get a mirror; a line about decent work does not get a thermometer. Show the evidence (a document, a chart, a photo of the situation) instead of a symbol for the word.
- Prefer real objects and documents over icons; a pictogram grid is fine for counts.

## 8. People and characters
- Vox-style films show people as **licensed photo cut-outs**, not drawn characters, and do not animate faces. People speak through the voice-over and captions.
- If the brief needs drawn characters: their art comes from a human artist, an owned asset, or a licensed asset (`character-design`, "Where character art comes from"). Give them the paper treatment (torn edge, shadow, color block); their bodies do not boil, the paper behind them does. Mouth swaps use `Vox.mouth` with the tracks from `tools/audio/timing.py`.
- Real, named people: only photos with a license that allows the use, credited. Generated illustrations are labeled "illustration" on screen.

## 9. Captions and timing
- The owner supplies the script and the recorded voice-over; nothing is generated. `tools/audio/timing.py` turns them into `window.TIMING` (words, lines, mouth tracks).
- Caption karaoke with `Vox.captions`: groups of 3 to 5 words, broken at punctuation and pauses, one group on screen at a time, the spoken word highlighted. White or cream text with a dark outline, heavy grotesque, centered just above the 65% line (section 4).
- Visual beats land on the word that names them (the stamp on the verdict, the highlighter ending on the stressed word).

## 10. Sound
- Few effects, each with a cause on screen: paper slide, stamp hit, pen scratch, a whoosh only on a whip. The hit lands one frame after the image. Vary repeated effects; the same whoosh on every cut is the clearest sign of a template.
- Loudness: master with `tools/audio/master_audio.py` (-14 LUFS, true peak -3 dBTP), confirm with `tools/audio/delivery_check.py`.
- Sound and music only from sources whose license allows it (CC0, MIT, CC BY with credit), each in `REFERENCES.md`.

## 11. Using vox-kit.js
Copy `.codex/skills/vox-editorial/vox-kit.js` next to the composition's scripts (into the folder the ticket's Allow names) and load it after GSAP. In the composition script:

```js
Vox.installFilters(document.getElementById("root"));      // once per composition
const tl = gsap.timeline({ paused: true });
Vox.cameraPush(tl, "#cam", 0, 4.4, 0.04);                  // smooth camera on the shot wrapper
Vox.boil(tl, document.getElementById("paper"), 0, 6);       // wrapper with class "vox-boil"
Vox.inkReseed(tl, 0, 6);                                    // display type uses filter: url(#vox-ink)
Vox.highlight(tl, "#band", wordEnd, 12);                    // band ends on the stressed word
Vox.slap(tl, "#stamp", verdictTime);                        // objects only
Vox.whip(tl, "#strip", 4.5, 1080);                          // panels side by side in one strip
Vox.captions(tl, document.getElementById("caps"), words);   // words from window.TIMING
```
CSS the kit expects:
- Boil wrapper: `position: absolute; inset: 0;` (a wrapper with no size makes `check` report its children as escaped) plus `.vox-boil { transform: translate(var(--bx, 0px), var(--by, 0px)) rotate(var(--br, 0deg)); }`; GSAP never moves the same element.
- Cut-outs: `filter: url(#vox-torn) drop-shadow(0 14px 18px rgba(0, 0, 0, .42));` with a tilted color block behind them.
- Highlighter: the band sits **behind** the words (band `z-index: 0`, words `position: relative; z-index: 1`) with `mix-blend-mode: multiply`; a band on top of the words is a `text_occluded` error in `check`. Start it hidden (`visibility: hidden`).
- Captions: `.vox-cap` lines positioned absolutely in one box above the 65% line; style the spoken word with `span[data-on="1"]`. `Vox.captions` merges groups shorter than the reading floor (0.5 s + 0.3 s a word) so `check` does not report `line_unread`. In a sub-composition the filter ids are shared with the page: pass `{ prefix: "s1" }` to `installFilters` and to the helpers that take it, and use `url(#s1-torn)`.

Tested on Windows with HyperFrames `latest` (version in the plugin's CHANGELOG): `hyperframes check` passed with 0 errors on a test composition using every helper; snapshots were identical between two HyperFrames versions; the ink filter changes between seed steps and is identical within one step; the whip blur peaks mid-move and is removed after landing.

## 12. Review checklist (visual-reviewer)
For each shot frame: paper world with three layers; one saturated accent; something drawn; photos printed with torn edge and shadow; no text overshoot or fly-in; headline and captions inside the 9:16 safe areas on the first **and last** frame; on-screen text is not the voice-over repeated; the visual concept matches the one approved in the animatic and is not a literal metaphor; sources and licenses of every photo, font, and sound are in `REFERENCES.md`.

## Sources
Rewritten as techniques and numbers; no code or assets copied. All MIT licensed:
- basharmokdad/papercut (github.com/basharmokdad/papercut): ease quantized to twos, paper boil through CSS variables, printed-ink filter re-seeded in steps, whip pan with an SVG blur, three layers, two type voices, stacked headline strips.
- SousekiL/vox-style-video (github.com/SousekiL/vox-style-video): two clocks, photos never boil, one saturated accent, overshoot only for objects, torn sticker edge filter, highlighter blend and duration, 9:16 layout margins, check the last frame.
- harshpuri84/vox-explainer-kit (github.com/harshpuri84/vox-explainer-kit): tilted color block behind a cut-out.
- CK42BB/vox-explainer-skill (github.com/CK42BB/vox-explainer-skill): caption style, component list.
- HyperFrames documentation (github.com/heygen-com/hyperframes): shot rhythm, transition kinds, caption grouping.
- Lessons from a real 9:16 explainer made with this workflow: literal metaphors rejected by the owner, drawn characters made from scratch by an agent rejected.
