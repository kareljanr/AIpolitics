# -*- coding: utf-8 -*-
import re
from collections import Counter
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2080")


def parse(path: Path) -> None:
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", path.name, len(t))
    m = re.search(r"<title>([^<]+)</title>", t)
    if m:
        print("TITLE", m.group(1)[:160])
    for m in re.finditer(r"0\d{3}\.\d{3}\.\d{3}", t):
        print("KBO", m.group(0))
        break
    for m in re.finditer(r"neergelegd op ([0-9\-]+)|filed on ([0-9\-]+)", t, re.I):
        print("FILED", m.group(0))
    blocks = re.findall(r"\{[^{}]*bruto_marge[^{}]*\}", t)
    print("blocks", len(blocks))
    for b in blocks[:4]:
        print(" ", re.sub(r"\s+", " ", b)[:280])
    # year labels before first block
    m = re.search(r"winst:\s*\"[^\"]+\".{0,400}", t, re.S)
    if m:
        ctx = m.group(0)
        # find preceding year key
        i = t.find(ctx)
        print("PRE", re.sub(r"\s+", " ", t[max(0, i - 80) : i + 200])[:260])
    th = Counter(re.findall(r">\s*(20\d\d)\s*<", t))
    print("years", th.most_common(6))
    for m in re.finditer(r"(\d+[\.,]\d)\s*FTE", t):
        print("FTE", m.group(0))
        break
    # FTE spans
    ftes = re.findall(r"<span>(\d+[\.,]\d)</span>", t)
    print("spans", ftes[:6])
    for m in re.finditer(
        r"(omzet van €[^.<]+|turnover of €[^.<]+|brutomarge van €[^.<]+)", t, re.I
    ):
        print("FAQ", m.group(1)[:120])
    # status / rechtsvorm
    for pat in ["Actief", "VZW", "ASBL", "aanbested", "NV", "CV"]:
        if pat.lower() in t.lower():
            print("HAS", pat)


for name in [
    "den_akker_nl.html",
    "den_akker_en.html",
    "faro_nl.html",
    "aiesh_nl.html",
    "rew_nl.html",
    "kbo_den.html",
]:
    parse(RAW / name)

# emails from site if we get it later
