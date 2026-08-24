import re
from pathlib import Path

base = Path(__file__).resolve().parent.parent / "tick2264"
for name in ["faro_en.html", "aiesh_en.html", "rew_en.html", "stallbois_en.html", "apre_en.html", "renaitre_en.html"]:
    t = (base / name).read_text(encoding="utf-8", errors="replace")
    print("===", name)
    m = re.search(r"cw\.kernCijfers\s*=\s*\{(.*?)\n\s*\};", t, re.S)
    if m:
        years = re.findall(r"(20\d{2})\s*:\s*\{([^}]+)\}", m.group(1))
        for y, body in years[:4]:
            fields = dict(re.findall(r"(winst|eigen_vermogen|bruto_marge|omzet):\s*\"([^\"]*)\"", body))
            print(y, fields)
    # personnel
    m2 = re.search(r"cw\.personeelsbestanden\s*=\s*\{(.*?)\n\s*\};", t, re.S)
    if not m2:
        m2 = re.search(r"aantalWerknemers|fte|Employees.*?cw\.", t[:5000], re.S)
    # try common keys
    for pat in [
        r"cw\.tewerkstelling\s*=\s*\{(.*?)\n\s*\};",
        r"cw\.werknemers\s*=\s*\{(.*?)\n\s*\};",
        r"personeel[^\{]{0,40}\{(.*?)\n\s*\};",
    ]:
        mm = re.search(pat, t, re.S | re.I)
        if mm:
            print("pers block", pat[:30], mm.group(1)[:300])
            break
    # inline FTE near years in table
    ftes = re.findall(r"(20\d{2})[^\{]{0,40}\{[^}]{0,80}?\"([0-9]+(?:[.,][0-9]+)?)\"[^}]{0,40}(?:FTE|werknemer|employee)", t, re.I)
    print("fte hints", ftes[:6])
    # simpler: look near kern for VTE
    for key in ["gemiddeld_fte", "fte", "vte", "werknemers", "aantal_werknemers", "personeelsbestand"]:
        if key in t:
            idx = t.find(key)
            print(" key", key, t[idx - 80 : idx + 120].replace("\n", " ")[:200])
