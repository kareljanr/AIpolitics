# -*- coding: utf-8 -*-
import re, ssl, urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2172")
kbo = "0433217935"


def fetch(url, name):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
    (out / name).write_bytes(data)
    print("OK", name, len(data))
    return data.decode("utf-8", "ignore")


for lang, name in [
    ("nl", "curaz_nl.html"),
    ("en", "curaz_en.html"),
    ("fr", "curaz_fr.html"),
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
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=433217935",
    "curaz_kbo.html",
)
print("Actief", "Actief" in kbo_html)
text = re.sub(r"<[^>]+>", " ", kbo_html)
text = re.sub(r"\s+", " ", text)
for pat in ["vestigingseenheden", "87.", "E-mail", "email", "Kwaremont", "Rechtsvorm"]:
    i = text.lower().find(pat.lower())
    if i >= 0:
        print(text[max(0, i - 20) : i + 100])
        print("---")
