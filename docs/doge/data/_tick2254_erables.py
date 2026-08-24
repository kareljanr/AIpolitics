# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2254")
OUT.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

URLS = {
    "erables_en": "https://www.companyweb.be/en/0445138245/les-erables",
    "erables_nl": "https://www.companyweb.be/nl/0445138245/les-erables",
    "erables_fr": "https://www.companyweb.be/fr/0445138245/les-erables",
    "erables_kbo": "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0445138245",
    "erables_site": "https://www.leserables.be/",
    # more candidates from web/known
    "mons_cw_guess": "https://www.companyweb.be/en/0408123456/x",  # placeholder skip
}


def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
            data = r.read()
        (OUT / f"{name}.html").write_bytes(data)
        print(name, "OK", len(data), r.geturl() if False else "")
        return data.decode("utf-8", errors="replace")
    except Exception as e:
        print(name, "ERR", e)
        return None


def parse(name, t):
    print("====", name)
    for label, pat in [
        ("EN last", r"Last balance sheet year.{0,250}"),
        ("NL last", r"Laatste balansjaar.{0,250}"),
        ("FR last", r"Dernier bilan.{0,250}"),
    ]:
        m = re.search(pat, t, re.S)
        if m:
            print(label, re.sub(r"\s+", " ", m.group(0))[:250])
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
        r'Employees = "([^"]+)"',
        r"(Big|Medium|Small|Grand|Groot|Moyen)",
        r"Actief|Active",
        r"NACE[^<]{0,40}",
        r"VE|vestiging",
    ]:
        ms = re.findall(pat, t)
        if ms:
            print(pat[:50], ms[:8])
    # KBO page fields
    for pat in [
        r"Status[^<]*</[^>]+>\s*<[^>]+>([^<]+)",
        r"Ondernemingsnummer[^<]*</[^>]+>\s*<[^>]+>([^<]+)",
        r"Maatschappelijke naam[^<]*</[^>]+>\s*<[^>]+>([^<]+)",
    ]:
        ms = re.findall(pat, t, re.I)
        if ms:
            print("kbo", pat[:30], ms[:3])


for n, u in URLS.items():
    if "guess" in n:
        continue
    t = fetch(n, u)
    if t:
        parse(n, t)
