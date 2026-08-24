# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, ssl
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
dst = Path("docs/doge/data/raw/tick2144")
dst.mkdir(parents=True, exist_ok=True)
blob = (
    Path("docs/doge/data/entities.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/leaderboard.csv").read_text(encoding="utf-8", errors="replace")
).lower()


def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read().decode("utf-8", "replace"), r.geturl()


# KBO phonetic search POST-like GET variants for REW
kbo_urls = [
    "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=fr&searchWord=REW&filterRechtstoestand=0&actionLu=Recherche",
    "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=fr&searchWord=energies+wavre&filterRechtstoestand=0&actionLu=Recherche",
    "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?lang=nl&searchWord=rew&filterRechtstoestand=0&actionLu=Recherche",
]
for u in kbo_urls:
    try:
        h, f = get(u)
        print("KBO", f[:100], "len", len(h))
        # result rows
        for m in re.finditer(r"ondernemingsnummer=(\d+)[^>]*>\s*([^<]{3,80})", h):
            print("  hit", m.group(1), re.sub(r"\s+", " ", m.group(2))[:70])
        for m in re.finditer(r"toonondernemingps\.html\?[^\"']*ondernemingsnummer=(\d+)", h):
            print("  link", m.group(1))
        # dump snippets with Wavre/REW
        for m in re.finditer(r".{0,40}(Wavre|REW|Energies).{0,60}", h, re.I):
            print("  snip", re.sub(r"\s+", " ", m.group(0))[:110])
    except Exception as e:
        print("KBO ERR", type(e).__name__, e)

# Try CWAPE / AREWAL pages for REW BCE
for u in [
    "https://www.arewal.be/bienvenue-sur-le-site-darewal/",
    "https://callmepower.be/fr/energie/guides/distributeurs/rew",
    "https://indemnisations-energie.be/grd.html",
    "https://www.cwape.be/",
]:
    try:
        h, f = get(u)
        print("PAGE", f[:90], len(h))
        for m in re.finditer(r"(BE\s?0\d{3}[\.\s]?\d{3}[\.\s]?\d{3}|0\d{3}[\.\s]\d{3}[\.\s]\d{3})", h):
            print("  num", re.sub(r"\s+", " ", m.group(0)))
        for m in re.finditer(r"href=\"([^\"]*rew[^\"]*)\"", h, re.I):
            print("  href", m.group(1)[:120])
    except Exception as e:
        print("PAGE ERR", u[:50], type(e).__name__, e)

# Candidate WZC/MRS names from AVIQ-style common unused list
mrs = [
    ("les_tilleuls_bruxelles", "https://www.companyweb.be/en/0400223456"),  # placeholder skip
]
# Better: scrape AVIQ list page for enterprise numbers if present
aviq = "https://www.aviq.be/fr/liste-des-maisons-de-repos-incl-maisons-de-repos-et-de-soins-et-court-sejour-residences-services-et"
try:
    h, f = get(aviq)
    print("AVIQ", f[:100], len(h))
    xs = re.findall(r'href="([^"]+\.(?:xlsx|xls|csv|pdf))"', h, re.I)
    print(" files", xs[:10])
    for m in re.finditer(r"(0\d{3}[\.\s]\d{3}[\.\s]\d{3})", h):
        print(" num", m.group(1))
except Exception as e:
    print("AVIQ ERR", type(e).__name__, e)

# Try Upswitch search
for u in [
    "https://upswitch.be/fr/entreprise/reseau-d-energies-de-wavre",
    "https://www.pappers.be/fr/company/reseau-denergies-de-wavre",
    "https://www.companyweb.be/fr/search?query=R%C3%A9seau+d%27%C3%89nergies+de+Wavre",
    "https://www.companyweb.be/fr/search?query=REW+Wavre",
]:
    try:
        h, f = get(u)
        print("ALT", f[:100], len(h))
        title = re.search(r"<title>([^<]+)", h)
        print(" title", title.group(1)[:90] if title else None)
        for m in re.finditer(r"(BE\s?0\d{3}[\.\s]?\d{3}[\.\s]?\d{3}|/fr/\d{10}/|/en/\d{10}/)", h):
            print(" ", re.sub(r"\s+", " ", m.group(0))[:80])
        years = re.findall(r"\n(202[0-9])\s*:", h)
        last = re.search(r"(Last balance sheet year|Dernier bilan)[^0-9]*([0-9]{4})", h, re.I)
        print(" years", years[:4], "last", last.group(2) if last else None)
    except Exception as e:
        print("ALT ERR", u[:60], type(e).__name__, e)
