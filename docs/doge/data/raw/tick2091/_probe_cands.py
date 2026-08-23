# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2091")
RAW.mkdir(parents=True, exist_ok=True)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob += " ".join(str(v).lower() for v in r.values()) + " "
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if (r.get("status") or "").lower() == "done":
            blob += ((r.get("entity_id") or "") + " " + (r.get("title") or "")).lower() + " "


def mined(*terms: str) -> bool:
    return any(t.lower() in blob for t in terms)


CANDS = [
    ("0893863017", "faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("0201712587", "association-intercommunale-d-electricite-du-sud-du-hainaut"),
    ("0644638937", "reseau-d-energies-de-wavre"),
    ("0410151137", "sint-lucia"),
    ("0413653827", "sint-elisabeth-s-dal"),
    ("0466266429", "helianthus"),
    ("0696715807", "woonzorgcentrum-crayenhof"),
    ("0480566704", "hof-ter-lande-woon-en-zorgcentrum"),
    ("0443249616", "rusthuis-stil-geluk"),
    ("0685516024", "immaculata"),
    ("0415223344", "woonzorgcentrum-de-vijvers"),
    ("0428901122", "woon-zorgcentrum-het-anker"),
    ("0407601720", "lidwina"),
    ("0471475527", "zilvervogel"),
]


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read(), resp.geturl()


for kbo, slug in CANDS:
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    already = mined(kbo, dotted, slug.replace("-", " "))
    if already and kbo not in ("0893863017", "0201712587", "0644638937"):
        print("MINED", kbo, slug)
        continue
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        data, final = fetch(url)
        t = data.decode("utf-8", "replace")
        if "Page Not Found" in t or "pagina niet gevonden" in t.lower():
            print("404", kbo, slug)
            continue
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        title = re.search(r"<title>([^<]+)</title>", t)
        filed = re.search(r"neergelegd op ([0-9.\-]+)", t)
        first = re.search(
            r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
            t,
        )
        fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
        print(
            "HIT",
            kbo,
            "YE",
            ye.group(1) if ye else "?",
            "filed",
            filed.group(1) if filed else "?",
            "fte",
            fte.group(1) if fte else "?",
            "mined" if already else "fresh",
        )
        if first:
            print(
                " ",
                first.group(1),
                "winst",
                first.group(2),
                "eq",
                first.group(3),
                "bruto",
                first.group(4),
                "omzet",
                first.group(5),
            )
        print("  title", (title.group(1)[:100] if title else "?"))
        (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
        if ye and ye.group(1) == "2025":
            print("  *** YE2025 ***")
    except Exception as e:
        print("FAIL", kbo, type(e).__name__, str(e)[:150])
