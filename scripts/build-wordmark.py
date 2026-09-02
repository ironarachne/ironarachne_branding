#!/usr/bin/env python3
"""Build the Iron Arachne wordmark as outlined SVG paths.

The wordmark is set in Cinzel Decorative (SIL OFL, Natanael Gama) — the same
face the site uses for display type. Text is converted to outlines so the
mark renders identically without the font installed, and so the SVG carries
no font data (the OFL Reserved Font Name applies to the font, not to
outlines drawn with it).

Kerning is read from the font's GPOS `kern` feature (Cinzel Decorative has
no legacy `kern` table), so the outlines carry the same pair adjustments a
browser would apply to live text, plus the logo tracking on top.

The viewBox is fitted to the drawn outlines, not to the advance widths: the
first glyph's flourish extends left of its origin and would otherwise be
clipped at x=0.

The font is vendored in fonts/ alongside its licence, so this repo rebuilds
standalone without the site repo checked out.
"""

import sys
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

FONT_PATH = (
    Path(__file__).resolve().parent.parent / "fonts" / "CinzelDecorative-Regular.woff"
)
TEXT = "Iron Arachne"
TRACKING = 0.02  # em, opens the setting slightly for logo use
GREEN = "#76e841"
INK = "#1b1e24"  # --ia-charcoal, not pure black


def load_font():
    if not FONT_PATH.exists():
        sys.exit(f"font not found: {FONT_PATH}")
    font = TTFont(FONT_PATH)
    font.flavor = None
    return font


def _pair_pos_subtables(gpos):
    """Yield every PairPos subtable reachable from the `kern` feature."""
    lookup_ids = set()
    for rec in gpos.FeatureList.FeatureRecord:
        if rec.FeatureTag == "kern":
            lookup_ids.update(rec.Feature.LookupListIndex)
    for i in sorted(lookup_ids):
        lookup = gpos.LookupList.Lookup[i]
        for st in lookup.SubTable:
            if lookup.LookupType == 9:  # Extension: unwrap
                if st.ExtensionLookupType == 2:
                    yield st.ExtSubTable
            elif lookup.LookupType == 2:
                yield st


def kern_value(font, left, right):
    """Horizontal kerning for a glyph pair, in font units (0 if none).

    Handles both PairPos formats: explicit pairs (format 1) and class-based
    (format 2). Legacy `kern` tables are also honoured if present. The first
    subtable that defines the pair wins, matching shaping-engine behaviour.
    """
    if "GPOS" in font:
        for st in _pair_pos_subtables(font["GPOS"].table):
            if left not in st.Coverage.glyphs:
                continue
            if st.Format == 1:
                pair_set = st.PairSet[st.Coverage.glyphs.index(left)]
                for pv in pair_set.PairValueRecord:
                    if pv.SecondGlyph == right:
                        return pv.Value1.XAdvance if pv.Value1 else 0
            elif st.Format == 2:
                c1 = st.ClassDef1.classDefs.get(left, 0)
                c2 = st.ClassDef2.classDefs.get(right, 0)
                v = st.Class1Record[c1].Class2Record[c2].Value1
                if v is not None and getattr(v, "XAdvance", 0):
                    return v.XAdvance
    if "kern" in font:
        for st in font["kern"].kernTables:
            if (left, right) in st.kernTable:
                return st.kernTable[(left, right)]
    return 0


def build_paths(font):
    """Return (path_data, bounds) in font units.

    bounds is (xmin, ymin, xmax, ymax) of the drawn outlines after
    positioning — the ink box, not the advance box.
    """
    upem = font["head"].unitsPerEm
    cmap = font.getBestCmap()
    glyphset = font.getGlyphSet()
    hmtx = font["hmtx"]

    parts = []
    x = 0.0
    xmin = ymin = float("inf")
    xmax = ymax = float("-inf")
    prev = None
    kerned = []

    for ch in TEXT:
        if ch == " ":
            x += hmtx[cmap[ord(" ")]][0] if ord(" ") in cmap else upem * 0.25
            prev = None
            continue

        if ord(ch) not in cmap:
            sys.exit(f"glyph missing for {ch!r}")
        name = cmap[ord(ch)]

        if prev is not None:
            k = kern_value(font, prev, name)
            if k:
                kerned.append((prev, name, k))
            x += k

        pen = SVGPathPen(glyphset)
        glyphset[name].draw(pen)
        d = pen.getCommands()

        if d:
            bp = BoundsPen(glyphset)
            glyphset[name].draw(bp)
            if bp.bounds:
                xmin = min(xmin, x + bp.bounds[0])
                ymin = min(ymin, bp.bounds[1])
                xmax = max(xmax, x + bp.bounds[2])
                ymax = max(ymax, bp.bounds[3])
            parts.append(f'<path transform="translate({x:.1f} 0)" d="{d}"/>')

        x += hmtx[name][0] + upem * TRACKING
        prev = name

    if kerned:
        print("kerning applied:", ", ".join(f"{a}{b} {k:+d}" for a, b, k in kerned))
    else:
        print("warning: no kerning pairs found for the wordmark text")

    return "\n    ".join(parts), (xmin, ymin, xmax, ymax)


def main():
    font = load_font()
    paths, (xmin, ymin, xmax, ymax) = build_paths(font)
    width = xmax - xmin
    height = ymax - ymin

    out_dir = Path(__file__).resolve().parent.parent / "logo" / "wordmark"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Shift the ink box to the origin, then flip the y-axis: font units run
    # up, SVG runs down.
    for name, color in [("wordmark-green.svg", GREEN), ("wordmark-black.svg", INK)]:
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {width:.1f} {height:.1f}" '
            f'width="{width:.1f}" height="{height:.1f}">\n'
            f'  <title>Iron Arachne</title>\n'
            f'  <g fill="{color}" transform="translate({-xmin:.1f} {ymax:.1f}) scale(1 -1)">\n'
            f'    {paths}\n'
            f'  </g>\n'
            f'</svg>\n'
        )
        (out_dir / name).write_text(svg)
        print(f"wrote {out_dir / name}  ({width:.0f} x {height:.0f} units)")

    print(f"aspect ratio: {width / height:.3f}")


if __name__ == "__main__":
    main()
