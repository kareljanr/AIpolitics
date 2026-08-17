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
import re
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


def build_digest() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"🏛 <b>Proposal Radar</b> daily digest",
        f"<i>{_e(now)}</i>",
        "",
    ]

    # loop state
    state_path = DATA / "loop_state.csv"
    if state_path.exists():
        with state_path.open(encoding="utf-8", newline="") as f:
            st = list(csv.DictReader(f))
        if st:
            s = st[0]
            lines.append(
                f"Ticks: <b>{_e(s.get('ticks_completed',''))}</b> · "
                f"Scored: <b>{_e(s.get('proposals_scored',''))}</b> · "
                f"Last: <code>{_e(s.get('last_unit_id',''))}</code>"
            )
            lines.append(f"Mode: {_e(s.get('mode',''))} · paused={_e(s.get('paused',''))}")
            lines.append("")

    # top clowns / genius from proposals
    prop_path = DATA / "proposals.csv"
    if prop_path.exists():
        with prop_path.open(encoding="utf-8", newline="") as f:
            rows = [r for r in csv.DictReader(f) if r.get("proposal_id") and r.get("clownpoints")]
        def fnum(x: str) -> float:
            try:
                return float(x)
            except (TypeError, ValueError):
                return float("-inf")

        clowns = sorted(rows, key=lambda r: -fnum(r.get("clownpoints", "")))[:3]
        genius = sorted(rows, key=lambda r: -fnum(r.get("genius_score", "")))[:3]

        if clowns:
            lines.append("<b>🤡 Top clowns</b>")
            for r in clowns:
                pain = r.get("pain_work_minutes") or "—"
                lines.append(
                    f"• {_e(r.get('title',''))[:80]} — "
                    f"c{r.get('clownpoints')} g{r.get('genius_score')} · {pain} min"
                )
            lines.append("")
        if genius:
            lines.append("<b>💡 Top genius</b>")
            for r in genius:
                lines.append(
                    f"• {_e(r.get('title',''))[:80]} — "
                    f"g{r.get('genius_score')} c{r.get('clownpoints')}"
                )
            lines.append("")

    # last log lines
    log_path = RADAR / "loop_log.md"
    if log_path.exists():
        text = log_path.read_text(encoding="utf-8")
        # last ## header block
        parts = re.split(r"\n## ", text)
        if len(parts) > 1:
            last = parts[-1].strip()
            snippet = last[:700]
            lines.append("<b>Last tick log</b>")
            lines.append(f"<pre>{_e(snippet)}</pre>")

    lines.append("")
    lines.append(
        f'<a href="https://github.com/kareljanr/AIpolitics/tree/main/docs/proposal-radar">'
        f"repo/proposal-radar</a>"
    )
    msg = "\n".join(lines)
    if len(msg) > 3900:
        msg = msg[:3880] + "\n…"
    return msg


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
    text = args.text.strip() if args.text else build_digest()
    try:
        send_message(token, chat, text, thread, dry_run=args.dry_run)
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
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
