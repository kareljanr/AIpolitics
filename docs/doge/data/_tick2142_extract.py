# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2142")
en = (base / "franciscus_cw_en.html").read_text(encoding="utf-8", errors="replace")
kbo = (base / "franciscus_kbo.html").read_text(encoding="utf-8", errors="replace")

om25, om24 = 30982834, 29637372
br25, br24 = 32903309, 31584808
pn25, pn24 = 164386, -245197
eq25, eq24 = 25153623, 25266634
for label, a, b in [
    ("omzet", om25, om24),
    ("bruto", br25, br24),
    ("pnl_delta", pn25 - pn24, abs(pn24)),
    ("equity", eq25, eq24),
]:
    if label == "pnl_delta":
        print(f"pnl flip improvement {a} vs prior loss; pct vs |loss| {(pn25-pn24)/abs(pn24)*100:+.2f}%")
    else:
        print(f"{label} {(a-b)/abs(b)*100:+.2f}%")

text = re.sub(r"<[^>]+>", "\n", kbo)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
for i, ln in enumerate(lines):
    if any(
        k in ln.lower()
        for k in [
            "status",
            "actief",
            "adres",
            "nace",
            "87.",
            "vestiging",
            "naam",
            "brakel",
            "aanbested",
            "email",
            "web",
            "franciscus",
        ]
    ):
        print("KBO", " | ".join(lines[i : i + 3])[:230])
