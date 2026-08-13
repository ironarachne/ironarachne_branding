# Iron Arachne — Usage Guidelines

Rules for using the marks. Every number here was measured against the actual
artwork, not chosen by eye — where a threshold exists, the reason is given.

For the reasoning behind the identity itself, see [`BRAND.md`](BRAND.md).

---

## Which file do I use?

| Situation | File |
|---|---|
| Default, anywhere horizontal space allows | `logo/primary/lockup-horizontal.svg` |
| Narrow or square space (cards, posters, avatars) | `logo/primary/lockup-stacked.svg` |
| On a dark surface | `…-green.svg` variants |
| One-colour printing, engraving, embroidery | `…-mono.svg` variants |
| Icon, avatar, favicon — 64px and above | `logo/glyph/glyph-green.svg` |
| Icon below 64px | `logo/glyph/glyph-simple-green.svg` |
| Type alone, no spider | `logo/wordmark/wordmark-*.svg` |
| Web/app icons, already generated | `logo/web-icons/` |

Everything is SVG. Generate rasters at the size you need rather than committing
new PNGs — the repo previously accumulated a dozen arbitrary export sizes.

## Minimum sizes

Below these the artwork stops resolving. These are floors, not targets.

| Asset | Screen | Print |
|---|---|---|
| Horizontal lockup | **200 px** wide | 35 mm wide |
| Stacked lockup | **140 px** wide | 25 mm wide |
| Full glyph | **64 px** tall | 12 mm |
| Simplified glyph | **16 px** tall | 4 mm |

**Why 64px for the full glyph.** Below it the legs and gears merge into a solid
shape: at 32px the gears are indistinct, and at 16px the mark is an
undifferentiated blob with no spider legible at all. The simplified glyph —
the carapace and star alone — is drawn from the same artwork and holds down to
16px. `scripts/build-icons.py` switches between them automatically.

## Clear space

Keep clear on all four sides:

- **Lockups:** half the glyph's height. In the horizontal lockup that equals
  the wordmark's cap height, which is the easiest thing to eyeball.
- **Glyph alone:** 25% of the glyph's width.

Nothing enters this zone — no text, no rules, no photo edges, no other logos.

## Colour

Use the tokens in [`tokens/colors.css`](tokens/colors.css). Don't hardcode hex
values; the site and this repo already drifted apart once.

**The green is a dark-surface colour.** Measured against WCAG 2.1:

| | on white | on charcoal |
|---|---|---|
| `--ia-green` `#76e841` | **1.57 ✗** | 10.65 ✓ |
| `--ia-green-acid` `#9eff5b` | **1.24 ✗** | 13.44 ✓ |

Consequences, which are not negotiable:

- **Never set green text on white.** It fails AA by a wide margin.
- **The charcoal keyline is structural.** On light backgrounds the green fill
  only reads because the outline carries the contrast. Don't remove it, don't
  lighten it, don't replace it with the green.
- On dark surfaces the green may be used freely, including for text.
- Use `--ia-charcoal` `#1b1e24`, never `#000000`. Pure black flattens the
  keyline against the green and reads harsh on screen.

## Typography

**Cinzel Decorative** (SIL OFL 1.1, Natanael Gama) — wordmark and display
headings. The wordmark ships as outlines, so the font isn't needed to render
it. Only install the font if you're setting new display text.

**Inclusive Sans** (SIL OFL 1.1, Olivia King, v2.004) — body copy and UI.
Vendored in `fonts/` as variable woff2, roman and italic, with a 300–700 weight
axis. Two files cover every weight; don't add static cuts.

```css
@font-face {
  font-family: "Inclusive Sans";
  src: url("fonts/InclusiveSans-Variable.woff2") format("woff2-variations");
  font-weight: 300 700;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Inclusive Sans";
  src: url("fonts/InclusiveSans-Italic-Variable.woff2") format("woff2-variations");
  font-weight: 300 700;
  font-style: italic;
  font-display: swap;
}
```

Stack: `"Inclusive Sans", system-ui, Helvetica, sans-serif`. Keep the fallbacks
— the font is a body face and the page must stay readable before it loads.

Use real weights from the axis rather than letting the browser synthesise them,
and use the italic file rather than letting it slant the roman. Faux bold and
faux italic undo the legibility work this face was picked for.

Never set the wordmark by typing "Iron Arachne" in Cinzel Decorative. Use the
outlined file — the master has tracking applied that live text won't match.

## Misuse

Don't:

- Recolour the glyph outside `--ia-green`, `--ia-green-acid`, charcoal, or a
  single flat colour in the mono variants
- Stretch, squash, rotate, or shear either element
- Rebuild a lockup by hand — the spacing comes from `build-lockups.py`
- Add effects: drop shadows, bevels, gradients, glows, outer strokes
- Place a lockup on a busy photo without a solid or scrimmed backing
- Set the wordmark in any face other than Cinzel Decorative
- Use the retired lockups in `logo/archive/` for anything new

## Rebuilding

```sh
python3 scripts/build-wordmark.py   # outlines the wordmark from the font
python3 scripts/build-lockups.py    # composes horizontal + stacked lockups
python3 scripts/build-icons.py      # regenerates the web icon set
```

Run all three after changing a master. Cinzel Decorative is vendored in
`fonts/` with its licence, so the repo rebuilds standalone — nothing needs to
be installed and the site repo doesn't need to be checked out.

Requires Python 3 with `fonttools`, plus `rsvg-convert` and ImageMagick.

## Keeping the site in sync

`logo/web-icons/` is the source of truth for the site's `static/` directory.
These drifted apart before — 24 of 26 files differed — because icons were
generated once by an online tool and then edited in place on both sides. Copy
from here to the site; never the other direction.
