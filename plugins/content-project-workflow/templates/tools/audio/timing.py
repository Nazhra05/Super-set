"""Word timing and mouth shapes from the owner's own recorded voice-over and script.

Input (both supplied by the owner; this tool never generates speech):
  - one voice-over file for the whole film (any format ffmpeg reads)
  - a script file, JSON:
      {"lang": "en",
       "lines": [{"id": "s1-01", "scene": 1, "speaker": "Ana", "text": "What the viewer reads.",
                  "spoken": "optional: what was actually said, when the take departs from the script"}]}
    Lines are in the order they are heard.

What it does:
  1. Transcribes the whole recording once with faster-whisper (word timestamps); the result is
     cached in <out>/asr_cache.json, keyed by the audio file's size and modification time.
  2. Aligns every script word onto the transcript (difflib). Words the transcript missed are
     spread over the gap by length, so every word gets a time.
  3. Snaps word edges to the audible speech (Whisper starts words early inside pauses).
  4. Builds one mouth-shape track per speaker, one value per frame: rest, mbp, a, i, u, e, o, half.
     Letters map to shapes, which is accurate for languages spelled as they sound (Indonesian,
     Malay, Spanish, Italian) and rough for English.

Output: <out>/timing.json and <out>/timing.js (window.TIMING = ...; for compositions that must not
fetch). Every line reports how well the recording matched the script; a low match usually means the
take differs from the script: write what was said in "spoken" and run again.

Usage:
  python tools/audio/timing.py --audio audio/voice-over.mp3 --script data/script.json [--out data]
         [--fps 30] [--model small] [--retranscribe]
Needs: ffmpeg on PATH (or the FFMPEG environment variable), Python packages in tools/audio/requirements.txt.
"""
import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import time

import numpy as np

SR = 16000
REST, MBP, HALF = "rest", "mbp", "half"
VOWELS = {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"}
LIPS = set("mbpfv")


def ffmpeg_bin():
    path = os.environ.get("FFMPEG") or shutil.which("ffmpeg")
    if not path:
        sys.exit("ffmpeg not found: install it (tools/tools-check.sh) or set FFMPEG to its path")
    return path


def decode(path):
    raw = subprocess.run([ffmpeg_bin(), "-v", "quiet", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0


def norm(token):
    t = re.sub(r"[^\w]+", "", token.lower(), flags=re.UNICODE)
    return t.replace("_", "")


def tokens(text):
    return [w for w in re.split(r"\s+", text.strip()) if w]


def transcribe(audio, lang, model_name):
    from faster_whisper import WhisperModel

    print(f"loading faster-whisper ({model_name})...", flush=True)
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=os.cpu_count() or 2)
    t0 = time.time()
    # samples decoded by ffmpeg, not a path: faster-whisper's own decoder breaks across PyAV versions.
    # No script prompt: a prompt helps spelling but can make Whisper hallucinate whole takes.
    segments, _ = model.transcribe(audio, language=lang, word_timestamps=True, beam_size=1, temperature=0.0,
                                   condition_on_previous_text=False, vad_filter=True)
    words = [{"w": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)}
             for seg in segments for w in (seg.words or [])]
    print(f"transcribed {len(words)} words in {time.time() - t0:.0f}s", flush=True)
    return words


def align(script, asr, start, end):
    """Map every script word onto transcript timing; unmatched runs are spread by character count."""
    s_norm = [norm(w) for w in script]
    a_norm = [norm(w["w"]) for w in asr]
    times = [None] * len(script)
    sm = difflib.SequenceMatcher(a=s_norm, b=a_norm, autojunk=False)
    matched = 0
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            aw = asr[blk.b + k]
            times[blk.a + k] = [aw["start"], aw["end"]]
            matched += 1
    n, i = len(script), 0
    while i < n:
        if times[i] is not None:
            i += 1
            continue
        j = i
        while j < n and times[j] is None:
            j += 1
        left = times[i - 1][1] if i > 0 else start
        right = times[j][0] if j < n else end
        if right <= left:
            right = left + 0.08 * (j - i)
        weights = [max(1, len(s_norm[k])) for k in range(i, j)]
        total, t = float(sum(weights)), left
        for k, wgt in zip(range(i, j), weights):
            dur = (right - left) * wgt / total
            times[k] = [round(t, 3), round(t + dur, 3)]
            t += dur
        i = j
    for k in range(1, n):
        if times[k][0] < times[k - 1][1]:
            times[k][0] = times[k - 1][1]
        if times[k][1] < times[k][0] + 0.04:
            times[k][1] = round(times[k][0] + 0.04, 3)
    return [{"w": w, "start": t[0], "end": t[1]} for w, t in zip(script, times)], matched / max(1, n)


def envelope(x, fps):
    hop = SR / fps
    n = int(np.ceil(len(x) / hop))
    env = np.array([np.sqrt((x[int(i * hop):int((i + 1) * hop)] ** 2).mean() or 0) for i in range(n)], np.float32)
    voiced = env[env > 1e-4]
    gate = float(np.percentile(voiced, 20) * 0.6) if voiced.size else 0.0
    return env, gate


def snap_to_speech(words, env, gate, fps, max_shift=0.8):
    """Move a word onset that starts in silence forward to the first voiced frame."""
    n = len(env)
    for w in words:
        f = int(w["start"] * fps)
        limit = min(w["start"] + max_shift, w["end"] - 0.06)
        if f >= n or env[f] >= gate:
            continue
        g = f + 1
        while g < n and g / fps <= limit and env[g] < gate:
            g += 1
        if g < n and g / fps <= limit:
            w["start"] = round(g / fps, 3)
    return words


def word_shapes(word, start, end):
    letters = [c for c in norm(word) if c.isalpha()]
    if not letters:  # digits or symbols: open and half-open, alternating
        steps = max(2, len(norm(word)))
        d = (end - start) / steps
        return [(start + k * d, start + (k + 1) * d, "a" if k % 2 == 0 else HALF) for k in range(steps)]
    shapes, weights = [], []
    for c in letters:
        if c in VOWELS:
            shapes.append(VOWELS[c]); weights.append(1.0)
        elif c in LIPS:
            shapes.append(MBP); weights.append(0.7)
        elif c == "w":
            shapes.append("u"); weights.append(0.6)
        elif c == "y":
            shapes.append("i"); weights.append(0.5)
        else:
            shapes.append(HALF); weights.append(0.45)
    total, out, t = sum(weights), [], start
    for s, wgt in zip(shapes, weights):
        d = (end - start) * wgt / total
        out.append((t, t + d, s))
        t += d
    return out


def shape_track(words, n_frames, env, gate, fps):
    track = [REST] * n_frames
    for w in words:
        for a, b, s in word_shapes(w["w"], w["start"], w["end"]):
            fa = int(round(a * fps))
            fb = max(fa + 1, int(round(b * fps)))
            for f in range(fa, min(fb, n_frames)):
                track[f] = s
    for f in range(n_frames):  # silence inside a word closes the mouth
        if track[f] != REST and env[f] < gate:
            track[f] = REST
    f = 0
    while f < n_frames:  # no shape shorter than 2 frames; never swallow a word onset
        g = f
        while g < n_frames and track[g] == track[f]:
            g += 1
        if g - f == 1 and f > 0:
            track[f] = track[f - 1] if track[f - 1] != REST or g >= n_frames else track[g]
        f = g
    out, prev = [], None
    for f, s in enumerate(track):
        if s != prev:
            out.append([f, s])
            prev = s
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--audio", required=True)
    ap.add_argument("--script", required=True)
    ap.add_argument("--out", default="data")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--model", default="small", help="faster-whisper model: tiny, base, small, medium")
    ap.add_argument("--retranscribe", action="store_true")
    args = ap.parse_args()

    script = json.load(open(args.script, encoding="utf-8"))
    lines = script["lines"]
    lang = script.get("lang")
    os.makedirs(args.out, exist_ok=True)
    cache_path = os.path.join(args.out, "asr_cache.json")
    st = os.stat(args.audio)
    key = f"{os.path.basename(args.audio)}:{st.st_size}:{int(st.st_mtime)}:{args.model}:{lang}"
    cache = json.load(open(cache_path, encoding="utf-8")) if os.path.exists(cache_path) else {}
    x = decode(args.audio)
    if cache.get("key") != key or args.retranscribe:
        cache = {"key": key, "words": transcribe(x, lang, args.model)}
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False)
    asr = cache["words"]
    duration = len(x) / SR
    env, gate = envelope(x, args.fps)

    # one alignment over the whole film keeps line boundaries right even when a take ran long
    flat, owner = [], []
    for i, ln in enumerate(lines):
        for w in tokens(ln.get("spoken") or ln["text"]):
            flat.append(w)
            owner.append(i)
    words, _ = align(flat, asr, 0.0, duration)
    words = snap_to_speech(words, env, gate, args.fps)

    out_lines, per_speaker = [], {}
    for i, ln in enumerate(lines):
        ws = [w for w, o in zip(words, owner) if o == i]
        if not ws:
            continue
        spoken = tokens(ln.get("spoken") or ln["text"])
        window = [a for a in asr if ws[0]["start"] - 0.5 <= a["start"] <= ws[-1]["end"] + 0.5]
        _, ratio = align(spoken, window, ws[0]["start"], ws[-1]["end"])
        out_lines.append({"id": ln.get("id", str(i)), "scene": ln.get("scene"), "speaker": ln.get("speaker"),
                          "start": ws[0]["start"], "end": ws[-1]["end"], "text": ln["text"],
                          "words": ws, "match": round(ratio, 2)})
        per_speaker.setdefault(ln.get("speaker") or "voice", []).extend(ws)

    n_frames = len(env)
    data = {"fps": args.fps, "duration": round(duration, 3), "lines": out_lines,
            "visemes": {who: shape_track(ws, n_frames, env, gate, args.fps) for who, ws in per_speaker.items()}}
    with open(os.path.join(args.out, "timing.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(args.out, "timing.js"), "w", encoding="utf-8") as f:
        f.write("// GENERATED by tools/audio/timing.py - do not edit by hand\n")
        f.write("window.TIMING = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")

    low = 0
    for ln in out_lines:
        flag = "" if ln["match"] >= 0.5 else "  LOW MATCH: check the take, set \"spoken\""
        low += flag != ""
        print(f"{ln['id']:<10} {str(ln['speaker']):<12} {ln['start']:8.2f}-{ln['end']:8.2f}  "
              f"words={len(ln['words']):<3} match={ln['match']:.2f}{flag}")
    print(f"wrote {args.out}/timing.json and timing.js: {len(out_lines)} lines, {low} with low match")


if __name__ == "__main__":
    main()
