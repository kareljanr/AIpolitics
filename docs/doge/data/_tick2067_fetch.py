# ephemeral fetch tick2067 Leiehome
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2067")
outdir.mkdir(parents=True, exist_ok=True)


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / name).write_text(html, encoding="utf-8")
    print(name, len(html), url[:80])
    return html


nl = fetch("leiehome_nl.html", "https://www.companyweb.be/nl/0410556557/leiehome")
en = fetch("leiehome_en.html", "https://www.companyweb.be/en/0410556557/leiehome")
fr = fetch("leiehome_fr.html", "https://www.companyweb.be/fr/0410556557/leiehome")
kbo = fetch(
    "leiehome_kbo.html",
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410556557",
)
site = None
for u in ["https://www.leiehome.be/", "https://leiehome.be/"]:
    try:
        site = fetch("leiehome_site.html", u)
        print("SITE OK", u)
        break
    except Exception as e:
        print("SITE FAIL", u, type(e).__name__, str(e)[:80])

blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    en,
)
print("BLOCKS", blocks[:3])
emp = re.search(r'Employees\s*=\s*"([^"]+)"', en)
filed = re.search(r"filed on ([0-9\-]+)", en, re.I)
print("EMP", emp.group(1) if emp else None, "FILED", filed.group(1) if filed else None)
print("TITLE", (re.search(r"<title>([^<]+)", en) or type("x", (), {"group": lambda *a: None})()).group(1))
addr = re.search(r"streetAddress[^>]*>([^<]+)", en)
print("ADDR", addr.group(1).strip() if addr else None)
print("aanbest", "aanbestedende" in kbo.lower())
print("NACE", re.findall(r"87\.\d+", kbo)[:4])
for lab in ["Adres van de zetel", "Rechtsvorm", "Status"]:
    i = kbo.find(lab)
    if i >= 0:
        sn = re.sub(r"<[^>]+>", " ", kbo[i : i + 260])
        sn = re.sub(r"\s+", " ", sn).strip()
        print("KBO", sn[:170])
emails = set()
for html in [nl, en, fr, kbo, site or ""]:
    for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html or ""):
        low = m.lower()
        if not any(x in low for x in ["companyweb", "sentry", "example", "w3.org", "schema", "google", "cookie"]):
            emails.add(m)
print("EMAILS", sorted(emails)[:10])
