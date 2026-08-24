# -*- coding: utf-8 -*-
from pathlib import Path
import re
import urllib.request
import ssl
import csv

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


def nums(t):
    # companyweb embeds year objects
    for y in ["2025", "2024"]:
        block = re.search(rf"{y}\s*:\s*\{{([^}}]+)\}}", t)
        if not block:
            continue
        b = block.group(1)
        def g(k):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None
        print(y, {k: g(k) for k in ["omzet", "winst", "brutomarge", "eigenvermogen", "werknemers", "totaleactiva", "schulden"]})


for lang, url in [
    ("nl", "https://www.companyweb.be/nl/0447771695/seniorie-de-l-epinette"),
    ("en", "https://www.companyweb.be/en/0447771695/seniorie-de-l-epinette"),
    ("fr", "https://www.companyweb.be/fr/0447771695"),
]:
    t = fetch(url, out / f"epinette_{lang}_full.html")
    print("====", lang)
    nums(t)
    # emails / activity
    plain = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    plain = re.sub(r"<[^>]+>", " ", plain)
    plain = re.sub(r"\s+", " ", plain)
    print("emails", sorted(set(re.findall(r"[\w.+-]+@[\w.-]+", plain)))[:10])
    for key in ["Principal activity", "Hoofdactiviteit", "Activité principale", "Commercial name", "Commerciële", "aanbestedende", "Actief", "Active", "VE", "vestiging"]:
        i = plain.lower().find(key.lower())
        if i >= 0:
            print(key, ":", plain[max(0, i - 20) : i + 120])

# KBO detail
t = fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0447771695",
    out / "epinette_kbo_nl.html",
)
plain = re.sub(r"<[^>]+>", " ", t)
plain = re.sub(r"\s+", " ", plain)
for key in ["Status", "Actief", "Adres", "NACE", "84.", "87.", "E-mail", "Telefoon", "vestigingseenheden", "Aanbestedende", "Rechtsvorm", "Naam"]:
    i = plain.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", plain[max(0, i - 10) : i + 140])

# unused check
csv.field_size_limit(10**7)
with open(Path(r"docs/doge/data/entities.csv"), newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        b = " ".join(str(v) for v in row.values()).replace(".", "")
        if "0447771695" in b or "epinette" in b.lower():
            print("ENTITY HIT", row["entity_id"])
print("done")
