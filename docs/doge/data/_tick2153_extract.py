# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2153")
ua = {"User-Agent": "Mozilla/5.0"}
digits = "0500915423"

for name, url in {
    "bw_nl.html": f"https://www.companyweb.be/nl/{digits}",
    "bw_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        f"?lang=nl&ondernemingsnummer={digits}"
    ),
    "bw_site.html": "https://brabant-wallon.secourspompiers.be/",
}.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        (base / name).write_bytes(data)
        print(name, "OK", len(data))
    except Exception as e:
        print("FAIL", name, e)

t = (base / "bw_kbo.html").read_text(encoding="utf-8", errors="replace")
plain = re.sub(r"<[^>]+>", " ", t)
plain = re.sub(r"\s+", " ", plain)
for lab in [
    "Status",
    "Adres van de zetel",
    "Rechtsvorm",
    "Aantal vestiging",
    "Ondernemingsnummer",
    "Hulpverleningszone",
    "84.250",
    "aanbestedende",
    "Actief",
    "LA ZONE",
    "E-mail",
    "Telefoon",
]:
    i = plain.lower().find(lab.lower())
    if i >= 0:
        print("KBO", lab, "->", plain[i : i + 180])

t = (base / "bw_nl.html").read_text(encoding="utf-8", errors="replace")
plain = re.sub(r"<[^>]+>", " ", t)
plain = re.sub(r"\s+", " ", plain)
i = plain.lower().find("ondernemingsnummer")
print("NL", plain[i : i + 240] if i >= 0 else "no")
fte = re.search(r'Employees\s*=\s*"([^"]+)"', t)
print("fte", fte.group(1) if fte else None)

if (base / "bw_site.html").exists():
    tt = (base / "bw_site.html").read_text(encoding="utf-8", errors="replace")
    plain = re.sub(r"<[^>]+>", " ", tt)
    plain = re.sub(r"\s+", " ", plain)
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", tt))
    emails = {
        e
        for e in emails
        if not any(
            x in e.lower()
            for x in ["wix", "sentry", "google", "example", "schema", "wordpress"]
        )
    }
    print("emails", emails)
    for kw in ["27", "commune", "Wavre", "budget", "Place du Brabant"]:
        if kw.lower() in plain.lower():
            j = plain.lower().find(kw.lower())
            print(kw, plain[max(0, j - 30) : j + 120])
