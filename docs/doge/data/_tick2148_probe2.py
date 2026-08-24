# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2148")
ua = {"User-Agent": "Mozilla/5.0"}
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()

for n in [
    "0500.916.710",
    "0500916710",
    "hemeco",
    "0500.927.004",
    "0500927004",
    "val de sambre",
    "val_de_sambre",
    "0500.916.908",
    "vesdre",
    "huis vincent",
    "huize vincent",
]:
    print("mined", n, n in ents)

for name, url in {
    "hemeco_en.html": "https://www.companyweb.be/en/0500916710",
    "hemeco_nl.html": "https://www.companyweb.be/nl/0500916710",
    "hemeco_fr.html": "https://www.companyweb.be/fr/0500916710",
    "hemeco_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0500916710"
    ),
    "vds_en.html": "https://www.companyweb.be/en/0500927004",
    "vds_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0500927004"
    ),
}.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        (base / name).write_bytes(data)
        t = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)", t)
        years = re.findall(r"\n(202[0-9])\s*:", t)
        print(name, "OK", len(data), "years", years[:5], (title.group(1)[:90] if title else None))
        for y in ["2025", "2024"]:
            mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
            if mm:
                print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:280])
        m = re.search(r'Employees\s*=\s*"([^"]+)"', t)
        if m:
            print("  fte", m.group(1))
    except Exception as e:
        print("FAIL", name, e)

with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2148":
        print("2148", x.get("status"))
