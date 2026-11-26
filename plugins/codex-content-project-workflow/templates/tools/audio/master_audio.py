"""Loudness-master a rendered video for social delivery.

Default target: -14 LUFS integrated, true peak at or below -3 dBTP after AAC encoding.
Steps: an optional gentle compressor evens out voices recorded at different levels; loudnorm
(measured first, then applied in linear mode) sets the loudness; a 4x oversampled limiter holds the
peaks (linear loudnorm alone let a quiet, peaky voice-over reach +1.2 dBTP after AAC); the result is
measured and the gain in front of the limiter is corrected, at most 3 passes, until both targets hold.
Video is copied untouched; audio is re-encoded (AAC 192 kbit/s, 48 kHz) with +faststart.

Usage: python tools/audio/master_audio.py <in.mp4> <out.mp4> [--lufs -14] [--tp -3] [--no-compress]
Needs: ffmpeg on PATH (or the FFMPEG environment variable). Standard library only.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

COMPRESS = "acompressor=threshold=-24dB:ratio=2.5:attack=8:release=180:makeup=2"


def ffmpeg_bin():
    path = os.environ.get("FFMPEG") or shutil.which("ffmpeg")
    if not path:
        sys.exit("ffmpeg not found: install it (tools/tools-check.sh) or set FFMPEG to its path")
    return path


def measure(ff, path):
    """Integrated loudness (LUFS) and true peak (dBTP) of the first audio stream."""
    err = subprocess.run([ff, "-hide_banner", "-nostats", "-i", path, "-map", "0:a:0", "-af", "ebur128=peak=true",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    summary = err[err.rfind("Summary:"):]
    i = re.search(r"I:\s+(-?[\d.]+) LUFS", summary)
    tp = re.search(r"Peak:\s+(-?[\d.]+) dBFS", summary)
    if not (i and tp):
        sys.exit(f"could not measure {path} (no audio stream?)")
    return float(i.group(1)), float(tp.group(1))


def main():
    ap = argparse.ArgumentParser(description="Loudness-master a video.")
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--lufs", type=float, default=-14.0)
    ap.add_argument("--tp", type=float, default=-3.0)
    ap.add_argument("--lra", type=float, default=9.0)
    ap.add_argument("--no-compress", action="store_true")
    a = ap.parse_args()
    if os.path.abspath(a.src) == os.path.abspath(a.dst):
        sys.exit("write to a new file; the input is never overwritten")
    ff = ffmpeg_bin()
    pre = "" if a.no_compress else COMPRESS + ","
    target = f"loudnorm=I={a.lufs}:TP={a.tp}:LRA={a.lra}"
    err = subprocess.run([ff, "-hide_banner", "-nostats", "-i", a.src, "-af", pre + target + ":print_format=json",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    found = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", err, re.S)
    if not found:
        sys.exit("loudness measurement failed (no audio stream?):\n" + err[-800:])
    m = json.loads(found.group(0))
    norm = (pre + target + f":measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
            f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    limit = 10 ** ((a.tp - 0.5) / 20)  # half a dB of headroom for the AAC encoder
    gain = 0.0
    for attempt in range(1, 4):
        af = (f"{norm},volume={gain:.2f}dB,aresample=192000,"
              f"alimiter=limit={limit:.4f}:attack=1:release=60:level=false,aresample=48000")
        subprocess.run([ff, "-hide_banner", "-y", "-i", a.src, "-c:v", "copy", "-af", af, "-c:a", "aac", "-b:a", "192k",
                        "-ar", "48000", "-movflags", "+faststart", a.dst], check=True, capture_output=True)
        lufs, tp = measure(ff, a.dst)
        print(f"pass {attempt}: gain {gain:+.2f} dB -> {lufs} LUFS, {tp} dBTP")
        if abs(lufs - a.lufs) <= 0.5 and tp <= a.tp + 0.2:
            break
        gain += a.lufs - lufs
    print(f"input {m['input_i']} LUFS / {m['input_tp']} dBTP -> {a.dst}: {lufs} LUFS / {tp} dBTP "
          f"(target {a.lufs} LUFS / {a.tp} dBTP)")


if __name__ == "__main__":
    main()
