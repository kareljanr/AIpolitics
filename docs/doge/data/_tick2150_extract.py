# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2150")
ua = {"User-Agent": "Mozilla/5.0"}

# fix Bornem/FARO KBO digits from prior ticks
for name, url in {
    "bornem_en.html": "https://www.companyweb.be/en/0877.556.627".replace(".", ""),
    "faro_en.html": "https://www.companyweb.be/en/0474.694.877".replace(".", ""),
}.items():
    # try known from prior: Bornem BE0877556627 already failed; lookup via search in ents
    pass

# re-fetch prefs with known-good from tick2148/2149 raw
from shutil import copy
for src in [
    Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2149\bornem_en.html"),
    Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2149\faro_en.html"),
]:
    if src.exists():
        copy(src, base / src.name)
        t = (base / src.name).read_text(encoding="utf-8", errors="replace")
        years = re.findall(r"\n(202[0-9])\s*:", t)
        title = re.search(r"<title>([^<]+)", t)
        print(src.name, "copied years", years[:5], title.group(1)[:80] if title else None)
        for y in ["2025", "2024"]:
            mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
            if mm:
                print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:200])

t = (base / "vds_kbo.html").read_text(encoding="utf-8", errors="replace")
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
]:
    i = plain.lower().find(lab.lower())
    if i >= 0:
        print("KBO", lab, "->", plain[i : i + 160])

t = (base / "vds_nl.html").read_text(encoding="utf-8", errors="replace")
plain = re.sub(r"<[^>]+>", " ", t)
plain = re.sub(r"\s+", " ", plain)
print("NL hit", plain[plain.lower().find("ondernemingsnummer") : plain.lower().find("ondernemingsnummer") + 220] if "ondernemingsnummer" in plain.lower() else "no")

for name, url in {
    "vds_site.html": "https://www.zonevaldesambre.be/",
    "vds_budget_avis.html": "https://www.zonevaldesambre.be/?s=budget",
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
            "Budget",
            "Avis",
            "2026",
            "euro",
            "€",
            "Rue de la Vacherie",
            "commune",
            "Sambreville",
        ]:
            if kw.lower() in plain.lower():
                i = plain.lower().find(kw.lower())
                print(" ", kw, plain[max(0, i - 30) : i + 140])
        # find budget post links
        for m in re.finditer(r'href="([^"]*budget[^"]*)"', tt, re.I):
            print("  href", m.group(1)[:160])
    except Exception as e:
        print("FAIL", name, e)
