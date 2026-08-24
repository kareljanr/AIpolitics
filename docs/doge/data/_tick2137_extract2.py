# -*- coding: utf-8 -*-
import re
from pathlib import Path

en = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2137\corolles_en.html").read_text(
    encoding="utf-8", errors="replace"
)
m = re.search(r"window\.cw\.address\s*=\s*(\{.*?\});", en, re.S)
print("ADDR", re.sub(r"\s+", " ", m.group(1))[:400] if m else None)
m = re.search(r'window\.cw\.startDate\s*=\s*"([^"]+)"', en)
print("start", m.group(1) if m else None)
m = re.search(r'window\.cw\.companySize\s*=\s*"([^"]+)"', en)
print("size", m.group(1) if m else None)
# YoY calcs
om25, om24 = 9741365, 9385583
br25, br24 = 10263326, 9813565
pn25, pn24 = 467552, 424611
eq25, eq24 = 9934798, 9613283
for label, a, b in [
    ("omzet", om25, om24),
    ("bruto", br25, br24),
    ("pnl", pn25, pn24),
    ("equity", eq25, eq24),
]:
    pct = (a - b) / abs(b) * 100
    print(f"{label}: {a} vs {b} => {pct:+.2f}%")

site = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2137\corolles_site.html")
if site.exists():
    t = site.read_text(encoding="utf-8", errors="replace")
    print("site_len", len(t))
    title = re.search(r"<title>([^<]+)", t)
    print("site_title", title.group(1)[:100] if title else None)
    for m in re.finditer(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", t, re.I):
        print("email", m.group(0))

# KBO VE / vestigingen count
kbo = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2137\corolles_kbo.html").read_text(
    encoding="utf-8", errors="replace"
)
text = re.sub(r"<[^>]+>", "\n", kbo)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
for i, ln in enumerate(lines):
    if "vestiging" in ln.lower() or "établissement" in ln.lower() or "unit" in ln.lower():
        print("VE", " | ".join(lines[i : i + 4])[:250])
    if "0434.384.014" in ln or "La Moisson" in ln or "0409.232.013" in ln:
        print("LINK", " | ".join(lines[i : i + 3])[:250])
