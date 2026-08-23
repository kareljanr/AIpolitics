# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2081")
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# claim
path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2081":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = "2026-08-25T01:20:00Z"
        row["notes"] = "CLAIM tick2081 probing AGB/FARO/AIESH/REW then unused WZC Sint-Barbara or similar"
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2081")


def fetch(name: str, url: str) -> None:
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"}
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
            final = resp.geturl()
        (RAW / name).write_bytes(data)
        print(f"OK {name} {len(data)} {final}")
    except Exception as e:
        print(f"FAIL {name}: {e}")


URLS = {
    "faro_nl.html": "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_nl.html": "https://www.companyweb.be/nl/0201712587/aiesh",
    "rew_nl.html": "https://www.companyweb.be/nl/0644638937/rew",
    "bornem_jr.html": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    # candidates deferred / unused from prior ticks
    "sint_barbara_nl.html": "https://www.companyweb.be/nl/search?q=0414",  # placeholder
}

# Prefer known deferred from tick2078 raw if exists: sint_barbara
prev = Path("docs/doge/data/raw/tick2078/sint_barbara_nl.html")
if prev.exists():
    t = prev.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"BE0(\d{9})", t) or re.search(r"0\d{3}\.\d{3}\.\d{3}", t)
    title = re.search(r"<title>([^<]+)</title>", t)
    print("prev sint_barbara", title.group(1)[:120] if title else None, m.group(0) if m else None)
    # extract companyweb path
    m2 = re.search(r"companyweb\.be/nl/(\d+)/([a-z0-9\-]+)", t)
    if m2:
        print("slug", m2.group(1), m2.group(2))
        URLS["sint_barbara_nl.html"] = f"https://www.companyweb.be/nl/{m2.group(1)}/{m2.group(2)}"
        URLS["sint_barbara_en.html"] = f"https://www.companyweb.be/en/{m2.group(1)}/{m2.group(2)}"
        URLS["sint_barbara_fr.html"] = f"https://www.companyweb.be/fr/{m2.group(1)}/{m2.group(2)}"
        URLS["kbo_sb.html"] = f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={m2.group(1)}"

# also check den_akker deferred peers: search companyweb for other WZC YE2025
# try WZC Sint-Barbara common KBOs from prior raw name
for name, url in list(URLS.items()):
    if "search" in url:
        continue
    fetch(name, url)

# parse year from stall pages
for name in ["faro_nl.html", "aiesh_nl.html", "rew_nl.html", "sint_barbara_nl.html"]:
    p = RAW / name
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
    filed = re.search(r"neergelegd op ([0-9\-]+)|filed on ([0-9\-]+)", t, re.I)
    title = re.search(r"<title>([^<]+)</title>", t)
    print(
        name,
        "YE",
        m.group(1) if m else "?",
        "filed",
        filed.group(0) if filed else "?",
        "title",
        (title.group(1)[:80] if title else "?"),
    )
