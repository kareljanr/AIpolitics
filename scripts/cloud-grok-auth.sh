#!/usr/bin/env bash
# Shared login for the Actions ticks. Source this file. Do not execute it.
# A cached ~/.grok/auth.json is kept only when `grok models` accepts it.
# Otherwise the script writes GROK_AUTH_JSON and stops if that login is rejected.

mkdir -p "${HOME}/.grok"
export PATH="${HOME}/.grok/bin:${PATH}"

AUTH="${HOME}/.grok/auth.json"

# `grok models` exits 0 even when logged out. It prints "You are not authenticated".
# A rejected auth.json can also be deleted by the CLI, so the exit code is not enough.
grok_login_ok() {
  local err first
  err="$(grok models 2>&1)" || true
  first="${err%%$'\n'*}"
  if [[ "$first" == *"logged in"* || "$first" == *"not authenticated"* || "$first" == *"Not signed in"* ]]; then
    echo "Grok login check: ${first}"
  else
    echo "Grok login check: unrecognized response."
  fi
  [[ "$first" == *"logged in"* && "$first" != *"not authenticated"* && "$first" != *"Not signed in"* ]]
}

describe_auth() {
  command -v python3 >/dev/null 2>&1 || return 0
  python3 - <<'PY'
import json, os
path = os.path.expanduser("~/.grok/auth.json")
try:
    data = json.load(open(path, encoding="utf-8"))
except Exception:
    print(f"auth.json is not valid JSON ({os.path.getsize(path)} bytes).")
    raise SystemExit(0)
if not isinstance(data, dict) or not data:
    print("auth.json has no login entry.")
    raise SystemExit(0)
for key, val in data.items():
    issuer = key.split("::", 1)[0]
    if not isinstance(val, dict):
        print(f"auth entry {issuer}: not an object")
        continue
    print(
        "auth entry"
        f" issuer={issuer}"
        f" mode={val.get('auth_mode')}"
        f" expires_at={val.get('expires_at')}"
        f" has_refresh={bool(val.get('refresh_token'))}"
    )
PY
}

# Hide the secret from `grok models` so a value in the environment cannot mask a bad file.
SECRET="${GROK_AUTH_JSON:-}"
unset GROK_AUTH_JSON || true

if [[ -s "${AUTH}" ]] && grok_login_ok; then
  echo "Using the saved Grok login."
elif [[ -n "${SECRET}" ]]; then
  printf '%s' "${SECRET}" > "${AUTH}"
  unset SECRET
  chmod 600 "${AUTH}"
  echo "Wrote GROK_AUTH_JSON ($(wc -c < "${AUTH}" | tr -d ' ') bytes)."
  describe_auth
  if grok_login_ok; then
    echo "GROK_AUTH_JSON is accepted."
  else
    echo "GROK_AUTH_JSON was rejected. Replace the Actions secret with the current ~/.grok/auth.json from a machine where grok models succeeds." >&2
    exit 1
  fi
else
  echo "Missing GROK_AUTH_JSON." >&2
  exit 1
fi
if [[ ! -s "${AUTH}" ]]; then
  echo "Grok did not leave a login at ~/.grok/auth.json." >&2
  exit 1
fi
chmod 600 "${AUTH}"
