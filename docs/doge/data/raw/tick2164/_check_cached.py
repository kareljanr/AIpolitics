# -*- coding: utf-8 -*-
from pathlib import Path
import re

raw = Path(__file__).resolve().parent
for name in [
    "faro_en.html",
    "aiesh_en.html",
    "rew_en.html",
    "oudenburg_en.html",
    "residentie_oudenburg_en.html",
    "mbn_en.html",
    "sja_en.html",
    "hof_en.html",
    "lorkh_en.html",
    "wzc_de_meers_en.html",
    "wzc_de_wingerd_en.html",
    "wzc_zonnige_ruste_en.html",
    "thofke_en.html",
    "huis_ter_meulen_en.html",
    "le_hanois_check_en.html",
    "bernardus_check_en.html",
    "ruggeveld_check_en.html",
    "home_vrijzicht_ieper_en.html",
    "sint_anna_brugge_en.html",
    "sint_jozef_aarschot_en.html",
    "olvf_kortrijk_en.html",
    "residentie_sonneweelde_en.html",
    "rusthuis_ter_veste_en.html",
]:
    p = raw / name
    if not p.exists():
        print(name, "MISSING")
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year.{0,80}", t, re.S | re.I)
    plain = re.sub(r"<[^>]+>", " ", year.group(0)) if year else ""
    print("==", name, "==")
    print("title", (title.group(1)[:90] if title else "?"))
    print("YEAR", re.sub(r"\s+", " ", plain)[:100])
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t)[:2]:

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        print(
            y,
            {
                k: g(k)
                for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
            },
        )
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    print("fte", fte.group(1) if fte else "-")
