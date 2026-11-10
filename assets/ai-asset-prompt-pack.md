# AI Asset Prompt Pack: [Video Title]

<!-- Fill this for every project where the creator generates assets with AI
(Higgsfield, Google Flow/Veo, Runway, Kling, Midjourney/Flux, Suno, ElevenLabs…).
Every prompt must be paste-ready: no unexplained placeholders left behind. -->

**Target platform & aspect**: [16:9 / 9:16 / both — list every deliverable ratio]
**Tools in the creator's stack**: [image gen / video gen / music / voice tools]

## Style anchor (paste into EVERY visual prompt, verbatim)

> [One reusable line locking the look: art direction, lighting, color palette,
> lens/film feel, mood — e.g. "cinematic photorealism, soft golden-hour key
> light, teal-and-amber palette, 35mm shallow depth, subtle film grain"]

**Consistency plan**: [character/set reference strategy — reference images or
character sheet to reuse, image-first-then-animate for recurring subjects,
seed/reference reuse where the tool supports it]

**No-text rule**: every visual prompt in this pack carries "no text, no words,
no letters" in its negatives. All type — titles, captions, labels, channel-art
text — is overlaid in the editor/Canva, never generated: models garble
letterforms, and baked-in text can't be edited or localized.

## Thumbnail prompts (one per packaging concept, 16:9)

**Concept [n] — [handle]**
```
[SUBJECT + EMOTION], [FRAMING], [BACKGROUND], [LIGHTING], {style anchor},
negative space [side] for text, 16:9 --no [clutter/artifacts to exclude],
no text, no words, no letters
```
*Post note*: add title text in Canva/Photoshop — never ask the AI to render text.

## Scene & B-roll generation list (numbered to the script)

| # | Script ref | Asset prompt (paste-ready) | Motion/animate prompt (if image→video) | Ratio | Length |
|---|---|---|---|---|---|
| 1 | [mm:ss] | [full prompt incl. style anchor] | [camera move + subject motion, e.g. "slow push-in, steam rising"] | [16:9] | [4–8s] |
| 2 | ... | ... | ... | ... | ... |

*Every VISUAL beat in the script that isn't A-cam or screen recording gets a row.*

## Motion graphics / text animation prompts
- [element]: [prompt or editor recipe — keep text rendering in the editor]

## Music generation (Suno-class) — one track per section, not one per video

**Sound branding**: [intro/outro theme prompt — reuse across every video]

| # | Script sections | Track prompt (paste-ready) | BPM feel | Length | Loopable |
|---|---|---|---|---|---|
| 1 | [hook] | [genre, mood, instrumentation, instrumental, no vocals, {energy}] | [...] | [...] | [y/n] |
| 2 | [teaching bed] | ... | ... | ... | ... |
| 3 | [payoff] | ... | ... | ... | ... |

*All beds instrumental; match BPM feel to the edit's cut rhythm; structure
follows duration (under ~30s = one section, 30–90s = intro + body, 90s+ =
full arc); genre/era/instrumentation words, never artist names; set length
via the tool's duration parameter, not in the prompt text; check the tool's
commercial-use terms.*

## Voiceover generation (ElevenLabs-class) — chunked for regeneration

**Voice**: [creator's cloned voice (with consent) / library voice + why]
**Locked settings**: [voice + stability/expressiveness values — reuse verbatim
channel-wide; this is audio branding]
**Pronunciation guide**: [name/term → phonetic spelling, reused in every chunk]

| Chunk | Script section | Emotional read & pace | Pause/emphasis notes |
|---|---|---|---|
| 1 | [00:00 hook] | [e.g. urgent, leaning-in, slightly faster] | [pause after "..."; punch "..."] |
| 2 | [setup] | ... | ... |

*One generation per chunk — regenerate flubs individually. Read each chunk
aloud mentally first; shorten anything that reads written-not-spoken. Proof
punctuation as pacing: TTS obeys commas, periods, and ellipses literally —
a stray comma changes the cadence.*

## SFX list (ElevenLabs SFX-class or library)
- [mm:ss] [sound + energy, e.g. "short bright whoosh, subtle"] — [generation
  prompt or library search term] — mix low

## Sponsored / UGC ad block (only if this project includes brand content)

**Reference inputs**: [creator photo (face + upper body) + product photo
(neutral background, logo legible)]

**Hero image prompt (image-edit model, both references, 9:16)**
```
Ultra-realistic lifestyle photo of {creator} with {product} in [SETTING that
matches real product use]. [Worn naturally if wearable / held or applied
naturally if handheld]. Product is the focal point, logo/text legible.
Creator's face unchanged. No added text, captions, or graphics. {style anchor},
soft natural light, shallow depth, 9:16
```
*No-text rule here too: the product's own label (from the reference photo) is
the only text in frame — any headline/CTA gets overlaid in the editor.*
*Gate: creator approves the hero image BEFORE any video generation is spent.*

**Ad clip prompt (image-to-video from approved hero, 9:16, native audio)**
```
Single uninterrupted handheld-feel shot, ~10s. Person looks at camera,
relaxed, natural hand gestures with the product, and says: "[1–2 sentence
script — no more per 10s clip]". No cuts, no on-screen text. Ends with a
small smile or nod.
```
*Longer ad? Generate hero-image variations and animate each as its own clip.*

**Disclosure (both required)**: [ ] paid-promotion flag / #ad  [ ] synthetic-
media flag (AI video of a real person endorsing a product)

## Regeneration troubleshooting
- Wrong composition → restate framing FIRST in the prompt; simplify to one subject.
- Character drift → return to the reference image; animate stills instead of
  re-prompting text-to-video.
- AI artifacts (hands, text, physics) → add to negatives; cut the shot shorter;
  or swap to an angle that hides the weakness.
- Style drift across shots → confirm the style anchor is verbatim in every prompt.
- When delivering any generated asset, name one concrete variation knob the
  creator can turn ("swap tempo 92→108 BPM", "push framing to a close-up") —
  never "regenerate for something different."

## Disclosure check
- [ ] Realistic synthetic media flagged per platform rules (e.g. YouTube's
      altered-content disclosure); AI voice of a real person only with consent.
