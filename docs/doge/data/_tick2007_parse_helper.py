import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2007/glorieux_en.html").read_text(encoding="utf-8", errors="replace")
print("FTE", re.findall(r"([0-9][0-9.,]*)\s*FTE", t)[:5])
print("email CW", re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", t)[:15])
k = Path("docs/doge/data/raw/tick2007/glorieux_kbo.html").read_text(encoding="utf-8", errors="replace")
print("---KBO---")
for lab in ["Status", "Actief", "Rechtsvorm", "Adres", "E-mail", "email", "Vestiging", "Datum begin"]:
    i = k.lower().find(lab.lower())
    if i >= 0:
        print(lab, repr(k[i : i + 200]))
print("emails kbo", re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", k)[:10])
s = Path("docs/doge/data/raw/tick2007/glorieux_site.html").read_text(encoding="utf-8", errors="replace")
print("---SITE---")
print("emails site", re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", s)[:15])
print("title", re.search(r"<title>([^<]+)</title>", s))
b = Path("docs/doge/data/raw/tick2007/bornem_site.html").read_text(encoding="utf-8", errors="replace")
print("---BORNEM---")
for y in ["Jaarrekening 2025", "jaarrekening 2025", "2025", "2024"]:
    print(y, b.count(y))
