import re
import json
import html as H
from pathlib import Path

p = Path("docs/doge/data/raw/tick2185")
raw = (p / "weerwerk_en.html").read_text(encoding="utf-8")

# Find JSON-ish numeric series / KPI blocks
for pat in [
    r"Turnover[^<]{0,200}",
    r"Profit[^<]{0,200}",
    r"Employees[^<]{0,200}",
    r"Gross margin[^<]{0,200}",
    r"Equity[^<]{0,200}",
    r"filed[^<]{0,120}",
    r"Filing[^<]{0,120}",
    r"Last balance[^<]{0,120}",
    r"neerlegging[^<]{0,120}",
    r"26-0[0-9]-2026[^<]{0,80}",
    r"05-0[0-9]-2026[^<]{0,80}",
]:
    ms = re.findall(pat, raw, re.I)
    if ms:
        print("PAT", pat)
        for m in ms[:4]:
            print(" ", re.sub(r"\s+", " ", m)[:220])

# Look for data attributes / chart series
series = re.findall(r"data-series=\"([^\"]+)\"", raw)
print("series attrs", len(series))
for s in series[:10]:
    print(H.unescape(s)[:200])

# Search for profit/loss numbers near 197
text = H.unescape(re.sub(r"<[^>]+>", " ", raw))
text = re.sub(r"\s+", " ", text)
for key in ["Profit", "Loss", "197", "Net result", "Result of the financial year", "Earnings"]:
    i = 0
    c = 0
    low = text.lower()
    while c < 5:
        j = low.find(key.lower(), i)
        if j < 0:
            break
        print("CTX", key, ":", text[max(0, j - 40) : j + 160])
        i = j + len(key)
        c += 1

# FR page often has clearer narrative
raw_fr = (p / "weerwerk_fr.html").read_text(encoding="utf-8")
text_fr = H.unescape(re.sub(r"<[^>]+>", " ", raw_fr))
text_fr = re.sub(r"\s+", " ", text_fr)
for key in [
    "Bénéfice",
    "Perte",
    "résultat",
    "197",
    "dépôt",
    "Dernier bilan",
    "Marge brute",
    "effectif",
]:
    i = 0
    c = 0
    low = text_fr.lower()
    while c < 4:
        j = low.find(key.lower(), i)
        if j < 0:
            break
        print("FR", key, ":", text_fr[max(0, j - 30) : j + 160])
        i = j + len(key)
        c += 1

# NL narrative Q&A
raw_nl = (p / "weerwerk_nl.html").read_text(encoding="utf-8")
text_nl = H.unescape(re.sub(r"<[^>]+>", " ", raw_nl))
text_nl = re.sub(r"\s+", " ", text_nl)
for key in [
    "winst",
    "verlies",
    "omzet",
    "neerlegging",
    "brutomarge",
    "197",
    "FTE",
    "laatste",
]:
    i = 0
    c = 0
    low = text_nl.lower()
    while c < 5:
        j = low.find(key.lower(), i)
        if j < 0:
            break
        print("NL", key, ":", text_nl[max(0, j - 30) : j + 180])
        i = j + len(key)
        c += 1

# KBO VE count + juridische vorm
kbo = (p / "weerwerk_kbo.html").read_text(encoding="utf-8")
kbo_t = H.unescape(re.sub(r"<[^>]+>", " ", kbo))
kbo_t = re.sub(r"\s+", " ", kbo_t)
for key in [
    "Juridische vorm",
    "Aantal vestigingen",
    "Vestigingseenhe",
    "Status",
    "Maatschappelijke zetel",
    "Functies",
    "Bestuurder",
    "RSZ",
    "88.993",
    "88.999",
    "Gaardeniersweg",
]:
    j = kbo_t.lower().find(key.lower())
    if j >= 0:
        print("KBO", key, ":", kbo_t[j : j + 220])
