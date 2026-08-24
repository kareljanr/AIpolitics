# -*- coding: utf-8 -*-
import urllib.request, ssl, re
from pathlib import Path
from urllib.parse import quote

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        print("OK", path.name, len(data), url)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, e)
        return None


# Prefer path checks + unused care entities
direct = {
    "aiesh_en.html": "https://www.companyweb.be/en/0201712587",
    "rew_en.html": "https://www.companyweb.be/en/0644638937",
    "faro_search.html": "https://www.companyweb.be/nl/search?q=FARO+Vlaams+steunpunt",
    "epinette_en.html": "https://www.companyweb.be/en/0447771695",
    "apricusa_en.html": "https://www.companyweb.be/en/search?q=Apricusa",
}

for name, url in direct.items():
    fetch(url, out / name)

names = [
    ("neuve_cour", "Neuve Cour Tubize"),
    ("la_reposee", "La Reposee Mons maison"),
    ("new_beaugency", "New Beaugency Bernissart"),
    ("service_ardennes", "Service des Ardennes Attert"),
    ("homyad", "Homyad"),
    ("novadia", "Novadia woonzorg"),
]

for key, q in names:
    t = fetch(f"https://www.companyweb.be/nl/search?q={quote(q)}", out / f"search_{key}.html")
    if not t:
        continue
    nums = re.findall(r"/nl/(0\d{9})/", t)
    titles = re.findall(r'href="/nl/0\d{9}/[^"]+"[^>]*>([^<]{3,90})<', t)
    print(key, "nums", nums[:10], "titles", titles[:6])
