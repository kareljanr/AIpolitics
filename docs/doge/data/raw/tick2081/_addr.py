# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2081")
t = (RAW / "wijshage_nl.html").read_text(encoding="utf-8", errors="replace")
kbo = (RAW / "kbo_wij.html").read_text(encoding="utf-8", errors="replace")

# CW address fields
for key in ["address", "street", "city", "zip", "email", "website", "phone"]:
    ms = re.findall(rf"{key}[\"']?\s*[:=]\s*[\"']([^\"']+)", t, re.I)
    if ms:
        print(key, ms[:5])

m = re.search(r"Adres van de zetel:.*?</table>", kbo, re.S | re.I)
if not m:
    m = re.search(r"Adres van de zetel:.*", kbo, re.S | re.I)
print("KBOADDR raw snippet:")
idx = kbo.find("Adres van de zetel")
print(re.sub(r"<[^>]+>", " | ", kbo[idx : idx + 500]))

emails = re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", t)
print("CW emails", emails[:10])

UA = "Mozilla/5.0"
for name, url in [
    ("wij_sociale.html", "https://www.desocialekaart.be/?s=Wijshage"),
    ("wij_goud.html", "https://www.goudengids.be/zoeken/WZC%20De%20Wijshage%20Rumst/"),
    ("wij_info.html", "https://www.companyweb.be/nl/0449425546"),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            data = r.read()
            final = r.geturl()
        (RAW / name).write_bytes(data)
        text = data.decode("utf-8", "replace")
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text))
        )
        emails = [
            e
            for e in emails
            if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare"))
        ]
        print(name, final[:90], "emails", emails[:8])
        for m in re.finditer(r".{0,40}(straat|laan|Rumst|2840|@).{0,40}", text, re.I):
            s = re.sub(r"\s+", " ", m.group(0))
            if "Rumst" in s or "@" in s or "straat" in s.lower():
                print(" ", s[:140])
                break
    except Exception as e:
        print("FAIL", name, e)

# From KBO HTML specifically parse street
for line in kbo.splitlines():
    if "Rumst" in line or "straat" in line.lower() or "Wijtshage" in line:
        print("KLINE", re.sub(r"<[^>]+>", "", line).strip()[:160])
