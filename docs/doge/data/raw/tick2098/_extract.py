# -*- coding: utf-8 -*-
"""Extract SLG metadata from CW + KBO HTML."""
import re
from pathlib import Path

RAW = Path(__file__).resolve().parent
nl = (RAW / "slg_nl.html").read_text(encoding="utf-8")
kbo = (RAW / "slg_kbo.html").read_text(encoding="utf-8")

# strip scripts
def scrub(h):
    h = re.sub(r"<script[^>]*>.*?</script>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<style[^>]*>.*?</style>", " ", h, flags=re.S | re.I)
    return h

nls = scrub(nl)
kbos = scrub(kbo)

# financial table rows visible
for label in [
    "Winst/Verlies",
    "Omzet",
    "Eigen vermogen",
    "Brutomarge",
    "Personeel",
    "Balans totaal",
    "Schulden",
    "EBITDA",
]:
    m = re.search(rf"{label}.*?(?=</tr>|<tr)", nls, re.S | re.I)
    if m:
        cells = re.findall(r">\s*([^<>]{1,40}?)\s*<", m.group(0))
        print(label, [c.strip() for c in cells if c.strip()][:12])

# JSON-ish years already known
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
print("YEARS", PAT.findall(nl)[:4])

# address / name
for pat in [
    r'itemprop="streetAddress"[^>]*>([^<]+)',
    r'itemprop="postalCode"[^>]*>([^<]+)',
    r'itemprop="addressLocality"[^>]*>([^<]+)',
    r"Maatschappelijke zetel[^<]{0,40}</[^>]+>\s*<[^>]+>([^<]+)",
    r"Grasmarkt|Kontich|Stationsstraat|Alsemberg|Prins|",
]:
    m = re.search(pat, nls, re.I)
    if m and m.lastindex:
        print("ADDR", pat[:30], m.group(1)[:80])

# free text address
m = re.search(r"(\d{4}\s+[A-Za-z\- ]+).*?(Kontich|Antwerpen)", nls)
print("LOC hint", m.group(0)[:100] if m else None)
m = re.search(r"([A-Za-z][A-Za-z0-9 .'\-]{5,60})\s*,?\s*2550\s+Kontich", nls)
print("STREET", m.group(0) if m else None)

# FTE from personnel table - look for Middelgroot / FTE
for m in re.finditer(r"(Middelgroot|Klein|Groot)[^<]{0,40}([\d.,]+)\s*FTE", nls, re.I):
    print("SIZE", m.group(0))
for m in re.finditer(r">([\d]+[.,]\d+)<", nls):
    pass
# personnel column often near 'Personeel'
m = re.search(
    r"Personeel.*?<td[^>]*>\s*([\d]+[.,]\d+|[\d]+)\s*<",
    nls,
    re.S | re.I,
)
print("PERS TD", m.group(1) if m else None)
# alternate: Bedrijfsgrootte
m = re.search(r"Bedrijfsgrootte.*?</td>\s*<td[^>]*>\s*([^<]+)", nls, re.S | re.I)
print("GROOTTE", m.group(1).strip() if m else None)

# NACE from KBO
for m in re.finditer(
    r"(?:Nace[^<]{0,40}|Activiteit[^<]{0,80})(.*?)</tr>",
    kbos,
    re.S | re.I,
):
    txt = re.sub(r"<[^>]+>", " ", m.group(0))
    txt = re.sub(r"\s+", " ", txt).strip()
    if len(txt) > 20:
        print("KBO ACT", txt[:200])

# status / rechtsvorm / VE
for label in [
    "Status van de entiteit",
    "Rechtsvorm",
    "Aantal vestigingen",
    "Start datum",
    "Eind datum",
    "Aard van de gegevens",
]:
    m = re.search(rf"{label}</td>\s*<td[^>]*>(.*?)</td>", kbos, re.S | re.I)
    if m:
        txt = re.sub(r"<[^>]+>", " ", m.group(1))
        print(label, re.sub(r"\s+", " ", txt).strip()[:120])

# aanbestedende
print("AANBEST", bool(re.search(r"aanbestedende|pouvoir adjudicateur", kbos, re.I)))

# website / email on CW
for m in re.finditer(r'href="(https?://(?!www\.companyweb)[^"]+)"', nls):
    u = m.group(1)
    if "facebook" in u or "linkedin" in u or "twitter" in u:
        continue
    if any(x in u for x in ("http",)):
        print("LINK", u[:120])
for m in re.finditer(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", nls + kbos):
    print("EMAIL", m.group(0))

# % changes
for m in re.finditer(r"(\d[\d.]*)\s*%", nls):
    pass
# YoY from table classes
m = re.findall(r'data-year="2025"[^>]*>.*?([\+\-]?[\d.,]+)\s*%', nls, re.S)
print("PCT samples", m[:10])

# Always Home / Armonea board?
for key in ["Armonea", "Always", "Colis", "Orpea", "emeis", "Senior Living", "SLG", "Kontich"]:
    if key.lower() in nls.lower() or key.lower() in kbos.lower():
        print("KEYHIT", key)

# print a window around zetel
m = re.search(r".{0,80}2550 Kontich.{0,80}", nls)
print("ZETELWIN", m.group(0).replace("\n", " ") if m else None)
m = re.search(r".{0,80}2550 Kontich.{0,80}", kbos)
print("KBOZETEL", m.group(0).replace("\n", " ") if m else None)
