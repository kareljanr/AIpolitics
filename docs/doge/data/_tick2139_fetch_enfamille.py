# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
needles = [
    "0466.114.791",
    "0466114791",
    "en famille",
    "maison de repos en famille",
    "vaux-sur-sure",
    "vaux-sur-sûre",
]
for fn in ["entities.csv", "leaderboard.csv", "sources.csv", "commitments.csv"]:
    t = (Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data") / fn).read_text(
        encoding="utf-8", errors="replace"
    ).lower()
    hits = [n for n in needles if n.lower() in t]
    print(fn, hits or "none")

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2139")
ua = {"User-Agent": "Mozilla/5.0"}
urls = {
    "enfamille_en.html": "https://www.companyweb.be/en/0466114791/maison-de-repos-en-famille",
    "enfamille_nl.html": "https://www.companyweb.be/nl/0466114791/maison-de-repos-en-famille",
    "enfamille_fr.html": "https://www.companyweb.be/fr/0466114791/maison-de-repos-en-famille",
    "enfamille_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0466114791"
    ),
}
for name, url in urls.items():
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read()
    (base / name).write_bytes(data)
    print("OK", name, len(data))

en = (base / "enfamille_en.html").read_text(encoding="utf-8", errors="replace")
print("title", re.search(r"<title>([^<]+)", en).group(1)[:100])
for y in ["2025", "2024"]:
    mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
    print(y, re.sub(r"\s+", " ", mm.group(1))[:300] if mm else None)
m = re.search(r'Employees\s*=\s*"([^"]+)"', en)
print("fte", m.group(1) if m else None)
m = re.search(r"filed on ([0-9\-]+)", en)
print("filed", m.group(1) if m else None)

kbo = (base / "enfamille_kbo.html").read_text(encoding="utf-8", errors="replace")
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
            "87.",
            "email",
            "web",
            "vestiging",
            "rechtsvorm",
            "naam",
            "famille",
            "salvacourt",
        ]
    ):
        print("KBO", " | ".join(lines[i : i + 3])[:220])

br25, br24 = 1033029, 988068
pn25, pn24 = -19390, 9411
eq25, eq24 = 197533, 216923
print(f"bruto {(br25-br24)/abs(br24)*100:+.2f}%")
print(f"equity {(eq25-eq24)/abs(eq24)*100:+.2f}%")
print(f"pnl flip from {pn24} to {pn25}")
