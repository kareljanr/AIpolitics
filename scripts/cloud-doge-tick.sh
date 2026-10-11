#!/usr/bin/env bash
# One DOGE loop tick inside GitHub Actions. See .github/workflows/doge-loop.yml.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

mkdir -p "${HOME}/.grok"
if [[ -z "${GROK_AUTH_JSON:-}" ]]; then
  echo "Missing GROK_AUTH_JSON." >&2
  exit 1
fi
printf '%s' "${GROK_AUTH_JSON}" > "${HOME}/.grok/auth.json"
chmod 600 "${HOME}/.grok/auth.json"
unset GROK_AUTH_JSON || true

git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git config user.name "github-actions[bot]"

git pull --rebase --autostash origin main

export PATH="${HOME}/.grok/bin:${PATH}"
grok --version

grok \
  --cwd "$ROOT" \
  --permission-mode bypassPermissions \
  --max-turns 24 \
  --output-format plain \
  -p "You are running one DOGE Belgium research tick inside GitHub Actions. Follow .grok/skills/doge-loop/SKILL.md and docs/doge/LOOP.md exactly. Do one primary unit, then commit and push, then stop. Do not send FOI letters. Do not force-push. Do not start a second unit. The PDF archive docs/doge/data/raw is not in this checkout; if a stored PDF is required, fetch the public source URL instead. If paused=yes, stop without an empty commit. If git push conflicts, pull --rebase once and push once, then stop."
