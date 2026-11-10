#!/usr/bin/env python3
"""
Humanizer lint: flags AI-tell vocabulary, hedging stacks, and negative-parallelism
constructions in viewer-facing copy (scripts, captions, descriptions, posts).

The term lists mirror references/scriptwriting.md (humanizer pass) and the
humanizer assertions in evals/evals.json. Keep all three in sync.

Usage:
    python3 tools/humanizer_lint.py FILE [FILE ...]
    cat draft.txt | python3 tools/humanizer_lint.py -

Exit code 1 when any kill-list term or hedging stack is found, or when
negative-parallelism constructions exceed the budget (1 per file).
Also importable: lint_text(text) -> dict.
"""
import re
import sys

# Hard fails: the eval kill-list plus the generic closers from scriptwriting.md.
KILL_LIST = [
    "delve", "delves", "delving", "tapestry", "testament", "seamless", "seamlessly",
    "showcase", "showcases", "showcasing", "underscore", "underscores",
    "underscoring", "elevate", "elevates", "elevating", "foster", "fosters",
    "fostering", "game-changer", "game changer", "serves as", "stands as",
    "marks a pivotal moment", "in the heart of", "reflects a broader shift",
    "the future looks bright", "exciting times ahead", "at the end of the day",
]

# Warnings: AI-flavored in essay/promo prose, but legitimate in some niches
# ("landscape photography", "vibrant colors" in a painting tutorial). Judge in context.
SOFT_LIST = ["landscape", "intricate", "vibrant", "breathtaking", "must-see", "stunning"]

HEDGING = [
    "could potentially", "might possibly", "has the ability to", "have the ability to",
    "in order to", "due to the fact that",
]

VAGUE_AUTHORITY = ["experts say", "studies show", "many people believe", "research shows"]

NEG_PARALLEL = [
    r"\b(it'?s|this is|that'?s|they'?re|we'?re) not (just|only|merely) [^.?!]{1,60}?[,;:—–-]+\s*(it'?s|this is|that'?s|they'?re|we'?re|but)\b",
    r"\bnot only\b[^.?!]{1,80}?\bbut (also)?\b",
]

NEG_PARALLEL_BUDGET = 1


def _find_terms(text: str, terms: list) -> list:
    hits = []
    low = text.lower()
    for t in terms:
        for m in re.finditer(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", low):
            line = low.count("\n", 0, m.start()) + 1
            hits.append({"term": t, "line": line})
    return hits


def lint_text(text: str) -> dict:
    neg = []
    for pat in NEG_PARALLEL:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            neg.append({"match": m.group(0)[:80], "line": text.count("\n", 0, m.start()) + 1})
    return {
        "kill_list": _find_terms(text, KILL_LIST),
        "soft": _find_terms(text, SOFT_LIST),
        "hedging": _find_terms(text, HEDGING),
        "vague_authority": _find_terms(text, VAGUE_AUTHORITY),
        "negative_parallelism": neg,
    }


def failed(result: dict) -> bool:
    return bool(result["kill_list"] or result["hedging"]
                or len(result["negative_parallelism"]) > NEG_PARALLEL_BUDGET)


def report(name: str, result: dict) -> str:
    out = [f"== {name}"]
    for key, label, status in (
            ("kill_list", "AI-tell term", "FAIL"),
            ("hedging", "Hedging stack", "FAIL"),
            ("soft", "Context-dependent AI-tell (keep only if literal)", "WARN"),
            ("vague_authority", "Vague authority (name the source or cut)", "WARN")):
        for h in result[key]:
            out.append(f"  {status}  line {h['line']}: {label}: '{h['term']}'")
    n = len(result["negative_parallelism"])
    for h in result["negative_parallelism"]:
        status = "FAIL" if n > NEG_PARALLEL_BUDGET else "INFO"
        out.append(f"  {status}  line {h['line']}: negative parallelism: '{h['match']}'")
    if n:
        out.append(f"  negative-parallelism count: {n} (budget {NEG_PARALLEL_BUDGET})")
    out.append("  RESULT: " + ("FAIL" if failed(result) else "PASS"))
    return "\n".join(out)


def main(argv: list) -> int:
    if not argv:
        print(__doc__.strip())
        return 2
    any_fail = False
    for path in argv:
        text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
        res = lint_text(text)
        print(report("stdin" if path == "-" else path, res))
        any_fail |= failed(res)
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
