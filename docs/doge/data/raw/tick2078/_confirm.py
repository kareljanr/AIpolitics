import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2078/tenanker_en.html").read_text(
    encoding="utf-8", errors="replace"
)
print("mails", re.findall(r"mailto:([^\"'>\s]+)", t)[:5])
print("tels", re.findall(r"tel:([^\"'>\s]+)", t)[:5])

tn = Path("docs/doge/data/raw/tick2078/tenanker_nl.html").read_text(
    encoding="utf-8", errors="replace"
)
for lab in ["Omzet", "Winst/Verlies", "Eigen vermogen", "Bruto", "Personeel"]:
    m = re.search(
        re.escape(lab) + r".{0,200}?</td>\s*((?:<td[^>]*>.*?</td>\s*){1,8})",
        tn,
        re.S | re.I,
    )
    if not m:
        print(lab, "NONE")
        continue
    euros = re.findall(r"€\s*</span>\s*<span>\s*([0-9\.\-]+)</span>", m.group(1))
    plain = re.findall(r">\s*([0-9]+(?:[,\.][0-9]+)?)\s*<", m.group(1))
    print(lab, euros or plain[:6])
