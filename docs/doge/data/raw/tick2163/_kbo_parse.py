# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path(r"docs/doge/data/raw/tick2163/bernardus_kbo.html").read_text(encoding="utf-8", errors="ignore")
# strip tags roughly for readable dump of key sections
text = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text = re.sub(r"<[^>]+>", " | ", text)
text = re.sub(r"\s+", " ", text)
# find interesting chunks
for key in [
    "Naam",
    "Status",
    "Rechtsvorm",
    "Adres",
    "zetel",
    "NACE",
    "87.",
    "vestiging",
    "E-mail",
    "Web",
    "Actief",
    "De Panne",
    "8660",
    "Oprichtingsdatum",
]:
    idx = text.lower().find(key.lower())
    if idx >= 0:
        print(key, "=>", text[max(0, idx - 40) : idx + 160])
        print("---")

# Also NL companyweb for address
nl = Path(r"docs/doge/data/raw/tick2163/bernardus_nl.html").read_text(encoding="utf-8", errors="ignore")
for pat in [
    r"8660[^<]{0,80}",
    r"De Panne[^<]{0,40}",
    r"adress[^<]{0,120}",
    r"Adres[^<]{0,120}",
    r"Street[^<]{0,120}",
    r"Kerkstraat[^<]{0,40}",
    r"Nieuwpoort[^<]{0,40}",
    r"info@[A-Za-z0-9.-]+",
]:
    ms = re.findall(pat, nl, re.I)
    if ms:
        print("NL", pat, ms[:3])

en = Path(r"docs/doge/data/raw/tick2163/bernardus_en.html").read_text(encoding="utf-8", errors="ignore")
for pat in [
    r"Street address[^<{]{0,160}",
    r"8660[^<{]{0,80}",
    r"De Panne[^<{]{0,40}",
    r"Company size[^<{]{0,80}",
    r"Employees[^<{]{0,80}",
    r"Established[^<{]{0,80}",
    r"Commercial name[^<{]{0,120}",
    r"Full name[^<{]{0,120}",
]:
    ms = re.findall(pat, en, re.I)
    if ms:
        print("EN", pat[:30], "=>", ms[0][:150])

# site3 check - might be Gent wrong Bernardus
s3 = Path(r"docs/doge/data/raw/tick2163/bernardus_site3.html").read_text(encoding="utf-8", errors="ignore")
print("site3 title", re.search(r"<title>([^<]+)", s3))
print("site3 panne?", "Panne" in s3, "Gent" in s3, "Zwijnaarde" in s3)

s2 = Path(r"docs/doge/data/raw/tick2163/bernardus_site2.html").read_text(encoding="utf-8", errors="ignore")
print("site2 title", re.search(r"<title>([^<]+)", s2))
print("site2 panne?", "Panne" in s2, "Bornem" in s2 or "bornem" in s2.lower())
