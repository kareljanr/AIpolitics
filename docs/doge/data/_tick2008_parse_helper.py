# ephemeral helper — parse Damiaan / AZ Oostende / KBO
import re
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2008")


def dump(name):
    path = dst / f"{name}.html"
    if not path.exists():
        print("MISSING", name)
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", name, "====")
    title = re.search(r"<title>([^<]+)</title>", t)
    print("title", title.group(1)[:140] if title else None)
    for pat in [
        r"Employees\s*=\s*\"([^\"]+)\"",
        r"FTE[^\n<]{0,60}",
        r"[\w.+-]+@(?:azdamiaan|azoostende|[\w.-]+)\.\w+",
    ]:
        ms = re.findall(pat, t, re.I)
        if ms:
            print(pat[:40], ms[:8])
    for lab in [
        "NACE",
        "Activity",
        "Hospital",
        "Establishment",
        "Vestiging",
        "Juridische",
        "Status",
        "Actief",
        "email",
        "E-mail",
        "0464",
        "0800",
        "Damiaan",
        "Oostende",
        "rebrand",
        "fusion",
        "fusie",
    ]:
        i = t.lower().find(lab.lower())
        if i >= 0:
            print(lab, repr(t[i : i + 180]))
    # VE count
    ve = re.findall(r"(\d+)\s*(?:vestiging|establishment)", t, re.I)
    print("VE-ish", ve[:5])
    print()


for n in ["damiaan_en", "damiaan_nl", "azo_en", "damiaan_kbo", "damiaan_site"]:
    dump(n)
