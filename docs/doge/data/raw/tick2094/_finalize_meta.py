# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# Bornem correct URL from prior tick HTML
url = "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"
req = urllib.request.Request(url, headers=UA)
try:
    with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
        html = r.read().decode("utf-8", errors="replace")
    (OUT / "bornem_jr.html").write_text(html, encoding="utf-8")
    print("BORNEM OK", len(html))
    for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{0,120})', html, re.I):
        href, txt = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
        blob = (href + " " + txt).lower()
        if any(k in blob for k in ["jaarrekening", "agb", "2025", "2024", "pdf", "bbc", "2023"]):
            print(" ", txt[:80], "->", href[:160])
    # also plain text years
    plain = re.sub(r"<[^>]+>", " ", html)
    plain = re.sub(r"\s+", " ", plain)
    for y in ["2025", "2024", "2023"]:
        if f"jaarrekening {y}" in plain.lower() or f"JR{y}" in plain or f"jaar {y}" in plain.lower():
            print(" year mention", y)
    # pdf links
    for m in re.finditer(r'href="([^"]+\.pdf[^"]*)"', html, re.I):
        print(" PDF", m.group(1)[:160])
except Exception as e:
    print("BORNEM FAIL", e)

# VE from KBO
kbo = (OUT / "lucia_kbo.html").read_text(encoding="utf-8", errors="replace")
# count establishment units table rows or "Aantal vestigingseenheden"
for pat in [
    r"Aantal vestigingseenheden[^0-9]{0,40}(\d+)",
    r"vestigingseenheid",
    r"Number of establishment units[^0-9]{0,40}(\d+)",
]:
    ms = re.findall(pat, kbo, re.I)
    print("VE pat", pat[:40], ms[:10] if isinstance(ms, list) else ms)

# list VE addresses
text = re.sub(r"<script[\s\S]*?</script>", " ", kbo, flags=re.I)
text = re.sub(r"<[^>]+>", "\n", text)
lines = [re.sub(r"\s+", " ", L).strip() for L in text.splitlines() if L.strip()]
for i, L in enumerate(lines):
    if "vestiging" in L.lower() or "Clarissen" in L or "Clarissendreef" in L or re.match(r"2\.\d+\.\d+", L):
        print("L", L[:120])

# FTE YoY - check if historical FTE in lucia pages
nl = (OUT / "lucia_nl.html").read_text(encoding="utf-8")
# sometimes chart has years
m = re.search(r"amountOfEmployees\s*=\s*\"([^\"]+)\"", nl)
print("FTE now", m.group(1) if m else None)
# look for employeesByYear or similar
for key in ["employees", "personeel", "werknemers", "fteHistory", "employeesHistory"]:
    i = nl.lower().find(key.lower())
    if i >= 0 and "amountOfEmployees" not in key:
        snippet = nl[i : i + 400]
        if "2024" in snippet or "2025" in snippet:
            print(key, re.sub(r"\s+", " ", snippet)[:250])

# site contact page
for url, name in [
    ("https://www.sint-lucia.be/contact", "lucia_contact.html"),
    ("https://www.sint-lucia.be/contacteer-ons", "lucia_contact2.html"),
]:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            html = r.read().decode("utf-8", errors="replace")
        (OUT / name).write_text(html, encoding="utf-8")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
        print("CONTACT", url, emails[:8], "len", len(html))
    except Exception as e:
        print("CONTACT FAIL", url, e)

# YoY calc
om25, om24 = 7669915, 7451613
br25, br24 = 8087569, 8164107
pn25, pn24 = 158746, 315038
eq25, eq24 = 12346388, 12441379


def pct(a, b):
    return (a - b) / abs(b) * 100


print(f"omzet YoY {pct(om25,om24):+.2f}%")
print(f"bruto YoY {pct(br25,br24):+.2f}%")
print(f"pnl YoY {pct(pn25,pn24):+.2f}%")
print(f"equity YoY {pct(eq25,eq24):+.2f}%")
