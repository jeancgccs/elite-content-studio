#!/usr/bin/env python3
"""
Keyword ideas from YouTube's own search-box autocomplete. Free, no API key.

Autocomplete shows phrases people actually type, roughly ordered by popularity.
It does NOT give search volume or competition. Treat it as evidence of demand
and of the viewer's exact wording, nothing more. Paid tools (vidIQ/TubeBuddy)
or a connected MCP give volume; say which one the numbers came from.

The endpoint (suggestqueries.google.com, ds=yt) is unofficial and can change or
rate-limit without notice. Some sandboxes block it; the script says so and exits.

Usage:
    python3 tools/keyword_ideas.py "meal prep" [--deep] [--lang en] [--region US]

  default  seed + intent modifiers (how to, why, best, vs, for beginners, mistakes...)
  --deep   also seed + a..z (about 26 more requests; be polite, use sparingly)
"""
import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ENDPOINT = "https://suggestqueries.google.com/complete/search"
MODIFIERS = ["{s}", "how to {s}", "why {s}", "what {s}", "best {s}", "{s} vs",
             "{s} for beginners", "{s} mistakes", "{s} tips", "{s} without", "is {s}"]


def suggest(q: str, lang: str, region: str) -> list:
    params = urllib.parse.urlencode({"client": "firefox", "ds": "yt", "q": q, "hl": lang, "gl": region})
    req = urllib.request.Request(f"{ENDPOINT}?{params}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as r:
        data = json.loads(r.read().decode("utf-8", errors="replace"))
    return [s for s in data[1] if isinstance(s, str)]


def main() -> int:
    p = argparse.ArgumentParser(description="YouTube autocomplete keyword ideas (no volume data).")
    p.add_argument("seed")
    p.add_argument("--deep", action="store_true")
    p.add_argument("--lang", default="en")
    p.add_argument("--region", default="US")
    a = p.parse_args()

    seed = a.seed.strip().lower()
    queries = [m.format(s=seed) for m in MODIFIERS]
    if a.deep:
        queries += [f"{seed} {c}" for c in "abcdefghijklmnopqrstuvwxyz"]

    seen, rows, errors = set(), [], 0
    for q in queries:
        try:
            for s in suggest(q, a.lang, a.region):
                k = s.lower().strip()
                if k not in seen:
                    seen.add(k)
                    rows.append((s, q))
        except Exception as e:
            errors += 1
            if errors == 1 and not rows:
                print(f"Autocomplete unreachable from this environment ({type(e).__name__}: {e}).")
                print("Fallback: type the seed into YouTube's search box by hand, or use a connected keyword tool.")
                return 2
        time.sleep(0.25)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"# YouTube autocomplete for '{a.seed}' ({a.lang}-{a.region}), fetched {stamp}")
    print(f"# {len(rows)} unique phrases from {len(queries)} queries"
          + (f", {errors} failed" if errors else "") + ". No volume data.\n")
    for s, q in rows:
        print(f"{s}\t[from: {q}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
