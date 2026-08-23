# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2083")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Build mined name+kbo blob
blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(str(r).lower() for r in csv.DictReader(f))
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(
        ((r.get("entity_id") or "") + " " + (r.get("title") or "") + " " + (r.get("notes") or "")).lower()
        for r in csv.DictReader(f)
    )


def mined_term(term: str) -> bool:
    return term.lower() in blob


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl"})
    with urllib.request.urlopen(req, timeout=35) as resp:
        return resp.read(), resp.geturl()


CANDS = [
    ("0466266429", "helianthus", "helianthus"),
    ("0696715", "crayenhof", "crayenhof"),  # incomplete
    ("0696715807", "woonzorgcentrum-crayenhof", "crayenhof"),
    ("0696715024", "crayenhof", "crayenhof"),
    ("0685516024", "woonzorgcentrum-immaculata", "immaculata"),  # from earlier search 0685.516.024
    ("0685516024", "immaculata", "immaculata"),
    ("0478123456", "x", "x"),
    ("0422620585", "woon-en-zorgcentrum-sint-vincentius", "vincentius erpe"),  # YE2024 likely
    ("0405555555", "x", "x"),
    # try Prinsenhof already mined?
    ("0416493254", "ben-woonzorgnetwerk", "ben woonzorg"),  # YE2024
    ("0432505281", "rustoord-t-hoge", "t hoge"),
    ("0460123456", "x", "x"),
    ("0456789012", "x", "x"),
    ("0444555666", "x", "x"),
    ("0433444555", "x", "x"),
    ("0422333444", "x", "x"),
    ("0411222333", "x", "x"),
    ("0400111222", "x", "x"),
    ("0477000111", "woonzorgcentrum-het-park", "het park"),
    ("0466000222", "home-elisabeth", "home elisabeth"),
    ("0455000333", "sint-jan-berchmans", "berchmans"),
    ("0444000444", "de-voorzienigheid", "voorzienigheid"),
    ("0433000555", "de-olijfboom", "olijfboom"),
]

# dedupe by kbo
seen = set()
for kbo, slug, term in CANDS:
    if kbo in seen or kbo.startswith("04") and len(kbo) != 10 and kbo != "0696715":
        if len(kbo) != 10:
            continue
    if len(kbo) != 10:
        continue
    seen.add(kbo)
    if mined_term(term) or mined_term(kbo) or mined_term(".".join([kbo[:4], kbo[4:7], kbo[7:]])):
        print("SKIP mined", term, kbo)
        continue
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        data, final = fetch(url)
        text = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)</title>", text)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", text)
        filed = re.search(r"neergelegd op ([0-9\-]+)", text)
        omzet = re.search(r"omzet:\s*\"([^\"]+)\"", text)
        print(
            "HITPAGE",
            kbo,
            "YE",
            ye.group(1) if ye else "?",
            "filed",
            filed.group(1) if filed else "?",
            "omzet0",
            omzet.group(1) if omzet else "?",
            "title",
            (title.group(1)[:90] if title else "?"),
            "final",
            final.split("/")[-1][:40],
        )
        if ye and ye.group(1) == "2025":
            (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
            print("  SAVED YE2025", kbo)
    except Exception as e:
        print("FAIL", kbo, slug, type(e).__name__, e)

# Also try pappers pages for Crayenhof / Immaculata KBO resolve
for url in [
    "https://www.pappers.be/nl/company/immaculata-0685516024",
    "https://www.companyweb.be/nl/0685516024",
    "https://www.companyweb.be/nl/0432505281/rustoord-t-hoge",
]:
    try:
        data, final = fetch(url)
        text = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)</title>", text)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", text)
        print("ALT", final[:100], "YE", ye.group(1) if ye else "?", "title", (title.group(1)[:80] if title else "?"))
        if ye and ye.group(1) == "2025":
            (RAW / ("alt_" + re.sub(r"\W+", "_", final.split("/")[-1])[:30] + ".html")).write_bytes(data)
    except Exception as e:
        print("ALTFAIL", url[:60], e)
