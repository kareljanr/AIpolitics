# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2259\erables_en.html").read_text(
    encoding="utf-8", errors="replace"
)
tn = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2259\erables_nl.html").read_text(
    encoding="utf-8", errors="replace"
)

for key in [
    "bruto",
    "gross",
    "equity",
    "eigen",
    "marge",
    "personnel",
    "fte",
    "balans",
    "asset",
    "debt",
    "schuld",
    "cash",
    "liquid",
    "filed",
    "neerleg",
]:
    print(key, len(re.findall(key, t, re.I)))

# JSON-like assignments
for m in re.finditer(
    r"(brutomarge|eigenVermogen|fte|omzet|winst|balanstotaal|schulden|liquiditeiten|omzetGroei|winstGroei|brutomargeGroei|eigenVermogenGroei|fteGroei)\s*[:=]\s*\"([^\"]+)\"",
    t,
):
    print("KV", m.group(1), m.group(2))

# repeated values arrays in scripts
for m in re.finditer(
    r"(brutomarge|eigenVermogen|fte|omzet|winst)\s*:\s*\[([^\]]{0,400})\]",
    t,
):
    print("ARR", m.group(1), m.group(2)[:300])

# Highcharts-like
for m in re.finditer(r"name\s*:\s*'([^']+)'\s*,\s*data\s*:\s*\[([^\]]+)\]", t):
    print("SERIES", m.group(1), m.group(2)[:250])

# FAQ
for label, html in (("EN", t), ("NL", tn)):
    m = re.search(r"Frequently asked questions[\s\S]{0,5000}|Veelgestelde vragen[\s\S]{0,5000}", html, re.I)
    if m:
        chunk = re.sub(r"<[^>]+>", " ", m.group(0))
        chunk = re.sub(r"\s+", " ", chunk)
        print("FAQ", label, chunk[:2000])

# financial table rows: look for 2025 near euro amounts in DOM
# sample windows around '2025'
idxs = [m.start() for m in re.finditer(r">2025<", t)]
print("2025 idxs", len(idxs))
for i in idxs[:3]:
    chunk = re.sub(r"<[^>]+>", " ", t[max(0, i - 200) : i + 800])
    chunk = re.sub(r"\s+", " ", chunk)
    print("WIN", chunk[:500])

# look for percent growth strings
for m in re.finditer(r"([+-]?\d[\d,]*)\s*%", t):
    pass
pcts = re.findall(r"(-?\d[\d\.]*)\s*%", t)
print("sample pcts", pcts[:30])

# NL growth labels
for pat in [
    r"brutomarge[^|]{0,80}",
    r"eigen vermogen[^|]{0,80}",
    r"Gross margin[^|]{0,120}",
    r"Equity[^|]{0,120}",
    r"Employees[^|]{0,120}",
    r"Profit/Loss[^|]{0,200}",
]:
    ms = re.findall(pat, t, re.I)
    if ms:
        print("PAT", pat[:30], [re.sub(r"\s+", " ", x)[:120] for x in ms[:3]])
