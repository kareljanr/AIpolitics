import re
from pathlib import Path
for name in ["ouvroir_en.html","ouvroir_nl.html","faro_nl.html"]:
    t = Path("docs/doge/raw/tick2268/"+name).read_text(encoding="utf-8", errors="replace")
    print("====", name, "====")
    # balansjaar near label
    m = re.search(r"(Latest balance sheet year|Laatste balansjaar|Dernier bilan).{0,80}?(\d{4})", t, re.S)
    print("balans", m.groups() if m else None)
    years = list(re.finditer(r"(20\d{2})\s*:\s*\{([^}]{0,500})\}", t))
    for ym in years[:4]:
        body = ym.group(2)
        if any(k in body for k in ("bruto", "omzet", "winst", "marge", "eigen")):
            print(ym.group(1), body.strip()[:350])
    m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
    print("FTE", m.group(1) if m else None)
    for pat in [r"filed on ([0-9.-]+)", r"neergelegd op ([0-9.-]+)", r"d.pos.es? le ([0-9.-]+)"]:
        m = re.search(pat, t, re.I)
        if m:
            print("filed", m.group(1))
            break
    # employees table 95.7 style
    i = t.find("Employees")
    if i < 0:
        i = t.find("Personeel")
    if i > 0:
        chunk = re.sub(r"\s+", " ", t[i:i+900])
        nums = re.findall(r">([0-9]+(?:[.,][0-9]+)?)<", t[i:i+1200])
        print("emp nums", nums[:8])
