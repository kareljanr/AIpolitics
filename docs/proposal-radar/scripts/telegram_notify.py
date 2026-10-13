#!/usr/bin/env python3
"""Send Proposal Radar digest to Telegram (separate chat from finance).

Loads:
  1) env vars TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID / TELEGRAM_THREAD_ID
  2) docs/proposal-radar/config/telegram.env
  3) portfolio signals/.env for TOKEN only (never finance CHAT_ID)

Usage:
  python telegram_notify.py --dry-run
  python telegram_notify.py
  python telegram_notify.py --text "custom message"
"""
from __future__ import annotations

import argparse
import csv
import html
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    print("Need requests: pip install requests", file=sys.stderr)
    sys.exit(1)

RADAR = Path(__file__).resolve().parents[1]
ROOT = RADAR.parents[1]  # AIpolitics
DATA = RADAR / "data"
CONFIG_ENV = RADAR / "config" / "telegram.env"
DEFAULT_PORTFOLIO_ENV = Path(r"C:\Users\karel\dev\portfolio\signals\.env")

# Finance chat — never default to this for politics
FINANCE_CHAT_ID = "-1003740047943"


def _load_dotenv(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.exists():
        return out
    text = path.read_text(encoding="utf-8-sig")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def load_telegram_config() -> tuple[str, str, int | None]:
    env: dict[str, str] = {}
    # 1) process env
    for k in ("TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID", "TELEGRAM_THREAD_ID", "PORTFOLIO_ENV"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    # 2) AIpolitics telegram.env
    env = {**_load_dotenv(CONFIG_ENV), **env}
    # 3) portfolio token only
    portfolio = Path(env.get("PORTFOLIO_ENV") or DEFAULT_PORTFOLIO_ENV)
    p = _load_dotenv(portfolio)
    if not env.get("TELEGRAM_BOT_TOKEN") and p.get("TELEGRAM_BOT_TOKEN"):
        env["TELEGRAM_BOT_TOKEN"] = p["TELEGRAM_BOT_TOKEN"]

    token = (env.get("TELEGRAM_BOT_TOKEN") or "").strip()
    chat = (env.get("TELEGRAM_CHAT_ID") or "").strip()
    thread_raw = (env.get("TELEGRAM_THREAD_ID") or "").strip()
    thread = int(thread_raw) if thread_raw.isdigit() else None

    if chat and chat == FINANCE_CHAT_ID and not thread:
        print(
            "REFUSING: TELEGRAM_CHAT_ID is the finance group without a separate thread. "
            "Use a new group or a dedicated forum topic for AIpolitics.",
            file=sys.stderr,
        )
        sys.exit(2)

    return token, chat, thread


def send_message(token: str, chat_id: str, text: str, thread_id: int | None, dry_run: bool) -> None:
    if dry_run:
        print("=== DRY RUN Telegram ===")
        print(text)
        return
    if not token or not chat_id:
        raise SystemExit(
            "Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID.\n"
            f"Create {CONFIG_ENV} from telegram.env.example and set a politics-only chat id."
        )
    payload: dict = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    if thread_id is not None:
        payload["message_thread_id"] = thread_id
    r = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json=payload,
        timeout=30,
    )
    body = r.json()
    if not body.get("ok"):
        raise SystemExit(f"Telegram API error: {body}")
    print("Telegram sent OK")


def _e(s: str) -> str:
    return html.escape(s or "", quote=False)


SENT_PATH = DATA / "digest_sent.csv"
SENT_FIELDS = ("kind", "record_id", "stamp", "sent_utc")


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _sent_index(rows: list[dict]) -> dict[tuple[str, str], str]:
    out: dict[tuple[str, str], str] = {}
    for row in rows:
        kind = (row.get("kind") or "").strip()
        record_id = (row.get("record_id") or "").strip()
        if kind and record_id:
            out[(kind, record_id)] = (row.get("stamp") or "").strip()
    return out


def _load_sent() -> tuple[dict[tuple[str, str], str], bool]:
    if not SENT_PATH.exists():
        return {}, False
    return _sent_index(_read_csv(SENT_PATH)), True


def _write_sent(index: dict[tuple[str, str], str]) -> None:
    SENT_PATH.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with SENT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SENT_FIELDS)
        writer.writeheader()
        for (kind, record_id), stamp in sorted(index.items()):
            writer.writerow(
                {"kind": kind, "record_id": record_id, "stamp": stamp, "sent_utc": now}
            )


def _is_new(index: dict[tuple[str, str], str], kind: str, record_id: str, stamp: str) -> bool:
    return index.get((kind, record_id)) != stamp


def _rating_block(row: dict) -> str:
    lines = [f"• <b>{_e((row.get('title') or '')[:140])}</b>"]
    lines.append(
        f"  clown {_e(row.get('clownpoints') or '—')} · "
        f"genius {_e(row.get('genius_score') or '—')} · "
        f"index {_e(row.get('policy_index') or '—')} · "
        f"{_e(row.get('score_confidence') or 'unscored')}"
    )
    summary = (row.get("summary_one_line") or "").strip()
    if summary:
        lines.append(f"  {_e(summary[:220])}")
    who = " · ".join(
        part
        for part in (
            (row.get("actor_name") or "").strip(),
            (row.get("status") or "").strip(),
            (row.get("jurisdiction") or "").strip(),
        )
        if part
    )
    if who:
        lines.append(f"  {_e(who)}")
    return "\n".join(lines)


def build_digest() -> tuple[list[str], dict[tuple[str, str], str]]:
    """Return (messages, sent-index to store).

    Messages are empty when no new rating should be posted. Unscored queue
    rows stay in the repo and are not sent. The all-time boards stay in
    public/leaderboard_*.md.
    """
    sent, _had_state = _load_sent()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    proposals = [
        row
        for row in _read_csv(DATA / "proposals.csv")
        if row.get("proposal_id") and (row.get("clownpoints") or "").strip()
    ]
    new_scored = [
        row
        for row in proposals
        if _is_new(sent, "scored", row["proposal_id"], (row.get("updated_utc") or "").strip())
    ]
    new_scored.sort(key=lambda row: row.get("updated_utc") or "", reverse=True)
    if not new_scored:
        return [], sent

    for row in new_scored:
        sent[("scored", row["proposal_id"])] = (row.get("updated_utc") or "").strip()

    footer = (
        '<a href="https://github.com/kareljanr/AIpolitics/blob/main/docs/proposal-radar/public/leaderboard_clowns.md">'
        "All-time boards</a>"
    )
    header = f"🏛 <b>Proposal Radar</b> — new ratings\n<i>{_e(now)}</i>"
    messages: list[str] = []
    chunk: list[str] = []

    def _flush() -> None:
        if not chunk:
            return
        messages.append(header + "\n\n" + "\n\n".join(chunk) + "\n\n" + footer)
        chunk.clear()

    for block in (_rating_block(row) for row in new_scored):
        trial = header + "\n\n" + "\n\n".join(chunk + [block]) + "\n\n" + footer
        if chunk and len(trial) > 3900:
            _flush()
        chunk.append(block)
    _flush()
    return messages, sent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--text", default="", help="Override message body (HTML ok)")
    ap.add_argument("--setup-help", action="store_true", help="Print chat setup steps")
    args = ap.parse_args()

    if args.setup_help:
        print(
            """
AIpolitics Telegram setup (KEEP SEPARATE FROM FINANCE)
======================================================
Finance already uses group -1003740047943 (portfolio screams / signals).
Do NOT send government analysis there without a dedicated forum topic.

Recommended: NEW group
  1. Telegram → New Group → name e.g. "AIpolitics Radar"
  2. Add your bot (same BotFather bot as portfolio is fine)
  3. Make bot admin (so it can post)
  4. Send any message in the group
  5. Get chat id:
       python docs/proposal-radar/scripts/telegram_notify.py --resolve-chats
     or open https://api.telegram.org/bot<TOKEN>/getUpdates after messaging the bot

Alternative: same SUPERGROUP with Topics enabled
  - Create topic "Proposal Radar"
  - Set TELEGRAM_CHAT_ID=<supergroup id> and TELEGRAM_THREAD_ID=<topic id>
  - Finance already uses thread_id=2 — use a different thread

Then:
  copy config\\telegram.env.example → config\\telegram.env
  set TELEGRAM_CHAT_ID=...
  (token can stay empty if portfolio signals\\.env has TELEGRAM_BOT_TOKEN)
"""
        )
        return 0

    token, chat, thread = load_telegram_config()
    pending_sent: dict[tuple[str, str], str] | None = None
    if args.text.strip():
        texts = [args.text.strip()]
    else:
        texts, pending_sent = build_digest()
        if not texts:
            print("No new ratings. Not sending.")
            if not args.dry_run and pending_sent is not None:
                _write_sent(pending_sent)
            return 0
    if not args.dry_run and (not token or not chat):
        print("Telegram chat is not configured. Not sending, and not marking these items as posted.")
        print("\n\n".join(texts))
        return 0
    try:
        for text in texts:
            send_message(token, chat, text, thread, dry_run=args.dry_run)
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
    if pending_sent is not None and not args.dry_run:
        _write_sent(pending_sent)
    return 0


if __name__ == "__main__":
    # optional resolve-chats subcommand via argv hack
    if "--resolve-chats" in sys.argv:
        token, _, _ = load_telegram_config()
        if not token:
            print("No token", file=sys.stderr)
            sys.exit(2)
        r = requests.get(f"https://api.telegram.org/bot{token}/getUpdates", timeout=30)
        data = r.json()
        if not data.get("ok"):
            print(data)
            sys.exit(1)
        seen = set()
        for u in data.get("result", []):
            msg = u.get("message") or u.get("channel_post") or {}
            chat = msg.get("chat") or {}
            key = (chat.get("id"), chat.get("title") or chat.get("username"), chat.get("type"))
            if key[0] is None or key in seen:
                continue
            seen.add(key)
            thread = (msg.get("message_thread_id"),)
            print(f"chat_id={chat.get('id')}  title={key[1]!r}  type={key[2]}  thread={msg.get('message_thread_id')}")
        if not seen:
            print("No updates. Message the bot/group first, then re-run.")
        sys.exit(0)
    raise SystemExit(main())
