# -*- coding: utf-8 -*-
import re
from pathlib import Path
from collections import Counter

raw = Path("docs/doge/data/raw/tick2080")


def extract(path: Path) -> None:
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", path.name, "len", len(t))
    m = re.search(r"<title>([^<]+)</title>", t)
    if m:
        print("TITLE", m.group(1)[:160])
    for m in re.finditer(
        r"neergelegd op ([0-9\-]+)|filed on ([0-9\-]+)|Last balance sheet year[^<\n]{0,60}|Balansjaar[^<\n]{0,80}|boekjaar 20\d\d|most recent financial",
        t,
        re.I,
    ):
        print("FILING", m.group(0)[:140])
    for m in re.finditer(
        r"(omzet van €[^.<]+|turnover of €[^.<]+|brutomarge van €[^.<]+|gross margin of €[^.<]+|winst van €[^.<]+|profit of €[^.<]+|verlies van €[^.<]+|loss of €[^.<]+|eigen vermogen van €[^.<]+|equity of €[^.<]+)",
        t,
        re.I,
    ):
        print("FAQ", m.group(1)[:160])
    for m in re.finditer(r"(\d+[\.,]\d)\s*FTE", t):
        print("FTE", m.group(0))
        break
    th = re.findall(r">\s*(20\d\d)\s*<", t)
    print("year top", Counter(th).most_common(8))
    blocks = re.findall(r"\{[^{}]*bruto_marge[^{}]*\}", t)
    print("blocks", len(blocks))
    for b in blocks[:8]:
        print(" ", b[:350])
    for key in [
        "omzet",
        "turnover",
        "winst",
        "profit",
        "eigen_vermogen",
        "equity",
        "bruto_marge",
        "gross_margin",
        "fte",
        "personeelsbestand",
    ]:
        ms = re.findall(rf"{key}[\"']?\s*:\s*[\"']?([\-]?[\d\.,]+)", t, re.I)
        if ms:
            print(key, ms[:12])
    # KBO status/email/VE
    for m in re.finditer(
        r"(Status van de entiteit|Entity status|Rechtsvorm|Juridical form|Aantal vestigingseenheden|Number of establishments|E-mail|Email)[^<\n]{0,120}",
        t,
        re.I,
    ):
        print("KBOFIELD", m.group(0)[:160])
    if "2025" in t:
        idx = t.find("2025")
        print("2025ctx", repr(t[max(0, idx - 50) : idx + 90]))
    else:
        print("NO literal 2025")


for name in [
    "faro_nl.html",
    "faro_en.html",
    "aiesh_nl.html",
    "aiesh_en.html",
    "rew_nl.html",
    "rew_en.html",
    "agb_bornem_en.html",
    "den_akker_nl.html",
    "den_akker_en.html",
    "den_akker_fr.html",
    "den_akker_kbo.html",
]:
    p = raw / name
    if p.exists():
        extract(p)
    else:
        print("MISSING", name)
