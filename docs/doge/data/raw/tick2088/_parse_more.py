# -*- coding: utf-8 -*-
import re
from pathlib import Path

te = Path("docs/doge/data/raw/tick2088/ocura_en.html").read_text(encoding="utf-8", errors="replace")
idx = te.find("Employees")
chunk = te[idx : idx + 1200]
print(re.sub(r"\s+", " ", chunk)[:900])
ftes = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", chunk)
print("FTE", ftes)

tk = Path("docs/doge/data/raw/tick2088/kbo_ocura.html").read_text(encoding="utf-8", errors="replace")
for pat in ["aanbestedende", "Aanbestedende", "Type entiteit", "Benaming", "Maatschappelijke"]:
    m = re.search(pat + r"[\s\S]{0,200}", tk, re.I)
    if m:
        print(pat, re.sub(r"<[^>]+>", " | ", m.group(0))[:200])

# quick site contact for general email
import urllib.request

UA = "Mozilla/5.0"
for url in ["https://www.ocura.be/", "https://www.ocura.be/beringen/contact"]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "replace")
        Path("docs/doge/data/raw/tick2088/site_" + url.split("//")[1].replace("/", "_")[:40] + ".html").write_text(
            html, encoding="utf-8"
        )
        emails = sorted(set(re.findall(r"[\w.+-]+@ocura\.be", html, re.I)))
        print(url, emails[:10])
    except Exception as e:
        print("FAIL", url, type(e).__name__, e)
