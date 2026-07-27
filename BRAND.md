# Iron Arachne — Brand Strategy

This is the layer that makes every design decision non-arbitrary. Without it,
"should this be green?" has no answer except taste. Read this before
`GUIDELINES.md`; the rules there are consequences of the positions here.

> **Status:** first draft, derived from the product itself rather than from a
> stated strategy. The positioning and voice sections are inferences that you
> should correct — they're written to be argued with, not accepted.

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

## Open questions

- Is there a tagline? "Procedural Generators for Tabletop Games" was baked into
  the retired banner. It's accurate but flat, and nothing currently uses it.
- Does the accent palette have a documented mapping to generator families, or
  is the domain column in `tokens/colors.json` an invention? It reads as
  sensible but should be confirmed against the site.
- Is there a sound, motion, or illustration dimension worth defining, or does
  the brand stop at mark, type, and colour?
