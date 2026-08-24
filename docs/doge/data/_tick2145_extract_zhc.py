# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2145")
ua = {"User-Agent": "Mozilla/5.0"}
# ensure ZHC NL/FR/KBO
for name, url in {
    "zhc_nl.html": "https://www.companyweb.be/nl/0500916215",
    "zhc_fr.html": "https://www.companyweb.be/fr/0500916215",
    "zhc_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0500916215"
    ),
}.items():
    if not (base / name).exists():
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40) as r:
            (base / name).write_bytes(r.read())
        print("OK", name)

kbo = (base / "zhc_kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<[^>]+>", "\n", kbo)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
for i, ln in enumerate(lines):
    if any(
        k in ln.lower()
        for k in [
            "status",
            "actief",
            "adres",
            "nace",
            "mons",
            "vestiging",
            "naam",
            "rechtsvorm",
            "email",
            "web",
            "hainaut",
            "84.250",
            "aanbested",
        ]
    ):
        print("KBO", " | ".join(lines[i : i + 3])[:230])

en = (base / "zhc_en.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r'Employees\s*=\s*"([^"]+)"', en)
print("fte", m.group(1) if m else None)
m = re.search(r'window\.cw\.startDate\s*=\s*"([^"]+)"', en)
print("start", m.group(1) if m else None)

with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2145":
        print("2145", x.get("status"))
