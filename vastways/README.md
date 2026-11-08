# Vastways

Vastways is a browser-based workshop for building tabletop role-playing worlds by Iron Arachne.
The tagline is “Build worlds for the table.”

## Artwork

The outlined Fenwick Woodtype Regular artwork comes from the approved prototype in
[the app repository](https://github.com/ironarachne/ironarachne/tree/a571fad40239bc1c643e161fb8823a6ddd52234f/branding/logo).
Use the horizontal lockup in the top bar, the stacked lockup in the home hero, and the simplified
bloom at icon sizes.

Use the plum and copper lockups on ivory. Use the reversed ivory and copper variants on dark
surfaces. One-colour versions are available in plum and ivory. Keep clear space of at least half
the height of the central star around the visible artwork. Keep the wordmark at least 20 CSS
pixels high in the app header and the stacked lockup at least 180 CSS pixels wide in the hero.
Use the simplified mark when the header cannot fit the wordmark at that size. The browser icons
place the ivory mark on plum with room for a platform mask.

## Colour and type

The primary palette is plum (#352038), copper (#B76A36), and ivory (#FCF8F0). Use ivory for
readable text on plum and the lighter copper link token for interactive text. The supporting
palette provides separate tokens for keyboard focus, control edges, and statuses. Measure
contrast on the rendered surface, including genre panels and interactive states.

The outlined wordmark ships as SVG. Inclusive Sans is the body and control face. Cinzel
Decorative is the app's display face. The two OFL notices are in the font directory.

## Distribution

The app pins a commit of this tree for its logos, browser metadata and icons, fonts, and colour
tokens. The studio's assets live outside this tree and use a separate pin. Update the source
here and run the app's asset sync to pick up an approved version.

Run bash vastways/build_web_assets.sh from the repository root after editing the favicon or
social-card SVG. The script uses librsvg and ImageMagick. The web manifest lives alongside
the generated browser icons.
