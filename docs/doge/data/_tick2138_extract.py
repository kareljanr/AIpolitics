# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2138")
en = (base / "prestige_cw_en.html").read_text(encoding="utf-8", errors="replace")
nl = (base / "prestige_cw_nl.html").read_text(encoding="utf-8", errors="replace")
kbo = (base / "prestige_kbo.html").read_text(encoding="utf-8", errors="replace")

br25, br24 = 3700707, 3142656
pn25, pn24 = 57786, -189310
eq25, eq24 = 277599, 219813
print(f"bruto {(br25-br24)/abs(br24)*100:+.2f}%")
print(f"equity {(eq25-eq24)/abs(eq24)*100:+.2f}%")
print(f"pnl flip from {pn24} to {pn25}; delta {pn25-pn24}")

for label, pat in [
    ("fte", r'Employees\s*=\s*"([^"]+)"'),
    ("start", r'window\.cw\.startDate\s*=\s*"([^"]+)"'),
    ("size", r'window\.cw\.companySize\s*=\s*"([^"]+)"'),
    ("filed", r"filed on ([0-9\-]+)"),
    ("hoofd", r"Hoofdactiviteit.{0,160}"),
]:
    m = re.search(pat, en + "\n" + nl, re.I | re.S)
    if m:
        print(label, re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(0)))[:200])

text = re.sub(r"<[^>]+>", "\n", kbo)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
keys = (
    "status",
    "actief",
    "adres",
    "chaudfontaine",
    "nace",
    "87.",
    "email",
    "web",
    "telefoon",
    "vestiging",
    "rechtsvorm",
    "naam",
    "prestige",
    "functie",
    "liège",
    "liege",
)
for i, ln in enumerate(lines):
    if any(k in ln.lower() for k in keys):
        print("KBO", " | ".join(lines[i : i + 3])[:230])
