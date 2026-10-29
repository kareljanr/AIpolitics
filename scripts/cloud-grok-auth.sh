#!/usr/bin/env bash
# Shared login for the Actions ticks. Source this file. Do not execute it.
# `grok models` does not refresh an expired access token. It prints
# "You are not authenticated" and can delete auth.json. This script refreshes
# the OIDC refresh token at the issuer, then asks grok models again.
# The entry with the later expires_at is tried first, so a login this runner
# already refreshed is not replaced by an older GROK_AUTH_JSON.

mkdir -p "${HOME}/.grok"
export PATH="${HOME}/.grok/bin:${PATH}"

AUTH="${HOME}/.grok/auth.json"

# `grok models` exits 0 even when logged out. It prints "You are not authenticated".
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
  python3 - "${AUTH}" << 'PY'
import json, os, sys
path = sys.argv[1]
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

auth_expires_at() {
  python3 - "$1" << 'PY'
import json, sys
path = sys.argv[1]
try:
    data = json.load(open(path, encoding="utf-8"))
except Exception:
    raise SystemExit(0)
best = ""
if isinstance(data, dict):
    for val in data.values():
        if isinstance(val, dict):
            exp = val.get("expires_at") or ""
            if exp > best:
                best = exp
print(best)
PY
}

# Refresh AUTH in place. Prints status only.
refresh_oidc() {
  python3 - "${AUTH}" << 'PY'
import json, sys, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timedelta, timezone

path = sys.argv[1]
data = json.load(open(path, encoding="utf-8"))
if not isinstance(data, dict) or not data:
    print("OIDC refresh failed: auth.json has no entries")
    raise SystemExit(1)

def expires(val):
    return val.get("expires_at") or "" if isinstance(val, dict) else ""

key = max(data, key=lambda item: expires(data[item]))
val = data[key]
refresh = val.get("refresh_token") if isinstance(val, dict) else None
client_id = val.get("oidc_client_id") if isinstance(val, dict) else None
issuer = ((val.get("oidc_issuer") if isinstance(val, dict) else None) or "https://auth.x.ai").rstrip("/")
if not refresh or not client_id:
    print("OIDC refresh failed: no refresh token or client id")
    raise SystemExit(1)

body = urllib.parse.urlencode(
    {
        "grant_type": "refresh_token",
        "refresh_token": refresh,
        "client_id": client_id,
    }
).encode()
req = urllib.request.Request(
    issuer + "/oauth2/token",
    data=body,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    },
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        status = resp.status
        payload = json.loads(resp.read().decode())
except urllib.error.HTTPError as exc:
    err = ""
    try:
        err = json.loads(exc.read().decode()).get("error", "")
    except Exception:
        err = ""
    print(f"OIDC refresh failed: http {exc.code} error={err}")
    raise SystemExit(1)

access = payload.get("access_token")
expires_in = payload.get("expires_in")
if not access or not expires_in:
    print("OIDC refresh failed: response missing access_token or expires_in")
    raise SystemExit(1)

now = datetime.now(timezone.utc)
exp = now + timedelta(seconds=int(expires_in))

def stamp(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f") + "000Z"

rotated = bool(payload.get("refresh_token")) and payload.get("refresh_token") != refresh
val["key"] = access
val["expires_at"] = stamp(exp)
val["create_time"] = stamp(now)
if payload.get("refresh_token"):
    val["refresh_token"] = payload["refresh_token"]
data[key] = val
tmp = path + ".refresh.tmp"
with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(data, fh, separators=(",", ":"))
os_replace = __import__("os")
os_replace.replace(tmp, path)
print(
    f"OIDC refresh: http {status} expires_at={val['expires_at']} "
    f"rotated_refresh={str(rotated).lower()} expires_in={int(expires_in)}"
)
PY
}

try_login_source() {
  local src="$1" label="$2"
  [[ -n "${src}" && -s "${src}" ]] || return 1
  cp "${src}" "${AUTH}"
  chmod 600 "${AUTH}"
  if grok_login_ok; then
    echo "Using ${label}."
    return 0
  fi
  if [[ ! -s "${AUTH}" ]]; then
    cp "${src}" "${AUTH}"
    chmod 600 "${AUTH}"
  fi
  if refresh_oidc && grok_login_ok; then
    echo "Refreshed ${label}."
    return 0
  fi
  return 1
}

# Hide the secret from `grok models` so a value in the environment cannot mask a bad file.
SECRET="${GROK_AUTH_JSON:-}"
unset GROK_AUTH_JSON || true

CACHE_COPY=""
SECRET_COPY=""
cleanup_auth_copies() {
  [[ -n "${CACHE_COPY}" ]] && rm -f "${CACHE_COPY}"
  [[ -n "${SECRET_COPY}" ]] && rm -f "${SECRET_COPY}"
}
trap cleanup_auth_copies EXIT

if [[ -s "${AUTH}" ]]; then
  CACHE_COPY="$(mktemp)"
  cp "${AUTH}" "${CACHE_COPY}"
  chmod 600 "${CACHE_COPY}"
fi
if [[ -n "${SECRET}" ]]; then
  SECRET_COPY="$(mktemp)"
  printf '%s' "${SECRET}" > "${SECRET_COPY}"
  unset SECRET
  chmod 600 "${SECRET_COPY}"
fi

FIRST_SRC="${SECRET_COPY}"
FIRST_LABEL="GROK_AUTH_JSON"
SECOND_SRC="${CACHE_COPY}"
SECOND_LABEL="cached login"
if [[ -n "${CACHE_COPY}" && -n "${SECRET_COPY}" ]]; then
  EXP_CACHE="$(auth_expires_at "${CACHE_COPY}")"
  EXP_SECRET="$(auth_expires_at "${SECRET_COPY}")"
  if [[ "${EXP_CACHE}" > "${EXP_SECRET}" ]]; then
    FIRST_SRC="${CACHE_COPY}"
    FIRST_LABEL="cached login"
    SECOND_SRC="${SECRET_COPY}"
    SECOND_LABEL="GROK_AUTH_JSON"
  fi
elif [[ -n "${CACHE_COPY}" ]]; then
  FIRST_SRC="${CACHE_COPY}"
  FIRST_LABEL="cached login"
  SECOND_SRC=""
  SECOND_LABEL=""
fi

if try_login_source "${FIRST_SRC}" "${FIRST_LABEL}"; then
  :
elif try_login_source "${SECOND_SRC}" "${SECOND_LABEL}"; then
  :
elif [[ -z "${SECRET_COPY}" && -z "${CACHE_COPY}" ]]; then
  echo "Missing GROK_AUTH_JSON." >&2
  exit 1
else
  echo "GROK_AUTH_JSON was rejected. The access token is expired and the refresh token was not accepted." >&2
  exit 1
fi

if [[ ! -s "${AUTH}" ]]; then
  echo "Grok did not leave a login at ~/.grok/auth.json." >&2
  exit 1
fi
chmod 600 "${AUTH}"
describe_auth
