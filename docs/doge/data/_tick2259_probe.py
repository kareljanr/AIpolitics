# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2259")
OUT.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

URLS = {
    "faro_en": "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_en": "https://www.companyweb.be/en/0201712587/aiesh",
    "rew_en": "https://www.companyweb.be/en/0644638937/rew",
    "erables_en": "https://www.companyweb.be/en/0445138245/les-erables",
    "erables_nl": "https://www.companyweb.be/nl/0445138245/les-erables",
    "erables_fr": "https://www.companyweb.be/fr/0445138245/les-erables",
    "erables_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0445138245",
    "alteria_en": "https://www.companyweb.be/en/0476855364/alteria",
    "alteria_nl": "https://www.companyweb.be/nl/0476855364/alteria",
    "alteria_fr": "https://www.companyweb.be/fr/0476855364/alteria",
    "alteria_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0476855364",
    "stallbois_en": "https://www.companyweb.be/en/0426239622/stallbois",
    "bornem_jr": "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
}


def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
            data = r.read()
        (OUT / f"{name}.html").write_bytes(data)
        print(name, "OK", len(data))
        return data.decode("utf-8", "replace")
    except Exception as e:
        print(name, "ERR", e)
        return None


def parse(name, t):
    print("====", name)
    title = re.search(r"<title>([^<]+)</title>", t, re.I)
    print("title", title.group(1)[:140] if title else None)
    for label, pat in [
        ("EN last", r"Last balance sheet year.{0,350}"),
        ("NL last", r"Laatste balansjaar.{0,350}"),
        ("FR last", r"Dernier bilan.{0,350}"),
    ]:
        m = re.search(pat, t, re.S | re.I)
        if m:
            print(label, re.sub(r"\s+", " ", m.group(0))[:300])
    pats = [
        r'omzet:\s*"([^"]+)"',
        r'brutomarge:\s*"([^"]+)"',
        r'winst:\s*"([^"]+)"',
        r'eigenVermogen:\s*"([^"]+)"',
        r'fte:\s*"([^"]+)"',
        r"filed on ([0-9-]+)",
        r"neergelegd op ([0-9.-]+)",
        r"turnover of \u20ac([0-9,.]+)",
        r"omzet van \u20ac\s*([0-9.]+)",
        r'Employees = "([^"]+)"',
        r"Gross margin of \u20ac([0-9,.]+)",
        r"profit of \u20ac([0-9,.]+)",
        r"loss of \u20ac([0-9,.]+)",
        r"equity of \u20ac([0-9,.]+)",
        r"(Big|Medium|Small|Grand|Groot|Moyen)",
        r"Actief|Active",
        r"088\.?993|88\.993",
    ]
    for pat in pats:
        ms = re.findall(pat, t, re.I)
        if ms:
            print(pat[:55], ms[:10])
    years = re.findall(r">(202[0-9])<", t)
    print("years", sorted(set(years)))
    if "bornem" in name or "jr" in name:
        for y in ("2025", "2024", "jaarrekening"):
            if y.lower() in t.lower():
                print("hit", y, t.lower().count(y.lower()))


for n, u in URLS.items():
    t = fetch(n, u)
    if t:
        parse(n, t)
