# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

out = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218")
ctx = ssl.create_default_context()
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
num = "0452454124"
slug = "veerkracht-4"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read()


for lang, path_slug in [
    ("nl", "veerkracht-4"),
    ("fr", "veerkracht-4"),
    ("en", "veerkracht-4"),
]:
    url = f"https://www.companyweb.be/{lang}/{num}/{path_slug}"
    data = fetch(url)
    (out / f"veerkracht4_{lang}.html").write_bytes(data)
    print(lang, "bytes", len(data))

# KBO
kbo_url = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
    f"?lang=nl&ondernemingsnummer={num}"
)
try:
    data = fetch(kbo_url)
    (out / "kbo.html").write_bytes(data)
    print("kbo", len(data))
except Exception as e:
    print("kbo FAIL", e)

# site
for site in [
    "https://www.veerkracht4.be/",
    "https://www.veerkracht4.be/contact",
    "https://www.veerkracht4.be/over",
]:
    try:
        data = fetch(site)
        name = site.rstrip("/").split("/")[-1] or "home"
        (out / f"site_{name}.html").write_bytes(data)
        print("site", name, len(data))
    except Exception as e:
        print("site FAIL", site, e)

t = (out / "veerkracht4_en.html").read_text(encoding="utf-8", errors="ignore")
# extract full year objects
blocks = re.findall(
    r"(20(?:24|25))\s*:\s*(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})", t
)
for y, blk in blocks:
    print("YEAR", y)
    print(blk[:500])

# FTE / employees
for pat in [
    r'fte[_\"]?\s*[:=]\s*"?([\d.,]+)"?',
    r'employees[_\"]?\s*[:=]\s*"?([\d.,]+)"?',
    r"Employees.{0,200}?([\d]+[.,]\d+)",
    r"gemiddelde.*?([\d]+[.,]\d+)",
    r"werknemers.{0,80}?([\d]+[.,]\d+)",
]:
    ms = re.findall(pat, t, re.I | re.S)
    if ms:
        print("pat", pat[:40], ms[:8])

# establishments / VE
ve = re.findall(r"(?:establishment|vestiging|VE).{0,40}?(\d+)", t, re.I)
print("ve-ish", ve[:10])

# NACE
nace = re.findall(r"(88\.\d{3}|94\.\d{3}|81\.\d{3}|43\.\d{3})", t)
print("nace", sorted(set(nace))[:20])

# filing date
filed = re.search(r"filed on ([0-9\-]+)", t, re.I)
print("filed", filed.group(1) if filed else None)

# address
addr = re.search(r"([\w\.\- ]+\d[^,]{0,40},\s*\d{4}\s+[A-Za-z\- ]+)", t)
print("addr sample", addr.group(1)[:80] if addr else None)

# faq omzet text
faq = re.search(r"brutomarge van Veerkracht 4 is € ([0-9\.,]+)", t)
print("faq bruto nl-ish", faq.group(1) if faq else None)
faq2 = re.search(r"Gross margin of Veerkracht 4 is € ([0-9\.,]+)", t, re.I)
print("faq bruto en", faq2.group(1) if faq2 else None)
