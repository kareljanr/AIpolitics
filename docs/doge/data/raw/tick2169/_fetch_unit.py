# -*- coding: utf-8 -*-
import re, ssl, urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2169")
out.mkdir(parents=True, exist_ok=True)
kbo = "0644497395"


def fetch(url, name):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
    p = out / name
    p.write_bytes(data)
    print("OK", name, len(data))
    return data.decode("utf-8", "ignore")


for lang, name in [
    ("nl", "prinsenhof_nl.html"),
    ("en", "prinsenhof_en.html"),
    ("fr", "prinsenhof_fr.html"),
]:
    t = fetch(f"https://www.companyweb.be/{lang}/{kbo}", name)
    # parse year blocks
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    print(lang, "2025", yb.get("2025"), "2024", yb.get("2024"))

kbo_html = fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=644497395",
    "prinsenhof_kbo.html",
)
print("KBO Actief", "Actief" in kbo_html or "Active" in kbo_html)
print("NACE", re.findall(r"87\.\d{3}", kbo_html)[:6])
print("email", re.findall(r"[\w.+-]+@[\w.-]+", kbo_html)[:5])
