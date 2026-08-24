# -*- coding: utf-8 -*-
import urllib.request
from pathlib import Path
import re

base = Path("docs/doge/data/raw/tick2138")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-doge/1.0)"}
urls = {
    "prestige_cw_nl.html": "https://www.companyweb.be/nl/0416528391/residence-prestige",
    "prestige_cw_fr.html": "https://www.companyweb.be/fr/0416528391/residence-prestige",
    "prestige_cw_en.html": "https://www.companyweb.be/en/0416528391/residence-prestige",
    "prestige_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0416528391"
    ),
    "faro_cw_en.html": (
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"
    ),
    "aiesh_cw_en.html": (
        "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut"
    ),
}
for name, url in urls.items():
    path = base / name
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=45) as r:
            data = r.read()
        path.write_bytes(data)
        print(f"OK {name} {len(data)}")
    except Exception as e:
        print(f"FAIL {name}: {e}")

# parse prestige EN
html = (base / "prestige_cw_en.html").read_text(encoding="utf-8", errors="replace")
for year in ("2025", "2024", "2023"):
    m = re.search(rf"{year}\s*:{{([^}}]+)}}", html)
    print(f"=== {year} ===")
    print(m.group(1).strip() if m else "MISSING")
bal = re.search(r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(\d{4})", html)
fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
filed = re.search(r"filed on ([0-9-]{10})", html)
print("balance", bal.group(1) if bal else "?", "fte", fte.group(1) if fte else "?", "filed", filed.group(1) if filed else "?")

# KBO facts
kbo = (base / "prestige_kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<[^>]+>", " ", kbo)
text = re.sub(r"\s+", " ", text)
for needle in [
    "Status",
    "Adres van de zetel",
    "E-mail",
    "Webadres",
    "Rechtsvorm",
    "Aantal vestiging",
    "87.",
    "Chaudfontaine",
]:
    i = text.find(needle)
    if i >= 0:
        print(text[i : i + 160])

# stall check
for name in ("faro_cw_en.html", "aiesh_cw_en.html"):
    h = (base / name).read_text(encoding="utf-8", errors="replace")
    b = re.search(r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(\d{4})", h)
    print(name, "balance", b.group(1) if b else "?")
