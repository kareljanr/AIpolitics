import re
from pathlib import Path

kbo = Path("docs/doge/data/raw/tick2031/cassiers_kbo.html").read_text(encoding="utf-8")
text = re.sub(r"<[^>]+>", " ", kbo)
text = re.sub(r"\s+", " ", text)
for key in [
    "Actief",
    "Status",
    "vestiging",
    "E-mail",
    "Begindatum",
    "9 december",
    "Vereniging",
    "Aantal",
    "Houthulst",
]:
    i = text.lower().find(key.lower())
    if i >= 0:
        print(key, ":", text[max(0, i - 30) : i + 90])

en = Path("docs/doge/data/raw/tick2031/cassiers_en.html").read_text(encoding="utf-8")
m = re.search(r'Employees\s*=\s*"([^"]+)"', en)
print("emp js", m.group(1) if m else None)
m = re.search(r"Big\s+([\d,]+)\s*FTE|([\d,]+)\s*FTE", en)
print("fte text", m.group(0) if m else None)
# VE count often in establishment units
for lab in ["establishment units", "vestigingseenheden", "unités d"]:
    j = en.lower().find(lab.lower())
    if j >= 0:
        print(lab, en[j : j + 80].replace("\n", " "))
