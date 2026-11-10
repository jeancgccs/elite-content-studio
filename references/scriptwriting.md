# Phase 4: Scriptwriting

Write scripts that are shootable as-is. Default to **word-for-word** for beginners
and educational content; offer a **beat sheet** (bullet talking points per section)
for experienced presenters — ask once and remember the preference.

Use `assets/script-template.md` as the skeleton for long-form scripts.

## Retention architecture (design before writing)

Before drafting prose, lay out the video's spine:

1. **The promise** (from packaging) — what the viewer was told they'd get.
2. **The payoff** — the moment the promise is fully delivered. Place it at ~70–85%
   of runtime, not the very end and never the first minute.
3. **Open loops** — 2–4 questions opened early and closed at staggered points.
   Announce them ("later I'll show you the one that broke everything") sparingly;
   mostly let structure imply them.
4. **Re-hook points** — plan a re-engagement beat roughly every 60–90 seconds of
   long-form (every 3–7 seconds of short-form): a reveal, a stakes raise, a visual
   change, a question, a joke. Mark these in the script margin. Write each one from
   this video's content; a stock re-hook line reused across uploads stops working
   and makes the channel sound templated.
5. **The ending** — end on momentum, not a fade-out. The last 20 seconds bridge
   directly into the next-video recommendation (see End screens below).

## Story structures (pick one per video, name it in the script header)

- **Problem → Agitate → Solve (PAS)** — tutorials and advice. Make the pain vivid
  before offering relief; the agitation is what makes the solution land.
- **Hero's journey / transformation** — challenges, experiments, journeys.
  Ordinary state → commitment → obstacles (escalating) → low point → breakthrough → new state.
- **List with escalation** — rank items so the best/biggest/weirdest is last, and
  say so up front ("number one still blows my mind") to hold viewers through the list.
- **Documentary / mystery** — question-driven: pose the mystery, investigate,
  false leads, revelation. Great for essays and deep dives.
- **Dual timeline** — cut between "now" (results) and "then" (process). Lets you
  show the payoff early without spending it.

## Teaching flow (for educational content)

- One concept per section; each section = claim → example → application.
- Use concrete examples and demos over abstractions; show, then explain.
- **Signposting**: tell viewers where they are ("that's step 2 of 4") — clarity
  retains better than mystery in tutorials.
- Anticipate and voice the viewer's objection at the moment they'd think it
  ("you're probably thinking this only works if you have an audience — here's
  why it doesn't").
- End each section by paying off its mini-promise and opening the next
  ("…which works — until you hit the problem that kills most channels").

## Script formatting

For every beat, pair narration with visuals. Format each block:

```
### [mm:ss approx] Section name        [RETENTION BEAT: reveal/joke/stakes/visual]
VO/CAM: "The exact words spoken..."
VISUAL: [A-cam / B-roll: description / screen recording / graphic]
TEXT ON SCREEN: [if any — keep to ≤6 words]
SFX/MUSIC: [cue if it changes]
```

Include throughout:

- **Pattern interrupts**: change *something* (shot, location, energy, graphic,
  music) at every planned re-hook point.
- **B-roll & graphics suggestions** written specifically ("close-up: hands
  plugging in the mic cable" — not "relevant b-roll"). For narration over
  visuals, give each section a context shot, a detail shot, and a concept shot
  (see `faceless-automation.md`).
- **Transitions** written as spoken bridges, not visual gimmicks: the last line of
  each section should make the next section feel inevitable.
- **CTAs**: one primary CTA maximum, placed *after* significant value delivery
  (never in the first 30 seconds). Subscribe asks work best tied to a reason
  ("I'm testing this for 90 days — subscribe to see the results"). Mid-roll
  "comment" prompts should ask a specific, easy-to-answer question. Every CTA
  must be true: don't promise to read every comment unless someone will.

## Runtime math (count, don't estimate)

Timestamps in a script are claims, so compute them. Runtime = spoken words ÷
words per minute. Measure the creator's pace once (read one section aloud with
a timer; for TTS, time one generated chunk) and store it in the channel profile.
Then run:

```
python3 tools/script_timing.py script.md --wpm <measured> --target <m:ss>
```

It reports each section's start time, the payoff's position as a % of runtime,
the longest stretch without a marked retention beat, paste-ready chapters, and
the humanizer lint on spoken words only. Fix FAILs before delivering, and put the
measured (or placeholder) wpm in the script header so the numbers can be checked.
Without code execution, compute from word counts by hand and say it's approximate.

## Short-form scripts (Shorts / Reels / TikTok)

Different physics: the first 1–2 seconds decide everything, and loops matter.

- **Hook is frame one**: visual + text + first word all working. No setup.
- Structure: Hook (0–2s) → Promise/context in one line (2–5s) → rapid value beats
  (every 2–4s a new visual or point) → payoff → **loop seam**: write the last line
  so it flows back into the first (rewatches are a major ranking signal).
- Write for sound-off: every spoken line has matching on-screen text or captions.
- One idea only. If a short needs two ideas, it's two shorts.
- 20–40s is the sweet spot for most niches; go longer only when retention holds.

## The fact-grounding pass (any script that states facts)

A confident wrong number on camera costs more credibility than the video earns.
Before the humanizer pass, build a **claim ledger** at the bottom of the script
(the template has the table):

| # | Claim as spoken | Type | Source | Status |
|---|---|---|---|---|
| 1 | "[exact line]" | number / date / name / causal / quote | [link or citation] | verified / creator to verify / opinion / speculation |

Rules:
- Every number, date, proper name, quote, and cause-and-effect claim gets a row.
- **Never fill the Source column from memory.** With web search, find and cite
  the primary source (paper, dataset, official page) and note the access date.
  Without search, mark the row "creator to verify" and list it in your reply;
  don't present it as checked.
- Encyclopedias and news are fine for orientation; for numbers, cite what they cite.
  Other YouTube videos and AI answers are never sources.
- Opinions stay in the script as opinions ("I think", "my read is"). Speculation
  is labeled on air with whose idea it is ("one hypothesis, from [researcher]...").
- Verified sources go in the description's SOURCES block (`publishing-seo.md`).
- If a load-bearing claim can't be verified, rewrite the line around what can be.

Opinion pieces, vlogs, and comedy skip the ledger unless they state facts as facts.

## The humanizer pass (run on every draft before delivery)

Scripts are spoken. Prose that merely looks "off" on a blog sounds instantly
artificial on camera, and viewers now pattern-match AI-flavored narration to
low-effort channels. After drafting, rewrite with this pass:

**Sound like a person with opinions**
- State a point of view plainly ("I think this mic is overpriced") instead of
  neutral reporting; specific reactions beat generic ones ("I almost returned
  it twice" not "it was quite frustrating").
- Vary the rhythm. Mix short punchy sentences with longer ones; uniform
  sentence length is the audio equivalent of a monotone. Read it aloud —
  anywhere you run out of breath, cut.
- Let a little mess live: an occasional tangent, a self-correction
  ("actually, wait—"), a half-thought. Used sparingly these are humanity
  markers, and they double as pattern interrupts.
- First person, contractions, and the creator's actual vocabulary (check the
  channel profile's voice notes). If they wouldn't say a word at dinner, cut it.

**Cut the AI-tells** (applies to scripts, captions, and descriptions):
- Essay vocabulary nobody says out loud: delve, landscape, tapestry, showcase,
  underscore, testament, intricate, vibrant, foster, elevate, seamless,
  game-changer, "in the heart of."
- Significance inflation: "serves as," "stands as," "marks a pivotal moment,"
  "reflects a broader shift" → just say what it is and what it did:
  "is," "changed how I edit."
- The negative-parallelism crutch: "It's not just X — it's Y" and
  "Not only… but also" are the most overused AI script constructions.
  Budget: one per script, ideally zero.
- Forced rule-of-three lists, and synonym-cycling to avoid repeating a word —
  repetition is natural in speech; cycling sounds like a thesaurus.
- Hedging stacks: "could potentially" → "could"; "has the ability to" → "can";
  "in order to" → "to"; "due to the fact that" → "because."
- Vague authority: "experts say," "studies show," "many people believe" —
  name the actual source or cut the claim (this is the claim ledger wearing
  its scriptwriting hat).
- Generic closers: "the future looks bright," "exciting times ahead," "at the
  end of the day" — the ending's job is the bridge to the next video, not a
  fortune cookie.
- Promotional adjective clusters ("stunning," "breathtaking," "must-see") —
  show the thing and let the viewer be stunned.

**Machine check**: `tools/humanizer_lint.py` (or `script_timing.py`, which runs
it on spoken lines) catches the countable tells: kill-list terms, hedging
stacks, the negative-parallelism budget. It can't judge rhythm or voice; the
read-aloud test still applies.

**Final test**: read the whole script aloud. Any sentence that sounds like a
press release, an essay, or a LinkedIn post gets rewritten as the creator
would say it to one friend.

## Podcast & livestream adaptations

- **Podcast**: replace visual beats with verbal texture — stories, questions,
  recaps every ~10 min for audio-only listeners who drift. Write segment rundowns
  with timestamps, guest questions (open-ended, story-eliciting, ordered
  easy → deep), and clip-worthy moments flagged for repurposing.
- **Livestream**: write a run-of-show, not a script — opening hook for replay
  viewers, segment blocks with time boxes, interaction prompts every segment,
  planned "peak" moment to clip later, and a hard ending with CTA.

## Script QA checklist

- [ ] First 15 seconds confirm the title/thumbnail promise
- [ ] Payoff lands at 70–85%, not the end credits (verified by `script_timing.py`)
- [ ] A retention beat every 60–90s (3–7s short-form), marked in the script
- [ ] Every section has explicit visual direction
- [ ] One primary CTA, placed after value, and true
- [ ] Ending bridges to a specific next video
- [ ] Claim ledger complete for factual content; unverified rows listed for the creator
- [ ] Read the whole script aloud mentally: does any section drag? Cut 10%.
- [ ] Humanizer pass done: no AI-tell vocabulary, varied rhythm, plain-spoken
      opinions, ≤1 "it's not just X" construction, read-aloud test passed,
      lint output reported
