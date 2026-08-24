# -*- coding: utf-8 -*-
import re
from pathlib import Path
from html import unescape
t=Path("docs/doge/data/raw/tick2168/sint_lodewijk_kbo.html").read_text(encoding="utf-8",errors="replace")
t=unescape(t)
# extract table rows
rows=re.findall(r"<tr[^>]*>([\s\S]*?)</tr>", t, re.I)
for row in rows:
    cells=[re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",c)).strip() for c in re.findall(r"<t[dh][^>]*>([\s\S]*?)</t[dh]>", row, re.I)]
    cells=[c for c in cells if c]
    if not cells: continue
    blob=" | ".join(cells)
    if any(k in blob.lower() for k in ["adres","straat","telefoon","mail","web","vestiging","nace","87.","actief","juridische","begindatum","schilde","lodewijk","aanbested"]):
        print(blob[:200])
# also check entity functions / establishment
ests=re.findall(r"vestigingseenheid[\s\S]{0,400}", t, re.I)
print("est chunks", len(ests))
# try CW for address
en=Path("docs/doge/data/raw/tick2168/sint_lodewijk_en.html").read_text(encoding="utf-8",errors="replace")
for pat in [r"street['\"]?\s*[:=]\s*['\"]([^'\"]+)", r"address['\"]?\s*[:=]\s*['\"]([^'\"]+)", r"Schilde[^<\n]{0,40}", r"2970[^<\n]{0,60}", r"0\d/\d{2,3}\.\d{2}\.\d{2}", r"info@[a-z0-9.-]+", r"www\.[a-z0-9.-]+"]:
    ms=re.findall(pat, en, re.I)
    if ms: print(pat, ms[:5])
# gsearch for contact
g=Path("docs/doge/data/raw/tick2168/gsearch.html").read_text(encoding="utf-8",errors="replace")
for m in re.findall(r"(?:\+32|0)\d[\d\s./-]{7,}|(?:info|contact|secretariaat)@[a-z0-9.-]+\.[a-z]{2,}|sint[- ]?lodewijk[^\s\"']{0,40}", g, re.I):
    if "0098" in m: continue
    print("g", m[:80])
