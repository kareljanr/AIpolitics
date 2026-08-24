# -*- coding: utf-8 -*-
from pathlib import Path
import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


def summarize(name, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
    om2 = re.search(r'omzet:\s*"([^"]+)"', t)
    winst = re.search(r'winst:\s*"([^"]+)"', t)
    bruto = re.search(r'brutomarge:\s*"([^"]+)"', t)
    ev = re.search(r'eigenvermogen:\s*"([^"]+)"', t)
    fte = re.search(r'werknemers:\s*"([^"]+)"', t)
    if not fte:
        fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    print(
        name,
        (title.group(1)[:55] if title else "?"),
        "Y",
        year.group(1) if year else "-",
        "omzet",
        om2.group(1) if om2 else "-",
        "winst",
        winst.group(1) if winst else "-",
        "bruto",
        bruto.group(1) if bruto else "-",
        "equity",
        ev.group(1) if ev else "-",
        "fte",
        fte.group(1) if fte else "-",
    )


for f in ["aiesh_en.html", "rew_en.html", "epinette_en.html"]:
    summarize(f, (out / f).read_text(encoding="utf-8", errors="ignore"))

# FARO KBO 0893.863.017
for name, url in [
    ("faro_en.html", "https://www.companyweb.be/en/0893863017"),
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017"),
    ("epinette_nl.html", "https://www.companyweb.be/nl/0447771695"),
    ("epinette_fr.html", "https://www.companyweb.be/fr/0447771695"),
    ("epinette_kbo.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0447771695"),
]:
    try:
        t = fetch(url, out / name)
        summarize(name, t)
    except Exception as e:
        print("FAIL", name, e)
