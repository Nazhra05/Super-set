---
name: design-basics
description: Use when laying out frames, slides, thumbnails, or graphics - hierarchy, layout and grid, typography, color, contrast, and consistency with the style guide. Read before style frames and any ticket that places text or graphics.
---

# Design basics

How to make a frame read at a glance. `STYLE.md` holds the project's palette, type, and rules; this file explains how to apply them.

## Hierarchy
- Decide the order the eye should read the frame in: first, second, third. Size, weight, color, and position make that order; use as few as needed.
- One focal point per frame. If everything is bold, nothing is.
- Squint test: blur the frame (or look at a small thumbnail); the most important element must still stand out.

## Layout and grid
- Work on a grid with consistent margins; align edges and baselines to it. Elements that are almost aligned look like mistakes.
- Leave empty space on purpose; crowded frames read slower.
- Respect the safe zones in `content-fundamentals` for vertical video.
- Keep related things close and unrelated things apart (proximity).

## Typography
- One or two typefaces per project, named in `STYLE.md`, bundled as files so the renderer does not substitute them.
- Hierarchy by size and weight, not by many fonts. Keep line length short on vertical video.
- Numbers that matter are the biggest text in their frame; their source sits nearby in small text when the brief requires it.
- Check legibility on a phone at real size.

## Color
- Use the palette in `STYLE.md` by hex value; sample colors from reference files with a script instead of guessing them.
- A common balance is roughly 60% dominant, 30% secondary, 10% accent [common practice, the "60-30-10" guideline]; the accent marks what matters.
- Contrast for text at least 4.5:1, or 3:1 for large text (WCAG 2.x AA); measure it.
- Brand colors that fail contrast with white text (for example many oranges) need dark text, a dark backing, or an outline.

## Consistency
- The same element looks the same everywhere: same type style for captions, same position for sources, same treatment for numbers.
- Style frames set these decisions; later shots follow them. A change goes through `STYLE.md` with the owner's approval.

## Working with references
- Name what you take from each reference (`REFERENCES.md`): layout, palette, type treatment, illustration style, motion. Do not copy a whole reference.
- Show new frames next to the references they answer, at the same size, so the owner can compare.

## Sources
- WCAG 2.2, 1.4.3 Contrast (Minimum): w3.org/TR/WCAG22.
- Robin Williams, *The Non-Designer's Design Book* (contrast, repetition, alignment, proximity).
- 60-30-10 color guideline: common interior and graphic design practice, not a standard.
