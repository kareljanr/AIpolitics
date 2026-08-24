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
root = Path(r"C:\Users\karel\dev\AIpolitics")

mined = set()
with open(root / "docs/doge/data/entities.csv", newline="", encoding="utf-8") as f:
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


def summarize(label, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
    print(label, (title.group(1)[:55] if title else "?"), "Y", year.group(1) if year else "-")
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
        if y >= "2023":

            def g(k, b=body):
                m = re.search(rf'{k}:\s*"([^"]*)"', b)
                return m.group(1) if m else None

            print(
                " ",
                y,
                {
                    k: g(k)
                    for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
                },
            )
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
    print(" FTE", fte.group(1) if fte else "-")
    filed = re.search(r"filed on ([0-9-]{10})", t) or re.search(
        r"neergelegd op ([0-9-]{10})", t
    )
    print(" filed", filed.group(1) if filed else "-")


cands = [
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0500952540", "wznd"),
]

for kbo, label in cands:
    free = kbo not in mined
    print("===", label, kbo, "FREE" if free else "MINED")
    for lang in ["en", "nl", "fr"]:
        t = fetch(f"https://www.companyweb.be/{lang}/{kbo}", out / f"{label}_{lang}.html")
        if t and lang == "en":
            summarize(label, t)

# KBO for WZND
fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=500952540",
    out / "wznd_kbo.html",
)
print("done")
