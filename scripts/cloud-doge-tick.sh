#!/usr/bin/env bash
# One DOGE loop tick inside GitHub Actions. See .github/workflows/doge-loop.yml.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# shellcheck source=cloud-grok-auth.sh
source "${ROOT}/scripts/cloud-grok-auth.sh"

git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git config user.name "github-actions[bot]"

git pull --rebase --autostash origin main

grok --version

grok \
  --cwd "$ROOT" \
  --permission-mode bypassPermissions \
  --max-turns 48 \
  --output-format plain \
  -p "You are running one DOGE Belgium research tick inside GitHub Actions. Rules: one primary unit, sourced euros only, no invented numbers, do not send FOI letters, do not force-push, do not open a second unit. Do not open research_queue.csv, SKILL.md, or LOOP.md. Run: python scripts/next_doge_unit.py. That output is the only unit. Do it, update the CSVs and docs/doge/loop_log.md with a small Python or line edit, commit, push, and stop. The PDF archive docs/doge/data/raw is not checked out; fetch the public source URL if you need a document. If paused=yes, stop without an empty commit. If git push conflicts, pull --rebase once and push once, then stop."
