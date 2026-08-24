# -*- coding: utf-8 -*-
"""Scan tick2170+2171 raw HTML for FREE YE2025 care/IGS with material euros."""
import re
from pathlib import Path

text = ""
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    text += open(path, encoding="utf-8", errors="replace").read().lower()
blob = re.sub(r"[.\s]", "", text)


def is_mined(kbo):
    d = re.sub(r"\D", "", kbo or "")
    if len(d) < 10:
        return True
    return d in blob


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
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        last.group(1) if last else None,
        (act.group(1).strip() if act else ""),
    )


def euro(s):
    if not s:
        return 0
    s = str(s).replace("\xa0", "").replace(" ", "").replace(".", "").replace(",", "")
    try:
        return int(s)
    except Exception:
        return 0


seen = set()
hits = []
for raw in [
    Path("docs/doge/data/raw/tick2170"),
    Path("docs/doge/data/raw/tick2171"),
]:
    if not raw.exists():
        continue
    for p in sorted(raw.glob("*.html")):
        t = p.read_text(encoding="utf-8", errors="ignore")
        if "Error 404" in t or len(t) < 800:
            continue
        yb, fte, filed, title, last, act = parse(t)
        m = re.search(r"BE0?(\d{9,10})", title or "")
        if not m:
            m = re.search(r"_(\d{10})_", p.name) or re.search(r"_(\d{10})\.", p.name)
        if not m:
            continue
        kbo = re.sub(r"\D", "", m.group(1)).zfill(10)[-10:]
        if kbo in seen:
            continue
        seen.add(kbo)
        if is_mined(kbo):
            continue
        y5 = yb.get("2025", {})
        if last != "2025" and not y5:
            continue
        om = euro(y5.get("omzet"))
        br = euro(y5.get("bruto_marge"))
        pnl = euro(y5.get("winst"))
        eq = euro(y5.get("eigen_vermogen"))
        if om + br < 150000:
            continue
        care = any(
            x in ((title or "") + " " + act).lower()
            for x in [
                "woonzorg",
                "wzc",
                "rusthuis",
                "nursing",
                "repos",
                "mrs",
                "residence",
                "zorg",
                "elderly",
                "rest home",
            ]
        )
        hits.append((om + br, care, kbo, (title or p.name)[:65], om, br, pnl, eq, fte, filed, act[:50]))

hits.sort(reverse=True)
print(f"FREE YE2025 material hits: {len(hits)}")
for h in hits[:40]:
    print(
        f"{'CARE' if h[1] else 'other'} {h[2]} tot={h[0]} om={h[4]} br={h[5]} "
        f"pnl={h[6]} eq={h[7]} fte={h[8]} filed={h[9]}"
    )
    print(f"  {h[3]}")
    print(f"  act={h[10]}")
