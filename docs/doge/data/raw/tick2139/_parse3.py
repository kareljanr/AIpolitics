from pathlib import Path
import re
kbo=Path("docs/doge/data/raw/tick2139/denderrust_kbo.html").read_text(encoding="utf-8", errors="replace")
# address block
m=re.search(r"Adres van de zetel:</td><td[^>]*>(.*?)</td>", kbo, re.S|re.I)
print("ADDR", re.sub(r"<[^>]+>"," ", m.group(1) if m else "?"))
m=re.search(r"Aantal vestigingseenheden \(VE\):.*?<[^>]+>(\d+)", kbo, re.S)
print("VE", m.group(1) if m else "?")
# aanbestedende
print("aanbest", "aanbestedende" in kbo.lower())
for m in re.finditer(r"Hoedanigheden.{0,500}", kbo, re.S|re.I):
    print("HOED", re.sub(r"<[^>]+>"," ", m.group(0))[:400])
# FTE prior year from EN
en=Path("docs/doge/data/raw/tick2139/denderrust_cw_en.html").read_text(encoding="utf-8", errors="replace")
# look for personeel year series
for m in re.finditer(r"202[0-9]\s*:\s*\{[^}]{0,400}\}", en):
    print("Y", m.group(0)[:300])
# also search personeel chart values
for m in re.finditer(r"personeel[^,]{0,20}:\s*\"?[0-9.,]+", en, re.I):
    print("P", m.group(0))
