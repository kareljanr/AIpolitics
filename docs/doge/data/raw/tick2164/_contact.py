# -*- coding: utf-8 -*-
import re

t = open(
    "docs/doge/data/raw/tick2164/zorgsaam_site1.html", encoding="utf-8", errors="replace"
).read()
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
emails = [
    e
    for e in emails
    if not any(
        x in e.lower()
        for x in ("wix", "example", "sentry", "schema", "cloudflare", "dynamate")
    )
]
print("emails unique:")
for e in sorted(set(emails)):
    print(" ", e)

for pat in [
    r"info@[^\s\"'<>]+",
    r"secretariaat@[^\s\"'<>]+",
    r"contact@[^\s\"'<>]+",
    r"Onze Lieve Vrouwstraat[^<]{0,100}",
    r"9041[^<]{0,80}",
]:
    ms = re.findall(pat, t, re.I)
    print(pat, ms[:6])

for kw in ["hoofdzetel", "directie", "contacteer", "Onze Lieve", "algemeen nummer"]:
    i = t.lower().find(kw.lower())
    if i >= 0:
        print("KW", kw, re.sub(r"\s+", " ", t[i : i + 220])[:200])

# also check contact page
import ssl, urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
for url in [
    "https://www.zorg-saam.be/contact",
    "https://www.zorg-saam.be/over-ons",
    "https://www.zorg-saam.be/nl/contact",
]:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            html = r.read().decode("utf-8", "ignore")
        print("PAGE", url, len(html))
        em = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        em = [
            e
            for e in em
            if not any(x in e.lower() for x in ("wix", "sentry", "dynamate", "schema"))
        ]
        print("  emails", list(dict.fromkeys(em))[:12])
        open(
            f"docs/doge/data/raw/tick2164/zorgsaam_contact_{url.split('/')[-1]}.html",
            "w",
            encoding="utf-8",
        ).write(html)
    except Exception as e:
        print("FAIL", url, e)
