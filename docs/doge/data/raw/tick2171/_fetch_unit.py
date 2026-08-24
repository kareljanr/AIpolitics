# -*- coding: utf-8 -*-
"""Fetch De Vlietoever WZC Bornem YE2025 mirrors + KBO."""
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2171")
KBO = "0898596122"
SLUG = "de-vlietoever-wzc"


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        p.write_bytes(data)
        print("OK", p.name, len(data))
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", p.name, type(e).__name__, e)
        return None


def parse(t):
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed = re.search(r"filed on ([0-9-]{10})", t or "")
    title = re.search(r"<title>([^<]+)", t or "")
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", t or "", re.I)
    act = re.search(r"Principal activity</[^>]+>\s*([^<]+)", t or "", re.I)
    # NL fields
    if not last:
        last_m = re.search(r"Laatste balansjaar[^0-9]*(\d{4})", t or "", re.I)
        last = last_m.group(1) if last_m else None
    if not filed:
        filed_m = re.search(
            r"neergelegd op ([0-9]{2}-[0-9]{2}-[0-9]{4})", t or "", re.I
        )
        filed = filed_m.group(1) if filed_m else None
    nace = re.findall(r"87\.\d{3}|86\.\d{3}|88\.\d{3}|68\.\d{3}", t or "")[:8]
    return yb, fte, filed, title, last, act, nace


en = fetch(f"https://www.companyweb.be/en/{KBO}", out / f"vlietoever_{KBO}_en.html")
nl = fetch(
    f"https://www.companyweb.be/nl/{KBO}/{SLUG}",
    out / f"vlietoever_{KBO}_nl.html",
)
fr = fetch(f"https://www.companyweb.be/fr/{KBO}", out / f"vlietoever_{KBO}_fr.html")
kbo = fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"lang=nl&ondernemingsnummer={KBO}",
    out / f"vlietoever_{KBO}_kbo.html",
)

for label, t in [("EN", en), ("NL", nl), ("FR", fr)]:
    if not t:
        continue
    yb, fte, filed, title, last, act, nace = parse(t)
    print(f"\n=== {label} ===")
    print("title", (title.group(1) if title else "")[:80])
    print("last", last, "fte", fte.group(1) if fte else None, "filed", filed)
    print("act", (act.group(1).strip() if act else "")[:80])
    print("nace", nace)
    for y in sorted(yb):
        print(y, yb[y])

if kbo:
    # extract key KBO fields
    for pat in [
        r"Status van de entiteit</td>\s*<td[^>]*>([^<]+)",
        r"Rechtsvorm</td>\s*<td[^>]*>.*?>([^<]+)",
        r"Adres van de zetel</td>\s*<td[^>]*>(.*?)</td>",
        r"E-mailadres</td>\s*<td[^>]*>(.*?)</td>",
        r"Telefoonnummer</td>\s*<td[^>]*>(.*?)</td>",
        r"Aantal vestigingen.*?</td>\s*<td[^>]*>([^<]+)",
        r"BTW[^<]*</td>\s*<td[^>]*>(.*?)</td>",
        r"RSZ[^<]*</td>\s*<td[^>]*>(.*?)</td>",
        r"Nace[^<]*</td>\s*<td[^>]*>(.*?)</td>",
    ]:
        m = re.search(pat, kbo, re.I | re.S)
        if m:
            val = re.sub(r"<[^>]+>", " ", m.group(1))
            val = re.sub(r"\s+", " ", val).strip()
            print("KBO", pat[:40], "=>", val[:120])
