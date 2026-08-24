import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

cands = {
    "faro_nl": "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_nl": "https://www.companyweb.be/nl/0201712587/aiesh",
    "rew_nl": "https://www.companyweb.be/nl/0203720275/rew",
    "reset_nl": "https://www.companyweb.be/nl/0460015174/reset",
    "reset_en": "https://www.companyweb.be/en/0460015174/reset",
    "reset_fr": "https://www.companyweb.be/fr/0460015174/reset",
    "reset_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0460015174",
    "midwest_nl": "https://www.companyweb.be/nl/0456349366/de-kringwinkel-midden-west-vlaanderen",
    "midwest_en": "https://www.companyweb.be/en/0456349366/de-kringwinkel-midden-west-vlaanderen",
    "midwest_fr": "https://www.companyweb.be/fr/0456349366/de-kringwinkel-midden-west-vlaanderen",
    "midwest_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0456349366",
    "herop_nl": "https://www.companyweb.be/nl/0406678141/heropbeuring",
    "vites_nl": "https://www.companyweb.be/nl/0431067802/vites",
    "midwest_site": "https://www.kringwinkel.be/midwest",
}

for k, u in cands.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (compatible; research)"})
        with urllib.request.urlopen(req, context=CTX, timeout=35) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print("====", k, len(html), final)
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
            r"Dernier bilan\s*</div>\s*<div[^>]*>\s*(\d{4}|N/A)",
            r"Latest financial year\s*</div>\s*<div[^>]*>\s*(\d{4}|N/A)",
        ]:
            ms = re.findall(pat, html, re.I)
            if ms:
                print(pat[:40], ms[:3])
        if "kbo" in k:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            for lab in [
                "Status:",
                "Aantal vestigingseenheden (VE):",
                "Adres van de zetel:",
                "Rechtsvorm:",
            ]:
                m = re.search(lab + r".{0,140}", text)
                if m:
                    print(m.group(0)[:160])
            print("naces", re.findall(r"88\.\d{3}|47\.\d{3}|87\.\d{3}|94\.\d{3}", text)[:8])
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
        )
        print(
            "emails",
            [e for e in emails if "sentry" not in e and "example" not in e][:8],
        )
    except Exception as e:
        print(k, type(e).__name__, e)
