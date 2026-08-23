# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2087/lindelo_nl.html").read_text(encoding="utf-8", errors="replace")
te = Path("docs/doge/data/raw/tick2087/lindelo_en.html").read_text(encoding="utf-8", errors="replace")
print("Employees global", re.search(r'Employees\s*=\s*"([^"]+)"', t).group(1))

idx = t.find("Personeel")
chunk = t[idx : idx + 5000]
print("--- Personeel chunk ---")
print(re.sub(r"\s+", " ", chunk)[:1800])
print("---")
ms = re.findall(r"<td[^>]*>\s*([0-9]+[.,][0-9]+)\s*</td>", chunk)
print("td nums", ms[:30])

# year headers near personnel
years = re.findall(r">\s*(20\d\d)\s*<", chunk)
print("years near", years[:20])

# FAQ answer about employees
for m in re.finditer(r"FTE[^.]{0,120}", t):
    s = re.sub(r"\s+", " ", m.group(0))
    if any(ch.isdigit() for ch in s):
        print("FTE faq", s[:160])

# EN staff section
idxe = te.lower().find("staff")
print("--- EN staff ---")
print(re.sub(r"\s+", " ", te[idxe : idxe + 2000])[:1200])

# try to find series in JS
for pat in [
    r"personeel[^;]{0,200}",
    r"employeesByYear\s*=\s*(\{.*?\});",
    r"fteByYear\s*=\s*(\{.*?\});",
    r"socialBalanceFigures\s*=\s*(\{.*?\});",
]:
    m = re.search(pat, t, re.I | re.S)
    if m:
        print("HIT", pat, re.sub(r"\s+", " ", m.group(0))[:240])

# KBO nace all
tk = Path("docs/doge/data/raw/tick2087/kbo_lindelo.html").read_text(encoding="utf-8", errors="replace")
print("--- NACE rows ---")
for m in re.finditer(r"(\d{2}\.\d{3})\s*[\s\S]{0,80}", tk):
    print(re.sub(r"<[^>]+>", " ", m.group(0))[:120])
# names
for m in re.finditer(r"(Maatschappelijke|Afgekorte|Benaming)[\s\S]{0,200}", tk):
    print(re.sub(r"<[^>]+>", " | ", m.group(0))[:200])
