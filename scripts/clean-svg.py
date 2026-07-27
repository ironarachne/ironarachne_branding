#!/usr/bin/env python3
"""Strip Inkscape/Sodipodi editor cruft from the SVG masters.

Editor metadata (sodipodi:nodetypes, inkscape:connector-curvature, RDF
license blocks, namedviews) bloats the files and breaks composition when the
drawing content is lifted out of its original <svg> wrapper. None of it
affects rendering.
"""

import re
import sys
from pathlib import Path

NS_ATTR = re.compile(r'\s+(?:sodipodi|inkscape|rdf|cc|dc):[\w-]+="[^"]*"')
BLOCK = re.compile(
    r"<(sodipodi:namedview|metadata|defs)\b.*?</\1>|<(sodipodi:namedview|defs)\b[^>]*/>",
    re.S,
)
NS_DECL = re.compile(r'\s+xmlns:(?:sodipodi|inkscape|rdf|cc|dc)="[^"]*"')


def clean(path: Path) -> None:
    before = path.read_text()
    after = BLOCK.sub("", before)
    after = NS_ATTR.sub("", after)
    after = NS_DECL.sub("", after)
    after = re.sub(r"\n\s*\n+", "\n", after)
    path.write_text(after)
    saved = len(before) - len(after)
    pct = saved / len(before) * 100 if before else 0
    print(f"{path.name:24s} {len(before):>7} -> {len(after):>7} bytes  (-{pct:.0f}%)")


if __name__ == "__main__":
    targets = [Path(p) for p in sys.argv[1:]]
    if not targets:
        sys.exit("usage: clean-svg.py FILE...")
    for t in targets:
        clean(t)
