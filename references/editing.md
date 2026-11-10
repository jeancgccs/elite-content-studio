# Phase 6: Editing Direction

Produce an edit plan an editor (or the creator at midnight) can execute without
guessing. Reference the script's timestamps and retention beats — the edit's job
is to protect and amplify the retention architecture the script designed.

## Edit plan format

```
## Edit Plan: [video title]
**Runtime target**: [mm:ss] | **Pace**: [cuts every ~Xs baseline]
**Software**: [creator's NLE — tailor terminology to it]

### Global treatments
- Captions: [style, when]
- Color: [grade direction]
- Music: [tracks by section, with the emotional function of each]
- Sound design: [SFX families, mix notes]

### Timeline (by script section)
[mm:ss] Section — cut rhythm, zooms, graphics, b-roll coverage, music cue, notes
```

## Cutting principles

- **Kill dead air ruthlessly**: breaths, "um"s, restarts, and the half-second
  pauses between sentences. Jump cuts are the native grammar of YouTube — but vary
  them with angle changes and b-roll so the rhythm doesn't hypnotize.
- **Cut on motion or meaning**, not on a timer. Baseline pace by genre:
  high-energy entertainment 1.5–3s per cut; teaching 4–8s; storytelling breathes
  longer where emotion needs room.
- **First 30 seconds get triple attention**: tightest cuts, best b-roll, no logo
  intros. Most abandonment happens here; the edit either confirms the click or loses it.
- **Punch-in zooms** (10–20%) on key sentences substitute for a second camera and
  re-focus attention. Alternate in/out; never zoom on every line.
- **The J-cut and L-cut** (audio leads or trails the picture) make transitions
  feel professional and keep momentum across scene changes.

## Retention edits

- At every scripted retention beat, make the edit do something: graphic pops in,
  music shifts, cut to b-roll, zoom, or silence.
- **Payoff protection**: when the video's biggest moment arrives, slow down —
  wider shot, music drop or swell, let it land. Rushing the payoff wastes the
  whole build.
- Trim the ending hard: the moment the content is done, get to the bridge and
  end screen. Long goodbyes crater average view duration.

## Captions & text

- Short-form: always-on captions, 1–4 words at a time, synced to speech, safe-zone
  aware (see `platforms.md` for zones). Emphasize keywords with color/scale — one
  accent color, consistent.
- Long-form: on-screen text for key numbers, steps, and quotes only; lower thirds
  for names/sources; keep every text element inside title-safe margins and on
  screen long enough to read twice.
- Upload real subtitle files (or edit auto-captions) — accessibility and
  search indexing both benefit.

## Graphics, memes & motion

- Graphics must earn their place: clarify a number, map a concept, or land a joke.
  Style-match the brand palette from `production.md`.
- Meme/reaction inserts: genre-dependent — great for gaming/commentary, jarring
  for premium educational brands. Match the channel's register; when in doubt, less.
- Motion design defaults: 0.2–0.4s eases in/out, elements animate in with the VO
  mention (not before), and everything exits — lingering graphics read as clutter.

## Audio mix

- Dialogue is king: music beds 15–25 dB under voice; duck music automatically or
  manually on every spoken line.
- Target loudness around -14 LUFS integrated for online platforms; peaks ≤ -1 dB.
- De-noise lightly (aggressive NR sounds underwater), EQ: high-pass ~80 Hz,
  gentle presence boost 2–5 kHz, then light compression for consistency.
- Sound effects mixed low — felt, not noticed.

## Color

- Correct first (white balance, exposure, skin tones), grade second (mood).
- One consistent look per channel; save it as a preset/LUT for every video.
- Skin tones are the reference — stylize backgrounds, protect faces.

## Music timing

- Map music sections to script sections before fine cutting; cut picture to the
  music's phrase boundaries where possible — edits that land on beats feel "expensive".
- Change or drop the track at major section changes as an invisible pattern interrupt.

## Editing QA checklist

- [ ] First 30s: no intro bloat, promise confirmed visually
- [ ] Every scripted retention beat has a corresponding edit event
- [ ] No stretch >20s without visual change (long-form)
- [ ] Captions accurate, on-brand, inside safe zones
- [ ] Audio: voice clear, music ducked, ~-14 LUFS, no clipping
- [ ] Payoff moment given room to land
- [ ] Ending cuts to bridge + end screen within seconds of content finishing
