import re
from pathlib import Path

base = Path(__file__).resolve().parent.parent / "tick2264"
for name in [
    "faro_en.html",
    "aiesh_en.html",
    "rew_en.html",
    "stallbois_en.html",
    "apre_en.html",
    "renaitre_en.html",
    "sipres_en.html",
]:
    t = (base / name).read_text(encoding="utf-8", errors="replace")
    print("===", name)
    # Find year keys near financial chart objects
    for m in re.finditer(
        r"(20\d{2})\s*:\s*\{\s*winst:\s*\"([^\"]*)\",\s*eigenVermogen:\s*\"([^\"]*)\",\s*brutoMarge:\s*\"([^\"]*)\",\s*omzet:\s*\"([^\"]*)\"",
        t,
    ):
        print(" fin", m.groups())
    for m in re.finditer(r"(20\d{2})\s*:\s*\{[^}]{0,120}?aantalWerknemers:\s*\"?([0-9.,]+)\"?", t):
        print(" fte", m.group(1), m.group(2))
    fil = re.search(r"filed on ([0-9.\-/]+)", t)
    print(" filing", fil.group(1) if fil else None)
    # last balansjaar text
    for pat in [
        r"Latest annual accounts[^0-9]{0,40}(20\d{2})",
        r"most recent financial statements[^.]{0,80}",
        r"Dernier bilan[^0-9]{0,40}(20\d{2})",
    ]:
        m = re.search(pat, t, re.I)
        if m:
            print(" hint", m.group(0)[:120])
