# -*- coding: utf-8 -*-
from pathlib import Path
import re

out = Path(__file__).resolve().parent
for f in sorted(out.glob("*.html")):
    t = f.read_text(encoding="utf-8", errors="ignore")
    # find balance year near keywords
    m = re.search(r"Last balance sheet year.{0,200}", t, re.I | re.S)
    m2 = re.search(r"Laatste balansjaar.{0,200}", t, re.I | re.S)
    m3 = re.search(r"Dernier bilan.{0,200}", t, re.I | re.S)
    years = re.findall(r"(20\d\d)\s*:\s*\{\s*winst", t)
    filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
    if not filed:
        filed = re.search(r"neergelegd op[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
    print("====", f.name)
    if m:
        plain = re.sub(r"<[^>]+>", " ", m.group(0))
        plain = re.sub(r"\s+", " ", plain)
        print(" EN:", plain[:160])
    if m2:
        plain = re.sub(r"<[^>]+>", " ", m2.group(0))
        plain = re.sub(r"\s+", " ", plain)
        print(" NL:", plain[:160])
    if m3:
        plain = re.sub(r"<[^>]+>", " ", m3.group(0))
        plain = re.sub(r"\s+", " ", plain)
        print(" FR:", plain[:160])
    print(" years_json", years[:6], "filed", filed.group(1) if filed else "-")
