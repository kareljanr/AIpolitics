# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2141":
        print("2141", x.get("status"))

t = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()
print("mined 0409698009", "0409698009" in t or "0409.698.009" in t)

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2141")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0"}
for name, url in {
    "dg_en.html": "https://www.companyweb.be/en/0409698009",
    "dg_nl.html": "https://www.companyweb.be/nl/0409698009",
    "dg_fr.html": "https://www.companyweb.be/fr/0409698009",
    "dg_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0409698009"
    ),
}.items():
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read()
    (base / name).write_bytes(data)
    print("OK", name, len(data))

en = (base / "dg_en.html").read_text(encoding="utf-8", errors="replace")
print("title", re.search(r"<title>([^<]+)", en).group(1)[:100])
for y in ["2025", "2024"]:
    mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
    print(y, re.sub(r"\s+", " ", mm.group(1))[:300] if mm else None)
m = re.search(r'Employees\s*=\s*"([^"]+)"', en)
print("fte", m.group(1) if m else None)
m = re.search(r"filed on ([0-9\-]+)", en)
print("filed", m.group(1) if m else None)

kbo = (base / "dg_kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<[^>]+>", "\n", kbo)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
for i, ln in enumerate(lines):
    if any(
        k in ln.lower()
        for k in [
            "status",
            "stopgezet",
            "actief",
            "adres",
            "nace",
            "87.",
            "vestiging",
            "naam",
            "opgeslorpt",
            "denderrust",
            "email",
            "web",
        ]
    ):
        print("KBO", " | ".join(lines[i : i + 3])[:230])

om25, om24 = 627905, 617808
br25, br24 = 317497, 324000
pn25, pn24 = 82762, 81539
eq25, eq24 = 1098146, 1015384
for label, a, b in [
    ("omzet", om25, om24),
    ("bruto", br25, br24),
    ("pnl", pn25, pn24),
    ("equity", eq25, eq24),
]:
    print(f"{label} {(a-b)/abs(b)*100:+.2f}%")
