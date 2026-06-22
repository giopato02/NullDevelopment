#!/usr/bin/env python3
"""
Regenerate public/og-image.png (1200x630) to match public/og-image.svg.

This is a DEV-ONLY utility — it is NOT part of `npm run build`, so the site
never depends on Python. The committed og-image.png is what ships. Re-run this
only if you change the OG art:

    python3 -m venv .venv && .venv/bin/pip install pillow
    .venv/bin/python scripts/og-image.py

Uses macOS system fonts (Menlo for the mono "Null", Helvetica for the rest) so
it works out of the box on a Mac with no font downloads.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ── palette ────────────────────────────────────────────────────────────────
PARCHMENT = (237, 228, 211)
OXBLOOD = (123, 45, 56)
CYPRESS = (67, 84, 58)
BRASS = (176, 141, 87)
INK = (42, 37, 32)
MUTED = (90, 80, 70)
ON_ACCENT = (251, 247, 239)

W, H = 1200, 630
MARGIN = 96


def load(paths, size, index=0):
    """Load the first font path that works; fall back to PIL default."""
    for p in paths:
        try:
            return ImageFont.truetype(p, size=size, index=index)
        except Exception:
            continue
    return ImageFont.load_default()


SF = "/System/Library/Fonts/"
SUP = "/System/Library/Fonts/Supplemental/"

mono_bold = load([SF + "Menlo.ttc"], 84, index=1)
mono_reg = load([SF + "Menlo.ttc", SF + "SFNSMono.ttf"], 26, index=0)
mono_sm = load([SF + "Menlo.ttc", SF + "SFNSMono.ttf"], 24, index=0)
mono_chip = load([SF + "Menlo.ttc", SF + "SFNSMono.ttf"], 18, index=1)
sans_bold = load([SF + "Helvetica.ttc", SUP + "Arial Bold.ttf"], 84, index=1)
sans_tag = load([SF + "Helvetica.ttc", SUP + "Arial Bold.ttf"], 40, index=1)
sans_sub = load([SF + "Helvetica.ttc", SUP + "Arial.ttf"], 28, index=0)

img = Image.new("RGB", (W, H), PARCHMENT)
d = ImageDraw.Draw(img)

# top brass hairline
d.rectangle([0, 0, W, 8], fill=BRASS)

# null-set mark tile
tx, ty, ts = MARGIN, 96, 104
d.rounded_rectangle([tx, ty, tx + ts, ty + ts], radius=24, fill=OXBLOOD)
cx, cy, r = tx + ts // 2, ty + ts // 2, 25
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ON_ACCENT, width=7)
d.line([cx - 21, cy + 21, cx + 21, cy - 21], fill=ON_ACCENT, width=7)
for ex, ey in [(cx - 21, cy + 21), (cx + 21, cy - 21)]:
    d.ellipse([ex - 3, ey - 3, ex + 3, ey + 3], fill=ON_ACCENT)

# eyebrow
d.text((MARGIN + 2, 248), "// solo app & web studio", font=mono_reg, fill=CYPRESS, anchor="ls")

# wordmark: "Null" (mono, oxblood) + "Development" (sans, ink) on one baseline
base = 340
d.text((MARGIN, base), "Null", font=mono_bold, fill=OXBLOOD, anchor="ls")
null_w = d.textlength("Null", font=mono_bold)
d.text((MARGIN + null_w + 4, base), "Development", font=sans_bold, fill=INK, anchor="ls")

# tagline + subline
d.text((MARGIN + 2, 408), "From null to shipped.", font=sans_tag, fill=INK, anchor="ls")
d.text((MARGIN + 2, 458), "Solo-built apps and websites, each carrying the Null.",
       font=sans_sub, fill=MUTED, anchor="ls")

# footer url
d.text((MARGIN + 2, 574), "nulldevelopment.co", font=mono_sm, fill=OXBLOOD, anchor="ls")

# "NullState — live on Play" chip, right-aligned
chip_text = "NullState — live on Play"
pad_x, dot_gap = 22, 16
tw = d.textlength(chip_text, font=mono_chip)
chip_w = pad_x + 9 + dot_gap + tw + pad_x
chip_h = 38
chip_x1 = W - MARGIN - chip_w
chip_y1 = 540
d.rounded_rectangle([chip_x1, chip_y1, chip_x1 + chip_w, chip_y1 + chip_h],
                    radius=chip_h // 2, fill=CYPRESS)
dot_cx = chip_x1 + pad_x
dot_cy = chip_y1 + chip_h // 2
d.ellipse([dot_cx - 4, dot_cy - 4, dot_cx + 4, dot_cy + 4], fill=ON_ACCENT)
d.text((dot_cx + dot_gap, dot_cy), chip_text, font=mono_chip, fill=ON_ACCENT, anchor="lm")

out = Path(__file__).resolve().parent.parent / "public" / "og-image.png"
img.save(out, "PNG")
print(f"wrote {out} ({out.stat().st_size} bytes)")
