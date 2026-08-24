# -*- coding: utf-8 -*-
import re
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2254")


def grab(t, *pats):
    for p in pats:
        m = re.search(p, t, re.S | re.I)
        if m:
            return re.sub(r"\s+", " ", m.group(0))[:400]
    return None


for lang in ["en", "nl", "fr"]:
    t = (OUT / f"erables_{lang}.html").read_text(encoding="utf-8", errors="replace")
    print("====", lang)
    for key in [
        "omzet",
        "brutomarge",
        "winst",
        "eigenVermogen",
        "fte",
        "turnover",
        "gross margin",
        "equity",
        "Profit",
        "Marge brute",
        "Capitaux",
        "Chiffre",
        "Bénéfice",
    ]:
        # json-ish pairs
        ms = re.findall(rf'{key}[^"]{{0,20}}"\s*:\s*"([^"]+)"', t, re.I)
        if ms:
            print(key, ms[:6])
    # chart series arrays near labels
    for label in ["omzet", "brutomarge", "winst", "eigenVermogen", "fte"]:
        m = re.search(rf'{label}\s*:\s*"([^"]+)"', t)
        if m:
            print("single", label, m.group(1))
    print("size", grab(t, r"Company size.{0,80}", r"Bedrijfsgrootte.{0,80}", r"Taille d.entreprise.{0,80}"))
    print("name", grab(t, r"Commercial name.{0,100}", r"Handelsnaam.{0,100}", r"Nom commercial.{0,100}"))
    print("activity", grab(t, r"Principal activity.{0,120}", r"Hoofdactiviteit.{0,120}", r"Activité principale.{0,120}"))
    print("address", grab(t, r"Rue Du Bois[^<\n]{0,60}", r"7522[^<\n]{0,40}"))
    print("filed", grab(t, r"filed on [0-9-]+", r"neergelegd op [0-9.-]+", r"déposés le [0-9-]+"))

# KBO details
t = (OUT / "erables_kbo.html").read_text(encoding="utf-8", errors="replace")
print("==== KBO")
# strip tags lightly
text = re.sub(r"<script[\s\S]*?</script>", " ", t)
text = re.sub(r"<style[\s\S]*?</style>", " ", text)
text = re.sub(r"<[^>]+>", " | ", text)
text = re.sub(r"\s+", " ", text)
for needle in [
    "Status",
    "Rechtsvorm",
    "Maatschappelijke naam",
    "Adres",
    "Aantal",
    "NACE",
    "E-mail",
    "Web",
    "Begin",
    "Entreprisenummer",
    "Ondernemingsnummer",
    "vestiging",
]:
    idx = text.lower().find(needle.lower())
    if idx >= 0:
        print(needle, ":", text[idx : idx + 180])

# also look for number of establishments in EN page
t = (OUT / "erables_en.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Number of establishments.{0,80}",
    r"(\d+)\s*establishment",
    r"Establishments.{0,100}",
    r"brutomarge.{0,80}",
    r"Gross margin.{0,200}",
    r"Equity.{0,200}",
]:
    m = re.search(pat, t, re.S | re.I)
    if m:
        print("EN", re.sub(r"\s+", " ", m.group(0))[:220])

# Extract chart data blocks more carefully from EN
# Companyweb often embeds: years: [2025,2024,...] and series
years = re.findall(r"\b(202[0-9])\b", t)
print("year sample", years[:20])

# Find JSON-like financial table values adjacent
block = re.search(r"Financial data from.{0,5000}", t, re.S)
if block:
    b = re.sub(r"<[^>]+>", " ", block.group(0))
    b = re.sub(r"\s+", " ", b)
    print("FINBLOCK", b[:800])
