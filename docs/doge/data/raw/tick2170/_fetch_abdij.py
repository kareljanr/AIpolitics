# -*- coding: utf-8 -*-
import re, ssl, urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2170")
out.mkdir(parents=True, exist_ok=True)
kbo = "0400371161"


def fetch(url, name):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
    (out / name).write_bytes(data)
    print("OK", name, len(data))
    return data.decode("utf-8", "ignore")


for lang, name in [
    ("nl", "abdij_nl.html"),
    ("en", "abdij_en.html"),
    ("fr", "abdij_fr.html"),
]:
    t = fetch(f"https://www.companyweb.be/{lang}/{kbo}", name)
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    print(lang, yb.get("2025"), yb.get("2024"))

fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=400371161",
    "abdij_kbo.html",
)
