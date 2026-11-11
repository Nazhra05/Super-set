---
name: motion-principles
description: Use when animating characters, text, or graphics - the twelve principles of animation, timing, easing, staging, and how to review motion frame by frame. Read before shot tickets and animatics.
---

# Motion principles

How to make motion feel intentional instead of mechanical. The project's `STYLE.md` (section Motion) sets the pace and easing family; this file explains the craft behind it.

## The twelve principles (Thomas and Johnston, *The Illusion of Life*, 1981)
1. **Squash and stretch:** shapes deform to show weight and flexibility; volume stays the same.
2. **Anticipation:** a small opposite move before the main action (lean back before a throw, a blink before a head turn).
3. **Staging:** one idea per moment; the viewer's eye goes where you need it. One focal point per shot.
4. **Straight ahead and pose to pose:** plan key poses first (pose to pose) for control; fill in between.
5. **Follow through and overlapping action:** parts keep moving after the body stops (hair, clothing, hands) and start at different times.
6. **Slow in and slow out:** movement accelerates and decelerates; nothing starts or stops at full speed.
7. **Arcs:** natural movement follows curved paths, not straight lines.
8. **Secondary action:** a smaller action that supports the main one (a nod while speaking), never competing with it.
9. **Timing:** the number of frames for an action sets its weight and mood.
10. **Exaggeration:** push poses and expressions enough to read at phone size.
11. **Solid drawing:** forms keep volume and perspective from every angle (see the turnaround in `character-design`).
12. **Appeal:** clear, readable, pleasant design and motion.

## Easing
- **Entering the frame: ease-out** (fast start, soft landing). **Leaving: ease-in** (soft start, fast exit). **Moving within the frame: ease-in-out.** [common practice; also in Material Design motion guidance]
- Linear easing only for constant motion (a ticker, a rotating background).
- One easing family per project, named in `STYLE.md`; mixing families looks accidental.

## Timing and readability
- Text stays on screen long enough to read it twice at normal speed; never cut mid-sentence of on-screen text.
- Hold a key pose before and after an important beat so it registers.
- Lip sync: mouth shapes land on or one frame before the sound; expressions change on the beat the script implies, not at random.
- Idle life: characters on screen breathe, blink at irregular intervals, and shift weight; a frozen character looks broken.

## Reviewing motion
- Check key frames: the first frame, every pose change, every text change, the last frame. Grab them at exact time codes and look.
- Scrub at full speed with sound for rhythm; a single frame cannot show timing.
- Look for: pops (a part jumping between frames), wrong pivots (a limb rotating around the canvas corner instead of its joint), sliding feet, text appearing before it is spoken.

## Sources
- Frank Thomas and Ollie Johnston, *The Illusion of Life: Disney Animation* (1981).
- Material Design, "Easing and duration" (m3.material.io/styles/motion).
- Studio production guides on key poses and in-betweens, for example medium.com/studiotale/the-animation-process-step-by-step-production-guide.
