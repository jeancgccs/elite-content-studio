# Phase 7: Publishing & SEO

Produce a complete, paste-ready publishing package using
`assets/seo-package-template.md`. Nothing here is filler — every field either
helps discovery, helps the viewer decide, or feeds the next video's momentum.

## How discovery actually works (ground truth for all advice)

- **YouTube** recommends videos that satisfy viewers: click-through rate,
  average view duration / percentage, survey satisfaction, and post-watch behavior
  (does the session continue?). Metadata helps YouTube *understand* the video;
  packaging and retention make it *recommend* it. Never sell metadata tweaks as
  growth magic.
- **Search surfaces** (YouTube search, Google web + video results) rely on
  keywords in title, description, chapters, captions, and engagement on the result.
  Evergreen how-to/review content should be written with a target query in mind.
- **Short-form feeds** (Shorts/Reels/TikTok) key on early swipe-away rate,
  completion/loop rate, shares, and topic signals from caption + on-screen text +
  audio. Hashtags are topic hints, not magic.

## Finding the keyword (free first)

The primary keyword should be a phrase viewers actually type. With a shell and
network access, `tools/keyword_ideas.py "<seed>"` returns YouTube's own
autocomplete expansions (how-to, why, best, vs, for-beginners, mistakes; `--deep`
adds a–z). Autocomplete is evidence of demand and of exact wording; it has no
volume data. Connected keyword tools (vidIQ/TubeBuddy-class) add volume and
competition. Name which source each keyword came from.

## The SEO package (generate all of it)

1. **Primary title** + 2 alternates (from Phase 3, final-checked ≤60 chars).
2. **Description**:
   - First 1–2 lines (~150 chars): the hook restated with the primary keyword —
     this is what shows in search snippets and above the fold.
   - Middle: 2–3 short paragraphs naturally covering the keyword cluster
     (semantic variants, not keyword stuffing), what the viewer will learn,
     and credibility context.
   - **Sources** (factual videos): the verified rows of the script's claim
     ledger, as title + link. Cited sources are a trust signal viewers notice,
     and they make corrections easy.
   - **Visual credits** (when using third-party visuals): built from the asset
     log. Per-item attribution where the license requires it (CC BY and
     similar); a line noting AI-generated visuals where relevant.
   - Links: resources mentioned, playlist link, socials, disclosure lines for
     sponsors/affiliates (required where applicable).
3. **Keywords & tags**: one primary keyword, 3–5 secondary/semantic variants,
   10–15 tags (primary phrase first, then variants, then 2–3 broad topic tags),
   inside YouTube's 500-character tag budget. Tags are a minor signal — say so —
   but they cost nothing.
4. **Chapters**: timestamped, starting at 0:00, at least three, ascending, each
   at least 10 seconds long (YouTube won't render them otherwise). Each label is
   a mini-headline with keywords where natural (chapters appear in search and
   improve navigation — good chapter labels are both SEO and UX). Derive the
   times from `tools/script_timing.py` or the final edit, never by guessing.
5. **Hashtags**: 2–3 relevant hashtags. YouTube shows up to three above the
   title, picked from the title and description; over 60 and it ignores all of
   them. Platform-specific sets come from Phase 8.
6. **Pinned comment**: adds value (bonus tip, resource, correction space) or asks
   the one discussion question most likely to get replies — comment velocity in
   the first hours matters.
7. **Community post**: teaser posted at/near premiere (image or poll formats
   outperform plain text).
8. **Playlists**: which existing playlist(s) it joins; propose a new series
   playlist if this starts a cluster.
9. **Cards & end screen**: one card mid-video max at a natural mention; end
   screen = 1 target video/playlist + subscribe element, with the last 20 seconds
   of the video scripted to point at it verbally.
10. **Publish timing**: when the channel's audience is historically online
    (creator's analytics beat generic advice; if unknown, suggest testing
    consistent slots and reading Realtime + first-24h data).

**Lint before delivering**: with code execution, save the description to a file
and run `tools/metadata_lint.py --title ... --description-file ... --tags ...
--keyword ... --runtime ...`. Fix every FAIL, judge each WARN, and include the
lint summary with the package. Platform limits drift; re-verify against YouTube
Help when a number matters.

## Upload checklist

- [ ] Title, description, tags pasted; keyword appears in title, first line of
      description, and chapters naturally
- [ ] `metadata_lint.py` run: no FAILs
- [ ] Thumbnail uploaded; checked at small size next to competitors in search results
- [ ] Chapters verified (0:00 first, ≥3 chapters, ascending, each ≥10s)
- [ ] Sources and visual credits in the description where applicable
- [ ] Captions uploaded or auto-captions corrected
- [ ] End screen + card set; matching verbal CTA in final 20s
- [ ] Playlist(s) assigned; series linked
- [ ] Visibility, premiere, monetization, disclosure flags (sponsored? affiliate?
      realistic altered or synthetic media?) set correctly
- [ ] Pinned comment ready to post at publish
- [ ] Community post scheduled
- [ ] Promotion package (Phase 8) scheduled for first 24–48h

## Blog & web SEO (when repurposing to articles)

- One target query per article; put it in the H1, URL slug, first paragraph, and
  a natural subset of H2s. Cover the query's sub-questions (People-Also-Ask style)
  as sections — search intent coverage beats keyword density.
- Embed the video near the top (watch time + backlink to the channel), add a
  text summary that stands alone (don't force readers to watch), original
  images/screenshots, and internal links to related cluster articles.
- Write meta title (≤60 chars) and meta description (≤155 chars, includes the
  query and a reason to click).
- Entity/semantic optimization: name the concepts, tools, and people involved
  explicitly and consistently so search engines map the article to the right
  knowledge graph entities.

## Newsletter publishing

Subject line = a title-mechanism variant (curiosity/specificity) under ~45 chars;
preview text completes the promise. Body: personal note → the value itself
(standalone, not just "watch my video") → the video link with a reason → PS with
one secondary link. One CTA per email.
