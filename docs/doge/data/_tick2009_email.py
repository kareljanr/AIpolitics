from pathlib import Path
import re

for name in ["blasius_home", "blasius_contact", "blasius_site", "blasius_site2"]:
    t = Path(f"docs/doge/data/raw/tick2009/{name}.html").read_text(encoding="utf-8", errors="replace")
    ms = re.findall(r"mailto:([^\"'\s>]+)", t, re.I)
    print(name, "mailto", ms[:10])
    ms2 = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    print(name, "emails", sorted(set(ms2))[:20])
    i = t.find("Kroonveld")
    print(" kroon", repr(t[i : i + 100]) if i >= 0 else None)
