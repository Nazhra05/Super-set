"""Check a finished video file before upload: one command, one PASS or FAIL per item.

Checks: video codec, pixel format, resolution, frame rate, audio codec and sample rate, integrated
loudness, true peak, and that the index (moov atom) sits at the start of the file (+faststart).
Defaults fit vertical social video (Reels, Shorts, TikTok): 1080x1920, H.264, yuv420p, AAC,
-14 LUFS +/- 1, true peak at or below -1 dBTP. Duration is reported, not limited.

Usage: python tools/audio/delivery_check.py <file.mp4> [--width 1080 --height 1920] [--lufs -14]
Exit 0 when every item passes, 1 otherwise.
Needs: ffmpeg and ffprobe on PATH (or the FFMPEG / FFPROBE environment variables). Standard library only.
"""
import argparse
import json
import os
import re
import shutil
import struct
import subprocess
import sys


def tool(name):
    path = os.environ.get(name.upper()) or shutil.which(name)
    if not path:
        sys.exit(f"{name} not found: install ffmpeg (tools/tools-check.sh) or set {name.upper()}")
    return path


def atom_order(path):
    """Top-level MP4 atoms in file order (enough to see whether moov comes before mdat)."""
    order = []
    with open(path, "rb") as f:
        while True:
            head = f.read(8)
            if len(head) < 8:
                break
            size, kind = struct.unpack(">I4s", head)
            if size == 1:
                size = struct.unpack(">Q", f.read(8))[0]
                f.seek(size - 16, 1)
            elif size == 0:
                order.append(kind.decode("latin-1"))
                break
            else:
                f.seek(size - 8, 1)
            order.append(kind.decode("latin-1"))
    return order


def main():
    ap = argparse.ArgumentParser(description="Check a video file before upload.")
    ap.add_argument("file")
    ap.add_argument("--width", type=int, default=1080)
    ap.add_argument("--height", type=int, default=1920)
    ap.add_argument("--codec", default="h264")
    ap.add_argument("--min-fps", type=float, default=23.9)
    ap.add_argument("--max-fps", type=float, default=60.0)
    ap.add_argument("--lufs", type=float, default=-14.0)
    ap.add_argument("--lufs-tol", type=float, default=1.0)
    ap.add_argument("--max-tp", type=float, default=-1.0)
    a = ap.parse_args()

    probe = json.loads(subprocess.run([tool("ffprobe"), "-v", "error", "-show_streams", "-show_format", "-of", "json",
                                       a.file], capture_output=True, text=True, check=True).stdout)
    v = next((s for s in probe["streams"] if s["codec_type"] == "video"), None)
    au = next((s for s in probe["streams"] if s["codec_type"] == "audio"), None)
    rows = []

    def row(name, ok, got, want):
        rows.append((name, ok, got, want))

    if v:
        num, den = (int(p) for p in v.get("avg_frame_rate", "0/1").split("/"))
        fps = num / den if den else 0.0
        row("video codec", v["codec_name"] == a.codec, v["codec_name"], a.codec)
        row("pixel format", v.get("pix_fmt") == "yuv420p", v.get("pix_fmt"), "yuv420p")
        row("resolution", (v["width"], v["height"]) == (a.width, a.height), f"{v['width']}x{v['height']}",
            f"{a.width}x{a.height}")
        row("frame rate", a.min_fps <= fps <= a.max_fps, f"{fps:.3f}", f"{a.min_fps}-{a.max_fps}")
    else:
        row("video stream", False, "none", "present")
    if au:
        row("audio codec", au["codec_name"] == "aac", au["codec_name"], "aac")
        row("audio sample rate", int(au.get("sample_rate", 0)) in (44100, 48000), au.get("sample_rate"), "44100 or 48000")
        err = subprocess.run([tool("ffmpeg"), "-hide_banner", "-nostats", "-i", a.file, "-map", "0:a:0",
                              "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
        summary = err[err.rfind("Summary:"):]
        i_m = re.search(r"I:\s+(-?[\d.]+) LUFS", summary)
        tp_m = re.search(r"Peak:\s+(-?[\d.]+) dBFS", summary)
        if i_m:
            lufs = float(i_m.group(1))
            row("loudness", abs(lufs - a.lufs) <= a.lufs_tol, f"{lufs} LUFS", f"{a.lufs} +/- {a.lufs_tol}")
        else:
            row("loudness", False, "not measured", f"{a.lufs}")
        if tp_m:
            tp = float(tp_m.group(1))
            row("true peak", tp <= a.max_tp, f"{tp} dBTP", f"<= {a.max_tp}")
        else:
            row("true peak", False, "not measured", f"<= {a.max_tp}")
    else:
        row("audio stream", False, "none", "present")
    order = atom_order(a.file)
    fast = "moov" in order and "mdat" in order and order.index("moov") < order.index("mdat")
    row("faststart (moov first)", fast, " ".join(order[:4]), "moov before mdat")

    dur = float(probe["format"].get("duration", 0))
    print(f"{a.file}: duration {dur:.2f} s, size {int(probe['format'].get('size', 0)) / 1e6:.1f} MB")
    for name, ok, got, want in rows:
        print(f"{'PASS' if ok else 'FAIL'}  {name:<24} {got}  (want {want})")
    failed = sum(not r[1] for r in rows)
    print("delivery: OK" if not failed else f"delivery: {failed} item(s) failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
