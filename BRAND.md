# Iron Arachne — Brand Strategy

This is the layer that makes every design decision non-arbitrary. Without it,
"should this be green?" has no answer except taste. Read this before
`GUIDELINES.md`; the rules there are consequences of the positions here.

> **Status:** settled. Positioning, personality, voice, and the reasoning
> behind the identity are decided, and the rules in `GUIDELINES.md` follow from
> them. Settled isn't frozen — revise this when the product outgrows it — but
> changes from here are amendments to a stated position, not blanks being
> filled in. Where the two documents disagree, fix them together.

---

## What Iron Arachne is

A suite of procedural generators for tabletop roleplaying games. It produces
the raw material of a game session — characters, cultures, religions, regions,
settlements, star systems, planets, starships, heraldry — on demand and for
free, in a browser, with no account.

## What Iron Arachne is not

- **Not a virtual tabletop.** It doesn't run your game; it feeds it.
- **Not a system.** It's system-adjacent and generator-first. Where it touches
  a system (Stars Without Number, AD&D), it serves that system rather than
  competing with it.
- **Not an AI content mill.** The output is procedural — rule-driven,
  deterministic where it matters, and inspectable. This distinction is worth
  defending as the market fills with prompt wrappers.
- **Not a walled garden.** No login, no paywall, no drip-feed.

## Who it's for

**Primary — the Game Master preparing under time pressure.** Needs a plausible
settlement in ninety seconds and needs it to hold up under player scrutiny.
Values speed and coherence over depth of customisation.

**Secondary — the worldbuilder without a game.** Building a setting for its own
sake. Values variety, internal consistency, and the ability to keep generating
until something sparks.

**Tertiary — the player.** Rolling a character, naming a homeland. Arrives
through a single generator and mostly leaves through it.

The primary audience implies the whole interface: a generator should produce
something usable on first press, with no configuration required.

## Personality

Four adjectives, in priority order. When they conflict, the earlier wins.

1. **Utilitarian.** The tool gets out of the way. Output first, chrome second.
2. **Craftsmanlike.** Generators are built, not prompted. Rules are visible.
   The classical wordmark says "made deliberately."
3. **Generous.** Free, complete, unmetered. No dark patterns.
4. **Slightly uncanny.** The mark is an iron spider. The palette runs to acid
   green on near-black. This is a tool for inventing worlds, and it should feel
   a little strange — but never at the cost of the first three.

That fourth trait is what stops the brand from being generic developer-tool
minimalism. It's also the one to spend most carefully.

## Voice

**Plain, specific, unceremonious.** Say what a generator makes and what it
doesn't. Prefer the concrete noun to the evocative adjective.

- Write "Generates a settlement with population, government, and notable
  buildings," not "Breathe life into your world."
- Don't oversell randomness as magic. It's a generator; that's enough.
- Second person for instructions, no exclamation marks, no fantasy pastiche in
  UI copy. Save the flavour for generated output, where it belongs.
- Errors state the problem and the fix. No apology, no whimsy.

The generated content can be as purple as the genre demands. The interface
around it stays flat and clear. That contrast is the voice.

## Why the identity looks the way it does

- **The spider mark** predates the current site by roughly a decade and carries
  the only real recognition the brand has. It's kept.
- **Cinzel Decorative** for the wordmark, replacing the original vendor
  lettering. Classical Roman inscriptional forms suit worldbuilding, the face
  is already the site's display type, and it's SIL OFL — so the wordmark is
  finally on licensed, redrawable foundations. See [[typeface-decision]] below.
- **Inclusive Sans** for body and UI, replacing a `system-ui` stack. The output
  is the product and the output is text, so the reading face is not a
  background decision. Also SIL OFL.
- **Acid green on charcoal** is the brand's native environment. The green is a
  dark-surface colour and measurably fails on white (1.57:1); the heavy
  charcoal keyline in every lockup exists to supply the contrast the fill
  cannot. This is a constraint, not a preference.

### Typeface decision

Three faces were in play: the original vendor techno sans (unknown licence,
rasterised only), an ornate 2022 display face (unknown licence, barely used),
and Cinzel Decorative (already shipping on the site, OFL). Cinzel Decorative
won on licensing certainty and on unifying brand with product. The retired
lockups are preserved in `logo/archive/` as brand history.

### Body face decision

The body face was `system-ui, Helvetica, sans-serif` — which is not a choice,
it's the absence of one. It also isn't stable: `system-ui` resolves to a
different face on every operating system, so the one typeface carrying the
majority of the words was whatever the reader's OS happened to supply.

**Inclusive Sans** (SIL OFL 1.1, Olivia King) replaces it, on an argument
specific to what this product outputs. Iron Arachne generates proper nouns that
no reader has seen before — invented settlements, cultures, deities, star
systems. Ordinary body text is forgiving about ambiguous glyphs because context
repairs them; a reader who half-sees "burn" in a familiar sentence recovers it
for free. Generated names get no such help. `Ilyria` and `llyria`, `O5-Vaan`
and `05-Vaan`, `bdellium` with the b and d swapped — for an unfamiliar string
there is nothing to check the reading against, so a glyph that can be confused
will be. Inclusive Sans is designed precisely against those failures:
distinguished I/l/1, non-mirroring b/d/p/q, separated O and 0, open counters,
high x-height.

So this isn't an accessibility gesture bolted onto the brand — it's the face
that best serves the thing the brand exists to deliver. It happens to also be
the accessible choice, which is the trait ordering working correctly:
**utilitarian** first, **generous** third, and the two agreeing.

It stays subordinate to Cinzel Decorative. A neo-grotesque with no display
ambitions was the point of the original `system-ui` instinct; that instinct was
right, and only the execution was lazy. The display face still carries the
character.

Vendored as variable woff2 (roman and italic, 300–700 axis) rather than a pile
of static cuts, for the same reason the repo refuses to accumulate PNG exports.

### Accent colours and setting flavour

The green-on-charcoal core is the brand and never changes. The accent palette
in `tokens/colors.json` exists to solve a different problem: the suite spans
heraldry and starships, and a single acid green applied uniformly makes a
medieval settlement generator and a star system generator feel like the same
screen with different words on it. The accents let an individual generator
carry the flavour of its setting without any of them owning the brand.

The `domain` column is the mapping, and it is deliberate rather than
decorative. It splits along the suite's real seam:

- **Fantasy domains take pigment colours.** Gold, tan, emerald, crimson,
  amethyst — muted, earthy, all darker and less saturated than the brand green.
  These are the colours of materials: leaf, parchment, foliage, blood, dye.
- **Sci-fi domains take emitted-light colours.** Cyan, plasma blue, magenta —
  bright, synthetic, screen-native. These are the colours of things that glow.

That split is the whole trick. A reader never has to be told which half of the
suite they're in; the surface temperature says it.

The rules that keep this from fragmenting the identity:

- **One accent per component**, chosen by domain. A generator gets a colour; a
  page does not get a palette.
- **Accents tint, they don't fill.** Header rules, small icons, category
  labels, focus borders, tags. Never a large field, never body text, never a
  button that competes with the primary action.
- **Accents never touch the identity.** Not the glyph, not the wordmark, not a
  lockup — those recolour only within the constraints in `GUIDELINES.md`. An
  accent may sit near the mark; it may never be applied to it.
- **Green stays the brightest thing on the page.** This costs nothing for the
  fantasy set, which is muted by construction, but the sci-fi three are bright
  enough to compete. Keep them small. If an accent is drawing the eye before
  the generated output does, it's being used at the wrong scale.
- **Charcoal remains the ground everywhere.** The setting changes; the room
  doesn't.

The result is that flavour lives in a thin, disciplined layer on top of a fixed
identity. Swap every accent out and the brand is still intact — which is the
test for whether an accent system is doing its job or quietly becoming the
brand.

This document is the mapping's source of truth. It was not enforced on the site
at the time of writing, so treat any divergence there as site drift to correct,
in the same direction as everything else in this repo.

## Tagline

The tagline for Iron Arachne is "Weave Your Universe."

It does three jobs at once, which is why it beat the plainer candidates.

**"Weave"** is the only word in the brand that the spider earns. The mark is a
decade old and carries the brand's whole recognition, but a spider on its own
is just an animal; weaving is what makes it an apt image for this particular
tool. Procedural generation *is* weaving — separate rule-driven threads for
population, government, terrain, and faith, pulled together into one fabric
that holds. It also quietly says the thing the "not an AI content mill"
position depends on: a weave has visible structure. You can see how it was
made, and you could take it apart.

**"Your"** does the load-bearing work. It puts the user, not the generator, in
possession of the result. Iron Arachne produces raw material for someone else's
game; the tagline should not imply the tool is the author. This is the same
commitment as "it doesn't run your game; it feeds it," compressed to one word.

**"Universe"** covers the full span of the suite without listing it. The
generators run from heraldry to star systems, and any narrower noun — world,
setting, campaign — would quietly exclude half of them.

The obvious objection is that this is the closest the brand comes to breaking
its own voice rule against evocative language. That's accepted deliberately and
bounded tightly: the tagline is the one permitted flourish, sitting beside the
mark. Everywhere else — generator descriptions, buttons, errors — the plain
register holds. A brand is allowed exactly one line of romance, and this is it.

## Scope

**The brand stops at mark, type, and colour.** Sound, motion, and illustration
are deliberately out of scope, and their absence is a position rather than a
gap waiting to be filled.

Each would work against the first personality trait. A tool whose whole promise
is a usable settlement on first press has nothing to gain from an audio
signature, and transitions between a press and its output are latency dressed
up as polish. Illustration is the closest call — an illustrated house style
would be genuinely attractive — but the generators produce text, and pairing
text output with decorative art invites the reader to treat the art as the
product. The mark, the type, and the palette already carry the identity.

This means there is no motion vocabulary, no sound palette, and no illustration
style to specify, and requests for one should be answered with this section.
The accent system is the sanctioned place for visual variety; it's sufficient.

Revisit only if the product grows a dimension that genuinely needs it.
