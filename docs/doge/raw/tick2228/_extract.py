import re
from pathlib import Path

OUT = Path("docs/doge/raw/tick2228")
for name in [
    "vitesbe_nl.html",
    "vitesbe_en.html",
    "vitesbe_fr.html",
    "vitesbe_kbo.html",
]:
    t = (OUT / name).read_text(encoding="utf-8", errors="ignore")
    print("====", name)
    for pat in [
        r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};",
        r"amountOfEmployees\s*=\s*\"([^\"]+)\"",
        r"window\.cw\.[A-Za-z]+\s*=\s*\"[^\"]{0,80}\"",
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        r"neergelegd op ([0-9.-]+)",
        r"filed on ([0-9.-]+)",
        r"FTE.{0,40}",
        r"11[,.]8.{0,60}",
        r"werknemers.{0,80}",
        r"employees.{0,80}",
        r"vites\.be",
        r"telefoon.{0,60}",
        r"Phone.{0,60}",
    ]:
        ms = re.findall(pat, t, re.I | re.S)
        if not ms:
            continue
        if pat.startswith("window.cw.kern"):
            print("kern", ms[0][:900])
        else:
            print(pat[:40], "->", ms[:6])
