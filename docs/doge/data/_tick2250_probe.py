# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from collections import Counter
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2250")
OUT.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

URLS = {
    "aiesh_en": "https://www.companyweb.be/en/0201712587/association-intercommunale-delectricite-du-sud-du-hainaut",
    "aiesh_nl": "https://www.companyweb.be/nl/0201712587/association-intercommunale-delectricite-du-sud-du-hainaut",
    "rew_en": "https://www.companyweb.be/en/0644638937/rew",
    "rew_nl": "https://www.companyweb.be/nl/0644638937/rew",
    "gaillettes_en": "https://www.companyweb.be/en/search?q=0407750123",
}


def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
            data = r.read()
        (OUT / f"{name}.html").write_bytes(data)
        print(name, "OK", len(data))
    except Exception as e:
        print(name, "ERR", e)


def parse(path: Path):
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", path.name, len(t))
    years = re.findall(r">(202[0-9])<", t)
    print("year tags", Counter(years).most_common(8))
    for label, pat in [
        ("EN last", r"Last balance sheet year.{0,250}"),
        ("NL last", r"Laatste balansjaar.{0,250}"),
        ("FR last", r"Dernier bilan.{0,250}"),
    ]:
        m = re.search(pat, t, re.S)
        if m:
            print(label, re.sub(r"\s+", " ", m.group(0))[:220])
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
        r"Employees = \"([^\"]+)\"",
        r"Big|Medium|Small|Groot|Moyen",
        r"Actief|Active",
    ]:
        ms = re.findall(pat, t)
        if ms:
            print(pat, ms[:8])
    # chart years in table headers
    th = re.findall(r"<th[^>]*>\s*(202[0-9])\s*<", t)
    if th:
        print("th years", th[:10])


if __name__ == "__main__":
    for n, u in URLS.items():
        fetch(n, u)
    for f in [
        "dauphins_vise_en.html",
        "dauphins_vise_nl.html",
        "dauphins_vise_fr.html",
        "saupont_en.html",
        "saupont_nl.html",
        "aiesh_en.html",
        "aiesh_nl.html",
        "rew_en.html",
        "rew_nl.html",
        "faro_en.html",
        "agb_bornem_en.html",
    ]:
        p = OUT / f
        if p.exists():
            parse(p)
