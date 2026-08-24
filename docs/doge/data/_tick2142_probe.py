# -*- coding: utf-8 -*-
import csv
import re
import shutil
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
src = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2141")
dst = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2142")
dst.mkdir(parents=True, exist_ok=True)

# copy or fetch
ua = {"User-Agent": "Mozilla/5.0"}
urls = {
    "franciscus_cw_en.html": "https://www.companyweb.be/en/0412763704/groep-van-voorzieningen-sint-franciscus",
    "franciscus_cw_nl.html": "https://www.companyweb.be/nl/0412763704/groep-van-voorzieningen-sint-franciscus",
    "franciscus_cw_fr.html": "https://www.companyweb.be/fr/0412763704/groep-van-voorzieningen-sint-franciscus",
    "franciscus_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0412763704"
    ),
    "bornem_en.html": "https://www.companyweb.be/en/0877556624",
    "faro_en.html": "https://www.companyweb.be/en/0893863017",
    "aiesh_en.html": "https://www.companyweb.be/en/0201712587",
}
for name, url in urls.items():
    dest = dst / name
    alt = src / name
    if alt.exists() and name.startswith("franciscus"):
        shutil.copy2(alt, dest)
        print("copy", name)
    else:
        try:
            req = urllib.request.Request(url, headers=ua)
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
            dest.write_bytes(data)
            print("OK", name, len(data))
        except Exception as e:
            print("FAIL", name, e)

en = (dst / "franciscus_cw_en.html").read_text(encoding="utf-8", errors="replace")
print("title", re.search(r"<title>([^<]+)", en).group(1)[:110])
for y in ["2025", "2024"]:
    mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
    print(y, re.sub(r"\s+", " ", mm.group(1))[:320] if mm else None)
m = re.search(r'Employees\s*=\s*"([^"]+)"', en)
print("fte", m.group(1) if m else None)
m = re.search(r"filed on ([0-9\-]+)", en)
print("filed", m.group(1) if m else None)

# mined?
with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
hits = [
    r
    for r in rows
    if "0412.763.704" in str(r)
    or "0412763704" in str(r)
    or "groep_sint_franciscus" in str(r).lower()
    or ("sint-franciscus" in str(r).lower() and "brakel" in str(r).lower())
]
print("entity hits", len(hits))
for h in hits[:3]:
    print(" ", h.get("entity_id"), (h.get("notes") or "")[:140])

# preferred years
for name in ["bornem_en.html", "faro_en.html", "aiesh_en.html"]:
    t = (dst / name).read_text(encoding="utf-8", errors="replace")
    years = re.findall(r"\n(202[0-9])\s*:", t)
    print(name, "years", years[:5])

# calcs
om25, om24 = 30982834, 29637600  # will verify from HTML
# from FOI: YE2024 loss -245197; need exact YE2024 omzet from HTML
mm = re.search(r"2024\s*:\s*\{([^}]+)\}", en)
print("2024 raw", re.sub(r"\s+", " ", mm.group(1)) if mm else None)
mm = re.search(r"2025\s*:\s*\{([^}]+)\}", en)
print("2025 raw", re.sub(r"\s+", " ", mm.group(1)) if mm else None)

# rq still open?
with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2142":
        print("2142", x.get("status"))
