import re
from pathlib import Path
for name in ["apre_en.html","apre_nl.html","apre_fr.html","faro_nl.html"]:
    t = Path("docs/doge/raw/tick2267/"+name).read_text(encoding="utf-8", errors="replace")
    print("====", name, "====")
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
    m = re.search(r"gross margin of .([0-9.,]+)|brutomarge van .?\s*([0-9.,]+)|marge brute de .?\s*([0-9.,]+)", t, re.I)
    if m:
        print("faq bruto", [g for g in m.groups() if g])
    # personnel prior year near chart
    m = re.search(r"Personnel</|staff|personeel", t, re.I)
