---
name: character-design
description: Use when creating, redesigning, or rigging a character for animation - references, options, turnaround, expression sheet, mouth chart, pose sheet, colors, cut-out rig, and the originality rule. Read before any character ticket.
---

# Character design

A character is designed and approved before it is animated. Skipping the sheet produces characters that change between shots and look unfinished.

## Steps (each is a ticket; the sheet is a gate in `WORKFLOW.md`)
1. **Brief:** role in the story, personality in three words, age range, setting, what the audience must feel. Taken from `PRD.md` and the script, not invented.
2. **References:** list the `REFERENCES.md` IDs that apply (style, clothing, culture, posture) and what to take from each. Ask the owner when none exist; research with the `researcher` if needed.
3. **Options:** 2 or 3 designs that differ in a real way (silhouette, proportions, clothing, color), shown side by side next to the references at the same size. The owner picks or combines.
4. **Turnaround:** front, three-quarter, side, back, all at the same scale on one sheet so proportions line up. This is the on-model reference for every later shot.
5. **Expression sheet:** at least neutral, joy, sadness, anger, surprise, doubt or suspicion, plus the expressions the script needs. Eyes, brows, and mouth carry most of it.
6. **Mouth chart:** the mouth shapes for lip sync, named consistently. A workable minimum: closed (M, B, P), A, I and E, U and O, a half-open shape for other consonants, and a smile or rest shape. Match the shapes to the language of the voice-over.
7. **Pose sheet:** the character's typical postures and gestures from the script (pointing, explaining, listening), full body.
8. **Colors:** hex values per part, sampled or defined, recorded in `STYLE.md`.
9. **Rig plan (cut-out animation):** each moving part on its own layer (head, eyes, brows, mouth set, torso, upper and lower arms, hands, hair parts that sway), a pivot at each joint, consistent layer names, and the mouth set as swappable drawings. Keep the design simple enough to rig; detail goes where the camera looks.
10. **Test:** a short test animation (a blink, a head turn, a line of lip sync) reviewed frame by frame before the character enters a shot.

## Quality bar
- Detail matches the references: line weight, shading layers, texture, proportions. A flat placeholder is not a design.
- The silhouette alone tells who it is.
- Two characters on screen together share scale and style unless the brief says otherwise.
- Drawing in code (SVG, canvas) is allowed, but invest in shapes, shading, and highlights; render it large and compare with the references before showing it.

## Originality rule (C-07)
Never build a new character by recoloring or editing an existing character, mascot, or brand asset unless the owner approved it for this project. Using a reference for style is fine; reusing its drawing is not. Third-party assets need a license check and the owner's approval.

## Common pitfalls in cut-out rigs
- Rotating a part around the canvas corner instead of its joint: set the pivot at the joint.
- Parts that hide the face when they move (hair over brows): check the layer order with extreme poses.
- Expressions that do not match the script line: map each line to an expression before animating.

## Sources
- Character sheets: blog.cg-wire.com/character-sheet-animation; characterhub.com/blog/character-resources/character-design-sheet.
- Expression sheets: 21-draw.com/how-to-make-a-character-design-sheet.
- Cut-out rigs and mouth charts: toonboom.com (designing and rigging the Smilez character); mattwattsart.gumroad.com/l/mouths.
- Turnarounds: binus.ac.id/bandung/dkv/2025/11/04/character-turnarounds-understanding-form-in-2d-space.
