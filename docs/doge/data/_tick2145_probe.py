# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()
for n in [
    "0500.916.512",
    "0500916512",
    "hesbaye",
    "0500.916.215",
    "0500916215",
    "hainaut-centre",
    "zhc",
]:
    print("mined", n, n in ents)

with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2145":
        print("2145", x.get("status"))

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2145")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0"}
for name, url in {
    "hesbaye_en.html": "https://www.companyweb.be/en/0500916512",
    "hesbaye_nl.html": "https://www.companyweb.be/nl/0500916512",
    "hesbaye_fr.html": "https://www.companyweb.be/fr/0500916512",
    "hesbaye_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0500916512"
    ),
    "zhc_en.html": "https://www.companyweb.be/en/0500916215",
    "bornem.html": "https://www.companyweb.be/en/0877556624",
    "faro.html": "https://www.companyweb.be/en/0893863017",
    "aiesh.html": "https://www.companyweb.be/en/0201712587",
}.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        (base / name).write_bytes(data)
        t = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)", t)
        years = re.findall(r"\n(202[0-9])\s*:", t)
        print(
            name,
            "OK",
            len(data),
            "years",
            years[:5],
            (title.group(1)[:80] if title else None),
        )
        for y in ["2025", "2024"]:
            mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
            if mm:
                print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:280])
        m = re.search(r'Employees\s*=\s*"([^"]+)"', t)
        if m:
            print("  fte", m.group(1))
    except Exception as e:
        print("FAIL", name, e)
