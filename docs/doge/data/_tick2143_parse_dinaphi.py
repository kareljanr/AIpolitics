# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2143")
en = (base / "dinaphi_en.html").read_text(encoding="utf-8", errors="replace")
nl = (base / "dinaphi_nl.html").read_text(encoding="utf-8", errors="replace")
fr = (base / "dinaphi_fr.html").read_text(encoding="utf-8", errors="replace")
kbo = (base / "dinaphi_kbo.html").read_text(encoding="utf-8", errors="replace")

for label, t in [("EN", en), ("NL", nl), ("FR", fr)]:
    print("====", label, "len", len(t))
    for pat in [
        r"Last balance sheet year.{0,80}",
        r"Laatste balansjaar.{0,80}",
        r"Dernier bilan.{0,80}",
        r"omzet.{0,120}",
        r"Turnover.{0,120}",
        r"Chiffre d.affaires.{0,120}",
        r"bruto.{0,100}",
        r"Gross margin.{0,100}",
        r"winst.{0,100}",
        r"Profit.{0,100}",
        r"eigen_vermogen.{0,100}",
        r"Equity.{0,100}",
        r"2025.{0,60}",
        r"2024.{0,60}",
        r"noindex|paywall|premium|credits",
        r"window\.cw\.[a-zA-Z]+",
    ]:
        ms = list(re.finditer(pat, t, re.I))
        for m in ms[:2]:
            print(" ", pat[:40], "=>", re.sub(r"\s+", " ", m.group(0))[:160])

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
            "beauraing",
            "dinant",
            "vestiging",
            "naam",
            "rechtsvorm",
            "email",
            "web",
            "zone",
        ]
    ):
        print("KBO", " | ".join(lines[i : i + 3])[:230])
