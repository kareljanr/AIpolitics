# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

cands = {
    "faro_en": "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_en": "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut",
    "rew_en": "https://www.companyweb.be/en/0200736255/rew",
    "bornem": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    "herop_en": "https://www.companyweb.be/en/0406678141/heropbeuring",
    "sdb_nl": "https://www.companyweb.be/nl/0665861844/sociaal-dienstenchequebedrijf",
    "sdb_en": "https://www.companyweb.be/en/0665861844/sociaal-dienstenchequebedrijf",
    "sdb_fr": "https://www.companyweb.be/fr/0665861844/sociaal-dienstenchequebedrijf",
    "sdb_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0665861844",
    "travie_en": "https://www.companyweb.be/en/0420015938/travie",
    "rucher_en": "https://www.companyweb.be/en/0860345458/le-rucher",
    "vleugels_en": "https://www.companyweb.be/en/0431408290/de-vleugels",
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
            print("kern", m.group(1)[:1400])
        m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
        print("emp", m.group(1) if m else None)
        for pat in [
            r"neergelegd op ([0-9-]+)",
            r"filed on ([0-9-]+)",
            r"déposés le ([0-9-]+)",
            r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*(\d{4})",
            r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(\d{4})",
            r"Dernier bilan\s*</div>\s*<div[^>]*>\s*(\d{4})",
        ]:
            ms = re.findall(pat, html)
            if ms:
                print(pat[:28], ms[:3])
        if "kbo" in k:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
            print("VE", m.group(1) if m else None)
            m = re.search(r"Adres van de zetel:.{0,140}", text)
            print("addr", m.group(0)[:160] if m else None)
            m = re.search(r"Status:\s*(\w+)", text)
            print("status", m.group(1) if m else None)
            print("naces", re.findall(r"8[178]\.\d{3}|97\.\d{3}", text)[:8])
            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
            print("kbo emails", emails[:5])
        if "bornem" in k:
            print("JR2025", bool(re.search(r"Jaarrekening 2025", html)))
            print("JR2024", bool(re.search(r"Jaarrekening 2024", html)))
    except Exception as e:
        print(k, type(e).__name__, e)
