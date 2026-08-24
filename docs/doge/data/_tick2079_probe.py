# -*- coding: utf-8 -*-
import re
from pathlib import Path

raw = Path("docs/doge/data/raw/tick2079")


def extract_cw(path: Path) -> None:
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", path.name, "len", len(t))
    m = re.search(r"<title>([^<]+)</title>", t)
    if m:
        print("TITLE", m.group(1)[:160])
    for m in re.finditer(r"0\d{3}\.\d{3}\.\d{3}", t):
        print("KBO", m.group(0))
        break
    for m in re.finditer(
        r"neergelegd op ([0-9\-]+)|filed on ([0-9\-]+)|Balansjaar[^<\n]{0,80}|boekjaar 20\d\d|most recent financial statements",
        t,
        re.I,
    ):
        print("FILING/YEAR", m.group(0)[:140])
    blocks = re.findall(r"\{[^{}]*bruto_marge[^{}]*\}", t)
    print("blocks", len(blocks))
    for b in blocks[:12]:
        print(" ", b[:350])
    # year arrays near chart
    for pat in [
        r"categories\s*:\s*\[([^\]]+)\]",
        r"labels\s*:\s*\[([^\]]+)\]",
        r"years\s*:\s*\[([^\]]+)\]",
    ]:
        ms = re.findall(pat, t, re.I)
        if ms:
            print("ARR", pat, "->", ms[:3])
    for key in [
        "winst",
        "eigen_vermogen",
        "omzet",
        "bruto_marge",
        "fte",
        "personeelsbestand",
        "profit",
        "equity",
        "turnover",
        "gross_margin",
    ]:
        ms = re.findall(rf"{key}[\"']?\s*:\s*[\"']?([\-]?[\d\.,]+)", t, re.I)
        if ms:
            print(key, ms[:12])
    # FAQ turnover sentence
    for m in re.finditer(r"(omzet van €[^.<]+|turnover of €[^.<]+|brutomarge van €[^.<]+|gross margin of €[^.<]+)", t, re.I):
        print("FAQ", m.group(1)[:120])
    # FTE
    for m in re.finditer(r"(\d+[\.,]\d)\s*FTE", t):
        print("FTE", m.group(0))
        break
    # look for year:NNNN near financials
    yrs = re.findall(r'"jaar"\s*:\s*"?(20\d\d)"?', t)
    if yrs:
        print("jaar keys", yrs[:15])
    yrs2 = re.findall(r"jaar\s*:\s*['\"]?(20\d\d)", t)
    if yrs2:
        print("jaar keys2", yrs2[:15])
    # HTML table year headers
    th = re.findall(r">\s*(20\d\d)\s*<", t)
    from collections import Counter

    c = Counter(th)
    print("year counts top", c.most_common(8))


for name in [
    "vander_stokken_nl.html",
    "vander_en.html",
    "vander_fr.html",
    "faro_nl.html",
    "aiesh_nl.html",
    "rew_nl.html",
    "kbo.html",
]:
    p = raw / name
    if p.exists():
        extract_cw(p)
    else:
        print("MISSING", name)
