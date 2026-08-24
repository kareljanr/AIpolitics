# -*- coding: utf-8 -*-
from pathlib import Path
import re

html = Path(r"docs/doge/data/raw/tick2136/corolles_cw_en.html").read_text(
    encoding="utf-8", errors="replace"
)
# year blocks
for year in ("2025", "2024", "2023"):
    m = re.search(rf"{year}\s*:\{{([^}}]+)\}}", html)
    if m:
        print(f"=== {year} ===")
        print(m.group(1).strip())

# key window.cw fields
for key in (
    "amountOfEmployees",
    "enterpriseNumber",
    "companyName",
    "lastBalanceSheetYear",
    "vatNumber",
):
    m = re.search(rf'window\.cw\.{key}\s*=\s*"([^"]*)"', html)
    if m:
        print(f"{key}={m.group(1)}")

# filing dates near FAQ
for m in re.finditer(r"filed on ([0-9-]{10})", html):
    print("filed", m.group(1))
for m in re.finditer(r">\s*([0-9]{2}-[0-9]{2}-[0-9]{4})\s*<", html):
    pass
# dates near neerlegging section - print lines with dd-mm-yyyy near financial statements
for i, line in enumerate(html.splitlines()):
    if re.search(r"\d{2}-\d{2}-20\d{2}", line) and (
        "2025" in line or "2024" in line or "filed" in line.lower() or "neerleg" in line.lower()
    ):
        if len(line.strip()) < 80:
            print(f"L{i}:{line.strip()}")

# address / nace from meta
for pat in [
    r'"street"[^"]*"([^"]+)"',
    r"Chauss[ée]e de Renaix[^<]{0,40}",
    r"Principal activity[^<]{0,80}",
    r"NACE[^<]{0,100}",
    r"Active[^<]{0,40}",
]:
    m = re.search(pat, html, re.I)
    if m:
        print("HIT", m.group(0)[:120])
