# ephemeral tick2017 — fetch AZ Rivierenland NL/FR + KBO + site
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2017")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, len(data), url)
        return data
    except Exception as e:
        print("FAIL", name, e, url)
        return None


targets = [
    ("az_rivierenland_nl", "https://www.companyweb.be/nl/0416851659/az-rivierenland"),
    ("az_rivierenland_fr", "https://www.companyweb.be/fr/0416851659"),
    ("az_rivierenland_en2", "https://www.companyweb.be/en/0416851659/az-rivierenland"),
    (
        "kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416851659",
    ),
    ("site", "https://www.azrivierenland.be/"),
]

for name, url in targets:
    fetch(name, url)

# quick extract emails / VE from kbo + site
for name in ["kbo", "site", "az_rivierenland_nl", "az_rivierenland_en2"]:
    p = dst / f"{name}.html"
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)))
    print("emails", name, emails[:12])
    for lab in [
        "Status van de entiteit",
        "Actief",
        "Juridische vorm",
        "Aantal vestigingseenheden",
        "Start van de rechtspersoon",
        "Adres van de zetel",
        "neergelegd op",
        "Laatste balansjaar",
        "filed on",
        "Last balance sheet year",
    ]:
        i = t.find(lab)
        if i >= 0:
            print(name, lab, repr(t[i : i + 200].replace("\n", " ")[:180]))
