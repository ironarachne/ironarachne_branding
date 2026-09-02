#!/usr/bin/env python3
"""Regenerate the web icon set from the glyph master.

The previous set was produced by an online favicon generator and had drifted
out of sync with the site's static/ directory (24 of 26 files differed).
Generating them here from logo/glyph makes the branding repo authoritative
and the drift reproducible away.

Every icon is flattened onto charcoal. The brand green is a dark-surface
colour (1.57:1 on white), so a transparent icon on a light tab bar or home
screen fails the one colour rule the guidelines call non-negotiable. The
charcoal square is the mark's native ground and travels with it. iOS also
composites its own mask and handles alpha poorly, so this was already the
rule for the Apple set.
"""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLYPH = ROOT / "logo" / "glyph" / "glyph-green.svg"
GLYPH_SMALL = ROOT / "logo" / "glyph" / "glyph-simple-green.svg"
OUT = ROOT / "logo" / "web-icons"

CHARCOAL = "#1b1e24"
GLYPH_SCALE = 0.82  # glyph height as a fraction of the icon square

# Below this size the full glyph's legs collapse into noise — measured, not
# guessed: on the charcoal backing the spider still reads at 32px, but at
# 16px it is an undifferentiated blob. Icons under 32px use the simplified
# carapace mark instead. (The 64px floor in GUIDELINES.md is for the glyph
# on arbitrary backgrounds, where the keyline has to do the work; here the
# ground is known.)
SIMPLIFY_BELOW = 32

ANDROID = [36, 48, 72, 96, 144, 192]
APPLE = [57, 60, 72, 76, 114, 120, 144, 152, 180]
FAVICON = [16, 32, 96]
MS = [70, 144, 150, 310]


def icon_master(source: Path, out_name: str) -> Path:
    """Square SVG with the given glyph centred."""
    import re

    svg = source.read_text()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    body = re.sub(r"^.*?<svg[^>]*>", "", svg, flags=re.S)
    body = re.sub(r"</svg>\s*$", "", body, flags=re.S)
    body = re.sub(r"<title\b.*?</title>", "", body, flags=re.S).strip()

    size = 512.0
    h = size * GLYPH_SCALE
    w = h * (vb[2] / vb[3])
    s = h / vb[3]
    x, y = (size - w) / 2, (size - h) / 2

    out = ROOT / "logo" / "glyph" / out_name
    out.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
        f'width="512" height="512">\n'
        f'  <title>Iron Arachne</title>\n'
        f'  <g transform="translate({x:.2f} {y:.2f}) scale({s:.6f}) '
        f'translate({-vb[0]:.3f} {-vb[1]:.3f})">{body}</g>\n'
        f"</svg>\n"
    )
    return out


def render(master: Path, size: int, dest: Path) -> None:
    subprocess.run(
        ["rsvg-convert", "-b", CHARCOAL, "-w", str(size), "-h", str(size),
         str(master), "-o", str(dest)],
        check=True,
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    full = icon_master(GLYPH, "icon-master.svg")
    small = icon_master(GLYPH_SMALL, "icon-master-small.svg")
    count = 0

    def pick(size: int) -> Path:
        return small if size < SIMPLIFY_BELOW else full

    for s in ANDROID:
        render(pick(s), s, OUT / f"android-icon-{s}x{s}.png")
        count += 1
    for s in APPLE:
        render(pick(s), s, OUT / f"apple-icon-{s}x{s}.png")
        count += 1
    render(full, 180, OUT / "apple-icon.png")
    render(full, 180, OUT / "apple-icon-precomposed.png")
    count += 2
    for s in FAVICON:
        render(pick(s), s, OUT / f"favicon-{s}x{s}.png")
        count += 1
    for s in MS:
        render(pick(s), s, OUT / f"ms-icon-{s}x{s}.png")
        count += 1

    subprocess.run(
        ["magick", str(OUT / "favicon-16x16.png"), str(OUT / "favicon-32x32.png"),
         str(OUT / "favicon-96x96.png"), str(OUT / "favicon.ico")],
        check=True,
    )
    count += 1

    manifest = {
        "name": "Iron Arachne",
        "short_name": "Iron Arachne",
        "description": "Procedural generators for tabletop roleplaying games.",
        "start_url": "/",
        "display": "standalone",
        "background_color": CHARCOAL,
        "theme_color": CHARCOAL,
        "icons": [
            {
                "src": f"/android-icon-{s}x{s}.png",
                "sizes": f"{s}x{s}",
                "type": "image/png",
                "density": str(s / 48),
            }
            for s in ANDROID
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

    (OUT / "browserconfig.xml").write_text(
        '<?xml version="1.0" encoding="utf-8"?>\n'
        "<browserconfig><msapplication><tile>\n"
        '  <square70x70logo src="/ms-icon-70x70.png"/>\n'
        '  <square150x150logo src="/ms-icon-150x150.png"/>\n'
        '  <square310x310logo src="/ms-icon-310x310.png"/>\n'
        f"  <TileColor>{CHARCOAL}</TileColor>\n"
        "</tile></msapplication></browserconfig>\n"
    )

    print(f"regenerated {count} icons + manifest.json + browserconfig.xml")


if __name__ == "__main__":
    main()
