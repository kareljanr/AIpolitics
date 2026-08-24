# -*- coding: utf-8 -*-
import csv
import re
from html import unescape
from pathlib import Path

csv.field_size_limit(10**7)
done = set()
for path in [
    Path("docs/doge/data/entities.csv"),
    Path("docs/doge/data/commitments.csv"),
    Path("docs/doge/data/leaderboard.csv"),
    Path("docs/doge/data/research_queue.csv"),
]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            blob = " ".join(str(v or "") for v in row.values())
            for m in re.findall(r"0\d{9}|\d{4}\.\d{3}\.\d{3}", blob):
                done.add(re.sub(r"\D", "", m))

print("done kbos", len(done))
raw = Path("docs/doge/data/raw/tick2100")
for p in sorted(raw.glob("cand_*.html")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    mname = re.search(r"<title>([^<]+)</title>", t, re.I)
    name = (mname.group(1) if mname else p.name)[:90]
    kbo = re.search(r"cand_(\d+)", p.name).group(1)
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))
    lb = re.search(r"Laatste balansjaar\s+(\d{4})", text)
    om = re.search(r"Omzet\s+€\s*([\d\.,]+)", text)
    pnl = re.search(r"Winst/Verlies\s+€\s*([-]?[\d\.,]+)", text)
    print(
        f"{kbo} done={kbo in done} lb={lb.group(1) if lb else '?'} "
        f"omzet={om.group(1) if om else '?'} pnl={pnl.group(1) if pnl else '?'} name={name}"
    )
