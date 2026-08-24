# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(__file__).resolve().parent
for f in sorted(p.glob("*.html")):
    t = f.read_text(encoding="utf-8", errors="ignore")
    title = re.search(r"<title>([^<]+)</title>", t)
    year = re.search(r"Last balance sheet year[^0-9]{0,120}(20\d\d)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9]{0,120}(20\d\d)", t)
    # JSON kerncijfers often has years as keys
    years = re.findall(r'(20\d\d)\s*:\s*\{\s*winst', t)
    om = re.search(r'omzet:\s*"([^"]+)"', t)
    winst = re.search(r'winst:\s*"([^"]+)"', t)
    fte = re.search(r'werknemers:\s*"([^"]+)"', t)
    name_h = re.search(r"<h1[^>]*>([^<]+)</h1>", t)
    print(
        f.name,
        (title.group(1)[:55] if title else "?"),
        "Y",
        year.group(1) if year else (years[0] if years else "-"),
        "omzet",
        om.group(1) if om else "-",
        "winst",
        winst.group(1) if winst else "-",
        "fte",
        fte.group(1) if fte else "-",
        (name_h.group(1).strip()[:35] if name_h else ""),
    )
