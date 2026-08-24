import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path("docs/doge/raw/tick2223")
OUT.mkdir(parents=True, exist_ok=True)

cands = {
    "bornem": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    "herop_nl": "https://www.companyweb.be/nl/0406678141/heropbeuring",
    "herop_en": "https://www.companyweb.be/en/0406678141/heropbeuring",
    "herop_fr": "https://www.companyweb.be/fr/0406678141/heropbeuring",
    "herop_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0406678141",
    # try FARO common KBOs
    "faro_try": "https://www.companyweb.be/nl/0453391266/faro",
}

for k, u in cands.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            data = r.read()
        # detect pdf vs html
        if data[:4] == b"%PDF":
            (OUT / f"{k}.pdf").write_bytes(data)
            print(k, "pdf", len(data))
            continue
        html = data.decode("utf-8", "replace")
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print("====", k, len(html), r.geturl())
        # kern
        m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
        if m:
            print("kern", m.group(1)[:800])
        else:
            # alternate: raw winst fields
            print("winsts", re.findall(r"winst:\s*\"([^\"]+)\"", html)[:6])
            print("bruto", re.findall(r"bruto_marge:\s*\"([^\"]+)\"", html)[:6])
            print("omzet", re.findall(r"omzet:\s*\"([^\"]*)\"", html)[:6])
            print("equity", re.findall(r"eigen_vermogen:\s*\"([^\"]+)\"", html)[:6])
        m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
        print("emp", m.group(1) if m else None)
        for pat in [
            r"neergelegd op ([0-9-]+)",
            r"filed on ([0-9-]+)",
            r"déposés le ([0-9-]+)",
            r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*(\d{4})",
        ]:
            ms = re.findall(pat, html, re.I)
            if ms:
                print(pat[:28], ms[:2])
        if "bornem" in k:
            print("JR2025?", bool(re.search(r"[Jj]aarrekening 2025", html)))
        if "kbo" in k:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
            print("VE", m.group(1) if m else None)
            m = re.search(r"Adres van de zetel:.{0,100}", text)
            print("addr", m.group(0)[:120] if m else None)
            m = re.search(r"Status:\s*(\w+)", text)
            print("status", m.group(1) if m else None)
            for n in re.findall(r"88\.\d{3}", text)[:3]:
                print("nace", n)
    except Exception as e:
        print(k, type(e).__name__, e)
