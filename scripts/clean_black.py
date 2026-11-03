#!/usr/bin/env python3
# Copyright 2026 Renaise Kim
# SPDX-License-Identifier: Apache-2.0
"""Black-level clean-up between Capamari rolls.

Each roll re-encodes the previous capsule through the VAE, and near-black background
pixels pick up colored quantization noise that compounds over several rolls. This
applies a plain levels curve: luminance below LOW goes to pure black, LOW..HIGH ramps
smoothly, above HIGH is untouched. It never adds or removes content.
Experimental: in our one test it did not help the next roll keep earlier objects.

Pillow only. Usage: python scripts/clean_black.py in.png out.png [--low 0.10] [--high 0.22]
"""
import argparse
from PIL import Image, ImageChops

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("dst")
ap.add_argument("--low", type=float, default=0.10)
ap.add_argument("--high", type=float, default=0.22)
a = ap.parse_args()

im = Image.open(a.src).convert("RGB")
lum = im.convert("L")  # ITU-R 601 luma

def curve(v):
    t = min(max((v / 255.0 - a.low) / (a.high - a.low), 0.0), 1.0)
    return round(255 * t * t * (3 - 2 * t))  # smoothstep

mask = lum.point([curve(v) for v in range(256)])
ImageChops.multiply(im, Image.merge("RGB", (mask, mask, mask))).save(a.dst)
