import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path("docs/doge/raw/tick2223")

cands = {
    "kw_maasland_nl": "https://www.companyweb.be/nl/0417701992/de-kringwinkel-maasland",
    "kw_maasland_en": "https://www.companyweb.be/en/0417701992/de-kringwinkel-maasland",
    "kw_maasland_fr": "https://www.companyweb.be/fr/0417701992/de-kringwinkel-maasland",
    "kw_midwest_nl": "https://www.companyweb.be/nl/0456349366/de-kringwinkel-midden-west-vlaanderen",
    "kw_midwest_en": "https://www.companyweb.be/en/0456349366/de-kringwinkel-midden-west-vlaanderen",
    "reset_nl": "https://www.companyweb.be/nl/0460015174/reset",
    "reset_en": "https://www.companyweb.be/en/0460015174/reset",
    "den_azalee_nl": "https://www.companyweb.be/nl/0456719748/den-azalee",
    "den_azalee_en": "https://www.companyweb.be/en/0456719748/den-azalee",
    "vites_nl": "https://www.companyweb.be/nl/0431067802/vites",
    "vites_en": "https://www.companyweb.be/en/0431067802/vites",
    "stroom_nl": "https://www.companyweb.be/nl/0448996568/stroom",
    "stroom_en": "https://www.companyweb.be/en/0448996568/stroom",
    # dig herop free-pub latest + kbo
    "herop_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0406678141",
    "herop_freepub": "https://www.companyweb.be/company/0406678141/free-pub/25237321",
}


def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=35) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        (OUT / f"{name}.html").write_text(html, encoding="utf-8")
        print("====", name, "len", len(html), "url", final)
        m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
        if m:
            # print only first year block
            years = re.findall(r"(20\d{2})\s*:\s*\{([^}]{0,350})\}", m.group(1))
            for y, body in years[:3]:
                print("Y", y, body.replace("\n", " ")[:220])
        else:
            print("kern NONE")
        for pat in [
            r"neergelegd op ([0-9.-]+)",
            r"filed on ([0-9.-]+)",
            r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*(\d{4})",
            r"Last financial year\s*</div>\s*<div[^>]*>\s*(\d{4})",
        ]:
            ms = re.findall(pat, html, re.I)
            if ms:
                print(pat[:28], ms[:3])
        m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
        print("emp", m.group(1) if m else None)
        title = re.search(r"<title>([^<]+)", html)
        if title:
            print("title", title.group(1)[:110])
        if "kbo" in name:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text)
            for pat in [
                r"Status:\s*(\w+)",
                r"Aantal vestigingseenheden \(VE\):\s*(\d+)",
                r"Adres van de zetel:.{0,100}",
                r"Begindatum:.{0,40}",
            ]:
                m = re.search(pat, text)
                if m:
                    print(m.group(0)[:120])
            for nace in re.findall(r"88\.\d{3}|47\.\d{3}|87\.\d{3}", text)[:5]:
                print("nace", nace)
    except Exception as e:
        print("====", name, type(e).__name__, e)


for k, u in cands.items():
    fetch(k, u)
