"""Prepare paper media without importing robot code.

Usage: python scripts/prepare_assets.py --proof PATH --videos PATH
The video directory contains scan_silent.mov, fill_silent.mp4 and
showcase/highlight_reel_1min.mp4 plus its SRT captions.
"""
import argparse
import io
from pathlib import Path
import re
import shutil
import subprocess
import imageio_ffmpeg
from PIL import Image
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
# Image references in the supplied 14-page proof.
FIGURES = {"system-overview": 10, "hardware": 35, "end-effector": 36,
           "segmentation": 16, "path-extraction": 20, "localization": 40,
           "spatial-lag": 26, "ielm": 9, "controller-comparison": 52,
           "paver": 53, "convergence": 57, "calibration": 44}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--videos", type=Path, required=True)
    args = parser.parse_args()
    images, videos = ROOT / "static/images", ROOT / "static/videos"
    images.mkdir(parents=True, exist_ok=True)
    videos.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(args.proof) as document:
        if len(document) != 14:
            raise ValueError("Expected the supplied 14-page proof; remap references for a new proof.")
        for name, reference in FIGURES.items():
            image = Image.open(io.BytesIO(document.extract_image(reference)["image"])).convert("RGB")
            image.thumbnail((1600, 1600))
            image.save(images / f"{name}.webp", quality=88)
    shutil.copy2(args.videos / "showcase/highlight_reel_1min.mp4", videos / "crack-repair-demo.mp4")
    captions = (args.videos / "showcase/highlight_reel_1min.srt").read_text(encoding="utf-8-sig")
    captions = re.sub(r"(\d{2}:\d{2}:\d{2}),(\d{3})", r"\1.\2", captions)
    (videos / "crack-repair-demo.vtt").write_text("WEBVTT\n\n" + captions, encoding="utf-8")
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    def run(*command):
        subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y", *map(str, command)], check=True)
    for name, source, start, duration in [("scanning", "scan_silent.mov", 0.5, 10), ("filling", "fill_silent.mp4", 0, 14)]:
        run("-ss", start, "-i", args.videos / source, "-t", duration, "-vf", "scale=1280:-2", "-an", "-c:v", "libx264", "-crf", 24, "-preset", "fast", "-pix_fmt", "yuv420p", "-movflags", "+faststart", videos / f"{name}.mp4")
        run("-ss", 1, "-i", videos / f"{name}.mp4", "-frames:v", 1, "-q:v", 3, images / f"{name}-poster.jpg")
    run("-ss", 6, "-i", videos / "crack-repair-demo.mp4", "-frames:v", 1, "-vf", "scale=1600:-2", "-q:v", 3, images / "demo-poster.jpg")
    print(f"Prepared {len(FIGURES)} figures, three videos, captions, and posters.")

if __name__ == "__main__":
    main()
