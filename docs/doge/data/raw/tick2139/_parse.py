import re
from pathlib import Path
t = Path("docs/doge/data/raw/tick2139/0419333572_zorgcampus_denderrust.html").read_text(encoding="utf-8", errors="replace")
patterns = [
    r"personeelsbestand.{0,200}",
    r"Average number of employees.{0,200}",
    r"Gemiddeld aantal werknemers.{0,200}",
    r"fte.{0,40}[0-9][0-9.,]*",
    r"filed on [0-9-]+",
    r"neergelegd.{0,80}",
    r"Last balance sheet year.{0,40}",
    r"Principal activity.{0,200}",
    r"NACE.{0,120}",
    r"mailto:[^\s\"'<>]+",
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    r"vestigingseenheden.{0,80}",
    r"establishment units.{0,80}",
    r"Denderrust|Aalst|Geraardsbergen|Denderhoutem|Molenstraat|Kerkstraat",
]
for pat in patterns:
    ms = list(re.finditer(pat, t, re.I | re.S))
    for m in ms[:4]:
        print(pat[:50], "=>", m.group(0)[:200].replace("\n", " "))
# FTE JSON
for m in re.finditer(r"personeel[^\n]{0,80}|aantal_werknemers[^\n]{0,80}|fte[\"']?\s*[:=]\s*[\"']?[0-9.,]+", t, re.I):
    print("HIT", m.group(0)[:120])
