# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2079/vander_stokken_nl.html").read_text(
    encoding="utf-8", errors="replace"
)

# Find chart/year headers around kerncijfers
idx = t.find("bruto_marge")
print("first bruto at", idx)

# Look for year labels near financial series
for m in re.finditer(r"(20\d\d)", t[idx - 500 : idx + 2500]):
    pass

# Extract a larger window around first financial block
m = re.search(r"winst:\s*\"1\.092\.351\".{0,800}", t, re.S)
if m:
    print("AROUND FIRST WINIST:\n", m.group(0)[:800])

# Find HTML table with years
for m in re.finditer(r"<th[^>]*>\s*(20\d\d)\s*</th>", t):
    print("TH", m.group(1), "at", m.start())

# Find year chips / buttons
for m in re.finditer(r"data-year=[\"']?(20\d\d)|jaar[=\"']+(20\d\d)|Balansjaar[^\d]{0,20}(20\d\d)", t, re.I):
    print("DY", m.group(0)[:80])

# Search for percent change strings that include years
for m in re.finditer(r".{0,40}2025.{0,40}", t):
    s = m.group(0).replace("\n", " ")
    if any(k in s.lower() for k in ["winst", "omzet", "bruto", "eigen", "fte", "neerleg", "boek"]):
        print("CTX2025", s[:120])

# FTE prior year
for m in re.finditer(r"personeel[^\d]{0,40}([\d,\.]+)", t, re.I):
    print("PERS", m.group(0)[:80])
    if m.start() > 5:
        break

# Look for staff series
ms = re.findall(r"personeelsbestand[\"']?\s*:\s*[\"']?([\d,\.]+)", t, re.I)
print("personeelsbestand", ms[:10])
ms = re.findall(r"fte[\"']?\s*:\s*[\"']?([\d,\.]+)", t, re.I)
print("fte key", ms[:10])
ms = re.findall(r"amountOfEmployees\s*=\s*\"([^\"]+)\"", t)
print("amountOfEmployees", ms)

# Compare FAQ FTE vs prior
for m in re.finditer(r".{0,30}98[,.]9.{0,30}|.{0,30}97[,.]7.{0,30}|.{0,30}99[,.]6.{0,30}", t):
    print("FTECTX", m.group(0).replace("\n", " ")[:100])

# site email
site = Path("docs/doge/data/raw/tick2079/site.html").read_text(encoding="utf-8", errors="replace")
print("SITE title", re.search(r"<title>([^<]+)</title>", site).group(1)[:120] if re.search(r"<title>", site) else None)
emails = set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", site))
print("EMAILS", sorted(emails)[:20])
for m in re.finditer(r"aanbested|overheid|WZC|Pepingen|Paloken", site, re.I):
    print("SITEHIT", m.group(0), "at", m.start())
    break
print("site len", len(site))
# also check companyweb for email / website
for m in re.finditer(r"(mailto:[^\"'\s]+|https?://[^\s\"']+vander[^\s\"']*|info@[^\s\"']+)", t, re.I):
    print("CWLINK", m.group(0)[:120])
