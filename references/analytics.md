# Phase 9: Analysis & Iteration

Work only from data the creator actually provides (screenshots, numbers, exports)
or that session tools can fetch. Never invent benchmarks or claim to know their
analytics. If no data is shared, list exactly which numbers to pull and from where,
then analyze when provided.

## The diagnostic tree

Diagnose in this order — each layer gates the next:

### 1. Impressions & reach ("did it get shown?")
- Low impressions + healthy CTR/retention → topic/entity mismatch with the
  audience, weak demand, or the channel lacks authority in this topic yet.
  Fix at Phase 1–2 (idea selection), not packaging.
- Impressions climbing over weeks → evergreen/search traction; feed it
  (cluster videos, playlist, blog article).

### 2. CTR ("did they click?")
- Interpret CTR **relative to the channel's own norm and the traffic mix** —
  browse traffic runs lower CTR than search; huge impression pushes dilute CTR.
  Never quote a universal "good CTR".
- Low CTR vs. own norm → packaging problem: test thumbnail variants first
  (YouTube's thumbnail A/B testing where available), then title. Change one
  variable at a time.
- High CTR + low retention → the packaging over-promised. Fix the promise, not
  just the content.

### 3. Retention ("did they stay?")
Read the retention graph like an editor:
- **Cliff in first 30s** → hook/intro problem: promise not confirmed fast enough.
- **Steady bleed** → pacing: sections too long, too few re-hooks; tighten cuts.
- **Sharp mid-video drops** → find the timestamp, identify what happened
  (tangent, ad-read, repeated info, energy dip) — that's the next video's lesson.
- **Spikes/rewatches** → the audience is telling you what they love; make more
  of that moment's type, clip it for Shorts.
- **End-cliff before CTA** → ending drags; move the bridge earlier.

### 4. Satisfaction & engagement ("was it worth it?")
- Comments' *content* beats comment count: confusion themes, requests, and
  objections are the next content calendar.
- Likes/shares/saves per view indicate share-worthiness — strong shares with
  modest views often means the idea deserves a better-packaged second attempt.

### 5. Audience building ("did they come back?")
- Returning vs. new viewers, subs gained per 1,000 views, and which videos
  convert viewers to subscribers — those are the channel's true pillars.
  Double down on pillar formats; prune formats that never convert.

**Podcast dialect**: run the same tree with podcast metrics — shown = search/
browse + clip reach; clicked = episode title/cover; stayed = consumption rate
and drop-off point; worth it = follows, shares, reviews; came back = the
first-7-day download trend across episodes. See `references/podcast-first.md`.

## Post-mortem output format

```
## Post-mortem: [video]
**Verdict**: [over/under/at expectation — relative to channel baseline]
**What the data says**: [layer-by-layer findings, only from provided data]
**Root cause (ranked)**: [1–3 causes with evidence]
**Fixes now**: [thumbnail/title/metadata changes worth making today, if any]
**Lessons → next videos**: [specific, testable changes]
**Follow-up opportunities**: [sequel, series, cluster, re-promotion]
```

## Iteration strategy

- Treat every video as an experiment with one primary hypothesis
  ("stronger cold-open raises 30s retention"). Log hypothesis → result across
  videos; patterns across 5–10 videos are signal, single videos are noise.
- **Double-down rule**: when something over-performs, make the sequel/series
  while momentum is live (within weeks, not months).
- **Kill rule**: a format that under-performs 3 consecutive times with good
  execution gets retired or radically reworked — sunk cost kills channels.
- Quarterly: re-audit the channel's top 10 by watch time; refresh packaging on
  old evergreen winners (new thumbnail can revive a ranking video); build
  clusters around proven pillars.
