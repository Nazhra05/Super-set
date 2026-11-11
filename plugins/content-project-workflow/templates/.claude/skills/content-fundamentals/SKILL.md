---
name: content-fundamentals
description: Use when planning or checking short-form video and social content - hook, pacing, captions, safe zones, format, loudness, and accessibility. Read before storyboards, shot tickets, and final checks.
---

# Content fundamentals

Ground rules for short-form video (Reels, Shorts, TikTok) and other social content. Each rule is marked **[platform spec]** (published by the platform), **[standard]** (a published standard), or **[common practice]** (agreed across creator guides, not official). The project's `PRD.md` and `STYLE.md` override this file.

## Before making anything
- One message per piece. Write it in one sentence in `PRD.md` before the storyboard; every shot must serve it.
- Know the viewer: who, what they already know, why they would stop scrolling. Facts on screen come only from the script or a named source.

## Hook and pacing
- **Hook in about the first 2 seconds** [common practice; guides range from 1.5 to 3 s]. Open on the question, the surprising number, or the conflict, not on a logo or title card.
- **Something changes every 2 to 4 seconds** [common practice]: a cut, a new text line, a camera move, an expression change. A static frame longer than that needs a reason.
- **Text on screen in the first frame** helps viewers with sound off [common practice].
- End with one clear next step (call to action) if the brief has one.

## Format
- **1080 × 1920, 9:16** for vertical short-form [platform spec, consistent across Reels, Shorts, TikTok].
- **Safe zones** [common practice; platforms change their UI]: keep text and faces out of roughly the top 14% and bottom 35% of the frame and away from the right edge, where the like, comment, and share buttons sit. When unsure, keep essential text in the middle 60% of the height. Check a frame with the platform UI overlaid before the final gate.
- Frame rate stays the same through the pipeline; mixing rates causes stutter.

## Captions and text
- **Captions on** for speech [common practice]; most feeds start muted.
- Captions match the spoken words exactly, including what the recording says that the script does not.
- Short lines (about one idea per line), large, bold, high contrast; never under a face or a key visual.
- Check legibility on a phone at real size, not only on a monitor.

## Audio
- **Loudness about −14 LUFS integrated, true peak −1 dBTP** [common practice; YouTube documents normalization near −14 LUFS; Instagram and TikTok publish no target]. Measure it (for example `ffmpeg -i <file> -af ebur128 -f null -`), do not guess.
- Voice is the priority: music and effects sit under it and duck where it speaks.
- Silence and pauses are deliberate; do not cut breathing room the script needs.

## Accessibility
- **Text contrast at least 4.5:1, or 3:1 for large text** [standard: WCAG 2.x AA]. Measure with sampled colors.
- No meaning carried by color alone; avoid fast full-screen flashes (more than three per second) [standard: WCAG 2.3.1].

## Final check list
Hook in the first 2 s · change every 2 to 4 s · text inside safe zones · captions match audio · loudness measured · contrast measured · watched on a phone with sound and without sound.

## Sources
- Instagram Reels sizes and safe areas: postsyncer.com/tips/instagram-reels-size-and-safe-areas; captions.ai/blog-post/how-to-make-a-reel (safe-zone percentages, hook, captions).
- Loudness per platform: forasoft.com/learn/audio-for-video/articles-audio/lufs-targets-per-platform-2026.
- WCAG 2.2: w3.org/TR/WCAG22 (1.4.3 Contrast Minimum, 2.3.1 Three Flashes).
