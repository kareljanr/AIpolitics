# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2085")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(str(r).lower() for r in csv.DictReader(f))
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(
        ((r.get("entity_id") or "") + " " + (r.get("title") or "") + " " + (r.get("notes") or "")).lower()
        for r in csv.DictReader(f)
    )


def mined(term: str) -> bool:
    return term.lower() in blob


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read(), resp.geturl()


CANDS = [
    ("0418352387", "woonzorgcentrum-lindelo", "lindelo"),
    ("0443072838", "woonzorgcentra-ocura", "ocura"),
    ("0696665975", "woonzorggroep-arendonk", "arendonk"),
    ("0632895801", "solidum-woonzorgsamenwerking", "solidum"),
    ("0428692191", "de-medemens", "medemens"),
    ("0410853396", "de-lovie", "de lovie"),
    ("0441313178", "woon-en-zorgcentrum-avondvrede", "avondvrede"),
    ("0410509443", "woonzorgcentrum-kanunnik-triest-vzw", "kanunnik"),  # likely mined
    ("0473762450", "zusterhof-woon-en-zorgcentrum", "zusterhof"),  # mined
]

for kbo, slug, term in CANDS:
    print(("SKIP" if mined(term) or mined(kbo) else "FREE"), term, kbo)
    if mined(term) or mined(kbo):
        continue
    for url in [
        f"https://www.companyweb.be/nl/{kbo}/{slug}",
        f"https://www.companyweb.be/nl/{kbo}",
    ]:
        try:
            data, final = fetch(url)
            t = data.decode("utf-8", "replace")
            title = re.search(r"<title>([^<]+)</title>", t)
            ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
            filed = re.search(r"neergelegd op ([0-9\-]+)", t)
            omzet = re.search(r"omzet:\s*\"([^\"]+)\"", t)
            winst = re.search(r"winst:\s*\"([^\"]+)\"", t)
            print(
                " ",
                final.split("/")[-1][:50],
                "YE",
                ye.group(1) if ye else "?",
                "filed",
                filed.group(1) if filed else "?",
                "omzet",
                omzet.group(1) if omzet else "?",
                "winst",
                winst.group(1) if winst else "?",
                (title.group(1)[:70] if title else "?"),
            )
            if ye and ye.group(1) == "2025":
                (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
                print("  SAVED")
            break
        except Exception as e:
            print("  FAIL", type(e).__name__, url[-40:])
