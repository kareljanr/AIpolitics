# -*- coding: utf-8 -*-
from pathlib import Path
import re

files = [
    "wzn_edegem_0685516024_en.html",
    "hof_ter_lande_0480566704_en.html",
    "stil_geluk_0443249616_en.html",
    "de_hoeksteen_0598966387_en.html",
    "abdij_affligem_0400371161_en.html",
    "melis_home_0787300696_en.html",
    "oudenburg_0450755634_en.html",
    "haagwinde_skip",
]
raw = Path("docs/doge/data/raw/tick2170")
for fn in files:
    p = raw / fn if not fn.endswith("skip") else raw / "cand_0410_0410219433_en.html"
    if not p.exists():
        print("MISSING", fn)
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", t, re.I)
    title = re.search(r"<title>([^<]+)", t)
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(k + r':\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    act = re.search(r"Principal activity</[^>]+>\s*([^<]+)", t, re.I)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    fte = re.search(r"([\d.,]+)\s*FTE", t)
    print(p.name)
    print(" ", (title.group(1) if title else "")[:70])
    print(
        "  last",
        last.group(1) if last else None,
        "act",
        (act.group(1).strip() if act else "")[:55],
        "fte",
        fte.group(1) if fte else None,
        "filed",
        filed.group(1) if filed else None,
    )
    print("  2025", yb.get("2025"))
    print("  2024", yb.get("2024"))
