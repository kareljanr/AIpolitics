# -*- coding: utf-8 -*-
import re
from pathlib import Path

for name in [
    "sint_felix_en.html",
    "sint_felix_nl.html",
    "sint_felix_fr.html",
    "sint_felix_kbo.html",
]:
    p = Path(__file__).resolve().parent / name
    if not p.exists():
        print("MISSING", name)
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    print("===", name, "len", len(t))
    title = re.search(r"<title>([^<]+)", t)
    print("title", title.group(1)[:90] if title else "?")
    y = (
        re.search(r"Last balance sheet year[^0-9]{0,120}(20\d\d)", t)
        or re.search(r"Laatste balansjaar[^0-9]{0,120}(20\d\d)", t)
        or re.search(r"Dernier bilan[^0-9]{0,120}(20\d\d)", t)
    )
    print("year", y.group(1) if y else "-")
    for key in ["omzet", "winst", "eigen_vermogen", "bruto_marge", "werknemers"]:
        m = re.search(key + r':\s*"([^"]+)"', t)
        print(key, m.group(1) if m else "-")
    # years block
    block = re.search(r"2025\s*:\s*\{([^}]+)\}", t)
    if block:
        print("2025block", block.group(1)[:200])
    nums = re.findall(r"€\s*([0-9][0-9.\s,]*)", t)
    print("euros", nums[:15])
    # filed date
    filed = re.search(r"filed on ([0-9\-]+)", t, re.I) or re.search(
        r"neergelegd op ([0-9\-]+)", t, re.I
    )
    print("filed", filed.group(1) if filed else "-")
