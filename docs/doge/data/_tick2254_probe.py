# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from collections import Counter
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2254")
OUT.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

URLS = {
    "faro_en": "https://www.companyweb.be/en/0893863017/faro",
    "aiesh_en": "https://www.companyweb.be/en/0201712587/association-intercommunale-delectricite-du-sud-du-hainaut",
    "rew_en": "https://www.companyweb.be/en/0644638937/rew",
    "relais_en": "https://www.companyweb.be/en/0415846819/relais-de-la-haute-sambre",
    "relais_nl": "https://www.companyweb.be/nl/0415846819/relais-de-la-haute-sambre",
    "relais_fr": "https://www.companyweb.be/fr/0415846819/relais-de-la-haute-sambre",
    "relais_kbo": "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0415846819",
    # other unused Walloon ETA candidates (skip known taken)
    "sipres_en": "https://www.companyweb.be/en/search?q=sipres+eta",
    "apn_en": "https://www.companyweb.be/en/search?q=APN+atelier",
    "criquelions_en": "https://www.companyweb.be/en/search?q=criquelions",
    "roseau_vert_en": "https://www.companyweb.be/en/search?q=roseau+vert+eta",
    "leseta_annuaire": "https://leseta.be/annuaire-eta/",
}


def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
            data = r.read()
            final = r.geturl()
        (OUT / f"{name}.html").write_bytes(data)
        print(name, "OK", len(data), final)
    except Exception as e:
        print(name, "ERR", type(e).__name__, e)


def parse(path: Path):
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", path.name, len(t))
    years = re.findall(r">(202[0-9])<", t)
    print("year tags", Counter(years).most_common(8))
    for label, pat in [
        ("EN last", r"Last balance sheet year.{0,300}"),
        ("NL last", r"Laatste balansjaar.{0,300}"),
        ("FR last", r"Dernier bilan.{0,300}"),
    ]:
        m = re.search(pat, t, re.S)
        if m:
            print(label, re.sub(r"\s+", " ", m.group(0))[:280])
    for pat in [
        r'omzet:\s*"([^"]+)"',
        r'brutomarge:\s*"([^"]+)"',
        r'winst:\s*"([^"]+)"',
        r'eigenVermogen:\s*"([^"]+)"',
        r'fte:\s*"([^"]+)"',
        r"filed on ([0-9-]+)",
        r"neergelegd op ([0-9.-]+)",
        r"turnover of €([0-9,.]+)",
        r"omzet van €\s*([0-9.]+)",
        r"([0-9]+[,.][0-9]) FTEs?",
        r'Employees = "([^"]+)"',
        r"Big|Medium|Small|Grand|Groot|Moyen",
        r"href=\"(/en/[0-9]+/[^\"]+)\"",
    ]:
        ms = re.findall(pat, t)
        if ms:
            print(pat[:60], ms[:10])


if __name__ == "__main__":
    for n, u in URLS.items():
        fetch(n, u)
    for f in sorted(OUT.glob("*.html")):
        parse(f)
