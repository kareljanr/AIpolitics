# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2080")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

urls = [
    ("site.html", "https://www.denakker.be/"),
    ("site2.html", "https://www.heemvzw.be/"),
    ("cobrha.html", "https://publiek.departementzorg.be/Cobrha/hcoid/WVG_VAZG3963"),
    ("bornem_jr.html", "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"),
]

for name, url in urls:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            data = resp.read()
            final = resp.geturl()
        (RAW / name).write_bytes(data)
        print("OK", name, len(data), final)
    except Exception as e:
        print("FAIL", name, e)

# KBO extract
kbo = (RAW / "kbo_den.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Status:.*?</",
    r"Rechtsvorm:.*?</",
    r"Aantal vestigingseenheden.*?</",
    r"Paloken|Montenaken|Sint-Truiden|aanbested|email|E-mail|Webadres",
    r"87\.\d+",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBOHIT", re.sub(r"\s+", " ", m.group(0))[:200])

# print key KBO lines
for line in kbo.splitlines():
    s = line.strip()
    if any(
        x in s
        for x in [
            "Actief",
            "Vereniging",
            "Montenaken",
            "Sint-Truiden",
            "vestiging",
            "87.",
            "aanbested",
            "E-mail",
            "Webadres",
            "Naam:",
        ]
    ):
        if s and len(s) < 200:
            print("L", s)

for site in ["site.html", "site2.html", "cobrha.html"]:
    p = RAW / site
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", t)))
    print(site, "emails", emails[:15])
    m = re.search(r"<title>([^<]+)</title>", t)
    print(site, "title", m.group(1)[:120] if m else None)

# bornem still 2024?
if (RAW / "bornem_jr.html").exists():
    t = (RAW / "bornem_jr.html").read_text(encoding="utf-8", errors="replace")
    print("BORNEM years", sorted(set(re.findall(r"Jaarrekening\s+(20\d\d)", t))))
