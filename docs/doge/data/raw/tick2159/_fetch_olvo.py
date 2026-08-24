# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)

mined = set()
with open(Path(r"docs/doge/data/entities.csv"), newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
        for m in re.findall(r"0\d{9}", blob):
            mined.add(m)


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        print("OK", path.name, len(data))
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, e)
        return None


def summarize(label, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
    nums = re.findall(r"/en/(0\d{9})", t) + re.findall(r"BE0(\d{9})", t) + re.findall(r"BE(\d{10})", t)
    nums = list(dict.fromkeys([n[-10:] if len(n) >= 10 else n for n in nums]))
    y25 = None
    yy = None
    for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t):
        if y in ("2025", "2026"):
            yy = y

            def g(k, b=body):
                m = re.search(rf'{k}:\s*"([^"]*)"', b)
                return m.group(1) if m else None

            y25 = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
            break
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    free = [n for n in nums if n not in mined]
    print(
        label,
        (title.group(1)[:60] if title else "?"),
        "Y",
        year.group(1) if year else "-",
        "ye",
        yy,
        y25,
        "fte",
        fte.group(1) if fte else "-",
        "FREE",
        free[:4],
        "nums",
        nums[:4],
    )


urls = [
    ("olvo_en.html", "https://www.companyweb.be/en/0435015702"),
    ("olvo_nl.html", "https://www.companyweb.be/nl/0435015702"),
    ("olvo_fr.html", "https://www.companyweb.be/fr/0435015702"),
    ("olvo_kbo.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0435015702"),
    ("lindeboom_en.html", "https://www.companyweb.be/en/search?q=Lindeboom+Knokke"),  # may 404
    ("lindeboom_site.html", "https://lindeboom.be/"),
]

# Also try parent vzw Lindeboom via known patterns / KBO search page
for name, url in urls:
    t = fetch(url, out / name)
    if t and "companyweb" in url and "search" not in url:
        summarize(name, t)

# KBO for Lindeboom - from site / news: vzw De Lindeboom
for name, url in [
    ("lindeboom_kbo_guess1.html", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?searchWord=Lindeboom&_memory=true"),
]:
    fetch(url, out / name)
