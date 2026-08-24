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

# Candidate unused ETAs (skip Metalgroup/Saupont/etc.)
URLS = {
    "annuaire_sitemap": "https://leseta.be/annuaire-eta-sitemap.xml",
    "ateliers_mons_site": "https://ateliersdemons.org/",
    "ateliers_mons_cw": "https://www.companyweb.be/en/search?q=Ateliers+de+Mons+ASBL",
    "erables_cw": "https://www.companyweb.be/en/search?q=Les+Erables+Tournai+ETA",
    "hautes_ardennes_cw": "https://www.companyweb.be/en/search?q=Hautes+Ardennes+Vielsalm",
    "belair_cw": "https://www.companyweb.be/en/search?q=Belair+Marche+ETA",
    "lorraine_cw": "https://www.companyweb.be/en/search?q=Groupe+La+Lorraine+Arlon",
    "gaume_cw": "https://www.companyweb.be/en/search?q=P%C3%A9pini%C3%A8res+La+Gaume",
    "ajr_cw": "https://www.companyweb.be/en/search?q=Atelier+Jean+Regniers",
    "alteria_cw": "https://www.companyweb.be/en/search?q=Alteria+Colfontaine",
    "atelier85_cw": "https://www.companyweb.be/en/search?q=Atelier+85+Florennes",
    "cambier_cw": "https://www.companyweb.be/en/search?q=Atelier+Cambier+Jumet",
    "adapta_cw": "https://www.companyweb.be/en/search?q=Adapta+Kelmis",
    "criquelions_cw": "https://www.companyweb.be/en/search?q=Criquelions",
    "roseau_cw": "https://www.companyweb.be/en/search?q=Roseau+Vert+ETA",
    # direct leseta pages
    "leseta_erables": "https://leseta.be/annuaire-eta/les-erables/",
    "leseta_hautes": "https://leseta.be/annuaire-eta/les-hautes-ardennes/",
    "leseta_belair": "https://leseta.be/annuaire-eta/belair/",
    "leseta_lorraine": "https://leseta.be/annuaire-eta/groupe-la-lorraine/",
    "leseta_gaume": "https://leseta.be/annuaire-eta/pepinieres-la-gaume/",
    "leseta_mons": "https://leseta.be/annuaire-eta/les-ateliers-de-mons/",
    "leseta_ajr": "https://leseta.be/annuaire-eta/ajr/",
    "leseta_alteria": "https://leseta.be/annuaire-eta/alteria/",
    "leseta_atelier85": "https://leseta.be/annuaire-eta/atelier-85/",
    "leseta_cambier": "https://leseta.be/annuaire-eta/atelier-cambier/",
    "leseta_adapta": "https://leseta.be/annuaire-eta/adapta/",
}


def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
            data = r.read()
            final = r.geturl()
        (OUT / f"{name}.html").write_bytes(data)
        print(name, "OK", len(data), final)
        return data
    except Exception as e:
        print(name, "ERR", type(e).__name__, e)
        return None


def summarize(name, data: bytes):
    t = data.decode("utf-8", errors="replace")
    if "sitemap" in name or name.endswith("xml"):
        locs = re.findall(r"<loc>([^<]+)</loc>", t)
        print("  locs", len(locs))
        for u in locs:
            if "annuaire" in u:
                print("   ", u)
        return
    # companyweb year
    m = re.search(r"Last balance sheet year.{0,200}", t, re.S)
    if m:
        print("  EN", re.sub(r"\s+", " ", m.group(0))[:200])
    years = Counter(re.findall(r">(202[45])<", t))
    if years:
        print("  years", years)
    # KBO-ish / emails from leseta
    emails = [e for e in re.findall(r"[\w.+-]+@[\w.-]+\.\w+", t) if "leaflet" not in e and "wp" not in e][:6]
    if emails:
        print("  email", emails)
    # companyweb result cards
    cards = re.findall(r'href="(/en/(\d{10})/[^"]+)"[^>]*>\s*([^<]{3,80})', t)
    if cards:
        print("  cw cards", cards[:8])
    # BCE patterns
    bce = re.findall(r"BE\s*0?(\d{3}[\.\s]?\d{3}[\.\s]?\d{3})", t)
    if bce:
        print("  BCE", bce[:6])


if __name__ == "__main__":
    for n, u in URLS.items():
        data = fetch(n, u)
        if data:
            summarize(n, data)
