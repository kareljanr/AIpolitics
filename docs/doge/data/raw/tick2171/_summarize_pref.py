# -*- coding: utf-8 -*-
import re
import csv
from pathlib import Path

csv.field_size_limit(10**7)
mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, encoding="utf-8", errors="replace") as f:
        blob = re.sub(r"[.\s]", "", f.read())
        mined.update(re.findall(r"\d{10}", blob))


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
    act = re.search(r"Principal activity</[^>]+>\s*([^<]+)", t or "", re.I)
    nace = re.findall(
        r"87\.\d{3}|86\.\d{3}|88\.\d{3}|68\.\d{3}|55\.\d{3}|64\.\d{3}|47\.\d{3}|94\.\d{3}",
        t or "",
    )[:6]
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        last.group(1) if last else None,
        (act.group(1).strip() if act else ""),
        nace,
    )


raw = Path("docs/doge/data/raw/tick2170")
for p in sorted(raw.glob("*.html")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    if "Error 404" in t or len(t) < 500:
        continue
    yb, fte, filed, title, last, act, nace = parse(t)
    m = re.search(r"BE0?(\d{9,10})", title or "")
    if not m:
        m = re.search(r"_(\d{10})_", p.name) or re.search(r"_(\d{10})\.", p.name)
    kbo = None
    if m:
        kbo = re.sub(r"\D", "", m.group(1)).zfill(10)[-10:]
    st = "MINED" if kbo in mined else "FREE"
    y5 = yb.get("2025", {})
    if last == "2025" or y5:
        print(f"{st} {kbo} last={last} {(title or p.name)[:55]}")
        print(f"  act={act[:70]} nace={nace} fte={fte} filed={filed}")
        print(
            "  2025 omzet=%s bruto=%s pnl=%s eq=%s"
            % (
                y5.get("omzet"),
                y5.get("bruto_marge"),
                y5.get("winst"),
                y5.get("eigen_vermogen"),
            )
        )
