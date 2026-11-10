#!/usr/bin/env bash
# Build a clean .skill bundle for release.
#
# Always package through this script: zipping the working tree directly ships
# .git internals and build files. It stages a filtered copy, zips it, and
# verifies the result.
#
# tools/ and LICENSE ship in the bundle (the skill calls tools/ at runtime;
# MIT requires the notice to travel with copies); scripts/ and evals/ do not.
#
# Usage: scripts/package.sh [output-path]   (default: ../elite-content-studio.skill)
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
NAME="elite-content-studio"
OUT="${1:-$REPO_DIR/../$NAME.skill}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Fail fast if a bundled tool doesn't even compile.
python3 -m py_compile "$REPO_DIR"/tools/*.py
rm -rf "$REPO_DIR/tools/__pycache__"

rsync -a \
  --exclude '.git' \
  --exclude '.gitignore' \
  --exclude '.DS_Store' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  --exclude 'evals' \
  --exclude 'scripts' \
  --exclude '*.skill' \
  "$REPO_DIR/" "$TMP/$NAME/"

rm -f "$OUT"
(cd "$TMP" && zip -qr "$NAME.skill" "$NAME")
mv "$TMP/$NAME.skill" "$OUT"

echo "Packaged clean bundle: $OUT"
# Read the listing once. Piping `unzip -l` straight into `grep -q` breaks under
# pipefail: grep exits on the first match, unzip gets SIGPIPE (141), and the
# pipeline reports failure even though the file is there.
LISTING="$(unzip -l "$OUT")"
tail -2 <<<"$LISTING"
if grep -qE '\.git/|\.gitignore|evals/|scripts/|__pycache__' <<<"$LISTING"; then
  echo "ERROR: bundle contains excluded files" >&2
  exit 1
fi
for f in LICENSE tools/script_timing.py tools/metadata_lint.py tools/humanizer_lint.py tools/keyword_ideas.py; do
  grep -q "$NAME/$f" <<<"$LISTING" || { echo "ERROR: bundle missing $f" >&2; exit 1; }
done
echo "Verified: no repo internals, evals or build scripts in bundle; tools present"
