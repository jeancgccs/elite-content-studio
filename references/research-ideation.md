# Phase 1–2: Research & Ideation

## Phase 1 — Research

Goal: understand the audience and the competitive landscape well enough that ideas
practically write themselves. Never skip to brainstorming from a cold start.

### Audience profile

Build (or confirm with the creator) a one-paragraph viewer avatar:

- **Who**: age range, situation, skill level in the topic (beginner / intermediate / pro).
- **Job to be done**: what are they hiring this content for? (learn a skill, make a
  decision, be entertained, feel understood, stay current)
- **Pain points & fears**: what keeps them stuck or anxious? These become hooks.
- **Aspirations**: the after-state they want. This becomes the promise.
- **Watching context**: phone in bed vs. desktop taking notes changes pacing and format.

### Competitive & demand scan

If web search or platform tools (e.g. VidIQ/TubeBuddy MCP tools, YouTube search) are
available in the session, use them. Otherwise, work from the creator's knowledge and
say the research would be stronger with real data.

1. **Outlier scan**: find videos in the niche that dramatically over-performed their
   channel's baseline (views ≫ subscriber count). Outliers reveal proven demand.
   Ask: what promise did the packaging make? Can we make a stronger or fresher version?
2. **Format gap**: what formats exist in the niche (listicle, challenge, documentary,
   tutorial, reaction, vlog, essay)? A proven topic × an underused format is a classic
   opportunity.
3. **Search demand**: what phrases do viewers actually type? Autocomplete, FAQs,
   "vs", "how to", "best X for Y", "X mistakes". With a shell and network access,
   `tools/keyword_ideas.py "<seed>"` pulls YouTube's own autocomplete for these
   modifiers at no cost (phrasing and demand evidence, no volume numbers).
   Search-driven videos grow slower but compound for years (evergreen);
   browse/suggested-driven videos spike. A healthy channel mixes both — recommend a
   ratio based on channel size (small channels: lean search/evergreen to build a
   base; larger: lean browse).
4. **Comment mining**: top comments on competitor videos are free market research —
   objections, unanswered questions, and "please make a video about X" requests.
5. **Transcript study**: read the transcripts of the niche's top performers to see
   their hook construction, structure, and pacing on the page. Getting transcripts
   is free: platform transcript tools if connected in the session, otherwise
   `yt-dlp` pulls a video's auto-generated subtitles from a URL (dedupe the
   repeated lines), and local Whisper transcription covers videos with no
   subtitles at all. Study structure — never copy lines.
6. **Trend vs. evergreen call**: for each opportunity, label it *trend* (act within
   days/weeks) or *evergreen* (timeless). Note the window on trends.
   Free trend signals worth checking when search is available: Google Trends
   (search spikes), Wikipedia's most-read pages (mass curiosity), and the niche's
   own news feeds (Hacker News for tech, preprint servers for science, release
   notes for software, league news for sports). **Fit test**: ride a trend only
   when it connects naturally to the channel's niche and promise. If none fit,
   skip them; an off-niche spike attracts viewers who never return.

### Research output format

Deliver a tight brief, not a data dump:

```
## Research Brief: [topic/niche]
**Viewer avatar**: [one paragraph]
**Proven demand signals**: [3–5 bullets with evidence/reasoning — mark live data vs inference]
**Gaps & openings**: [2–4 bullets — underserved angles or formats]
**Search opportunities**: [keyword clusters with intent + where each came from]
**Risks**: [saturation, seasonality, difficulty, trust requirements]
```

## Phase 2 — Brainstorm

Generate **8–12 ideas** spanning different risk levels. Quantity first, then filter.
An idea is not a topic — it's a topic + angle + format + implied packaging.
"Email marketing" is a topic. "I sent 1,000 cold emails so you don't have to —
here's the only template that got replies" is an idea.

### Idea quality tests (apply to every candidate)

- **Title-first test**: can you write a compelling title for it right now? If not, kill or rework it.
- **Thumbnail test**: is there a single image that communicates the idea in <1 second?
- **"Why now / why me" test**: why should this creator make it, and why would the
  viewer click today instead of the 50 existing videos?
- **Payoff test**: does it have a satisfying ending worth staying for?
- **Effort-to-ceiling ratio**: high-effort ideas need high ceilings. Flag mismatches.
- **Already-covered check**: compare against the channel profile's Covered topics.
  A repeat is fine only as a deliberate sequel, update, or cluster spoke, and the
  packaging should say so. Accidental repeats split the channel's own traffic.

### Ranking rubric

Score each idea 1–5 on: **Demand** (proven interest), **Differentiation** (fresh angle),
**Fit** (creator's strengths, audience match, channel focus), **Packagability**
(title/thumbnail potential), **Feasibility** (can they actually make it well).
Rank by total, but flag any idea with a 1 in Fit or Packagability regardless of total —
those dimensions are vetoes, not tradeoffs.

### Performance tiers (never fake numbers)

Label each ranked idea:

- **Safe** — matches proven channel patterns; likely to perform at baseline.
- **Solid** — proven demand + small twist; modest upside, low risk.
- **Swing** — strong differentiation or trend timing; could meaningfully outperform.
- **Moonshot** — big idea, big effort, real chance of breakout *or* flop.

Recommend a portfolio, not a single bet: for a regular cadence, roughly
60% safe/solid, 30% swing, 10% moonshot — adjusted to the creator's risk appetite
and channel stage. Explain that breakouts usually come from swings and moonshots,
but safes fund the consistency the algorithm and audience need.

### Series & cluster thinking

For every winning idea, note whether it extends into a series or content cluster
(hub video + spoke videos interlinked via playlists, cards, and descriptions).
Clusters compound: they raise session watch time, feed suggested traffic between
your own videos, and build topical authority for search on both YouTube and Google.
