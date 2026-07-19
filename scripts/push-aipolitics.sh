#!/usr/bin/env bash
# Push prepared AIpolitics content into the empty GitHub repo.
# Run this on any machine where YOU are logged into GitHub (gh auth / git credentials).
set -euo pipefail

REPO_URL="${1:-https://github.com/kareljanr/AIpolitics.git}"
SRC_BRANCH="${2:-cursor/aipolitics-repo-af77}"
WORKDIR=$(mktemp -d)
trap 'rm -rf "$WORKDIR"' EXIT

echo "Cloning Taxonomy branch $SRC_BRANCH ..."
git clone --depth 1 --branch "$SRC_BRANCH" https://github.com/kareljanr/Taxonomy.git "$WORKDIR/src"

cd "$WORKDIR/src"
rm -f CREATE-AIPOLITICS-REPO.md
# Fresh history (no SEMIC Taxonomy ancestry)
git checkout --orphan main-aipolitics
git add -A
git -c user.email="cursoragent@cursor.com" -c user.name="Cursor Agent" \
  commit -m "Initial AIpolitics repository — Ghent smart liberal movement"

echo "Pushing to $REPO_URL ..."
git push -u "$REPO_URL" HEAD:main

echo "Done. Open: https://github.com/kareljanr/AIpolitics"
