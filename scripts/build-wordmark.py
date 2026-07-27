#!/usr/bin/env python3
"""Build the Iron Arachne wordmark as outlined SVG paths.

The wordmark is set in Cinzel Decorative (SIL OFL, Natanael Gama) — the same
face the site uses for display type. Text is converted to outlines so the
mark renders identically without the font installed, and so the SVG carries
no font data (the OFL Reserved Font Name applies to the font, not to
outlines drawn with it).

The font is vendored in fonts/ alongside its licence, so this repo rebuilds
standalone without the site repo checked out.
"""

import re
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont

FONT_PATH = (
    Path(__file__).resolve().parent.parent / "fonts" / "CinzelDecorative-Regular.woff"
)
TEXT = "Iron Arachne"
TRACKING = 0.02  # em, opens the setting slightly for logo use
GREEN = "#76e841"
INK = "#1b1e24"  # --charcoal, not pure black


def load_font():
    if not FONT_PATH.exists():
        sys.exit(f"font not found: {FONT_PATH}")
    font = TTFont(FONT_PATH)
    font.flavor = None
    return font


def build_paths(font):
    """Return (path_data, width, ymin, ymax) in font units."""
    upem = font["head"].unitsPerEm
    cmap = font.getBestCmap()
    glyphset = font.getGlyphSet()
    hmtx = font["hmtx"]

    kern = {}
    if "kern" in font:
        for st in font["kern"].kernTables:
            kern.update(st.kernTable)

    parts = []
    x = 0.0
    ymin, ymax = 0.0, 0.0
    prev = None

    for ch in TEXT:
        if ch == " ":
            x += hmtx[cmap[ord(" ")]][0] if ord(" ") in cmap else upem * 0.25
            prev = None
            continue

        if ord(ch) not in cmap:
            sys.exit(f"glyph missing for {ch!r}")
        name = cmap[ord(ch)]

        if prev is not None:
            x += kern.get((prev, name), 0)

        pen = SVGPathPen(glyphset)
        glyphset[name].draw(pen)
        d = pen.getCommands()

        if d:
            bp = BoundsPen(glyphset)
            glyphset[name].draw(bp)
            if bp.bounds:
                ymin = min(ymin, bp.bounds[1])
                ymax = max(ymax, bp.bounds[3])
            parts.append(f'<path transform="translate({x:.1f} 0)" d="{d}"/>')

        x += hmtx[name][0] + upem * TRACKING
        prev = name

    return "\n    ".join(parts), x - upem * TRACKING, ymin, ymax


def main():
    font = load_font()
    paths, width, ymin, ymax = build_paths(font)
    height = ymax - ymin

    out_dir = Path(__file__).resolve().parent.parent / "logo" / "wordmark"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Flip the y-axis: font units run up, SVG runs down.
    for name, color in [("wordmark-green.svg", GREEN), ("wordmark-black.svg", INK)]:
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {width:.1f} {height:.1f}" '
            f'width="{width:.1f}" height="{height:.1f}">\n'
            f'  <title>Iron Arachne</title>\n'
            f'  <g fill="{color}" transform="translate(0 {ymax:.1f}) scale(1 -1)">\n'
            f'    {paths}\n'
            f'  </g>\n'
            f'</svg>\n'
        )
        (out_dir / name).write_text(svg)
        print(f"wrote {out_dir / name}  ({width:.0f} x {height:.0f} units)")

    print(f"aspect ratio: {width / height:.3f}")


if __name__ == "__main__":
    main()
