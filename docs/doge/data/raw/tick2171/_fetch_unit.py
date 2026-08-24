# -*- coding: utf-8 -*-
import re, ssl, urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2171")
out.mkdir(parents=True, exist_ok=True)
kbo = "0835884236"


def fetch(url, name):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
    (out / name).write_bytes(data)
    print("OK", name, len(data))
    return data.decode("utf-8", "ignore")


for lang, name in [
    ("nl", "hetdorp_nl.html"),
    ("en", "hetdorp_en.html"),
    ("fr", "hetdorp_fr.html"),
]:
    t = fetch(f"https://www.companyweb.be/{lang}/{kbo}", name)
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"([\d.,]+)\s*FTE", t)
    filed = re.search(r"(?:filed on|neergelegd op|déposés le)\s*([0-9./-]{8,12})", t, re.I)
    print(lang, "2025", yb.get("2025"), "2024", yb.get("2024"), "fte", fte.group(1) if fte else None, "filed", filed.group(1) if filed else None)

kbo_html = fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=835884236",
    "hetdorp_kbo.html",
)
print("Actief", "Actief" in kbo_html or "Active" in kbo_html)
print("NACE", re.findall(r"87\.\d{3}|86\.\d{3}|88\.\d{3}|68\.\d{3}", kbo_html)[:8])
print("email", re.findall(r"[\w.+-]+@[\w.-]+\.\w+", kbo_html)[:5])
print("VE", re.search(r"Aantal vestigingseenheden.*?(\d+)", kbo_html, re.S))
