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
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:80])
        return None


def detail(label, t, kbo):
    title = re.search(r"<title>([^<]+)", t)
    # broader year
    year = None
    for pat in [
        r"Last balance sheet year[^0-9N]{0,120}(20\d\d|N/A)",
        r"Laatste balansjaar[^0-9N]{0,120}(20\d\d|N/A)",
        r"Dernier exercice[^0-9N]{0,120}(20\d\d|N/A)",
        r"Last financial year[^0-9N]{0,120}(20\d\d|N/A)",
    ]:
        m = re.search(pat, t, re.I)
        if m:
            year = m.group(1)
            break
    nace = re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3}|68\.\d{3}|84\.\d{3}|41\.\d{3})", t)
    nace = list(dict.fromkeys(nace))[:8]
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t) or re.search(r"neergelegd op ([0-9-]{10})", t)
    # status / legal form hints
    form = None
    for pat in [r"(ASBL|VZW|SRL|BV|NV|SC|CV)", r"Company form[^A-Za-z]{0,40}([A-Za-z. ]+)"]:
        m = re.search(pat, t)
        if m:
            form = m.group(1)
            break
    free = kbo not in mined
    print("=" * 60)
    print(label, "kbo", kbo, "FREE" if free else "MINED")
    print("title", title.group(1)[:90] if title else "?")
    print("year_label", year, "form", form, "fte", fte.group(1) if fte else "-", "filed", filed.group(1) if filed else "-")
    print("nace", nace)
    for y in sorted(yblocks, reverse=True)[:3]:
        print(" ", y, yblocks[y])
    # email / website snippets
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    emails = [e for e in emails if "companyweb" not in e.lower() and "example" not in e.lower()]
    print("emails", emails[:5])
    return free, year, yblocks


CANDS = [
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0893863017", "faro"),
    ("0450755634", "residentie_oudenburg"),
    ("0432582485", "wzc_sint_bernardus_de_panne"),
    ("0416337262", "home_vrijzicht_ieper"),
    ("0415653116", "maria_boodschap_niel"),
    ("0413055989", "sint_jozef_aarschot"),  # may be mined as rillaar
    ("0448190181", "sint_jozef_rumst"),  # likely mined
    ("0823488131", "thofke"),
    ("0755822317", "lork_hoeselt"),
]

for kbo, label in CANDS:
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if t:
        detail(label, t, kbo)
