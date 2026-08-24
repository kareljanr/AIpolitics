# -*- coding: utf-8 -*-
import re
from pathlib import Path

k = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218\kbo.html").read_text(
    encoding="utf-8", errors="ignore"
)
# keep some structure
for pat in [
    r"Status van de entiteit</[^>]+>\s*<[^>]+>([^<]+)",
    r"Actief|Stopgezet|Afgesloten",
    r"Bruggestraat[^<]{0,80}",
    r"Yv\.?\s*Serruys[^<]{0,80}",
    r"Nace[^<]{0,200}",
    r"88\.\d{3}",
    r"39\.\d{3}",
    r"43\.\d{3}",
    r"81\.\d{3}",
    r"BTW|RSZ",
    r"28\s*februari\s*1994",
    r"9\s*juni\s*2026",
]:
    ms = re.findall(pat, k, re.I)
    if ms:
        print(pat[:50], "->", ms[:8])

tn = Path(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218\veerkracht4_nl.html"
).read_text(encoding="utf-8", errors="ignore")
# activity / nace blocks
for m in re.finditer(r"(NACE|Activiteit|activiteit).{0,300}", tn, re.I | re.S):
    s = re.sub(r"\s+", " ", m.group(0))
    if any(x in s for x in ["88", "39", "43", "81", "maatwerk", "groen", "bouw"]):
        print("NL act", s[:220])

# phone from site
s = Path(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218\site_contact.html"
).read_text(encoding="utf-8", errors="ignore")
print("phones", re.findall(r"0\d[\d\s/\.]{6,16}\d", s)[:10])
print("addr site", re.findall(r"Serruysstraat[^<]{0,60}|Bruggestraat[^<]{0,60}", s)[:10])

# FR filing
tf = Path(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218\veerkracht4_fr.html"
).read_text(encoding="utf-8", errors="ignore")
print("FR filed", re.search(r"d[eé]pos[ée]s? le ([0-9\-]+)", tf, re.I))
print(
    "FR blocks",
    re.findall(
        r"(20(?:24|25))\s*:\s*\{\s*winst:\s*\"([^\"]+)\".*?bruto_marge:\s*\"([^\"]+)\".*?omzet:\s*\"([^\"]*)\"",
        tf,
        re.S,
    ),
)
