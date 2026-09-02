# Iron Arachne Branding

Brand strategy, identity system, and logo assets for
[Iron Arachne](https://ironarachne.com) — procedural generators for tabletop
roleplaying games.

## Start here

| | |
|---|---|
| [`BRAND.md`](BRAND.md) | Positioning, audience, personality, voice — why the identity is what it is |
| [`GUIDELINES.md`](GUIDELINES.md) | Which file to use, minimum sizes, clear space, colour rules, misuse |
| [`tokens/`](tokens/) | Colour tokens as CSS and JSON — the single source of truth |
| [`specimen.html`](specimen.html) | Every asset rendered on one page — open it after a rebuild |

## Layout

```
BRAND.md            strategy: the decisions everything else follows from
GUIDELINES.md       usage rules, all measured against the artwork
specimen.html       visual check: lockups, sizes, icons, palette, type
tokens/
  colors.css        CSS custom properties, with contrast notes
  colors.json       machine-readable twin
logo/
  primary/          horizontal + stacked lockups (green / black / mono)
  glyph/            spider mark alone, plus the simplified small-size mark
  wordmark/         outlined type alone
  web-icons/        generated favicon + app icon set, all on charcoal
  src/              editable masters (Affinity, Photoshop, legacy SVG)
  archive/          retired marks, kept as brand history
fonts/              Cinzel Decorative + Inclusive Sans, vendored with licences
scripts/            build scripts — see GUIDELINES.md § Rebuilding
```

## Quick facts

- **Brand green** `#76e841` — a dark-surface colour. It fails WCAG on white
  (1.57:1); the charcoal keyline is what makes the mark work on light
  backgrounds. See [`GUIDELINES.md`](GUIDELINES.md#colour).
- **Wordmark** is Cinzel Decorative (SIL OFL), shipped as outlines so the font
  isn't needed to render it. The font is vendored in `fonts/` for rebuilds.
- **Body text** is Inclusive Sans (SIL OFL), vendored as variable woff2. Picked
  for character-level legibility, because generated names give the reader no
  context to disambiguate glyphs from. See
  [`GUIDELINES.md`](GUIDELINES.md#typography) for the `@font-face` block.
- **Everything is SVG.** Generate rasters at the size you need; don't commit
  new fixed-size exports.

## Licensing

The Iron Arachne name and marks are project assets, not open-licensed artwork.

Both vendored fonts are SIL OFL 1.1, each with its licence text alongside it in
`fonts/` as OFL clause 2 requires.

**Cinzel Decorative** — Natanael Gama, `fonts/OFL-CinzelDecorative.txt`. The
wordmark outlines derive from it, which the licence permits; the Reserved Font
Name restriction applies to the font software, not to artwork set in it.

**Inclusive Sans** — Olivia King, `fonts/OFL-InclusiveSans.txt`. Upstream is
[LivKing/Inclusive-Sans](https://github.com/LivKing/Inclusive-Sans); the
vendored files are v2.004, renamed from upstream's `InclusiveSans[wght].woff2`
and `InclusiveSans-Italic[wght].woff2` so the paths are URL-safe. This font
declares no Reserved Font Name.
