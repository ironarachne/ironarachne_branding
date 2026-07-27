#!/usr/bin/env python3
"""Compose the horizontal and stacked lockups from the glyph and wordmark.

Both are built from the same two masters (logo/glyph, logo/wordmark) so a
change to either propagates to every lockup on the next build. Proportions
are expressed as multiples of the wordmark cap height, which is what keeps
the spider from swamping the type at small sizes.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLYPH_DIR = ROOT / "logo" / "glyph"
WORD_DIR = ROOT / "logo" / "wordmark"
OUT_DIR = ROOT / "logo" / "primary"

CAP = 100.0            # wordmark cap height in lockup units
GLYPH_H_HORIZ = 2.0    # glyph height, as multiples of cap height
GLYPH_H_STACK = 3.0
GAP_HORIZ = 0.45       # space between glyph and wordmark
GAP_STACK = 0.45



def inner(svg_text):
    """Strip the <svg> wrapper and any non-drawing cruft."""
    body = re.sub(r"^.*?<svg[^>]*>", "", svg_text, flags=re.S)
    body = re.sub(r"</svg>\s*$", "", body, flags=re.S)
    for tag in ("defs", "metadata", "title", "sodipodi:namedview"):
        body = re.sub(rf"<{tag}\b.*?</{tag}>", "", body, flags=re.S)
        body = re.sub(rf"<{tag}\b[^>]*/>", "", body, flags=re.S)
    return body.strip()


def viewbox(svg_text):
    vb = re.search(r'viewBox="([^"]+)"', svg_text).group(1).split()
    return [float(v) for v in vb]


def load(path):
    text = path.read_text()
    return inner(text), viewbox(text)


def compose(glyph_file, word_file, out_name, stacked):
    """Colour comes from the masters themselves, not from this function —
    pairing glyph-black with wordmark-black is what makes a mono variant."""
    g_body, g_vb = load(GLYPH_DIR / glyph_file)
    w_body, w_vb = load(WORD_DIR / word_file)

    g_ar = g_vb[2] / g_vb[3]
    w_ar = w_vb[2] / w_vb[3]

    word_w = CAP * w_ar
    glyph_h = CAP * (GLYPH_H_STACK if stacked else GLYPH_H_HORIZ)
    glyph_w = glyph_h * g_ar

    if stacked:
        gap = CAP * GAP_STACK
        total_w = max(word_w, glyph_w)
        total_h = glyph_h + gap + CAP
        gx, gy = (total_w - glyph_w) / 2, 0.0
        wx, wy = (total_w - word_w) / 2, glyph_h + gap
    else:
        gap = CAP * GAP_HORIZ
        total_w = glyph_w + gap + word_w
        total_h = glyph_h
        gx, gy = 0.0, 0.0
        wx, wy = glyph_w + gap, (glyph_h - CAP) / 2

    # Each master is normalised from its own viewBox into lockup units.
    g_s = glyph_h / g_vb[3]
    w_s = CAP / w_vb[3]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w:.2f} {total_h:.2f}" width="{total_w:.2f}" height="{total_h:.2f}">
  <title>Iron Arachne</title>
  <g transform="translate({gx:.2f} {gy:.2f}) scale({g_s:.6f}) translate({-g_vb[0]:.3f} {-g_vb[1]:.3f})">
    {g_body}
  </g>
  <g transform="translate({wx:.2f} {wy:.2f}) scale({w_s:.6f})">
    {w_body}
  </g>
</svg>
"""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / out_name).write_text(svg)
    print(f"wrote {out_name:34s} {total_w:7.1f} x {total_h:6.1f}  (aspect {total_w/total_h:.2f})")


def main():
    for stacked, label in [(False, "horizontal"), (True, "stacked")]:
        # default: green mark, charcoal type — for light backgrounds
        compose("glyph-green.svg", "wordmark-black.svg", f"lockup-{label}.svg", stacked)
        # green: all-green — for dark backgrounds
        compose("glyph-green.svg", "wordmark-green.svg", f"lockup-{label}-green.svg", stacked)
        # mono: single colour — for one-colour print, engraving, embroidery
        compose("glyph-black.svg", "wordmark-black.svg", f"lockup-{label}-mono.svg", stacked)


if __name__ == "__main__":
    main()
