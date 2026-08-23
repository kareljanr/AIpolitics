# extract equity + yearly kerncijfers + filing date for PPC Pittem
import re
from pathlib import Path

en = Path("docs/doge/data/raw/tick2021/ppc_pittem_en.html").read_text(encoding="utf-8")
nl = Path("docs/doge/data/raw/tick2021/ppc_pittem.html").read_text(encoding="utf-8")

# find kerncijfers objects
objs = re.findall(r"\{[^{}]*bruto_marge:[^{}]+\}", en)
print("n objs", len(objs))
for o in objs[:4]:
    print("---")
    print(o[:500])

# equity field name variants in JS
for pat in [
    r"eigen_vermogen:\s*\"([^\"]+)\"",
    r"eigenVermogen:\s*\"([^\"]+)\"",
    r"equity:\s*\"([^\"]+)\"",
    r"capita[^:]*:\s*\"([^\"]+)\"",
    r"vermogen:\s*\"([^\"]+)\"",
]:
    print(pat, re.findall(pat, en)[:8])
    print("NL", pat, re.findall(pat, nl)[:8])

# filed on
print("filed", re.findall(r"filed on ([0-9-]+)", en))
print("neergelegd", re.findall(r"neergelegd op ([0-9./-]+)", nl, re.I))

# employees series
print("emp", re.findall(r"employees?:\s*\"?([0-9]+[.,][0-9]+)", en, re.I)[:8])
print("personeel vals", re.findall(r"personeel[^:]*:\s*\"([^\"]+)\"", nl, re.I)[:8])
