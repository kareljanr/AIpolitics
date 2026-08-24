# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.parse
import urllib.request
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2254")
OUT.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"


def fetch(url, name=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
        data = r.read()
    if name:
        (OUT / name).write_bytes(data)
    return data


# WP REST API for ETA directory posts/pages
candidates = [
    ("wp_pages", "https://leseta.be/wp-json/wp/v2/pages?per_page=100&search=annuaire"),
    ("wp_posts", "https://leseta.be/wp-json/wp/v2/posts?per_page=100"),
    ("wp_eta", "https://leseta.be/wp-json/wp/v2/eta?per_page=100"),
    ("wp_types", "https://leseta.be/wp-json/wp/v2/types"),
    ("sitemap", "https://leseta.be/sitemap_index.xml"),
    ("sitemap_pages", "https://leseta.be/page-sitemap.xml"),
    ("eweta", "https://eweta.be/"),
]

for name, url in candidates:
    try:
        data = fetch(url, f"{name}.bin")
        print(name, "OK", len(data), data[:120])
    except Exception as e:
        print(name, "ERR", e)

# parse sitemap for annuaire-eta
for sm in ["sitemap_pages.bin", "sitemap.bin", "sitemap_index.bin"]:
    p = OUT / sm
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    urls = re.findall(r"<loc>([^<]*annuaire-eta[^<]*)</loc>", t)
    print(sm, "annuaire urls", len(urls))
    for u in urls[:80]:
        print(" ", u)

# also try companyweb direct KBOs for known Hainaut provincial ETAs
# Criquelions / Roseau Vert / Metalgroup already taken; Relais YE2024
# Try other known unused Walloon ETAs from public lists
PROBE = {
    "criquelions": "https://www.companyweb.be/en/search?q=0415.xxx",  # placeholder skip
}
# Known ETA names -> try companyweb search by name path guess
NAMES = [
    ("criquelions", "criquelions"),
    ("roseau_vert", "le-roseau-vert"),
    ("sipres", "sipres"),
    ("apn", "apn"),
    ("atelier_du_val", "atelier-du-val"),
    ("ateliers_saint_laurent", "ateliers-saint-laurent"),
    ("la_chanterelle", "la-chanterelle"),
    ("la_chance", "la-chance"),
    ("baticrea", "baticrea"),
    ("projet_t", "projet-t"),
    ("horizon", "horizon-vert"),
    ("ouvroir", "louvroir"),
    ("les_ateliers_namurois", "les-ateliers-namurois"),
    ("atelier_protege_arlon", "atelier"),
    ("la_ferme_abbaye", "ferme-abbaye"),
    ("travailler_ensemble", "travailler-ensemble"),
    ("wicare", "wicare"),
    ("adapte", "adapte"),
    ("solidarite", "solidarite-emploi"),
    ("ateliers_liegeois", "ateliers-liegeois"),
]

# Better: google-like via companyweb enterprise number from leseta individual pages
# Fetch known province Hainaut ETA pages
HAINAUT = [
    "https://leseta.be/annuaire-eta/le-roseau-vert/",
    "https://leseta.be/annuaire-eta/les-criquelions/",
    "https://leseta.be/annuaire-eta/criquelions/",
    "https://leseta.be/annuaire-eta/sipres/",
    "https://leseta.be/annuaire-eta/apn/",
    "https://leseta.be/annuaire-eta/relais-de-la-haute-sambre/",
    "https://leseta.be/annuaire-eta/le-relais-de-la-haute-sambre/",
    "https://leseta.be/annuaire-eta/metalgroup/",
    "https://actionsociale.hainaut.be/handicap/entreprises-de-travail-adapte-eta/",
]

for url in HAINAUT:
    slug = url.rstrip("/").split("/")[-1] or "index"
    try:
        data = fetch(url, f"leseta_{slug}.html")
        print("leseta", slug, "OK", len(data))
        # extract BCE / KBO
        t = data.decode("utf-8", errors="replace")
        kb = re.findall(r"(?:BE\s*)?(0\d{3}[\.\s]?\d{3}[\.\s]?\d{3})", t)
        print("  kbo-ish", kb[:8])
        emails = re.findall(r"[\w.+-]+@[\w.-]+\.\w+", t)
        print("  email", emails[:5])
    except Exception as e:
        print("leseta", slug, "ERR", e)
