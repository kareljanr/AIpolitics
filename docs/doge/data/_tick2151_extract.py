# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2151")
ua = {"User-Agent": "Mozilla/5.0"}

t = (base / "vesdre_kbo.html").read_text(encoding="utf-8", errors="replace")
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
    "Telefoon",
]:
    i = plain.lower().find(lab.lower())
    if i >= 0:
        print("KBO", lab, "->", plain[i : i + 180])

t = (base / "vesdre_nl.html").read_text(encoding="utf-8", errors="replace")
plain = re.sub(r"<[^>]+>", " ", t)
plain = re.sub(r"\s+", " ", plain)
i = plain.lower().find("ondernemingsnummer")
print("NL", plain[i : i + 240] if i >= 0 else "no")

for name, url in {
    "vesdre_site.html": "https://www.zone-vhp.be/",
    "vesdre_contact.html": "https://www.zone-vhp.be/contact/",
}.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        (base / name).write_bytes(data)
        tt = data.decode("utf-8", "replace")
        plain = re.sub(r"<[^>]+>", " ", tt)
        plain = re.sub(r"\s+", " ", plain)
        print(name, "OK", len(data))
        for kw in [
            "info@",
            "@zone",
            "commune",
            "Communes",
            "19",
            "Rue",
            "Verviers",
            "budget",
            "FTE",
            "tél",
            "Tel",
        ]:
            if kw.lower() in plain.lower():
                j = plain.lower().find(kw.lower())
                print(" ", kw, plain[max(0, j - 40) : j + 140])
        emails = set(
            re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", tt)
        )
        emails = {
            e
            for e in emails
            if not any(
                x in e.lower()
                for x in ["wix", "sentry", "google", "example", "schema", "wordpress"]
            )
        }
        if emails:
            print("  emails", emails)
    except Exception as e:
        print("FAIL", name, e)
