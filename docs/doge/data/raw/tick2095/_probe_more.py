# -*- coding: utf-8 -*-
"""Broader unused WZC/zorg YE2025 hunt via Companyweb search + known KBOs."""
import csv
import re
import urllib.parse
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path(__file__).resolve().parent
ROOT = RAW.parents[1]
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

blob = ""
with open(ROOT / "entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob += " ".join(str(v).lower() for v in r.values()) + " "
with open(ROOT / "research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if (r.get("status") or "").lower() == "done":
            blob += ((r.get("entity_id") or "") + " " + (r.get("title") or "")).lower() + " "


def mined(*terms: str) -> bool:
    return any(t.lower() in blob for t in terms)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8"}
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()


# Companyweb free-text searches that often surface WZC pages
SEARCHES = [
    "woonzorgcentrum",
    "woon-en-zorgcentrum",
    "rusthuis vzw",
    "rustoord vzw",
    "seniorencentrum",
    "woonzorggroep",
]

# Known-ish unused candidates (name/KBO pairs from Flanders care lists / prior probes)
DIRECT = [
    ("0412112345", "skip"),  # placeholder removed below
    ("0406.802.873", "katarinahof"),  # guess - will resolve via search
]

# Direct KBOs spotted in Antwerp repertory / common Flemish WZC not in do-not-redo
KBOS = [
    # try resolve via search pages first; then known numbers:
    "0455.901.234",  # dummy
]


def parse_cw(t: str):
    ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
    first = re.search(
        r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
        r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
        t,
    )
    title = re.search(r"<title>([^<]+)</title>", t)
    filed = re.search(r"neergelegd op ([0-9.\-]+)", t, re.I)
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
    kbo = re.search(r"BE0?(\d{9,10})", t)
    return ye, first, title, filed, fte, kbo


# 1) search pages -> extract company links with 2025
hits = []
for q in SEARCHES:
    url = "https://www.companyweb.be/nl/search?q=" + urllib.parse.quote(q)
    try:
        data = fetch(url)
        (RAW / f"search_{q.replace(' ', '_')}.html").write_bytes(data)
        t = data.decode("utf-8", "replace")
        # links like /nl/0410151137/sint-lucia
        for m in re.finditer(r'href="(/nl/(\d{9,10})/([^"]+))"', t):
            path, kbo, slug = m.group(1), m.group(2), m.group(3)
            name = slug.replace("-", " ")
            if mined(kbo, name):
                continue
            hits.append((kbo, slug, name, path))
        print("SEARCH", q, "links", len(re.findall(r"/nl/\d{9,10}/", t)), "fresh candidates buffered", len(hits))
    except Exception as e:
        print("SEARCH FAIL", q, type(e).__name__, str(e)[:120])

# dedupe
seen = set()
uniq = []
for h in hits:
    if h[0] in seen:
        continue
    seen.add(h[0])
    uniq.append(h)

print("UNIQUE fresh from search", len(uniq))

# probe up to 25 unique fresh
take = []
for kbo, slug, name, path in uniq[:40]:
    url = "https://www.companyweb.be" + path
    try:
        data = fetch(url)
        t = data.decode("utf-8", "replace")
        ye, first, title, filed, fte, _ = parse_cw(t)
        y = ye.group(1) if ye else "?"
        print(
            "PAGE",
            kbo,
            name[:40],
            "YE",
            y,
            "filed",
            filed.group(1) if filed else "?",
            "fte",
            fte.group(1) if fte else "?",
            (title.group(1)[:70] if title else "?"),
        )
        if y == "2025":
            (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
            if first:
                print(
                    "  YE2025 pnl",
                    first.group(2),
                    "eq",
                    first.group(3),
                    "bruto",
                    first.group(4),
                    "omzet",
                    first.group(5),
                )
            # keep if looks like care (title/nace keywords)
            blob_t = (title.group(1) if title else "") + " " + t[:5000]
            if re.search(
                r"rusthuis|woonzorg|R\.V\.T|R\.O\.B|verzorgingstehuis|senior|ouderenzorg|handicap|psychiatr",
                blob_t,
                re.I,
            ):
                take.append((kbo, slug, name, first, filed, fte, title))
                print("  *** CARE YE2025 CANDIDATE ***")
                if len(take) >= 5:
                    break
    except Exception as e:
        print("FAIL", kbo, type(e).__name__, str(e)[:100])

print("TAKE COUNT", len(take))
for row in take:
    print("TAKE", row[0], row[2], row[3].groups() if row[3] else None)
