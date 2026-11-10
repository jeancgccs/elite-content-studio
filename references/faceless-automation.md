# Faceless & Automated Pipelines

Read when the creator runs a faceless channel, uses a one-command video
pipeline (script → TTS → stock visuals → render → upload tools, n8n/Make
workflows, open-source "YouTube automation" repos), asks to "automate my
channel", or brings auto-generated output for review.

The stance: automate the tedium, keep the decisions. Rendering, captions,
file prep, metadata formatting, and credit lines are tedium. Topic choice,
angle, packaging, factual sign-off, and the final watch-through are decisions,
and they are what make a video worth watching. Pipelines that automate the
decisions produce the uploads platforms demonetize and viewers skip.

## The monetization risk, stated plainly

YouTube's Partner Program excludes mass-produced or repetitive content from
monetization; enforcement was tightened on July 15, 2025 (widely reported as
the "inauthentic content" update). This is not a ban on AI or on faceless
channels. The risk is a channel whose uploads are near-identical templates.
Policy wording changes, so check the current YPP policy page before giving
specific advice, and say when you haven't.

**The template test**: swap the topic out. Would most of the video stay the
same: section order, re-hook lines, CTA wording, stock look, voice cadence,
thumbnail layout? If yes, it reads as templated to viewers and to reviewers.

Cheap distinctiveness levers, in order of impact:
1. A point of view: an opinion, a ranking, a "here's what I'd do" per video.
2. Some original visuals in every video: screen recordings, diagrams or maps
   made for this video, a photographed object, a recurring set.
3. Structure chosen per topic (`scriptwriting.md` structures), not one
   skeleton for every upload.
4. A human-written hook and payoff, even when the middle is drafted by AI.
5. Real sources, cited in the description.

## Human checkpoints (the minimum)

- [ ] Topic + angle approved, checked against the channel profile's
      Covered topics list (no accidental repeats; repeats are sequels on purpose)
- [ ] Title + thumbnail pair approved **before** render (packaging first, as everywhere)
- [ ] Claim ledger signed off (`scriptwriting.md` fact-grounding pass)
- [ ] Script read aloud or humanizer-linted (`tools/humanizer_lint.py`)
- [ ] Full watch-through at 1× before publish: wrong stock clip, mispronounced
      names, captions out of sync, a visual that contradicts the narration
- [ ] Upload checklist, including AI and paid-promotion disclosures

Never wire a pipeline to auto-publish. Scheduling an upload after the
watch-through is fine.

## Fact-grounding: where pipelines fail first

Automated scripts fill gaps with confident fiction, and narration makes a
wrong number sound authoritative. Every factual script gets the claim ledger
from `scriptwriting.md`. Source order for grounding:

1. **Primary**: the paper, the official dataset, the agency page, the
   product's documentation, the court record.
2. **Reputable secondary**: encyclopedias and quality journalism. Good for
   orientation and for finding the primary source; for numbers, cite what
   they cite.
3. **Never as a source**: other YouTube videos, AI chat answers, content farms.

Speculation is allowed and often the most interesting part. Say on air that
it's speculative and whose idea it is.

## Visual sourcing ladder (faceless)

Work down the ladder; each rung adds licensing work or originality risk.

1. **Shoot or screen-record it.** Original footage is the strongest
   originality signal and is licensed by definition.
2. **Make it.** Diagrams, maps, charts, and text cards built for this video
   (Canva, slides, HTML). Text stays crisp and editable.
3. **Public domain.** Much US federal agency media (NASA, NOAA, USGS) is
   public domain, but check each item's page: some are third-party, and
   agency logos and implied endorsement are restricted.
4. **Free-license stock** (Pexels, Pixabay and similar): commercial use
   without attribution under their current licenses, with limits on
   identifiable people, brands, and reselling unmodified files. Read the
   license page once and note its date.
5. **Creative Commons** (Openverse searches across sources): CC0 and CC BY
   work with per-item attribution; CC BY-SA adds share-alike terms; avoid
   NC on a monetized channel; avoid ND if you crop, grade, or animate it.
6. **AI-generated**, for what can't be filmed or found. No text in the image
   (`ai-toolkit.md`), and disclose realistic synthetic media.

Keep an **asset log** as you download, not after: file, source, license,
author, link. Build the description's credits block from the log. Writing
credits from memory is how attribution goes missing.

## Pacing narration over visuals

- A still frame holds attention for far less time than a talking face.
  Plan visuals per idea or per sentence, not per section. The 20-second
  no-change ceiling in `editing.md` is far too loose for faceless work.
- Give each section three visually distinct shots: context (wide), detail
  (close), and concept (diagram, metaphor, abstract). Three near-identical
  stock clips read as one long shot.
- Match the visual to the exact noun being spoken. Mismatched stock (wrong
  animal, wrong city, wrong decade) is the most common faceless tell.
- Motion on stills (slow push-ins and pans) helps; the same push-in on every
  image becomes its own template tell. Vary direction, speed, and framing.

## Voice and runtime

TTS speed is fixed per voice, so runtime is arithmetic: generate one chunk,
time it, compute words per minute, then run `tools/script_timing.py --wpm N`
for real section timestamps, payoff position, and paste-ready chapters.
Voice direction and chunking follow `ai-toolkit.md`.

## Prompt hygiene for pipeline builders

Automation prompts tend to hardcode the same lines into every script. Fix:

- **No stock re-hook phrases.** Re-hook beats are planned from each video's
  content. A fixed "but here's where it gets weird" at the same minute in
  every upload is the template test failing out loud.
- **CTAs must be true.** Don't script "I read every comment" for a channel
  where nobody reads them. Viewers check, and it costs trust.
- **No named-creator imitation in prompts** ("write like [famous channel]").
  Describe the craft qualities you want (clear analogies, escalating stakes,
  one idea per section). Same originality rule as `SKILL.md`.
- **No hardcoded performance fields** ("virality: high"). Use the qualitative
  tiers from `research-ideation.md` with reasoning, or leave the field out.
- **Watch for third-party watermarks.** Some free tools stamp their own
  branding on every render. It sits on your channel permanently and signals
  template content; weigh that before adopting the tool.

## Reviewing auto-generated output

Run `content-critique.md` as usual, plus:

- [ ] Template test (above) across the last 3–5 uploads, not one video
- [ ] Trace three specific numbers or claims to a source; one miss means the
      ledger wasn't done
- [ ] Visual-match audit on a 60-second sample
- [ ] Voice: does every section have the same cadence and energy?
- [ ] `tools/metadata_lint.py` on the title, description, and tags

## Where this skill sits in a pipeline

The skill is the strategy and quality layer; a pipeline is the render layer.
Hand-off package from the skill: the approved title + thumbnail pair, the
script in `assets/script-template.md` format (VO lines + VISUAL lines), the
claim ledger, the asset log or prompt pack, and the SEO package. The pipeline
renders, a human watches, and the post-publish numbers come back for Phase 9.
