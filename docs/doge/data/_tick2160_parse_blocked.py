from pathlib import Path
import re

raws = [
    Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2159"),
    Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2158"),
]
for folder in raws:
    for name in ["faro_en.html", "faro_nl.html", "aiesh_en.html", "rew_en.html", "de_linde_en.html"]:
        p = folder / name
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(\d{4})", t)
        if not m:
            m = re.search(r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*(\d{4})", t)
        print(folder.name, name, "balance=", m.group(1) if m else "?")
        # chart data years
        years = re.findall(r"<span>(20\d{2})</span>", t)
        print("  year spans", years[:8])
        # filed date
        filed = re.search(r"most recent financial statements.*?filed on ([0-9\-]+)", t, re.I | re.S)
        if filed:
            print("  filed", filed.group(1))
        omz = re.findall(r'omzet:\s*"([0-9,\.]+)"', t)
        print("  omzet", omz[:5])
