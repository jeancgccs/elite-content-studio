#!/usr/bin/env python3
"""
Metadata lint: pass/fail checks for a YouTube upload package, each with a tip.

Deliberately NOT a score. A single number invites gaming and hides which rule
failed; every line here is a rule you can read, verify, and fix.

Checks: title length and keyword position, keyword in the description's first
~150 chars (the search snippet), description length, chapter validity (YouTube's
rules: first at 0:00, at least 3, ascending, each at least 10 seconds), tag
character budget, hashtag count, and the humanizer lint on title + description.

Usage:
    python3 tools/metadata_lint.py --title "..." --description-file desc.txt \
        --tags "tag one, tag two" --keyword "primary keyword" [--runtime 12:30] [--shorts]

Exit code 1 if any check FAILS. WARN lines are judgment calls, not failures.
Platform limits drift: re-verify against YouTube Help when precision matters.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from humanizer_lint import failed as hz_failed, lint_text  # noqa: E402

TS = re.compile(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})\s+\S", re.MULTILINE)
STOP = {"the", "a", "an", "of", "to", "in", "on", "and", "or", "for", "with", "how",
        "why", "what", "your", "you", "my", "is", "are", "vs"}


def secs(ts: str) -> int:
    parts = [int(p) for p in ts.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    h, m, s = parts
    return h * 3600 + m * 60 + s


def kw_words(keyword: str) -> list:
    return [w for w in re.findall(r"[\w']+", keyword.lower()) if w not in STOP]


def kw_coverage(text: str, words: list) -> float:
    if not words:
        return 1.0
    low = text.lower()
    return sum(1 for w in words if re.search(r"\b" + re.escape(w), low)) / len(words)


def tag_chars(tags: list) -> int:
    # YouTube Studio counts multi-word tags with surrounding quotes, plus separators.
    return sum(len(t) + (2 if " " in t else 0) for t in tags) + max(0, len(tags) - 1)


def run(a) -> list:
    rows = []

    def add(status, label, detail):
        rows.append((status, label, detail))

    title = a.title.strip()
    desc = open(a.description_file, encoding="utf-8").read() if a.description_file else ""
    tags = [t.strip() for t in (a.tags or "").split(",") if t.strip()]
    words = kw_words(a.keyword or "")

    # Title
    n = len(title)
    if n > 100:
        add("FAIL", "Title length", f"{n} chars. YouTube's hard cap is 100.")
    elif n > 60:
        add("WARN", "Title length", f"{n} chars. Over 60 truncates on many surfaces; front-load the payload.")
    else:
        add("PASS", "Title length", f"{n} chars.")

    if words:
        cov = kw_coverage(title, words)
        first40 = kw_coverage(title[:40], words)
        if cov == 1.0 and first40 == 1.0:
            add("PASS", "Keyword in title", "All keyword words appear in the first 40 chars.")
        elif cov == 1.0:
            add("WARN", "Keyword in title", "Keyword present but not in the first 40 chars. Move it forward if this is a search-intent video.")
        else:
            add("WARN", "Keyword in title", f"{cov:.0%} of keyword words present. Fine for browse titles; search-intent titles should carry the phrase intact.")

    # Description
    if desc:
        if len(desc) > 5000:
            add("FAIL", "Description length", f"{len(desc)} chars. YouTube's cap is 5,000.")
        else:
            add("PASS", "Description length", f"{len(desc)} chars.")
        if words:
            cov = kw_coverage(desc[:150], words)
            add("PASS" if cov == 1.0 else "WARN", "Keyword in first ~150 chars",
                "Present in the search snippet." if cov == 1.0
                else f"{cov:.0%} of keyword words in the first 150 chars. Restate the hook with the keyword there.")
    else:
        add("WARN", "Description", "No description file given; description checks skipped.")

    # Chapters
    if not a.shorts and desc:
        stamps = TS.findall(desc)
        if not stamps:
            add("WARN", "Chapters", "None found. Long-form videos usually benefit from chapters (navigation + search).")
        else:
            t = [secs(s) for s in stamps]
            problems = []
            if t[0] != 0:
                problems.append(f"first stamp is {stamps[0]}, must be 0:00")
            if len(t) < 3:
                problems.append(f"{len(t)} stamps, need at least 3")
            for i in range(1, len(t)):
                if t[i] <= t[i - 1]:
                    problems.append(f"{stamps[i]} is not after {stamps[i-1]}")
                elif t[i] - t[i - 1] < 10:
                    problems.append(f"chapter at {stamps[i-1]} is under 10s")
            if a.runtime:
                end = secs(a.runtime)
                if end - t[-1] < 10:
                    problems.append(f"last chapter ({stamps[-1]}) is under 10s before the {a.runtime} end")
            if problems:
                add("FAIL", "Chapters", "; ".join(problems) + ". YouTube will not render chapters until fixed.")
            else:
                add("PASS", "Chapters", f"{len(t)} valid chapters." + ("" if a.runtime else " (Pass --runtime to check the last one.)"))

    # Tags
    if tags:
        c = tag_chars(tags)
        add("FAIL" if c > 500 else "PASS", "Tag budget", f"{c}/500 chars across {len(tags)} tags.")
        if words and kw_coverage(tags[0], words) < 1.0:
            add("WARN", "Tag order", "First tag is not the primary keyword phrase. Tags are a minor signal; put the primary first anyway.")

    # Hashtags
    hashtags = re.findall(r"(?<!\w)#\w+", title + "\n" + desc)
    if len(hashtags) > 60:
        add("FAIL", "Hashtags", f"{len(hashtags)} found. Over 60 and YouTube ignores every hashtag on the video.")
    elif hashtags:
        add("PASS", "Hashtags", f"{len(hashtags)} found. YouTube shows up to 3 above the title, chosen from title + description.")
    else:
        add("WARN", "Hashtags", "None. 2-3 relevant hashtags give YouTube a topic hint.")

    # Humanizer
    hz = lint_text(title + "\n" + desc)
    if hz_failed(hz):
        terms = sorted({h["term"] for h in hz["kill_list"] + hz["hedging"]})
        detail = ("AI-tell terms: " + ", ".join(terms)) if terms else "Too many 'not just X, it's Y' constructions."
        add("FAIL", "Humanizer", detail.rstrip(".") + ". Run tools/humanizer_lint.py for line numbers.")
    else:
        add("PASS", "Humanizer", "No kill-list terms or hedging stacks in title/description.")
    return rows


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--title", required=True)
    p.add_argument("--description-file")
    p.add_argument("--tags", help="comma-separated")
    p.add_argument("--keyword", help="primary keyword phrase")
    p.add_argument("--runtime", help="video length m:ss or h:mm:ss, to check the last chapter")
    p.add_argument("--shorts", action="store_true", help="skip chapter checks")
    a = p.parse_args()
    rows = run(a)
    width = max(len(r[1]) for r in rows)
    for status, label, detail in rows:
        print(f"{status:<5} {label:<{width}}  {detail}")
    fails = sum(r[0] == "FAIL" for r in rows)
    print(f"\n{fails} fail(s), {sum(r[0] == 'WARN' for r in rows)} warning(s). No score by design: fix FAILs, judge WARNs.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
