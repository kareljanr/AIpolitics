# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path(__file__).resolve().parent

cands = {
    "travie_nl": "https://www.companyweb.be/nl/0420015938/travie",
    "travie_fr": "https://www.companyweb.be/fr/0420015938/travie",
    "travie_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0420015938",
    "travie_site": "https://www.travie.be/",
    "travie_nbb": "https://consult.cbso.nbb.be/consult-enterprise/0420015938",
}

for k, u in cands.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=35) as r:
            html = r.read().decode("utf-8", "replace")
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print("====", k, len(html), r.geturl())
        m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
        if m:
            print("kern", m.group(1)[:1600])
        m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
        print("emp", m.group(1) if m else None)
        for pat in [
            r"neergelegd op ([0-9-]+)",
            r"filed on ([0-9-]+)",
            r"déposés le ([0-9-]+)",
            r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*(\d{4})",
        ]:
            ms = re.findall(pat, html)
            if ms:
                print(pat[:28], ms[:3])
        if "kbo" in k:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
            print("VE", m.group(1) if m else None)
            m = re.search(r"Adres van de zetel:.{0,160}", text)
            print("addr", m.group(0)[:180] if m else None)
            m = re.search(r"Status:\s*(\w+)", text)
            print("status", m.group(1) if m else None)
            m = re.search(r"Begindatum:.{0,60}", text)
            print("begin", m.group(0) if m else None)
            print("naces", re.findall(r"88\.\d{3}|87\.\d{3}|47\.\d{3}", text)[:8])
            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
            print("kbo emails", emails[:5])
            print("rechtsvorm", re.search(r"Rechtsvorm.{0,80}", text).group(0) if re.search(r"Rechtsvorm.{0,80}", text) else None)
        if "site" in k:
            emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
            print("emails", [e for e in emails if "sentry" not in e.lower() and "google" not in e.lower()][:10])
        if "nbb" in k:
            print("2026 deposits", re.findall(r"2026-\d{8}", html)[:8])
            print("pdf links", len(re.findall(r"\.pdf", html, re.I)))
    except Exception as e:
        print(k, type(e).__name__, e)

# YoY
om25, om24 = 4014674, 4199547
br25, br24 = 11394051, 11427981
pn25, pn24 = 36871, 345798
eq25, eq24 = 5979074, 6050049
print("omzet%", round((om25 / om24 - 1) * 100, 2))
print("bruto%", round((br25 / br24 - 1) * 100, 2))
print("pnl%", round((pn25 / pn24 - 1) * 100, 2))
print("equity%", round((eq25 / eq24 - 1) * 100, 2))
print("bruto/omzet", round(br25 / om25, 2))
