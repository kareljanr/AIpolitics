# -*- coding: utf-8 -*-
import re
from pathlib import Path

raw = Path("docs/doge/data/raw/tick2080")
t = (raw / "den_akker_en.html").read_text(encoding="utf-8", errors="replace")

# Last balance sheet year label
for m in re.finditer(r"Last balance sheet year.{0,200}", t, re.S | re.I):
    print("LBSY", re.sub(r"\s+", " ", m.group(0))[:200])
    break

# filed on
for m in re.finditer(r"filed on ([0-9\-]+)", t, re.I):
    print("FILED", m.group(1))

# FTE previous year if present
for m in re.finditer(r"FTE[^0-9]{0,40}(\d+[\.,]\d)", t):
    print("FTEnear", m.group(0)[:80])

# year series near charts
for pat in [r"categories\s*:\s*\[([^\]]+)\]", r"labels\s*:\s*\[([^\]]+)\]"]:
    for m in re.finditer(pat, t, re.I):
        print("ARR", m.group(1)[:120])

# extract year-aligned series from JS if present
for m in re.finditer(r"jaar\s*[:=]\s*[\"']?(20\d\d)", t, re.I):
    print("jaar", m.group(1))

# KBO detail
k = (raw / "den_akker_kbo.html").read_text(encoding="utf-8", errors="replace")
for label in [
    "Status van de entiteit",
    "Rechtsvorm",
    "Aantal vestigingseenheden",
    "E-mail",
    "Adres van de zetel",
    "Ondernemingsnummer",
    "Naam",
    "BTW",
    "RSZ",
    "Aanbestedende",
]:
    idx = k.find(label)
    if idx >= 0:
        chunk = re.sub(r"\s+", " ", k[idx : idx + 250])
        print("KBO", chunk[:220])

# site email search
print("--- site hint ---")
for m in re.finditer(r"[\w.\-]+@[\w.\-]+\.[a-z]{2,}", t, re.I):
    e = m.group(0)
    if "companyweb" not in e.lower() and "example" not in e.lower():
        print("EMAIL", e)

# REW year check
for name in ["rew_en.html", "aiesh_en.html", "faro_en.html", "agb_bornem_en.html"]:
    tt = (raw / name).read_text(encoding="utf-8", errors="replace")
    yrs = re.findall(r">\s*(20\d\d)\s*<", tt)
    from collections import Counter

    print(name, "years", Counter(yrs).most_common(4))
    for m in re.finditer(r"filed on ([0-9\-]+)|Last balance sheet year", tt, re.I):
        print(" ", m.group(0)[:80])
        break
