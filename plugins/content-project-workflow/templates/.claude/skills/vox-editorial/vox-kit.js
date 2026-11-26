// vox-kit.js: paper-collage helpers for HyperFrames + GSAP.
// Deterministic: no Math.random, no clock. Every effect is a timeline tween or a function of
// timeline progress, so a seek to any frame renders the same image.
// Copy this file next to the composition's own scripts and load it after GSAP.
// Written for the Content Project Workflow; techniques credited in SKILL.md ("Sources").
(function (root) {
  "use strict";
  const TWOS = 12; // collage clock: 12 poses per second ("on twos" at 24 fps)
  const SVG_NS = "http://www.w3.org/2000/svg";

  // Ease quantized to 12 poses per second of its own duration. Paper, cut-outs, and stamps use it;
  // the camera and photos of people do not (two clocks).
  function onTwos(ease, dur) {
    const f = gsap.parseEase(ease || "none");
    const n = Math.max(1, Math.round(dur * TWOS));
    return (p) => f(Math.min(1, Math.floor(p * n + 1e-6) / n));
  }

  // Repeatable pseudo-random number in [0, 1) for step i.
  function hash(i, seed) {
    const x = Math.sin((i + 1) * 12.9898 + (seed || 0) * 78.233) * 43758.5453;
    return x - Math.floor(x);
  }

  // Filters used by the helpers below. Call once per composition, with the composition root.
  // paper: color of the torn white edge around cut-outs.
  function installFilters(host, opts) {
    const o = Object.assign({ paper: "#F4F0E6", prefix: "vox" }, opts);
    const p = o.prefix;
    const svg = document.createElementNS(SVG_NS, "svg");
    svg.setAttribute("width", "0");
    svg.setAttribute("height", "0");
    svg.setAttribute("aria-hidden", "true");
    svg.style.position = "absolute";
    svg.innerHTML =
      // torn sticker edge: grow the silhouette, roughen it with fixed-seed noise, fill with paper
      `<filter id="${p}-torn" x="-15%" y="-15%" width="130%" height="130%">` +
      `<feMorphology in="SourceAlpha" operator="dilate" radius="9" result="grown"/>` +
      `<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="3" seed="7" result="noise"/>` +
      `<feDisplacementMap in="grown" in2="noise" scale="12" xChannelSelector="R" yChannelSelector="G" result="rough"/>` +
      `<feFlood flood-color="${o.paper}" result="paper"/>` +
      `<feComposite in="paper" in2="rough" operator="in" result="edge"/>` +
      `<feMerge><feMergeNode in="edge"/><feMergeNode in="SourceGraphic"/></feMerge></filter>` +
      // printed ink on display type: a small displacement; its seed is stepped by inkReseed()
      `<filter id="${p}-ink" x="-5%" y="-10%" width="110%" height="120%">` +
      `<feTurbulence id="${p}-ink-noise" type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="1" result="n"/>` +
      `<feDisplacementMap in="SourceGraphic" in2="n" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>` +
      // horizontal motion blur for whip pans; stdDeviation is tweened by whip()
      `<filter id="${p}-whip" x="-20%" y="0%" width="140%" height="100%">` +
      `<feGaussianBlur id="${p}-whip-blur" stdDeviation="0 0"/></filter>`;
    host.appendChild(svg);
    return svg;
  }

  // Paper boil: a small wobble on twos through CSS variables. Put class "vox-boil" on a wrapper
  // (not on an element GSAP also moves) and never on photos of people.
  function boil(tl, el, start, dur, opts) {
    const o = Object.assign({ amp: 3, rot: 0.7, seed: 1 }, opts);
    const steps = Math.max(1, Math.round(dur * TWOS));
    const proxy = { p: 0 };
    tl.to(proxy, {
      p: 1, duration: dur, ease: "none",
      onUpdate() {
        const k = Math.min(steps - 1, Math.floor(proxy.p * steps));
        el.style.setProperty("--bx", ((hash(k, o.seed) * 2 - 1) * o.amp).toFixed(2) + "px");
        el.style.setProperty("--by", ((hash(k, o.seed + 1) * 2 - 1) * o.amp).toFixed(2) + "px");
        el.style.setProperty("--br", ((hash(k, o.seed + 2) * 2 - 1) * o.rot).toFixed(2) + "deg");
      },
    }, start);
  }

  // Re-seed the ink filter a few times per second so printed type never looks like screen type.
  function inkReseed(tl, start, dur, opts) {
    const o = Object.assign({ perSecond: 6, prefix: "vox" }, opts);
    const node = document.getElementById(o.prefix + "-ink-noise");
    const proxy = { p: 0 };
    tl.to(proxy, {
      p: 1, duration: dur, ease: "none",
      onUpdate() { node.setAttribute("seed", String(1 + Math.floor(proxy.p * dur * o.perSecond))); },
    }, start);
  }

  // Object pop with overshoot, on twos. Objects only; text never overshoots.
  // Hide `el` before the timeline (CSS visibility: hidden, or gsap.set) so frame 0 is right.
  function slap(tl, el, start) {
    tl.set(el, { autoAlpha: 1, scale: 0.28 }, start);
    [1.42, 1.12, 0.96, 1].forEach((s, i) => tl.set(el, { scale: s }, start + (i + 1) / TWOS));
  }

  // Highlighter sweep: a band BEHIND the words (lower z-index; multiply so paper grain shows through),
  // revealed left to right. Hide it before the timeline. It should end on the stressed word, so pass
  // the time that word is spoken as `end`.
  function highlight(tl, band, end, chars) {
    const dur = Math.min(24, Math.max(8, 6 + 0.6 * chars)) / 30;
    tl.set(band, { autoAlpha: 1, clipPath: "inset(0% 100% 0% 0%)" }, end - dur);
    tl.to(band, { clipPath: "inset(0% 0% 0% 0%)", duration: dur, ease: onTwos("power2.out", dur) }, end - dur);
  }

  // Whip pan between two panels inside one wrapper: the wrapper slides by `dist` px in 0.3 s with a
  // horizontal blur that peaks mid-move; the filter is removed after landing (it is expensive).
  function whip(tl, wrap, start, dist, opts) {
    const o = Object.assign({ dur: 0.3, blur: 60, prefix: "vox" }, opts);
    const node = document.getElementById(o.prefix + "-whip-blur");
    const proxy = { p: 0 };
    tl.set(wrap, { filter: `url(#${o.prefix}-whip)` }, start);
    tl.to(wrap, { x: `-=${dist}`, duration: o.dur, ease: "power3.inOut" }, start);
    tl.to(proxy, {
      p: 1, duration: o.dur, ease: "none",
      onUpdate() { node.setAttribute("stdDeviation", `${(Math.sin(proxy.p * Math.PI) * o.blur).toFixed(1)} 0`); },
    }, start);
    tl.set(wrap, { filter: "none" }, start + o.dur);
  }

  // Camera: one smooth push on the wrapper that holds the shot (2 to 5% over about 5 s).
  function cameraPush(tl, cam, start, dur, amount) {
    tl.fromTo(cam, { scale: 1 }, { scale: 1 + (amount || 0.04), duration: dur, ease: "none" }, start);
  }

  // Words of a line appear when they are spoken (times from window.TIMING), with a two-pose jump
  // instead of a fly-in. els[i] is the element for words[i].
  function wordsOn(tl, els, words) {
    els.forEach((el, i) => {
      const t = words[i].start;
      tl.set(el, { autoAlpha: 1, y: -6 }, t);
      tl.set(el, { y: 0 }, t + 1 / TWOS);
    });
  }

  // Caption karaoke: groups of up to `maxWords` words (shorter at punctuation and pauses), one group
  // on screen at a time, the spoken word marked with data-on="1" (style it in CSS). A group shorter
  // than the reading floor (0.5 s + 0.3 s a word) is merged with the next one, up to two lines
  // (2 x maxChars). Builds the DOM inside `box`; hidden states are set outside the timeline because a
  // zero-duration set at position 0 does not render at frame 0.
  function captions(tl, box, words, opts) {
    const o = Object.assign({ maxWords: 4, maxChars: 26, hold: 0.25 }, opts);
    const floor = (g) => 0.5 + 0.3 * g.length;
    const text = (g) => g.map((x) => x.w).join(" ");
    let groups = [];
    let cur = [];
    words.forEach((w, i) => {
      cur.push(w);
      const next = words[i + 1];
      const pause = next ? next.start - w.end > 0.35 : true;
      if (cur.length >= o.maxWords || text(cur).length >= o.maxChars || /[.,!?;:]$/.test(w.w) || pause) {
        groups.push(cur);
        cur = [];
      }
    });
    if (cur.length) groups.push(cur);
    const merged = [];
    groups.forEach((g) => {
      const prev = merged[merged.length - 1];
      if (prev) {
        const span = g[0].start - prev[0].start;
        if (span < floor(prev) && text(prev.concat(g)).length <= 2 * o.maxChars) {
          merged[merged.length - 1] = prev.concat(g);
          return;
        }
      }
      merged.push(g);
    });
    groups = merged;
    groups.forEach((g, gi) => {
      const line = document.createElement("div");
      line.className = "vox-cap";
      const spans = g.map((w) => {
        const s = document.createElement("span");
        s.textContent = w.w;
        line.appendChild(s);
        line.appendChild(document.createTextNode(" "));
        return s;
      });
      box.appendChild(line);
      gsap.set(line, { autoAlpha: 0 });
      const last = g[g.length - 1];
      const next = groups[gi + 1];
      const want = Math.max(last.end + o.hold, g[0].start + floor(g));
      const off = next ? Math.min(next[0].start, want) : want;
      tl.set(line, { autoAlpha: 1 }, g[0].start);
      tl.set(line, { autoAlpha: 0 }, off);
      g.forEach((w, k) => {
        tl.set(spans[k], { attr: { "data-on": "1" } }, w.start);
        tl.set(spans[k], { attr: { "data-on": "0" } }, w.end);
      });
    });
    return groups.length;
  }

  // Mouth swaps for a drawn character: track is [[frame, shape], ...] from tools/audio/timing.py;
  // mouths maps shape names to elements. Shapes without an element fall back to "rest".
  function mouth(tl, mouths, track, fps, offset) {
    const names = Object.keys(mouths);
    track.forEach(([frame, shape]) => {
      const on = mouths[shape] ? shape : "rest";
      const t = (offset || 0) + frame / fps;
      names.forEach((n) => tl.set(mouths[n], { autoAlpha: n === on ? 1 : 0 }, t));
    });
  }

  root.Vox = { onTwos, hash, installFilters, boil, inkReseed, slap, highlight, whip, cameraPush, wordsOn, captions, mouth };
})(window);
