# ephemeral fetch tick2068 Compostela
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2068")
outdir.mkdir(parents=True, exist_ok=True)


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / name).write_text(html, encoding="utf-8")
    print(name, len(html), url[:80])
    return html


nl = fetch("compostela_nl.html", "https://www.companyweb.be/nl/0432401155/compostela")
en = fetch("compostela_en.html", "https://www.companyweb.be/en/0432401155/compostela")
fr = fetch("compostela_fr.html", "https://www.companyweb.be/fr/0432401155/compostela")
kbo = fetch(
    "compostela_kbo.html",
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0432401155",
)
site = None
for u in [
    "https://www.compostela.be/",
    "https://compostela.be/",
    "https://www.zorggroepcompostela.be/",
    "https://www.compostelazorg.be/",
]:
    try:
        site = fetch("compostela_site.html", u)
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
addr = re.search(r"streetAddress[^>]*>([^<]+)", en)
print("ADDR", addr.group(1).strip() if addr else None)
print("aanbest", "aanbestedende" in kbo.lower())
print("NACE", re.findall(r"87\.\d+|88\.\d+|86\.\d+", kbo)[:8])
for lab in ["Adres van de zetel", "Rechtsvorm", "Status", "Ondernemingsnummer"]:
    i = kbo.find(lab)
    if i >= 0:
        sn = re.sub(r"<[^>]+>", " ", kbo[i : i + 280])
        sn = re.sub(r"\s+", " ", sn).strip()
        print("KBO", sn[:180])
emails = set()
for html in [nl, en, fr, kbo, site or ""]:
    for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html or ""):
        low = m.lower()
        if not any(x in low for x in ["companyweb", "sentry", "example", "w3.org", "schema", "google", "cookie"]):
            emails.add(m)
print("EMAILS", sorted(emails)[:15])
