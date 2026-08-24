# -*- coding: utf-8 -*-
import re
from pathlib import Path

raw = Path("docs/doge/data/raw/tick2132")
for name in ["faro_en.html", "aiesh_en.html", "rew_en.html", "bornem_en.html"]:
    html = (raw / name).read_text(encoding="utf-8", errors="replace")
    years = re.findall(r"(202[0-9])\s*:\s*\{\s*winst", html)
    i = html.lower().find("last balance sheet year")
    snip = html[i : i + 180].replace("\n", " ") if i >= 0 else ""
    print(name, "years", years[:6], "|", snip[:120])

html = (raw / "maagd_cw_en.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)", html).group(1))
years = re.findall(r"(202[0-9])\s*:\s*\{\s*winst", html)
print("years", years[:8])
# extract chart data blocks
for key in ["winst", "omzet", "eigen_vermogen", "bruto_marge", "personeel"]:
    ms = re.findall(rf'{key}\s*:\s*"([^"]+)"', html)
    print(key, ms[:8])
i = html.lower().find("filed on")
print("filed", html[i : i + 80].replace("\n", " ") if i >= 0 else "n/a")
i = html.lower().find("employees =")
print("emp", html[i : i + 40] if i >= 0 else "n/a")
i = html.lower().find("principal activity")
print("act", html[i : i + 120].replace("\n", " ") if i >= 0 else "n/a")

kbo = (raw / "maagd_kbo.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Status[^<]{0,40}",
    r"Rechtsvorm[^<]{0,80}",
    r"Adres[^<]{0,120}",
    r"Nace[^<]{0,120}",
    r"Vestigingseenheid",
]:
    m = re.search(pat, kbo, re.I)
    if m:
        print("KBO", m.group(0)[:100])
# count VE
print("VE mentions", len(re.findall(r"Vestigingseenheid", kbo, re.I)))
# emails / contact nearby in NL page?
nl = (raw / "maagd_cw_nl.html").read_text(encoding="utf-8", errors="replace")
emails = re.findall(r"[\w.+-]+@[\w.-]+\.\w+", nl)
print("emails", emails[:10])
