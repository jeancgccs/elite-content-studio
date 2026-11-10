#!/usr/bin/env python3
"""
Script timing: counts the spoken words in a script and turns them into real
timestamps, then checks the retention architecture against them.

Reads scripts in the assets/script-template.md layout:
  - a section starts at any '## ' or '### ' heading
  - spoken text is on lines labeled VO/CAM, VO, CAM or NARRATION (bold or plain),
    plus any unlabeled continuation lines that follow before a blank line
  - a heading tag like `[RETENTION ...]` marks a re-hook beat; 'PAYOFF' in a heading marks the payoff

Reports per-section duration and start time, then checks:
  - payoff starts at 70-85% of runtime
  - no gap between retention beats longer than --max-gap seconds
  - total runtime vs --target
  - chapters derived from the sections (each must be >= 10s for YouTube)
  - humanizer lint over the spoken words only

Words-per-minute is the creator's real pace. Measure it once: read one section
aloud with a timer, words / minutes. Typical conversational delivery lands
around 140-170 wpm; documentary narration and TTS voices often run slower.
Default 150 is a placeholder, so say so when reporting.

Usage:
    python3 tools/script_timing.py script.md [--wpm 150] [--target 10:00] [--max-gap 90] [--shorts]
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from humanizer_lint import failed as hz_failed, lint_text, report  # noqa: E402

HEAD = re.compile(r"^#{2,3}\s+(.*)$")
LABEL = re.compile(r"^\s*(?:\*\*)?(VO/CAM|VO|CAM|NARRATION|V\.O\.)(?:\*\*)?\s*:\s*(.*)$", re.I)
OTHER_LABEL = re.compile(r"^\s*(?:\*\*)?[A-Z][A-Z /&\-]{1,30}(?:\*\*)?\s*(?:\([^)]*\))?\s*:")
STAMP = re.compile(r"\[\s*\d{1,2}:\d{2}\s*\]")


def mmss(s: float) -> str:
    s = int(round(s))
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def clean_spoken(t: str) -> str:
    t = re.sub(r"\[[^\]]*\]", " ", t)          # [stage directions]
    t = re.sub(r"\([^)]*\)", " ", t)           # (parentheticals)
    return t.replace("**", "").replace('"', " ").replace("“", " ").replace("”", " ")


def parse(md: str) -> list:
    sections, cur, in_vo = [], None, False
    for line in md.splitlines():
        h = HEAD.match(line)
        if h:
            heading = h.group(1).strip()
            cur = {"heading": heading, "spoken": [],
                   "retention": bool(re.search(r"\[\s*RETENTION", heading, re.I)),
                   "payoff": "PAYOFF" in chapter_name(heading).upper()}
            sections.append(cur)
            in_vo = False
            continue
        if cur is None:
            continue
        m = LABEL.match(line)
        if m:
            cur["spoken"].append(m.group(2))
            in_vo = True
        elif not line.strip() or OTHER_LABEL.match(line) or line.lstrip().startswith(("-", "|", ">", "#")):
            in_vo = False
        elif in_vo:
            cur["spoken"].append(line)
    for s in sections:
        s["text"] = clean_spoken(" ".join(s["spoken"]))
        s["words"] = len(re.findall(r"[\w']+", s["text"]))
    return [s for s in sections if s["words"] or s["payoff"]]


def chapter_name(heading: str) -> str:
    h = re.sub(r"`[^`]*`", "", heading)
    h = STAMP.sub("", h)
    h = re.sub(r"\[[^\]]*\]", "", h)
    h = re.sub(r"^\s*SECTION\s+\d+\s*[—:-]\s*", "", h, flags=re.I)
    return h.strip(" —-:") or "Section"


def main() -> int:
    p = argparse.ArgumentParser(description="Time a script from its word count and check retention beats.")
    p.add_argument("script")
    p.add_argument("--wpm", type=float, default=150.0)
    p.add_argument("--target", help="target runtime m:ss")
    p.add_argument("--max-gap", type=float, help="max seconds between retention beats (default 90, Shorts 7)")
    p.add_argument("--shorts", action="store_true")
    a = p.parse_args()
    gap_limit = a.max_gap or (7.0 if a.shorts else 90.0)

    secs = parse(open(a.script, encoding="utf-8").read())
    if not secs:
        print("No sections with spoken lines found. Expected '## ' headings and VO/CAM: lines.")
        return 2

    if not any(s["words"] for s in secs):
        print("Sections found, but no spoken words yet (placeholders in [brackets] are ignored).")
        return 2

    t = 0.0
    for s in secs:
        s["start"] = t
        s["dur"] = s["words"] / a.wpm * 60
        t += s["dur"]
    total = t

    print(f"Timing at {a.wpm:g} wpm ({'measured' if a.wpm != 150 else 'DEFAULT placeholder: measure the real pace'})\n")
    print(f"{'start':>7} {'dur':>6} {'words':>6}  section")
    for s in secs:
        flag = " [RETENTION]" if s["retention"] else ""
        flag += " [PAYOFF]" if s["payoff"] else ""
        print(f"{mmss(s['start']):>7} {s['dur']:>5.0f}s {s['words']:>6}  {chapter_name(s['heading'])}{flag}")
    words = sum(s["words"] for s in secs)
    print(f"\nTotal: {words} spoken words, about {mmss(total)}")

    fails = 0
    print("\nChecks")
    if a.target:
        tgt = sum(int(x) * 60 ** i for i, x in enumerate(reversed(a.target.split(":"))))
        dev = (total - tgt) / tgt
        status = "PASS" if abs(dev) <= 0.10 else "WARN"
        print(f"  {status}  Runtime {mmss(total)} vs target {a.target} ({dev:+.0%}). Cut or add about {abs(total - tgt) / 60 * a.wpm:.0f} words." if status == "WARN"
              else f"  PASS  Runtime {mmss(total)} within 10% of target {a.target}.")

    pay = [s for s in secs if s["payoff"]]
    if not pay:
        print("  WARN  No section heading marked PAYOFF; payoff position not checked.")
    elif not a.shorts:
        pos = pay[0]["start"] / total if total else 0
        ok = 0.70 <= pos <= 0.85
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  Payoff starts at {mmss(pay[0]['start'])} = {pos:.0%} of runtime (target 70-85%).")

    beats = [0.0] + [s["start"] for s in secs if s["retention"]] + [total]
    beats = sorted(set(beats))
    worst = max((b - a_) for a_, b in zip(beats, beats[1:])) if len(beats) > 1 else total
    ok = worst <= gap_limit
    fails += not ok
    print(f"  {'PASS' if ok else 'FAIL'}  Longest stretch without a marked retention beat: {worst:.0f}s (limit {gap_limit:.0f}s).")

    if not a.shorts:
        short = [chapter_name(s["heading"]) for s in secs if s["dur"] < 10]
        if short:
            print(f"  WARN  Sections under 10s can't be their own YouTube chapter: {', '.join(short)}. Merge them in the chapter list.")
        print("\nChapters (rename each to a mini-headline with the keyword where natural; merge any flagged above):")
        for s in secs:
            if s["dur"] >= 10 or s is secs[0]:
                print(f"  {mmss(s['start'])} {chapter_name(s['heading']).title() if chapter_name(s['heading']).isupper() else chapter_name(s['heading'])}")

    hz = lint_text("\n".join(s["text"] for s in secs))
    print("\nHumanizer lint (spoken words only)")
    print(report("spoken", hz))
    fails += hz_failed(hz)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
