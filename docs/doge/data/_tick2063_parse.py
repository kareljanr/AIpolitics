# ephemeral parse tick2063 Sint-Antonius raw
import csv
import re
from pathlib import Path

csv.field_size_limit(10**7)
outdir = Path("docs/doge/data/raw/tick2063")
en = (outdir / "antonius_en.html").read_text(encoding="utf-8", errors="replace")
nl = (outdir / "antonius_nl.html").read_text(encoding="utf-8", errors="replace")
fr = (outdir / "antonius_fr.html").read_text(encoding="utf-8", errors="replace")
kbo = (outdir / "antonius_kbo.html").read_text(encoding="utf-8", errors="replace")
site = ""
if (outdir / "antonius_site.html").exists():
    site = (outdir / "antonius_site.html").read_text(encoding="utf-8", errors="replace")


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                return m.group(1)
    return None


blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    en,
)
print("Y", year_of(en))
print("BLOCKS", blocks[:3])
emp = re.search(r'Employees\s*=\s*"([^"]+)"', en)
filed = re.search(r"filed on ([0-9\-]+)", en, re.I)
print("EMP", emp.group(1) if emp else None, "FILED", filed.group(1) if filed else None)
title = re.search(r"<title>([^<]+)", en)
print("TITLE", title.group(1) if title else None)
addr = re.search(r"streetAddress[^>]*>([^<]+)", en)
print("ADDR", addr.group(1).strip() if addr else None)
print("aanbest", "aanbestedende" in kbo.lower())
print("NACE", re.findall(r"87\.\d+", kbo)[:6])
for lab in ["Adres van de zetel", "Rechtsvorm", "Status", "Ondernemingsnummer"]:
    i = kbo.find(lab)
    if i >= 0:
        sn = re.sub(r"<[^>]+>", " ", kbo[i : i + 280])
        sn = re.sub(r"\s+", " ", sn).strip()
        print("KBO", sn[:180])
emails = set()
for html in [nl, en, fr, kbo, site]:
    for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html or ""):
        low = m.lower()
        if not any(
            x in low
            for x in ["companyweb", "sentry", "example", "w3.org", "schema", "google", "cookie"]
        ):
            emails.add(m)
print("EMAILS", sorted(emails)[:20])

with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    ents = list(csv.DictReader(f))
for n in ["sint_antonius", "0424236725", "antonius", "vzw_wzc_sint"]:
    hits = [
        e.get("entity_id")
        for e in ents
        if n in ((e.get("entity_id") or "") + (e.get("notes") or "")).lower()
    ]
    print("ENT", n, hits[:5])

if (outdir / "faro_en.html").exists():
    print("FARO Y", year_of((outdir / "faro_en.html").read_text(encoding="utf-8", errors="replace")))
