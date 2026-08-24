import re
from pathlib import Path
# check FARO year keys to confirm YE2024
for name in ["faro_en.html","aiesh_en.html","rew_en.html"]:
    t = Path(rf"docs/doge/data/raw/tick2075/{name}").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"window\.cw\.kernCijfers = \{(.{0,200})", t, re.S)
    print(name, m.group(1)[:120] if m else "no")
    filed = re.search(r"filed on ([0-9-]+)", t)
    print(" filed", filed.group(1) if filed else None)
# also look for FTE yoy previous year if available in personnel history
t = Path(r"docs/doge/data/raw/tick2075/kuurne_en.html").read_text(encoding="utf-8", errors="replace")
# find personnel history numbers
for pat in [r'amountOfEmployees[^;]+;', r'personeel[^\n]{0,200}', r'215[,.]9', r'22[0-9][,.][0-9]', r'employeesHistory', r'fteHistory']:
    ms = re.findall(pat, t, re.I)
    print(pat, ms[:3])
# website from cw
for pat in [r'https?://[^\"\']+kuurne[^\"\']*', r'website[^,]{0,80}', r'www\.[a-z0-9.-]+']:
    ms = re.findall(pat, t, re.I)
    if ms:
        print("web", pat, ms[:5])
