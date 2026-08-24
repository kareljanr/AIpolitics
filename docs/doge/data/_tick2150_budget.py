# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2150")
ua = {"User-Agent": "Mozilla/5.0"}
url = "https://www.zonevaldesambre.be/2026-02-04-avis-de-publication-budget-2026/"
req = urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, timeout=40) as r:
    data = r.read()
(base / "vds_budget2026_avis.html").write_bytes(data)
t = data.decode("utf-8", "replace")
plain = re.sub(r"<[^>]+>", " ", t)
plain = re.sub(r"\s+", " ", plain)
print("len", len(data))
print(plain[:3000])
print("---LINKS---")
for m in re.finditer(r'href="([^"]+)"', t):
    h = m.group(1)
    if any(
        x in h.lower()
        for x in ["budget", "compte", "pdf", "download", "wp-content", "upload"]
    ):
        print("link", h[:220])
print("---EUR---")
for m in re.finditer(r"[\d][\d\s.,]{2,18}\s*(?:EUR|€|euros?)", plain, re.I):
    print("eur", m.group(0)[:100])
