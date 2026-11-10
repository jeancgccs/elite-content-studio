# Phase 3: Packaging (Titles, Thumbnails, Hooks)

Packaging is the single highest-leverage phase: it decides whether the content gets a
chance at all. Always develop **title + thumbnail as a pair** — they are one message
split across two surfaces, and they must complement, not repeat, each other.
If the thumbnail shows it, the title shouldn't say it (and vice versa).

## Titles

Generate **10 title options** per video, spanning different mechanisms, then rank
and recommend one. State the mechanism behind each so the creator learns the craft.

### Core mechanisms (mix across the 10)

- **Curiosity gap**: opens a question the viewer must click to close.
  "I Tried the 4 AM Routine for 30 Days" (what happened?)
- **Outcome + timeframe**: concrete result, concrete window.
  "How I Learned to Edit in 7 Days"
- **Specificity**: precise numbers and details signal real substance.
  "$127 → $8,400: My Exact Etsy Playbook" beats "How to Make Money on Etsy"
- **Stakes / negativity**: loss-framing and warnings pull harder than gains.
  "Stop Making These 5 Lighting Mistakes" — use sparingly; an all-negative
  channel erodes trust and mood.
- **Novelty / contrarian**: challenges an assumption the audience holds.
  "Why I Quit the 4 AM Routine (and grew faster)"
- **Authority / proof**: borrowed credibility from scale or experience.
  "I Analyzed 100 Viral Shorts — Here's the Pattern"
- **Search-intent**: mirrors the exact query for evergreen search traffic.
  "How to Set Up OBS for Streaming (2026 Guide)"

### Title rules

- Front-load the payload — the first ~40 characters carry the click; titles truncate
  on many surfaces (aim ≤60 characters total, hard cap 100).
- One idea per title. Compound promises dilute.
- Every word earns its place; cut "my thoughts on", "a video about".
- The title must be true. Curiosity gap ≠ deception — the video must close the gap
  satisfyingly or retention and channel trust pay the price.
- For search-intent titles, put the keyword phrase intact near the front.
- **Count, don't estimate**: character counts are easy to get wrong by eye. When
  working in an environment with code execution, verify every title's length with
  a quick script; print the count next to each title, and explicitly flag any title
  over 60 characters instead of claiming compliance. A wrong count presented as a
  fact is exactly the kind of invented data this skill forbids.

## Thumbnails

Provide **3–5 distinct concepts** (not variations of one). For each, specify:

```
**Concept [n] — [two-word handle]**
- Composition: [subject placement, rule of thirds, camera distance]
- Subject & expression: [who/what, exact emotion — surprise, focus, disgust, joy]
- Text: [≤4 words, or none — never repeat the title]
- Color & contrast: [bg/fg strategy, one accent color, brightness]
- The planted question: [what the viewer wonders in the first second]
- Difficulty: [phone selfie / simple shoot / edit-heavy / AI-generated]
```

### Thumbnail principles

- **3-element max**: face, object, short text — more than three elements turns to
  noise at 120px wide. Always evaluate at phone-feed size, not full screen.
- **Faces with clear emotion** outperform neutral faces; the emotion must match the
  video's actual tone (fake shock reads as bait and ages the channel).
- **Contrast is the mechanic**: subject must separate from background (light-on-dark
  or dark-on-light, complementary accent color, subtle outline/glow if needed).
- **Before/after, X-vs-Y, and arrows/circles** work because they compress a story
  into one glance — use when the idea has a visible transformation or comparison.
- **Consistency vs. novelty**: keep a recognizable style (palette, face treatment)
  so returning viewers spot you in the feed, but vary composition so uploads don't blur
  together.
- When the creator can generate images, include a ready-to-paste AI image prompt per
  concept (see `ai-toolkit.md` for prompt patterns).

## Hooks & opening lines

For each packaged video, write **3 hook options** (the first 5–15 seconds, or first
1–3 seconds for short-form). The hook's only job: confirm the click's promise and
open a loop that the intro doesn't yet close.

Hook patterns:

- **Cold open on the peak**: show the most dramatic moment first, then rewind.
- **Restate the promise + raise stakes**: "By the end of this video you'll X — and
  I'll show you the mistake that costs most people Y."
- **In-medias-res**: start mid-action, no greeting, no logo, no "hey guys welcome back".
- **Credibility flash**: one line of proof, then straight into value.
- **Contrarian slap**: "Everything you've heard about X is backwards."

Never open with channel intros, long branding animations, or "before we start."
Every second before the promise is confirmed bleeds viewers.

## Curiosity gaps & emotional triggers

Map the video's emotional driver explicitly (curiosity, fear of missing out,
aspiration, outrage→resolution, awe, belonging) and state it in the packaging
rationale. Use emotional triggers to serve the viewer's real interests —
manufactured outrage and anxiety farming grow fast and die faster.

## Packaging QA checklist

Before moving to scripting, verify:

- [ ] Title ≤60 chars, payload front-loaded, truthful
- [ ] Thumbnail readable at feed size; ≤3 elements; doesn't repeat title text
- [ ] Title + thumbnail together create one question the video answers
- [ ] The promise is deliverable by this creator at their production level
- [ ] A stranger scrolling could state the video's promise in one sentence
