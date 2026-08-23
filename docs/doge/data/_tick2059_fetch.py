# ephemeral fetch tick2059 Home Vrijzicht
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2059")
outdir.mkdir(parents=True, exist_ok=True)


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / name).write_text(html, encoding="utf-8")
    print(name, len(html), url[:70])
    return html


nl = fetch(
    "vrijzicht_nl.html",
    "https://www.companyweb.be/nl/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw",
)
en = fetch(
    "vrijzicht_en.html",
    "https://www.companyweb.be/en/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw",
)
fr = fetch(
    "vrijzicht_fr.html",
    "https://www.companyweb.be/fr/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw",
)
kbo = fetch(
    "vrijzicht_kbo.html",
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416337262",
)

site_html = None
for u in [
    "https://www.homevrijzicht.be/",
    "https://homevrijzicht.be/",
    "https://www.vrijzicht.be/",
    "https://www.ieper.be/",
]:
    try:
        site_html = fetch("vrijzicht_site.html", u)
        print("SITE OK", u)
        break
    except Exception as e:
        print("SITE FAIL", u, type(e).__name__, str(e)[:100])

blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    en,
)
print("BLOCKS", blocks[:3])
emp = re.search(r'Employees\s*=\s*"([^"]+)"', en)
filed = re.search(r"filed on ([0-9\-]+)", en, re.I)
print("EMP", emp.group(1) if emp else None, "FILED", filed.group(1) if filed else None)

# KBO extract
for lab in ["Adres van de zetel", "E-mail", "Aantal buitengewone", "Rechtsvorm", "Status", "Entiteitsnummer"]:
    i = kbo.find(lab)
    if i >= 0:
        snippet = re.sub(r"<[^>]+>", " ", kbo[i : i + 280])
        snippet = re.sub(r"\s+", " ", snippet).strip()
        print("KBO", snippet[:180])

emails = set()
for html in [nl, en, fr, kbo, site_html or ""]:
    for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html or ""):
        low = m.lower()
        if not any(x in low for x in ["companyweb", "sentry", "example", "w3.org", "schema"]):
            emails.add(m)
print("EMAILS", sorted(emails)[:20])

# address / title
title = re.search(r"<title>([^<]+)", en)
print("TITLE", title.group(1) if title else None)
addr = re.search(r"(\d{4})\s+Ieper", en)
print("ZIP hint", addr.group(0) if addr else None)
# street
for pat in [r"([A-Za-z\- ]+\d+[A-Za-z]?),\s*8906", r"streetAddress[^>]*>([^<]+)"]:
    m = re.search(pat, en)
    if m:
        print("ADDR", m.group(1) if m.lastindex else m.group(0))
