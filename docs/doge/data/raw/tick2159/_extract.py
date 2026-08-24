# -*- coding: utf-8 -*-
from pathlib import Path
import re

out = Path(__file__).resolve().parent
t = (out / "olvo_en.html").read_text(encoding="utf-8", errors="ignore")
for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t):
    if y >= "2022":
        print("YEAR", y)
        for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]:
            m = re.search(rf'{k}:\s*"([^"]*)"', body)
            print(" ", k, m.group(1) if m else None)

filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
print("filed", filed.group(1) if filed else "-")
fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
print("fte", fte.group(1) if fte else "-")

# KBO
k = (out / "olvo_kbo.html").read_text(encoding="utf-8", errors="ignore")
kp = re.sub(r"<[^>]+>", " ", k)
kp = re.sub(r"\s+", " ", kp)
for key in [
    "Status",
    "Actief",
    "Naam",
    "Adres van de zetel",
    "vestigingseenheden",
    "NACE",
    "87.",
    "E-mail",
    "Telefoon",
    "Aanbestedende",
    "Rechtsvorm",
    "Bremlaan",
    "Kursaal",
]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", kp[max(0, i - 20) : i + 150])

# site emails
s = (out / "lindeboom_site.html").read_text(encoding="utf-8", errors="ignore")
emails = sorted(set(re.findall(r"[\w.+-]+@lindeboom\.be", s, flags=re.I)))
print("site emails", emails)
