import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path("docs/doge/raw/tick2224")
OUT.mkdir(parents=True, exist_ok=True)

cands = {
    "kw_west_nl": "https://www.companyweb.be/nl/0461050502/kringwinkel-west",
    "kw_west_en": "https://www.companyweb.be/en/0461050502/kringwinkel-west",
    "kw_west_fr": "https://www.companyweb.be/fr/0461050502/kringwinkel-west",
    "kw_west_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0461050502",
    "bornem": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    "kw_west_site": "https://www.kringwinkel.be/west",
}

for k, u in cands.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print("====", k, len(html), r.geturl())
        m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
        if m:
            print("kern", m.group(1)[:900])
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
                print(pat[:28], ms[:2])
        if "kbo" in k:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
            print("VE", m.group(1) if m else None)
            m = re.search(r"Adres van de zetel:.{0,100}", text)
            print("addr", m.group(0)[:120] if m else None)
            m = re.search(r"Status:\s*(\w+)", text)
            print("status", m.group(1) if m else None)
            print("naces", re.findall(r"88\.\d{3}|47\.\d{3}", text)[:6])
        if "bornem" in k:
            print("JR2025", bool(re.search(r"Jaarrekening 2025", html)))
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
        )
        print("emails", [e for e in emails if "sentry" not in e][:6])
    except Exception as e:
        print(k, type(e).__name__, e)

# deltas from search snippet
br25, br24 = 2125485, 1842793
pn25, pn24 = -144804, -260994
eq25, eq24 = 1175497, 1214387
print("bruto pct", round((br25 / br24 - 1) * 100, 2))
print("pnl pct", round((pn25 / pn24 - 1) * 100, 2))  # loss narrow
print("equity pct", round((eq25 / eq24 - 1) * 100, 2))
