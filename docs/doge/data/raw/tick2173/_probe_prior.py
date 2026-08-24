# -*- coding: utf-8 -*-
"""Parse tick2172 CW HTML for YE2025 free candidates; recheck FARO/AIESH/REW live."""
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2173")
out.mkdir(parents=True, exist_ok=True)
prior = Path("docs/doge/data/raw/tick2172")

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)


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
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        last.group(1) if last else None,
    )


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        p.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", p.name, type(e).__name__, e)
        return None


print("=== LIVE prefer FARO/AIESH/REW/AGB ===")
for kbo, label in [
    ("0877556624", "agb_bornem"),
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
]:
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t:
        continue
    yb, fte, filed, title, last = parse(t)
    print(label, "last", last, "filed", filed, (title or "")[:60])
    for y in ("2025", "2024"):
        if y in yb:
            print(" ", y, yb[y], "fte", fte if y == last else "")

print("\n=== PRIOR HTML YE2025 candidates ===")
hits = []
for p in sorted(prior.glob("*_en.html")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    if "Error 404" in t or len(t) < 5000:
        continue
    yb, fte, filed, title, last = parse(t)
    y5 = yb.get("2025")
    if not y5 or not any(y5.values()):
        continue
    m = re.search(r"(\d{10})", p.name)
    kbo = m.group(1) if m else "?"
    st = "MINED" if kbo in mined else "FREE"
    hits.append((st, kbo, p.name, title, last, filed, y5, fte))

for st, kbo, name, title, last, filed, y5, fte in hits:
    if st != "FREE":
        continue
    print(st, kbo, (title or "")[:55], "last", last, "filed", filed)
    print(" ", y5, "fte", fte)
