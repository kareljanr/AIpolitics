# -*- coding: utf-8 -*-
import re
from pathlib import Path

out = Path(__file__).resolve().parent
tk = (out / "boterlaarhof_kbo.html").read_text(encoding="utf-8", errors="ignore")
m = re.search(r"Adres van de zetel:(.*?)</tr>", tk, re.S)
print("SEAT", re.sub(r"<[^>]+>", " ", m.group(1)) if m else None)
print("VE", re.search(r"vestigingseenheden \(VE\):.*?<strong>(\d+)</strong>", tk, re.S).group(1))

tn = (out / "boterlaarhof_nl.html").read_text(encoding="utf-8", errors="ignore")
for k in re.findall(r"window\.cw\.(\w+)\s*=", tn):
    pass
interesting = [
    "street",
    "city",
    "zip",
    "zipCode",
    "postalCode",
    "municipality",
    "address",
    "enterpriseName",
    "companyName",
    "name",
    "vat",
    "nace",
]
for k in interesting:
    m = re.search(rf'window\.cw\.{k}\s*=\s*"([^"]*)"', tn)
    if m:
        print(k, m.group(1))

# fallback street from visible
m = re.search(r"<title>([^<]+)", tn)
print("title", m.group(1) if m else None)
m = re.search(r"([A-Za-z\- ]+\s+\d+[A-Za-z]?),\s*2100", tn)
print("street2100", m.group(0) if m else None)

ts = (out / "boterlaarhof_site.html").read_text(encoding="utf-8", errors="ignore")
for m in re.finditer(r".{0,30}2100.{0,50}", ts):
    s = re.sub(r"<[^>]+>", " ", m.group(0))
    s = re.sub(r"\s+", " ", s).strip()
    print("SITE2100", s[:160])
