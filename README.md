# Elite Content Studio — How to Use This Skill

A Claude Skill that turns Claude into a full content production studio: strategist,
creative director, scriptwriter, film director, editor, SEO lead, and social media
manager. It runs a 9-phase workflow (Research → Brainstorm → Packaging → Script →
Production → Editing → Publishing → Promotion → Analysis) and produces
production-ready deliverables, not generic advice.

## Installing

- Download `elite-content-studio.skill` from the
  [latest release](https://github.com/jeancgccs/elite-content-studio/releases/latest).
- **Claude app (web/desktop)**: add it as a skill from your Claude settings
  (the skills/capabilities section), or open the file in the desktop app and save it.
- **Claude Code**: unzip it into your skills directory (e.g. `~/.claude/skills/`),
  or clone this repo there.
- The skill triggers automatically on content-creation requests (videos, titles,
  thumbnails, scripts, Shorts, SEO, channel analytics). You can also invoke it
  explicitly: "Use the elite content studio skill to…"

## Struggling? Start here

If your channel feels stuck, don't ask for video ideas yet — ask for an audit:

> My channel feels dead. [Niche], [n] videos over [time], [subs] subscribers,
> typical video gets [views]. Here are my last 5 titles: [paste]. Run a channel
> audit and tell me what my actual bottleneck is.

The skill will triage whether your problem is **demand** (wrong topics/niche),
**packaging** (titles/thumbnails), **retention** (hooks/pacing), or
**consistency** (no compounding formats) — each has a completely different fix —
then build you a 30-day program around the one that matters. It also keeps a
`channel-profile.md` memory file so every future session builds on what it
already knows about your channel, and you can ask it to critique any existing
video, script, or thumbnail ("review this thumbnail — screenshot attached")
for ranked fixes with rewrite samples.

## Faceless or automated channel?

Say so in your first message, and name your pipeline if you use one. The skill
keeps automation on the tedious parts and keeps you on the decisions that
protect quality and monetization: packaging approval, fact sign-off, and a
full watch-through before anything publishes. Factual scripts come with a
**claim ledger** (every number and date tied to a source, or flagged for you
to verify), and faceless projects get a visual sourcing plan with licensing
and credits handled.

## Getting the best results

1. **Front-load your context.** The single biggest quality lever. In your first
   message include: niche, audience, platform, channel size, upload cadence, your
   gear (phone? camera? mics?), your editing software, and your goal. Every
   recommendation gets scaled to what you actually have.
2. **Let it run the phases in order for new projects.** Idea and packaging come
   before scripting on purpose — a video that can't be packaged shouldn't be
   scripted. Don't skip to "write me a script" for an unvalidated idea; ask for
   the packaging first and pick a title+thumbnail pair you believe in.
3. **Share your numbers when you have them.** Real analytics (CTR, retention
   graph shape, traffic sources, past winners/losers) turn generic strategy into
   channel-specific strategy. The skill never invents benchmarks, so what you
   share is what it works with.
4. **Answer the intake questions — or say "make assumptions."** For big projects
   the skill asks up to 4–6 questions once. Answering them pays off across every
   phase; if you're in a hurry, tell it to assume and it will state its assumptions.
5. **Iterate on packaging, not just scripts.** Ask for another round of titles on
   a different mechanism ("give me 5 more, leaning contrarian"), or a thumbnail
   concept that works without your face. Packaging is cheap to iterate and worth it.
6. **Ask for the deliverable format you'll actually use**: word-for-word script vs
   beat sheet, files vs chat, full 9-phase package vs a single phase. State it once;
   the skill remembers your preference.
7. **Tell it your speaking pace once.** Read one script section aloud with a timer
   (or time one TTS chunk) and share the words per minute. Script timestamps,
   payoff placement, and chapters are then computed, not guessed.
8. **Close the loop after publishing.** Come back with the analytics ~7 days later
   and ask for a post-mortem — Phase 9 turns every upload into lessons and
   next-video ideas, which is where compounding growth comes from.

## 5 example prompts that get better video ideas

These are templates — replace the bracketed parts. Each one is engineered to
trigger the skill's strongest ideation behavior: rich context in, ranked and
reasoned ideas out.

**1. The full ideation sprint (best all-around)**
> I run a [niche] channel on [platform], [size] subscribers, posting [cadence],
> audience is [who + skill level]. My best performing videos so far: [2–3 titles
> or topics]. My gear: [gear]. Goal right now: [growth / authority / income].
> Run your research and brainstorm phases: give me a ranked slate of 10 video
> ideas with risk tiers, and tell me which one you'd shoot next and why.

**2. The outlier-hunt (steal proven demand, not content)**
> Here are 5 videos in my niche that massively over-performed their channel size:
> [titles/links]. Analyze what promise each one's packaging made, then generate
> 8 fresh ideas for my channel that tap the same proven demand with a different
> angle or format — I don't want copies. My channel context: [context].

**3. The audience-pain miner (evergreen idea engine)**
> My audience is [avatar]. Their most common questions and complaints, from my
> comments/DMs: [paste 5–10 real questions or pain points]. Turn these into a
> ranked list of video ideas — mark each as search-driven evergreen or
> browse-driven, and group them into a content cluster I could build a series
> around.

**4. The format-gap finder (differentiation on a crowded topic)**
> The topic [topic] is saturated in my niche — everyone makes [dominant format,
> e.g. listicles/tutorials]. What formats are underused here (documentary,
> challenge, experiment, dual-timeline, mystery)? Give me 6 ideas that pair this
> proven topic with an underused format, with a title-first test for each so we
> know it can be packaged before I commit.

**5. The one-video deep validation (before you invest a big shoot)**
> I'm considering this video idea: [describe idea]. Before I spend a weekend on
> it, pressure-test it: run the title-first, thumbnail, "why now/why me," payoff,
> and effort-to-ceiling tests. If it fails any, rework the angle until it passes,
> then show me the winning title + thumbnail pair and the 3 hook options you'd
> open with.

## Does it actually help? (benchmark)

On an earlier version of the skill, the same creator prompts were run through
Claude with and without it and graded against explicit assertions. **With the
skill: 20/20 assertions passed. Without: 11/20.** Typical differences: the
baseline offered 3 unlabeled titles where the skill delivered 10 with persuasion
mechanisms and character counts; the baseline produced an outline where the skill
delivered a full word-for-word script with marked retention beats and a payoff
placed at 72–82% of runtime; and the baseline invented plausible-sounding
benchmark numbers while the skill stayed inside the creator's real data.

That result predates the current version and has not been re-run on v1.6.0 yet;
updated numbers will replace it here when they exist. The suite lives in `evals/`
(8 prompts with written assertions) if you want to run it yourself.

## Limitations

- **Small, self-graded evals.** Eight prompts, single runs, graded by a Claude
  model. Treat the benchmark as directional evidence, not proof.
- **No large-scale outside validation yet.** If something misses for your niche
  or platform, open an issue with the prompt and what went wrong.
- **The bundled tools need code execution.** `tools/` runs wherever Claude can
  execute Python (Claude Code, or the Claude app with code execution enabled).
  Without it, the skill counts by hand and says the numbers are approximate.
  `keyword_ideas.py` also needs network access to YouTube's autocomplete, which
  some sandboxes block.
- **It's a strategist, not a crystal ball.** It never predicts views or promises
  growth, by design. Advice is only as specific as the data you share.
- **Platform rules drift.** Character limits, hashtag rules, and monetization
  policies change; the skill says when a number may be stale, and you should
  check the platform's help pages for anything that matters.

## What's in this folder

- `SKILL.md` — the skill's entry point (persona, principles, entry points, 9-phase workflow)
- `references/` — one playbook per phase, plus channel audit, content critique,
  small-channel playbook, faceless/automation playbook, platform specs, and
  AI-tool integration
- `assets/` — fill-in templates (script with claim ledger, SEO package, production
  checklist, promotion kit, channel profile, 30-day program, AI asset prompt pack)
- `tools/` — small standard-library Python checks the skill runs instead of
  eyeballing countable rules. You can run them yourself too:
  - `python3 tools/script_timing.py script.md --wpm 155 --target 10:00` — real
    timestamps from word count, payoff position, retention gaps, chapters
  - `python3 tools/metadata_lint.py --title "..." --description-file desc.txt --tags "a, b" --keyword "..."`
    — title/keyword/chapter/tag/hashtag checks, pass/fail with tips (no score)
  - `python3 tools/humanizer_lint.py draft.txt` — AI-tell vocabulary and constructions
  - `python3 tools/keyword_ideas.py "your topic"` — free YouTube autocomplete
    phrases (demand evidence, no volume data)

**AI-first creators**: if you generate your assets with AI (Higgsfield, Google
Flow/Veo, Runway, Midjourney, Suno, ElevenLabs…), say so in your first message —
the skill will deliver a complete prompt pack alongside the script: a
paste-ready generation prompt for every visual beat, thumbnail prompts per
concept, music brief, and voiceover direction, all sharing one style anchor so
the finished video looks like one production instead of stitched clips.
- `evals/` — the test-prompt suite used to benchmark the skill (eval 8, the
  faceless/automation case, was added in v1.6.0 and has not been benchmarked yet)

## License

MIT. See [LICENSE](LICENSE). Use it, change it, share it.
