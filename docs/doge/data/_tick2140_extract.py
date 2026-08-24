# -*- coding: utf-8 -*-
import csv
import re
import shutil
from pathlib import Path

csv.field_size_limit(10**7)
src = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2139")
dst = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2140")
dst.mkdir(parents=True, exist_ok=True)
for name in [
    "denderrust_cw_en.html",
    "denderrust_cw_nl.html",
    "denderrust_cw_fr.html",
    "denderrust_kbo.html",
    "denderrust_site.html",
    "denderrust_contact.html",
    "faro_cw_en.html",
    "aiesh_cw_en.html",
    "rew_cw_en.html",
]:
    p = src / name
    if p.exists():
        shutil.copy2(p, dst / name)
        print("copy", name, p.stat().st_size)

en = (dst / "denderrust_cw_en.html").read_text(encoding="utf-8", errors="replace")
for y in ["2025", "2024"]:
    mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
    print(y, re.sub(r"\s+", " ", mm.group(1))[:320] if mm else None)
for pat in [
    r'Employees\s*=\s*"([^"]+)"',
    r"filed on ([0-9\-]+)",
    r'window\.cw\.startDate\s*=\s*"([^"]+)"',
    r'window\.cw\.companySize\s*=\s*"([^"]+)"',
]:
    m = re.search(pat, en)
    if m:
        print(pat[:40], m.group(1) if m.lastindex else m.group(0))

om25, om24 = 11135834, 10742203
br25, br24 = 12099041, 11424596
pn25, pn24 = 47586, 152817
eq25, eq24 = 8526706, 8482380
for label, a, b in [
    ("omzet", om25, om24),
    ("bruto", br25, br24),
    ("pnl", pn25, pn24),
    ("equity", eq25, eq24),
]:
    print(f"{label} {(a-b)/abs(b)*100:+.2f}%")

# inventory counts
data = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
for fn in ["budgets.csv", "commitments.csv", "leaderboard.csv", "entities.csv", "sources.csv", "foi_queue.csv"]:
    with (data / fn).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if fn == "foi_queue.csv":
        ready = sum(1 for r in rows if r.get("status") == "ready")
        ans = sum(1 for r in rows if r.get("status") == "answered")
        part = sum(1 for r in rows if r.get("status") == "partial")
        print(fn, "total", len(rows), "ready", ready, "answered", ans, "partial", part)
    else:
        print(fn, len(rows))

# top10 verify from leaderboard
with (data / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    lbs = list(csv.DictReader(f))

def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0

def annual(r):
    try:
        return float(r.get("annual_cost_eur") or 0)
    except Exception:
        return 0

cands = [
    r
    for r in lbs
    if pi(r) <= 10
    and r.get("status") != "struck"
    and "stock" not in (r.get("notes") or "").lower()
]
# keep known top seed rows by id pattern + high pi
cands.sort(key=lambda r: (-pi(r), -annual(r)))
print("top candidates:")
for r in cands[:15]:
    print(f"  {pi(r):.2f} {annual(r):.0f} {r.get('item_id','')[:60]} {(r.get('name') or '')[:50]}")

# denderrust already in CSVs?
for fn in ["entities.csv", "leaderboard.csv", "foi_queue.csv"]:
    t = (data / fn).read_text(encoding="utf-8", errors="replace").lower()
    print("csvhit", fn, "denderrust" in t or "0419333572" in t or "0419.333.572" in t)
