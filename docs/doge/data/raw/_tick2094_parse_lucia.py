import re
from pathlib import Path
p = Path("docs/doge/data/raw/tick2091/cand_0410151137_nl.html")
t = p.read_text(encoding="utf-8", errors="replace")
print("size", len(t))
for pat in [
    r'bruto_marge:\s*"([^"]+)"',
    r'omzet:\s*"([^"]+)"',
    r'year:\s*(\d{4})',
    r"Laatste balansjaar[^0-9]*(\d{4})",
]:
    print(pat, re.findall(pat, t)[:12])
objs = re.findall(r"\{[^{}]*bruto_marge:[^{}]+\}", t)
print("objs", len(objs))
for o in objs[:8]:
    print(o[:350])
    print("---")
plain = re.sub(r"<[^>]+>", " ", t)
plain = re.sub(r"\s+", " ", plain)
for key in [
    "Laatste balansjaar",
    "Omzet",
    "Brutomarge",
    "Eigen vermogen",
    "Resultaat",
    "Personeel",
    "neergelegd",
    "Schulden",
    "Balanstotaal",
    "Bedrijfswinst",
    "Netto",
    "Winst",
    "Verlies",
    "code 70",
    "9904",
]:
    i = plain.lower().find(key.lower())
    if i >= 0:
        print("CTX", key, ":", plain[max(0, i - 30) : i + 200])
# also search for numeric year blocks in schema.org / json
m = re.search(r"financials[^\]]{0,2000}", t, re.I)
if m:
    print("FIN", m.group(0)[:800])
