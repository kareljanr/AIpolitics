# -*- coding: utf-8 -*-
import re, ssl, urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2169")
out.mkdir(parents=True, exist_ok=True)
kbo = "0644843825"


def fetch(url, name):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
    (out / name).write_bytes(data)
    print("OK", name, len(data))
    return data.decode("utf-8", "ignore")


for lang, name in [
    ("nl", "aaigem_nl.html"),
    ("en", "aaigem_en.html"),
    ("fr", "aaigem_fr.html"),
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
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=644843825",
    "aaigem_kbo.html",
)
print("status", "Actief" in kbo_html)
print("VE", re.search(r"Aantal vestigingseenheden.*?(\d+)", kbo_html, re.S))
# also parent WZC YE2024 for dual note
t2 = fetch("https://www.companyweb.be/en/0422620585", "parent_wzc_sint_vincentius_en.html")
yb2 = {}
for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t2):
    def g(k, b=body):
        m = re.search(rf'{k}:\s*"([^"]*)"', b)
        return m.group(1) if m else None

    yb2[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
print("parent last years", {k: yb2[k] for k in sorted(yb2)[-2:]})
