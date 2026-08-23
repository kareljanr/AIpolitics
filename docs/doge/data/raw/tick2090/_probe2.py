# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2090")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(str(r).lower() for r in csv.DictReader(f))
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(
        ((r.get("entity_id") or "") + " " + (r.get("title") or "")).lower()
        for r in csv.DictReader(f)
    )


def mined(term: str) -> bool:
    return term.lower() in blob


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read(), resp.geturl()


CANDS = [
    ("0407601720", "lidwina-vzw", "lidwina"),
    ("0471475527", "zilvervogel", "zilvervogel"),
    ("0471475527", "czd", "czd"),
    ("0415018755", "caria", "caria"),
    ("0428692191", "de-medemens", "medemens"),  # mined
    # more disability / WZC
    ("0410853396", "de-lovie", "lovie"),  # mined
    ("0443072838", "ocura", "ocura"),  # mined
    ("0409970203", "woonzorgcentrum-sint-carolus", "sint-carolus ternat"),  # maybe mined
    ("0418016550", "woonzorgcentrum-st-vincentius", "vincentius antwerpen"),  # mined YE2024
    ("0861646050", "woonzorgcentrum-sint-vincentius", "vincentius lochristi"),
    ("0448190181", "woon-en-zorgcentrum-sint-jozef-vzw", "sint-jozef rumst"),  # mined
]

for kbo, slug, term in CANDS:
    if mined(term) or mined(kbo) or mined(".".join([kbo[:4], kbo[4:7], kbo[7:]])):
        print("SKIP", term)
        continue
    try:
        data, final = fetch(f"https://www.companyweb.be/nl/{kbo}/{slug}")
        t = data.decode("utf-8", "replace")
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        omzet = re.search(r"omzet:\s*\"([^\"]+)\"", t)
        bruto = re.search(r"bruto_marge:\s*\"([^\"]+)\"", t)
        winst = re.search(r"winst:\s*\"([^\"]+)\"", t)
        title = re.search(r"<title>([^<]+)</title>", t)
        filed = re.search(r"neergelegd op ([0-9\-]+)", t)
        print(
            "PAGE",
            kbo,
            "YE",
            ye.group(1) if ye else "?",
            "filed",
            filed.group(1) if filed else "?",
            "omzet",
            omzet.group(1) if omzet else "?",
            "bruto",
            bruto.group(1) if bruto else "?",
            "winst",
            winst.group(1) if winst else "?",
            (title.group(1)[:75] if title else "?"),
        )
        if ye and ye.group(1) == "2025":
            (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
            print("  SAVED YE2025")
    except Exception as e:
        print("FAIL", kbo, slug, type(e).__name__)
