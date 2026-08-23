import urllib.request, re, ssl, json
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2103")
RAW.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

urls = {
    "korian_nl.html": "https://www.companyweb.be/nl/0869769702/korian-belgium",
    "korian_en.html": "https://www.companyweb.be/en/0869769702/korian-belgium",
    "korian_fr.html": "https://www.companyweb.be/fr/0869769702/korian-belgium",
    "korian_kbo.html": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=869769702",
    "comnexio_en.html": "https://www.companyweb.be/en/0727639263/comnexio",
    "agb_bornem_en.html": "https://www.companyweb.be/en/0877556624/agb-bornem",
}

pat = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

for fn, url in urls.items():
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
        html = r.read().decode("utf-8", errors="ignore")
    (RAW / fn).write_text(html, encoding="utf-8")
    print(f"saved {fn} len={len(html)}")

# Parse EN deeply
html = (RAW / "korian_en.html").read_text(encoding="utf-8", errors="ignore")
euros = {
    ym.group(1): {
        "pnl": ym.group(2).replace(",", ""),
        "eq": ym.group(3).replace(",", ""),
        "bruto": ym.group(4).replace(",", ""),
        "omzet": ym.group(5).replace(",", ""),
    }
    for ym in pat.finditer(html)
}
print("EUROS", json.dumps(euros, indent=2))

# FTE patterns
for label, rgx in [
    ("fte_block", r"Average number of employees.{0,800}"),
    ("fte_nl", r"Gemiddeld aantal werknemers.{0,800}"),
    ("deposit", r"(?:Filing date|Datum van neerlegging|Date de d.{0,5}p.{0,5}t).{0,200}"),
    ("latest", r"(?:Latest balance sheet year|Laatste balansjaar|Dernier exercice).{0,120}"),
    ("nace", r"(?:NACE|Nacebel).{0,300}"),
    ("employees_table", r"Social balance.{0,1200}"),
]:
    m = re.search(rgx, html, re.I | re.S)
    if m:
        chunk = re.sub(r"<[^>]+>", " ", m.group(0))
        chunk = re.sub(r"\s+", " ", chunk).strip()[:400]
        print(f"--- {label}: {chunk}")

# Also scan for FTE year pairs in script JSON
for m in re.finditer(r'(20\d\d)[^\d]{0,40}([\d]+(?:[.,]\d+)?)\s*(?:FTE|VTE|employees)', html, re.I):
    print("FTE_PAIR", m.group(1), m.group(2))

# Look for staff in financial JSON-ish
for m in re.finditer(r'personeel[^"]{0,40}"([^"]+)"', html, re.I):
    print("PERS", m.group(0)[:120])

# KBO identity
kbo = (RAW / "korian_kbo.html").read_text(encoding="utf-8", errors="ignore")
for rgx in [
    r"Status van de entiteit.{0,200}",
    r"Juridische vorm.{0,200}",
    r"Aantal vestigingseenheden.{0,120}",
    r"Nace.{0,400}",
    r"Adres van de zetel.{0,300}",
    r"E-mailadres.{0,200}",
]:
    m = re.search(rgx, kbo, re.I | re.S)
    if m:
        chunk = re.sub(r"<[^>]+>", " | ", m.group(0))
        chunk = re.sub(r"\s+", " ", chunk).strip()[:350]
        print(f"KBO {chunk}")

# Comnexio / AGB year check
for fn in ["comnexio_en.html", "agb_bornem_en.html"]:
    t = (RAW / fn).read_text(encoding="utf-8", errors="ignore")
    euros2 = {ym.group(1): ym.groups()[1:] for ym in pat.finditer(t)}
    h1 = re.search(r"<h1[^>]*>\s*([^<]+)", t)
    title = re.sub(r"\s+", " ", h1.group(1)).strip()[:60] if h1 else "?"
    print(fn, title, "years", sorted(euros2.keys()), "e25", euros2.get("2025"), "e24", euros2.get("2024"))
