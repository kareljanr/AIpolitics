# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2143")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0"}
KBO_DIGITS = "0500927301"
urls = {
    "dinaphi_en.html": f"https://www.companyweb.be/en/{KBO_DIGITS}",
    "dinaphi_nl.html": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
    "dinaphi_fr.html": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
    "dinaphi_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
    ),
}
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()
print("mined", "0500.927.301" in ents or "0500927301" in ents or "dinaphi" in ents)

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        (base / name).write_bytes(data)
        print("OK", name, len(data))
    except Exception as e:
        print("FAIL", name, e)

en = (base / "dinaphi_en.html").read_text(encoding="utf-8", errors="replace")
print("title", re.search(r"<title>([^<]+)", en).group(1)[:110] if re.search(r"<title>", en) else None)
years = re.findall(r"\n(202[0-9])\s*:", en)
print("years", years[:8])
for y in ["2025", "2024", "2023"]:
    mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
    if mm:
        print(y, re.sub(r"\s+", " ", mm.group(1))[:320])
m = re.search(r'Employees\s*=\s*"([^"]+)"', en)
print("fte", m.group(1) if m else None)
m = re.search(r"filed on ([0-9\-]+)", en)
print("filed", m.group(1) if m else None)

# rq still open?
with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2143":
        print("2143", x.get("status"))
