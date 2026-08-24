# -*- coding: utf-8 -*-
import re
from pathlib import Path

out = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2219")
for f in sorted(out.glob("site_*.html")):
    s = f.read_text(encoding="utf-8", errors="ignore")
    emails = sorted(set(re.findall(r"[\w.\-]+@[\w.\-]+\.\w+", s)))
    print(f.name, "emails", emails[:15])
tn = (out / "opnieuw_nl.html").read_text(encoding="utf-8", errors="ignore")
print("NL FAQ omzet", re.search(r"omzet van Opnieuw.{0,120}", tn))
print("NL bruto", re.search(r"brutomarge van Opnieuw.{0,80}", tn))
print("NL FTE/VTE", re.findall(r"([\d.,]+)\s*(?:VTE|FTE|werknemers)", tn)[:10])
# prior FTE in social balance tables?
for pat in [
    r"205[.,]3",
    r"personeelsbestand.{0,200}",
    r"gemiddeld aantal.{0,120}",
]:
    ms = re.findall(pat, tn, re.I | re.S)
    if ms:
        print(pat[:30], ms[:3] if isinstance(ms[0], str) else ms[:3])
