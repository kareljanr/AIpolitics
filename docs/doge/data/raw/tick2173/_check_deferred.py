# -*- coding: utf-8 -*-
import re
from pathlib import Path

prior = Path("docs/doge/data/raw/tick2172")
names = [
    "hof_ter_lande_0480566704_en.html",
    "stil_geluk_0443249616_en.html",
    "wzn_edegem_0685516024_en.html",
    "haagwinde_0410219433_en.html",
    "ocura_0428471856_en.html",
    "meander_0405443129_en.html",
    "zoetenaard_0428335615_en.html",
    "dhondt_0406877485_en.html",
    "helianthus_0466266429_en.html",
    "bethanie_0808910714_en.html",
    "seigneurie_0883694744_en.html",
    "passerinette_0539934860_en.html",
    "ry_chevreuil_0507866165_en.html",
    "le_progres_0808928827_en.html",
    "wsr_0441675147_en.html",
    "hoeksteen_0598966387_en.html",
    "hop_0883790853_en.html",
    "man_in_motion_0880226993_en.html",
    "ben_woonzorg_0416493254_en.html",
]


def parse(t):
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed = re.search(r"filed on ([0-9-]{10})", t or "")
    title = re.search(r"<title>([^<]+)", t or "")
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", t or "", re.I)
    return yb, fte, filed, title, last


for name in names:
    p = prior / name
    if not p.exists():
        print("MISS", name)
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    if "Error 404" in t:
        print("404", name)
        continue
    yb, fte, filed, title, last = parse(t)
    print(
        name.split("_en")[0],
        (title.group(1) if title else "")[:55],
        "last",
        last.group(1) if last else None,
        "filed",
        filed.group(1) if filed else None,
        "fte",
        fte.group(1) if fte else None,
    )
    print("  2025", yb.get("2025"))
    print("  2024", yb.get("2024"))
