# -*- coding: utf-8 -*-
import re
from pathlib import Path

raw = Path("docs/doge/data/raw/tick2133")
for name in ["faro_en.html", "aiesh_en.html", "rew_en.html", "bornem_en.html"]:
    html = (raw / name).read_text(encoding="utf-8", errors="replace")
    m = re.search(
        r"Last balance sheet year.*?font-medium[^>]*>\s*(\d{4})", html, re.S
    )
    print(name, "year", m.group(1) if m else "?")

html = (raw / "cigb_cw_en.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r"total turnover of €([0-9,\.]+)", html)
print("turnover FAQ", m.group(1) if m else None)
m = re.search(r"filed on ([0-9-]+)", html)
print("filed", m.group(1) if m else None)
m = re.search(r'Employees = "([^"]+)"', html)
print("emp js", m.group(1) if m else None)
yrs = re.findall(r"(202[0-9])\s*:\s*\{([^}]+)\}", html)
for y, body in yrs[:8]:
    print(y, body[:240].replace("\n", " "))

kbo = (raw / "cigb_kbo.html").read_text(encoding="utf-8", errors="replace")
for label in [
    "Status",
    "Rechtsvorm",
    "Adres",
    "E-mail",
    "Activiteiten",
    "Aantal vestigingseenheden",
    "Start datum",
    "Ondernemingsnummer",
]:
    i = kbo.find(label)
    if i >= 0:
        print("KBO", label, "->", re.sub(r"\s+", " ", kbo[i : i + 260])[:260])

# NACE / activity from EN page
for label in ["Principal activity", "Commercial name", "Full name", "Company size"]:
    i = html.find(label)
    if i >= 0:
        print("EN", label, "->", re.sub(r"\s+", " ", html[i : i + 200])[:200])
