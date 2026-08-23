# -*- coding: utf-8 -*-
"""Claim rq_2088 and fetch Ocura (preferred deferred) after stall check."""
import csv
import json
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2088")
RAW.mkdir(parents=True, exist_ok=True)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
UTC = "2026-08-25T03:05:00Z"

path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
claimed = False
for row in rows:
    if row["task_id"] == "rq_2088":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = UTC
        row["notes"] = "CLAIM tick2088 probing AGB/FARO/AIESH/REW then Ocura/De Lovie"
        claimed = True
if not claimed:
    raise SystemExit("rq_2088 missing")
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2088")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()


# stall
for name, url in [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/aiesh"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
]:
    data = fetch(url)
    (RAW / name).write_bytes(data)
    t = data.decode("utf-8", "replace")
    ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
    print(name, "YE", ye.group(1) if ye else "?")

KBO = "0443072838"
pages = [
    ("ocura_nl.html", f"https://www.companyweb.be/nl/{KBO}/ocura"),
    ("ocura_en.html", f"https://www.companyweb.be/en/{KBO}/ocura"),
    ("ocura_fr.html", f"https://www.companyweb.be/fr/{KBO}/ocura"),
    (
        "kbo_ocura.html",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    ),
]
for name, url in pages:
    data = fetch(url)
    (RAW / name).write_bytes(data)
    print("OK", name, len(data))

t = (RAW / "ocura_nl.html").read_text(encoding="utf-8", errors="replace")
te = (RAW / "ocura_en.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r"kernCijfers\s*=\s*(\{.*?\});", t, re.S)
blocks = re.findall(r"(20\d\d)\s*:\s*\{([^}]*)\}", m.group(1))
data = {}
for year, body in blocks:
    row = {}
    for key in ["winst", "eigen_vermogen", "bruto_marge", "omzet"]:
        km = re.search(rf'{key}:\s*"([^"]*)"', body)
        if km:
            row[key] = km.group(1)
    data[year] = row
print(json.dumps({k: data[k] for k in list(data)[:3]}, indent=2, ensure_ascii=False))
filed = re.search(r"neergelegd op ([0-9.\-]+)", t)
print("filed", filed.group(1) if filed else "?")
emp = re.search(r'Employees\s*=\s*"([^"]+)"', t)
print("Employees global", emp.group(1) if emp else "?")
idx = te.find("Employees")
chunk = te[idx : idx + 800]
ftes = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", chunk)
print("FTE series", ftes[:6])
title = re.search(r"<title>([^<]+)</title>", t)
print("title", title.group(1) if title else "?")

tk = (RAW / "kbo_ocura.html").read_text(encoding="utf-8", errors="replace")
for label in ["Status", "Rechtsvorm", "Aantal vestigingseenheden", "Adres van de zetel"]:
    mm = re.search(label + r"[\s\S]{0,220}", tk, re.I)
    if mm:
        print(label, re.sub(r"<[^>]+>", " ", mm.group(0))[:180])
for m2 in re.finditer(r"(87\.\d{3})[\s\S]{0,60}", tk):
    print("NACE", re.sub(r"<[^>]+>", " ", m2.group(0))[:100])
