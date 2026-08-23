# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2083")
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# claim
path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2083":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = "2026-08-25T01:50:00Z"
        row["notes"] = "CLAIM tick2083 probing AGB/FARO/AIESH/REW then unused WZC/IGS"
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2083")

# mined KBOs
mined = set()
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join((r.get(k) or "") for k in r)
        for m in re.findall(r"0\d{3}\.\d{3}\.\d{3}", blob):
            mined.add(m.replace(".", ""))
        for m in re.findall(r"\b0\d{9}\b", blob):
            mined.add(m)
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join((r.get(k) or "") for k in r)
        for m in re.findall(r"0\d{3}\.\d{3}\.\d{3}", blob):
            mined.add(m.replace(".", ""))


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        data = resp.read()
        final = resp.geturl()
    (RAW / name).write_bytes(data)
    print("OK", name, len(data), final[:100])
    return data.decode("utf-8", "replace")


# stall checks
for name, url in [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/aiesh"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
    ("bornem_jr.html", "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"),
]:
    try:
        t = fetch(name, url)
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        years = re.findall(r"Jaarrekening\s+(20\d\d)", t)
        print(" ", name, "YE", ye.group(1) if ye else years[:3])
    except Exception as e:
        print("FAIL", name, e)

# candidate WZCs / IGS with likely YE2025 — probe CW
CANDS = [
    ("0456789012", "skip"),  # placeholder
    # known-ish from prior searches / common unused
    ("0416501234", "skip"),
    ("0426123456", "skip"),
]

# Direct CW URLs to try (unused names from earlier FREE list / new finds)
URLS = [
    ("cand_meander.html", "https://www.companyweb.be/nl/search?q=WZC+De+Meander"),  # may 404
    ("cand_klippel.html", "https://www.companyweb.be/nl/0412345678/x"),
]

# Better: try specific KBOs via companyweb numeric redirects
NUMERIC = [
    # De Vaeren Rumst (mentioned alongside Wijshage) — check mined
    "0400123456",
]

# Search via known free names mapped to possible companyweb slugs
PROBE = [
    "https://www.companyweb.be/nl/0478123456/x",
]

# Use web-known unused: try WZC De Vaeren, Home Spermalie already HIT
# Try: WZC Sint-Anna, WZC De Bron, WZC Oliviers, WZC Dunebos, WZC Zeezicht
SLUGS = [
    ("0429901122", "woonzorgcentrum-de-vaeren"),
    ("0449123456", "woonzorgcentrum-de-vaeren"),
    ("0412345678", "woonzorgcentrum-zeezicht"),
    ("0477001122", "woonzorgcentrum-dunebos"),
    ("0465123456", "woonzorgcentrum-de-golf"),
    ("0450123789", "woonzorgcentrum-bellevue"),
    ("0433987654", "woonzorgcentrum-de-meander"),
    ("0425876543", "woonzorgcentrum-de-klippel"),
    ("0418765432", "woonzorgcentrum-immaculata"),
    ("0409654321", "woonzorgcentrum-zonneweelde"),
    ("0476543210", "woonzorgcentrum-lindenhof"),
    ("0465432109", "huize-godelieve"),
    ("0454321098", "woonzorgcentrum-sint-anna"),
    ("0443210987", "woonzorgcentrum-de-bron"),
    ("0432109876", "woonzorgcentrum-ter-rijst"),
    ("0421098765", "woonzorgcentrum-parkresidentie"),
]

# First resolve De Vaeren Rumst via known pattern - check entities
for term in ["de vaeren", "vaeren", "dunebos", "zeezicht", "de meander", "klippel", "lindenhof", "godelieve", "ter rijst", "parkresidentie", "de bron tongeren", "olivier wzc", "blankenberge wzc", "zonnebloem"]:
    hit = any(term in x for x in mined)  # mined is KBOs only
print("mined count", len(mined))

# Check entity names for free candidates
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    entblob = " ".join(str(r).lower() for r in csv.DictReader(f))
for term in [
    "de vaeren",
    "vaeren",
    "dunebos",
    "zeezicht",
    "de meander",
    "klippel",
    "lindenhof",
    "godelieve",
    "ter rijst",
    "parkresidentie",
    "zonnebloem",
    "de golf",
    "bellevue",
    "olivier",
    "rochus",
    "eikenbos",
    "waterdam",
    "zinnebinnen",
    "crayenhof",
]:
    print(("HIT" if term in entblob else "FREE"), term)
