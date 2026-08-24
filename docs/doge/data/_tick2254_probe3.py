# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from collections import Counter
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2254")
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

PAGES = [
    "leseta_erables.html",
    "leseta_hautes.html",
    "leseta_belair.html",
    "leseta_gaume.html",
    "leseta_mons.html",
    "leseta_alteria.html",
    "leseta_atelier85.html",
    "leseta_cambier.html",
    "leseta_adapta.html",
    "leseta_apn.html",
    "leseta_relais-de-la-haute-sambre.html",
]


def extract_ids(html: str):
    # common patterns in leseta cards
    pats = [
        r"entreprise[:\s]*BE\s*([0-9.\s]{10,14})",
        r"BCE[:\s]*BE?\s*([0-9.\s]{10,14})",
        r"TVA[:\s]*BE\s*([0-9.\s]{10,14})",
        r"BE\s*(0\d{3}\.\d{3}\.\d{3})",
        r"BE\s*(0\d{9})",
        r"nummer[:\s]*([0-9.]{10,14})",
        r"data-enterprise[^>]*=\"(\d{10})\"",
        r"companyweb\.be/(?:en|nl|fr)/(\d{10})",
        r"kbopub[^\"']*nummer=(\d{9,10})",
        r"ondernemingsnummer=(\d{9,10})",
    ]
    found = []
    for p in pats:
        found += re.findall(p, html, re.I)
    # also look near "numéro"
    for m in re.finditer(r".{0,40}(?:BCE|TVA|entreprise|KBO|numéro).{0,80}", html, re.I):
        chunk = re.sub(r"\s+", " ", m.group(0))
        if re.search(r"\d{4}", chunk):
            found.append("CTX:" + chunk[:120])
    return found


for fn in PAGES:
    p = OUT / fn
    if not p.exists():
        print("missing", fn)
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    print("====", fn)
    ids = extract_ids(t)
    print(" ids", ids[:20])
    # address blocks
    for pat in [r"Rue[^<\n]{5,80}", r"Chaussée[^<\n]{5,80}", r"Avenue[^<\n]{5,80}", r"Boulevard[^<\n]{5,80}"]:
        ms = re.findall(pat, t)
        if ms:
            print(" addr", ms[:3])
            break

# Direct companyweb by guessed names from public knowledge / google
# Use open_page style: fetch known companyweb slug patterns after web search
CANDIDATES = {
    # from prior public knowledge / likely KBOs we can discover via KBO search pages
    "erables": None,
    "mons": None,
    "hautes": None,
    "belair": None,
    "gaume": None,
    "alteria": None,
    "atelier85": None,
    "cambier": None,
    "adapta": None,
    "ajr": None,
    "lorraine": None,
    "criquelions": None,
}

# Try companyweb English pages with name slug guesses
SLUGS = [
    ("erables", "https://www.companyweb.be/en/0416105827/les-erables"),  # guessed from earlier kbo-ish 0416 105.827 on roseau page? maybe wrong
    ("mons_guess", "https://www.companyweb.be/en/0407750123/les-ateliers-de-mons"),
]

# Better approach: KBO public search by name
KBO_SEARCH = [
    ("kbo_erables", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Les+Erables&filterEnkelActieveEntiteiten=true"),
    ("kbo_mons", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Ateliers+de+Mons&filterEnkelActieveEntiteiten=true"),
    ("kbo_hautes", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Hautes+Ardennes&filterEnkelActieveEntiteiten=true"),
    ("kbo_belair", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Belair&filterEnkelActieveEntiteiten=true&pstcdeNPRP=6900"),
    ("kbo_gaume", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Pepinieres+La+Gaume&filterEnkelActieveEntiteiten=true"),
    ("kbo_alteria", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Alteria&filterEnkelActieveEntiteiten=true"),
    ("kbo_atelier85", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Atelier+85&filterEnkelActieveEntiteiten=true"),
    ("kbo_cambier", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Atelier+Cambier&filterEnkelActieveEntiteiten=true"),
    ("kbo_adapta", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Adapta&filterEnkelActieveEntiteiten=true"),
    ("kbo_ajr", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Jean+Regniers&filterEnkelActieveEntiteiten=true"),
    ("kbo_lorraine", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=La+Lorraine&filterEnkelActieveEntiteiten=true&pstcdeNPRP=6700"),
    ("kbo_criquelions", "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=Criquelions&filterEnkelActieveEntiteiten=true"),
]


def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
            data = r.read()
        (OUT / f"{name}.html").write_bytes(data)
        print(name, "OK", len(data))
        return data.decode("utf-8", errors="replace")
    except Exception as e:
        print(name, "ERR", e)
        return None


print("\n=== KBO name searches ===")
for name, url in KBO_SEARCH:
    t = fetch(name, url)
    if not t:
        continue
    # parse result rows
    rows = re.findall(
        r"ondernemingsnummer=(\d{9,10})[^>]*>\s*([^<]{2,80})",
        t,
    )
    if not rows:
        rows = re.findall(r"(\d{4}\.\d{3}\.\d{3}).{0,40}?([A-ZÉÈÀÂÊËÎÏÔÙÛÜÇ][^<\n]{3,60})", t)
    print(" ", name, "hits", rows[:8])
