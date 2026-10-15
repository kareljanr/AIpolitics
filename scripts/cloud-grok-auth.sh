#!/usr/bin/env bash
# Shared login for the Actions ticks. Source this file. Do not execute it.
# A cached ~/.grok/auth.json is kept only when `grok models` accepts it.
# Otherwise the script writes GROK_AUTH_JSON and stops if that login is rejected.

mkdir -p "${HOME}/.grok"
export PATH="${HOME}/.grok/bin:${PATH}"

AUTH="${HOME}/.grok/auth.json"

grok_login_ok() {
  grok models >/dev/null 2>&1
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

if [[ -s "${AUTH}" ]] && grok_login_ok; then
  echo "Using the saved Grok login."
elif [[ -n "${GROK_AUTH_JSON:-}" ]]; then
  printf '%s' "${GROK_AUTH_JSON}" > "${AUTH}"
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
chmod 600 "${AUTH}"
unset GROK_AUTH_JSON || true
