#!/usr/bin/env python3
"""Harvest allowlisted BE news/gov RSS feeds into ingest_queue.csv.

Usage (from repo root or this dir):
  python docs/proposal-radar/scripts/rss_harvest.py
  python docs/proposal-radar/scripts/rss_harvest.py --max-per-feed 30 --dry-run
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urlunparse

try:
    import feedparser
    import requests
except ImportError as e:
    print("Need feedparser + requests:", e, file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[3]
RADAR = ROOT / "docs" / "proposal-radar"
DATA = RADAR / "data"
RAW = RADAR / "raw"
CONFIG = Path(__file__).resolve().parent / "config_feeds.json"
INGEST = DATA / "ingest_queue.csv"
SOURCES = DATA / "sources.csv"

USER_AGENT = "AIpolitics-ProposalRadar/1.0 (+https://github.com/kareljanr/AIpolitics; research bot)"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def norm_url(url: str) -> str:
    if not url:
        return ""
    p = urlparse(url.strip())
    # drop fragment + common tracking
    q = p.query
    if q:
        parts = [kv for kv in q.split("&") if not kv.lower().startswith(("utm_", "fbclid"))]
        q = "&".join(parts)
    path = p.path.rstrip("/") or "/"
    return urlunparse((p.scheme, p.netloc.lower(), path, "", q, ""))


def slug_id(prefix: str, text: str) -> str:
    h = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
    return f"{prefix}_{h}"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def read_csv(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


BE_SIGNALS = (
    "belgi", "belgique", "belgium", "vlaams", "flander", "wallon", "brussel",
    "bruxelles", "federale", "fédéral", "de wever", "ministerraad", "regering",
    "gouvernement", "kamer", "parlement", "arizona", "n-va", "vooruit", "cd&v",
    "open vld", "mr ", "engagés", "ps ", "pvda", "ptb", "groen", "ecolo",
    "fwb", "vlaanderen", "diependaele", "jambon", "weyts", "gennez",
)

FOREIGN_HARD = (
    "trump", "netanyahu", "smithsonian", "new york", "mallorca", "iran ",
    "oekraïne", "ukraine", "moskou", "moscow", "china en rusland", "fifa",
    "tour de france", "alpe d", "club brugge", "frankfurt", "shein",
)


def score_proposal_likelihood(title: str, summary: str, cfg: dict, source_class: str = "press") -> tuple[int, str]:
    text = f"{title} {summary}".lower()
    for n in cfg.get("noise_keywords", []):
        if n.lower() in text:
            return 0, "noise"
    for f in FOREIGN_HARD:
        if f in text and not any(b in text for b in ("belgi", "vlaams", "brussel", "wallon")):
            # allow if explicitly Belgian angle later; default drop hard foreign
            if not any(b in text for b in BE_SIGNALS):
                return 0, "foreign"

    hits = []
    for kw in (
        cfg.get("proposal_keywords_nl", [])
        + cfg.get("proposal_keywords_fr", [])
        + cfg.get("proposal_keywords_en", [])
    ):
        if kw.lower() in text:
            hits.append(kw)
    if not hits:
        return 1, ""

    be = any(b in text for b in BE_SIGNALS) or source_class == "gov_press"
    if not be:
        # keyword hit but no BE signal → deprioritize heavily
        return 2, "|".join(sorted(set(hits))[:4]) + "|no_be"

    pri = min(10, 5 + len(set(hits)))
    return pri, "|".join(sorted(set(hits))[:8])


def fetch_feed(url: str, timeout: int = 25) -> feedparser.FeedParserDict:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/xml, text/xml, */*"}
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
        r.raise_for_status()
        return feedparser.parse(r.content)
    except Exception as e:
        # feedparser can try URL itself as fallback
        try:
            return feedparser.parse(url)
        except Exception:
            print(f"  FAIL {url}: {e}", file=sys.stderr)
            return feedparser.FeedParserDict(entries=[])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-per-feed", type=int, default=40)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-priority", type=int, default=4, help="Only enqueue priority >= this")
    args = ap.parse_args()

    cfg = load_json(CONFIG)
    ingest_fields = [
        "ingest_id",
        "title_hint",
        "url",
        "discovered_via",
        "jurisdiction_guess",
        "priority",
        "status",
        "proposal_id",
        "created_utc",
        "updated_utc",
        "notes",
    ]
    source_fields = [
        "source_id",
        "title",
        "url",
        "publisher",
        "accessed_date",
        "source_class",
        "language",
        "proposal_ids",
        "notes",
    ]

    existing = read_csv(INGEST)
    by_url = {norm_url(r.get("url", "")): r for r in existing if r.get("url")}
    sources = read_csv(SOURCES)
    source_urls = {norm_url(r.get("url", "")) for r in sources if r.get("url")}

    new_rows: list[dict] = []
    new_sources: list[dict] = []
    stats = {"feeds_ok": 0, "feeds_fail": 0, "entries": 0, "enqueued": 0, "dupes": 0, "low": 0}

    RAW.mkdir(parents=True, exist_ok=True)
    dump_lines = []

    for feed in cfg["feeds"]:
        print(f"Feed {feed['id']}: {feed['url']}")
        parsed = fetch_feed(feed["url"])
        entries = list(getattr(parsed, "entries", []) or [])
        if not entries and not getattr(parsed, "feed", None):
            stats["feeds_fail"] += 1
            print("  (empty/fail)")
            continue
        stats["feeds_ok"] += 1
        print(f"  {len(entries)} entries")

        for entry in entries[: args.max_per_feed]:
            stats["entries"] += 1
            title = (entry.get("title") or "").strip()
            link = norm_url(entry.get("link") or entry.get("id") or "")
            summary = entry.get("summary") or entry.get("description") or ""
            summary = re.sub(r"<[^>]+>", " ", str(summary))[:500]
            if not link or not title:
                continue

            pri, hits = score_proposal_likelihood(
                title, summary, cfg, source_class=feed.get("source_class", "press")
            )
            # gov feeds: lower bar
            if feed.get("source_class") == "gov_press" and pri >= 1:
                pri = max(pri, 5)

            dump_lines.append(
                f"{feed['id']}\t{pri}\t{title[:120]}\t{link}\t{hits}"
            )

            if pri < args.min_priority:
                stats["low"] += 1
                continue
            if link in by_url:
                stats["dupes"] += 1
                continue

            now = utc_now()
            iid = slug_id("ing", link)
            row = {
                "ingest_id": iid,
                "title_hint": title[:240],
                "url": link,
                "discovered_via": "rss",
                "jurisdiction_guess": feed.get("jurisdiction_hint", "multi"),
                "priority": str(pri),
                "status": "open",
                "proposal_id": "",
                "created_utc": now,
                "updated_utc": now,
                "notes": f"feed={feed['id']}; kw={hits}",
            }
            new_rows.append(row)
            by_url[link] = row
            stats["enqueued"] += 1

            if link not in source_urls:
                sid = slug_id("src", link)
                new_sources.append(
                    {
                        "source_id": sid,
                        "title": title[:240],
                        "url": link,
                        "publisher": feed.get("name", feed["id"]),
                        "accessed_date": now[:10],
                        "source_class": feed.get("source_class", "press"),
                        "language": feed.get("language", "nl"),
                        "proposal_ids": "",
                        "notes": f"rss:{feed['id']}",
                    }
                )
                source_urls.add(link)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dump_path = RAW / f"rss_dump_{stamp}.tsv"
    dump_path.write_text("\n".join(dump_lines) + "\n", encoding="utf-8")
    print(f"Dump: {dump_path}")

    if args.dry_run:
        print("DRY RUN stats:", stats)
        for r in new_rows[:15]:
            print(f"  [{r['priority']}] {r['title_hint'][:80]}")
        return 0

    all_ingest = existing + new_rows
    # sort open high priority first for humans/agents reading file
    write_csv(INGEST, ingest_fields, all_ingest)
    write_csv(SOURCES, source_fields, sources + new_sources)
    print("STATS", stats)
    print(f"ingest_queue rows total: {len(all_ingest)} (+{len(new_rows)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
