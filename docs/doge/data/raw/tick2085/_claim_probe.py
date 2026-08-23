# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2085")
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2085":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = "2026-08-25T02:20:00Z"
        row["notes"] = "CLAIM tick2085 probing AGB/FARO/AIESH/REW then unused WZC/IGS"
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2085")

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


# stall
for name, url in [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/aiesh"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
    ("bornem_jr.html", "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"),
]:
    try:
        data, final = fetch(url)
        (RAW / name).write_bytes(data)
        t = data.decode("utf-8", "replace")
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        years = re.findall(r"Jaarrekening\s+(20\d\d)", t)
        print(name, "YE", ye.group(1) if ye else years[:3])
    except Exception as e:
        print("FAIL", name, e)

# candidates: numeric KBO + slug
CANDS = [
    ("0478054321", "woonzorgcentrum-de-zonnebloem", "zonnebloem"),
    ("0466987654", "woonzorgcentrum-parkresidentie", "parkresidentie"),
    ("0455876543", "woonzorgcentrum-bellevue", "bellevue"),
    ("0444765432", "woonzorgcentrum-de-golf", "de golf"),
    ("0433654321", "woonzorgcentrum-zeezicht", "zeezicht"),
    ("0422543210", "woonzorgcentrum-dunebos", "dunebos"),
    ("0411432109", "woonzorgcentrum-lindenhof", "lindenhof"),
    ("0400321098", "huize-godelieve", "godelieve"),
    ("0477210987", "woonzorgcentrum-de-meander", "de meander"),
    ("0466109876", "woonzorgcentrum-de-klippel", "klippel"),
    ("0455098765", "woonzorgcentrum-eikenbos", "eikenbos"),
    ("0444987654", "woonzorgcentrum-waterdam", "waterdam"),
    ("0433876543", "woonzorgcentrum-ter-rijst", "ter rijst"),
    ("0422765432", "woonzorgcentrum-sint-rochus", "rochus"),
    ("0411654321", "woonzorgcentrum-olivier", "olivier"),
    # known from prior research trails
    ("0696715024", "crayenhof", "crayenhof"),
    ("0466266429", "helianthus", "helianthus"),  # YE2016 before
    ("0422620585", "woon-en-zorgcentrum-sint-vincentius", "vincentius erpe"),
    ("0432505281", "rustoord-t-hoge", "t hoge"),
    # try Gloria/Orelia-adjacent unused
    ("0475000111", "x", "skip"),
]

for kbo, slug, term in CANDS:
    if mined(term) or mined(kbo) or mined(".".join([kbo[:4], kbo[4:7], kbo[7:]])):
        print("SKIP", term, kbo)
        continue
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        data, final = fetch(url)
        t = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)</title>", t)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        filed = re.search(r"neergelegd op ([0-9\-]+)", t)
        omzet = re.search(r"omzet:\s*\"([^\"]+)\"", t)
        print(
            "PAGE",
            kbo,
            "YE",
            ye.group(1) if ye else "?",
            "filed",
            filed.group(1) if filed else "?",
            "omzet",
            omzet.group(1) if omzet else "?",
            (title.group(1)[:80] if title else "?"),
        )
        if ye and ye.group(1) == "2025":
            (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
            print("  SAVED YE2025")
    except Exception as e:
        print("FAIL", kbo, type(e).__name__)
