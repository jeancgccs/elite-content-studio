# AI Toolkit Integration

How to weave AI tools into a creator workflow. Two rules govern everything:

1. **AI accelerates; the creator's taste and truth decide.** Anything factual an
   AI produced gets verified; anything voice-like gets rewritten into the
   creator's voice. Recommend disclosure where platforms require it (e.g.
   synthetic media that could mislead) and honesty everywhere it builds trust.
2. **Recommend the tool the creator already has** before suggesting new
   subscriptions. Ask what's in their stack during intake.

If media-generation MCP tools are connected in the current session (image, video,
voice, music generation), offer to produce the asset directly instead of just
writing a prompt for an external tool.

## Where AI fits in the 9 phases

| Phase | High-leverage AI use |
|---|---|
| Research | LLM/Perplexity-style tools for landscape maps and FAQ mining (verify claims); transcript analysis of competitor videos |
| Brainstorm | Idea permutation and angle generation — human picks, rubric ranks |
| Packaging | Thumbnail mockups (Midjourney/Flux/Leonardo/Nano Banana-class tools); title variant generation |
| Script | Draft acceleration, restructuring, tightening — creator rewrites for voice |
| Production | AI b-roll (Runway/Veo-class) for abstract/impossible shots; TTS scratch-tracks for timing edits |
| Editing | Auto-captions, silence removal, auto-reframe (CapCut/Premiere/Resolve/Descript-class features); music generation (Suno-class) for license-safe beds |
| Publishing | Metadata drafts, chapter generation from transcript, translation/dubbing (ElevenLabs-class) |
| Promotion | Clip identification from transcript; per-platform caption rewrites |
| Analysis | Comment-theme clustering from exported comments |

## AI-first production (creators generating most or all assets with AI)

Many creators now build entire videos with AI tools — Higgsfield, Google Flow
(Veo-based filmmaking), Runway, Kling, Pika for video; Midjourney/Flux/Leonardo
for stills; Suno for music; ElevenLabs for voice. When the intake reveals this
(always ask), treat prompts as production deliverables, not suggestions:

- **Deliver a complete AI Asset Prompt Pack** (`assets/ai-asset-prompt-pack.md`)
  with every project: one paste-ready prompt for every visual beat in the script,
  thumbnail prompts per concept, plus music brief, VO direction, and SFX list.
  The creator should be able to go from script to finished asset set without
  writing a single prompt themselves.
- **Consistency is the craft.** Disconnected pretty shots read as slop; a
  consistent world reads as a produced video. Enforce: (1) one **style anchor**
  line reused verbatim in every prompt; (2) recurring characters/sets generated
  once as stills, then reused as reference images and animated via
  image-to-video — not re-described in text each time; (3) seeds/reference
  features reused where the tool supports them.
- **Image-first workflow**: still (cheap, controllable) → approve → animate.
  Text-to-video is the fallback for motion-defined shots, not the default.
- **No text in AI images — overlay type separately.** This is a hard rule for
  every generated still (thumbnails, channel art/banners, carousel slides), not
  just video frames: models garble spelling and letterforms, and baked-in text
  can't be edited, localized, or A/B-swapped without regenerating the art.
  Prompt for negative space where the type will sit, add "no text, no words,
  no letters" to the negatives, and set the type in Canva/Photoshop/the editor.
- **Plan for the medium's limits**: generate 4–8s clips and cut fast (matches
  retention pacing anyway); the no-text rule above applies doubly to video
  frames; design shots to hide known artifact zones (hands, crowds, physics);
  keep A-cam/talking-head real where audience trust depends on it.
- **Photograph what you own; generate what you can't shoot.** If the physical
  object is in the creator's hands — a product, their gear, their space — a
  phone photo beats a generation: it's free, label-accurate, and animates just
  as well via image-to-video. Reserve generation for what can't be filmed.
- **Aspect discipline**: generate at the target ratio per platform (16:9 YouTube,
  9:16 Shorts/Reels/TikTok) rather than cropping after.
- **Hard constraints go in parameters, not prose**: when the tool exposes a
  setting (duration, aspect ratio, seed, voice ID), set it there — "make it
  30 seconds" written in the prompt gets approximated or ignored; a duration
  parameter is obeyed.
- **Disclosure**: realistic synthetic media may require platform disclosure
  (e.g. YouTube's altered-content flag) — include the check in the pack.
- **Audio is half the production**: for narration-driven and faceless channels,
  the ElevenLabs-class VO pipeline and Suno-class section-mapped scoring (see
  the Voice and Music prompt patterns below) get the same rigor as visuals —
  chunked VO with locked voice settings, per-section music, and a reusable
  sound-branding theme, all delivered in the prompt pack.
- **Storyboard before you animate**: for narrative or multi-scene videos, map
  the story beats (setup → inciting moment → escalation → climax → resolution)
  to one keyframe each, generate all keyframes as stills first, approve the set,
  then animate. Continuity errors are cheap to fix at the still stage and
  expensive after animation.
- **The brief is the contract** (multi-scene projects): before any generation is
  spent, write a one-page production brief — concept + target length, the beat
  list, per-beat tool routing (which model/tool handles which shot type), the
  audio plan (VO/music/SFX), and the deliverables list with ratios — and get it
  approved. Generate only what the brief specifies; scope changes go back
  through the brief, not into ad-hoc extra generations. Don't over-decompose:
  plan in beats, not micro-shots — a 60-second video is 8–12 beats, not 40 rows.
- If media-generation MCP tools are connected to the session, offer to run the
  pack's prompts directly and deliver finished assets.

### Sponsored / UGC ad workflow (AI-generated brand content)

When a creator lands a sponsorship or makes TikTok Shop / affiliate content,
AI can produce the ad without a shoot. The reliable pipeline is two-stage:

1. **Hero image first**: fuse a real photo of the creator + a clear product
   photo (neutral background, logo legible) in an image-edit model that accepts
   multiple reference images. Direct the fusion explicitly: wearable products
   are *worn* naturally, handheld products are *held or applied* naturally; the
   product is the focal point and its logo/text stays readable; the setting
   matches real use (serum → bathroom counter, not a void). Keep the creator's
   face unchanged — audiences follow the person. The no-text rule applies: the
   product's own label is the only text in frame; any headline or CTA is
   overlaid in the editor, never generated.
2. **Approve, then animate**: only after the creator approves the hero image,
   run image-to-video (9:16, with native audio where the model supports spoken
   dialogue). Direct it as one uninterrupted handheld-feel shot, person
   addressing camera with natural gestures — cuts and camera changes are where
   these models break.

For product-only b-roll shots (bottle on the counter, texture close-ups),
prefer real phone photos of the product the creator already has — they're
label-accurate by definition and animate as well as generated stills. Save
generation for the shots that need the creator *in* them.

Constraints that make or break it: keep the spoken script to 1–2 sentences per
~10-second clip (video models compress or clip longer dialogue); for longer ads,
generate several hero-image variations and animate each as its own clip rather
than asking for one long take. Disclosure is double here: the sponsorship
itself (platform paid-promotion flags, #ad) AND the synthetic-media flag —
an AI video of a real person endorsing a product is exactly what disclosure
rules target.

## Prompt patterns (adapt values, keep structure)

### Thumbnail image prompt (Midjourney/Flux/Leonardo style)

```
[SUBJECT with EMOTION], [FRAMING e.g. chest-up, facing camera-left],
[BACKGROUND — simple, high contrast with subject], [LIGHTING e.g. soft key +
rim light], [STYLE e.g. photorealistic, vibrant], bold color palette of
[BRAND COLORS], negative space [LEFT/RIGHT] for text, 16:9 --no clutter,
small details, text, words, letters
```

Keep faces real where trust matters: composite the creator's photographed face
over AI backgrounds rather than generating fake faces of them.

### AI b-roll prompt (Runway/Veo style)

```
[SHOT SIZE] of [SUBJECT/ACTION], [CAMERA MOVE e.g. slow push-in],
[SETTING + TIME OF DAY], [MOOD/LIGHTING], [LENS/FILM LOOK], 4–8s, no text
```

Use AI b-roll for concepts you can't film (space, history, abstractions);
use real footage for anything the audience expects to be real.

### Voice — the AI narration pipeline (ElevenLabs-class)

For narration-driven and faceless channels the voiceover IS the performance, so
direct it like one:

- **Chunk the script by section**, one generation per chunk — flubbed lines get
  regenerated individually instead of redoing a 10-minute take, and pacing can
  differ per section.
- Per chunk provide: the exact text, target pace (slower for reveals and key
  numbers), an emotional read ("confident, slight smile; drop to near-whisper
  on the reveal"), and pause markers. Where the tool supports inline emotion/
  delivery tags, use them sparingly — over-tagged reads sound theatrical.
- **Pronunciation guide**: spell out names, brands, and jargon phonetically once
  and reuse it in every chunk that contains them.
- **Lock voice settings** (voice + stability/expressiveness values) in the pack
  and reuse them verbatim across the whole video — and the whole channel; a
  consistent voice is audio branding.
- Write for the ear before generating: read the script aloud mentally, shorten
  sentences, add contractions — TTS exposes written-not-spoken prose instantly.
- **Punctuation is pacing direction.** TTS runs the text verbatim, so proof each
  final chunk as a performance script, not prose: commas, periods, and ellipses
  are pacing instructions the model obeys literally — a stray comma changes the
  cadence of the read.
- **Dubbing/translation**: for multi-language channels, dub top evergreen
  winners first (proven demand), keep on-screen text minimal in the master so
  dubs don't fight burned-in text.
- Consent rules: clone only the creator's own voice; disclose AI narration where
  the audience would reasonably assume it's human and trust depends on it.

### Music — score, don't wallpaper (Suno-class)

```
[GENRE], [TEMPO/BPM feel], [MOOD ARC e.g. curious build → confident payoff],
instrumental, no vocals, loopable, [DURATION], understated enough to sit under speech
```

- **Map tracks to script sections** (hook / teaching beds / montage / payoff /
  outro) rather than one track for the whole video — the music change at section
  boundaries doubles as an invisible pattern interrupt.
- Match BPM feel to the edit's cut rhythm so cuts can land on beats.
- **Match structure to duration**: under ~30s = one section, no arc; 30–90s =
  intro + body; 90s+ = a full arc. Don't ask for a three-act build-and-payoff
  in a 15-second hook bed — the model will cram it and everything rushes.
- **Describe the sound, not the artist**: use genre/era/instrumentation words —
  many generators (Suno-class included) reject or silently strip artist names
  from prompts.
- **Sound branding**: generate one short intro/outro theme and reuse it across
  every video — audio recognizability compounds like visual branding. Regenerate
  variations from the same prompt to refresh without losing identity.
- Always instrumental under speech; save anything with vocals for montages
  where no one is talking.
- **SFX**: AI sound-effects generation (ElevenLabs SFX-class) covers whooshes,
  ambience, and UI sounds — describe the sound plus its energy ("short bright
  whoosh, subtle") and mix low.
- Generated music avoids licensing strikes, but check the tool's commercial-use
  terms match the creator's monetization.

## Tool-stack quick map

- **Writing/research**: Claude, ChatGPT, Gemini, Perplexity — drafts, angles,
  summaries; verify facts independently.
- **Image**: Midjourney, Flux, Leonardo, Nano Banana, Whisk, Canva AI, Photoshop
  generative tools — thumbnails, carousel art, channel art.
- **Video gen**: Runway, Google Veo / Google Flow, Higgsfield, Kling, Pika —
  b-roll, transitions, concept shots, full AI-first production.
- **Voice/audio**: ElevenLabs (VO, dubbing), Suno (music).
- **Editing**: CapCut (fast vertical + captions), Premiere Pro / DaVinci Resolve /
  Final Cut (long-form), Filmora (beginner-friendly), OBS (recording/streaming).
- **Ops**: Notion/Google Docs for pipelines and script review, Google Drive for
  asset handoff; suggest a simple pipeline board (Idea → Research → Script →
  Shoot → Edit → Publish → Promote → Analyze) matching the 9 phases.

## Anti-patterns to warn about

- Fully AI-generated faceless spam channels — platforms increasingly suppress
  mass-produced low-originality content; originality and human perspective are
  the moat.
- AI voice narrating content the audience believes is the creator speaking —
  trust damage outweighs time saved; disclose or don't do it.
- Publishing unverified AI "facts" — one confident hallucination in a video can
  cost years of credibility.
