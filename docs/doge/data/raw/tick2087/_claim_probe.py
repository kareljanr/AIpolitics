# -*- coding: utf-8 -*-
"""Claim rq_2087 and probe FARO/AIESH/REW + Lindelo/Ocura/De Lovie."""
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2087")
RAW.mkdir(parents=True, exist_ok=True)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
UTC = "2026-08-25T02:50:00Z"

path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
claimed = False
for row in rows:
    if row["task_id"] == "rq_2087":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = UTC
        row["notes"] = "CLAIM tick2087 probing AGB/FARO/AIESH/REW then Lindelo/Ocura/De Lovie"
        claimed = True
if not claimed:
    raise SystemExit("rq_2087 missing")
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2087")


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read(), resp.geturl()


def summarize(name: str, data: bytes):
    t = data.decode("utf-8", "replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
    filed = re.search(r"neergelegd op ([0-9.\-]+)", t)
    omzet = re.search(r'omzet:\s*"([^"]*)"', t)
    pnl = re.search(r'(?:winst|verlies|nettoResultaat|resultaat):\s*"([^"]*)"', t)
    # better extract from kernCijfers block
    block = re.search(r"kernCijfers\s*=\s*\{(.*?)\};", t, re.S)
    print(
        name,
        "YE",
        ye.group(1) if ye else "?",
        "filed",
        filed.group(1) if filed else "?",
        "omzet",
        omzet.group(1) if omzet else "?",
        (title.group(1)[:70] if title else "?"),
    )
    if block:
        first = re.search(
            r"(20\d\d)\s*:\s*\{([^}]{0,400})\}",
            block.group(1),
        )
        if first:
            print("  firstYE", first.group(1), re.sub(r"\s+", " ", first.group(2))[:220])


# stall checks
for name, url in [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/aiesh"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
]:
    try:
        data, _ = fetch(url)
        (RAW / name).write_bytes(data)
        summarize(name, data)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)

# preferred deferred
CANDS = [
    ("0418352387", "lindelo", "lindelo"),
    ("0443072838", "ocura", "ocura"),
    ("0410853396", "de-lovie", "lovie"),
    # backup unused WZC-ish if deferred fail
    ("0475837260", "woon-en-zorgcentrum-ten-anker", "ten anker"),  # likely mined
    ("0431632776", "de-zwaluw", "zwaluw"),
    ("0428692191", "de-medemens", "medemens"),
    ("0466266429", "helianthus", "helianthus"),
    ("0422620585", "woon-en-zorgcentrum-sint-vincentius", "vincentius"),
    ("0432505281", "rustoord-t-hoge", "t hoge"),
    ("0696715024", "crayenhof", "crayenhof"),
    ("0414678562", "wzc-h-vander-stokken", "vander stokken"),
    ("0459770496", "wzc-sint-augustinus", "augustinus halle"),
]

blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob += " ".join(str(v).lower() for v in r.values()) + " "
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if (r.get("status") or "").lower() == "done":
            blob += ((r.get("entity_id") or "") + " " + (r.get("title") or "")).lower() + " "


def mined(term: str, kbo: str) -> bool:
    kbo_dot = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    return term.lower() in blob or kbo in blob or kbo_dot in blob


for kbo, slug, term in CANDS:
    if mined(term, kbo) and term not in ("lindelo", "ocura", "lovie"):
        print("SKIP mined", term, kbo)
        continue
    if mined(term, kbo) and term in ("lindelo", "ocura", "lovie"):
        # still probe preferred deferred even if name appears in notes
        print("PROBE despite note-hit", term, kbo)
    urls = [
        f"https://www.companyweb.be/nl/{kbo}/{slug}",
        f"https://www.companyweb.be/nl/{kbo}",
    ]
    ok = False
    for url in urls:
        try:
            data, final = fetch(url)
            t = data.decode("utf-8", "replace")
            if "Page Not Found" in t or "pagina niet gevonden" in t.lower():
                print("404", url)
                continue
            ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
            (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
            summarize(f"cand_{kbo}", data)
            if ye and ye.group(1) == "2025":
                print("  *** YE2025 CANDIDATE ***", final)
            ok = True
            break
        except Exception as e:
            print("FAIL", url, type(e).__name__, e)
    if not ok:
        print("NOHIT", term, kbo)
