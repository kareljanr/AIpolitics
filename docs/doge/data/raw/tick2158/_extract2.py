# -*- coding: utf-8 -*-
from pathlib import Path
import re

t = Path(__file__).resolve().parent.joinpath("epinette_en_full.html").read_text(encoding="utf-8", errors="ignore")
# find financial table rows
plain = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
# look for euro amounts near labels
for label in [
    "Profit/Loss",
    "Turnover",
    "Equity",
    "Gross margin",
    "Employees",
    "Winst",
    "Omzet",
    "Eigen vermogen",
    "Brutomarge",
    "Personeel",
]:
    for m in re.finditer(re.escape(label), plain, re.I):
        chunk = plain[m.start() : m.start() + 500]
        chunk = re.sub(r"<[^>]+>", "|", chunk)
        chunk = re.sub(r"\s+", " ", chunk)
        print(label, "=>", chunk[:280])
        break

# address from KBO
k = Path(__file__).resolve().parent.joinpath("epinette_kbo_nl.html").read_text(encoding="utf-8", errors="ignore")
kp = re.sub(r"<[^>]+>", " ", k)
kp = re.sub(r"\s+", " ", kp)
for key in ["Adres van de zetel", "Chauss", "Alsemberg", "Comines", "Uccle", "Ukkel", "Moulins", "Sérénité", "Serenite"]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", kp[max(0, i - 30) : i + 160])

# try extract JSON more carefully for equity etc
objs = re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t)
for y, body in objs[:4]:
    print("OBJ", y, body[:300])
