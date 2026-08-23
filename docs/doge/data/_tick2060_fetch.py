# ephemeral fetch tick2060 Woonzorgcentrum Christine
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2060")
outdir.mkdir(parents=True, exist_ok=True)


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / name).write_text(html, encoding="utf-8")
    print(name, len(html), url[:80])
    return html


# also recheck stalls
for name, url in [
    ("faro_en.html", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_en.html", "https://www.companyweb.be/en/0201712587/aiesh"),
    ("rew_en.html", "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre"),
    ("agb_bornem_en.html", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
]:
    try:
        html = fetch(name, url)
        y = None
        for lab in ["Last balance sheet year", "Laatste balansjaar"]:
            i = html.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if m:
                    y = m.group(1)
        print("YEAR", name, y)
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:120])

nl = fetch(
    "christine_nl.html",
    "https://www.companyweb.be/nl/0421903676/woonzorgcentrum-christine",
)
en = fetch(
    "christine_en.html",
    "https://www.companyweb.be/en/0421903676/woonzorgcentrum-christine",
)
fr = fetch(
    "christine_fr.html",
    "https://www.companyweb.be/fr/0421903676/woonzorgcentrum-christine",
)
kbo = fetch(
    "christine_kbo.html",
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421903676",
)

site_html = None
for u in [
    "https://www.woonzorgcentrumchristine.be/",
    "https://woonzorgcentrumchristine.be/",
    "https://www.christine.be/",
    "https://www.wzcchristine.be/",
]:
    try:
        site_html = fetch("christine_site.html", u)
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
title = re.search(r"<title>([^<]+)", en)
print("TITLE", title.group(1) if title else None)

for lab in ["Adres van de zetel", "E-mail", "Rechtsvorm", "Status", "Ondernemingsnummer", "NACE"]:
    i = kbo.find(lab)
    if i >= 0:
        sn = re.sub(r"<[^>]+>", " ", kbo[i : i + 320])
        sn = re.sub(r"\s+", " ", sn).strip()
        print("KBO", sn[:200])

emails = set()
for html in [nl, en, fr, kbo, site_html or ""]:
    for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html or ""):
        low = m.lower()
        if not any(x in low for x in ["companyweb", "sentry", "example", "w3.org", "schema", "google", "cookie"]):
            emails.add(m)
print("EMAILS", sorted(emails)[:20])
