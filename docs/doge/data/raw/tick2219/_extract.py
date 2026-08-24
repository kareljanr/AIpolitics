# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

out = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2219")
out.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
num = "0466209120"
slug = "opnieuw-co"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read()


for lang in ["en", "nl", "fr"]:
    data = fetch(f"https://www.companyweb.be/{lang}/{num}/{slug}")
    (out / f"opnieuw_{lang}.html").write_bytes(data)
    print(lang, len(data))

kbo = fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
    f"?lang=nl&ondernemingsnummer={num}"
)
(out / "kbo.html").write_bytes(kbo)
print("kbo", len(kbo))

for site in [
    "https://www.opnieuw.be/",
    "https://opnieuwenco.be/",
    "https://www.opnieuwenco.be/",
]:
    try:
        data = fetch(site)
        name = site.replace("https://", "").replace("/", "_").strip("_")
        (out / f"site_{name}.html").write_bytes(data)
        print("site", name, len(data))
    except Exception as e:
        print("site FAIL", site, e)

t = (out / "opnieuw_en.html").read_text(encoding="utf-8", errors="ignore")
blocks = re.findall(
    r"(20(?:24|25))\s*:\s*(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})", t
)
for y, b in blocks:
    print("YEAR", y)
    print(b)
print("FTE", re.findall(r"([\d,]+)\s*FTE", t)[:8])
m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
print("amount", m.group(1) if m else None)
f = re.search(r"filed on ([0-9\-]+)", t, re.I)
print("filed", f.group(1) if f else None)

k = (out / "kbo.html").read_text(encoding="utf-8", errors="ignore")
text = re.sub(r"<[^>]+>", " ", k)
text = re.sub(r"\s+", " ", text)
for needle in [
    "Status van de entiteit",
    "Adres van de zetel",
    "Rechtsvorm",
    "Aantal vestiging",
    "88.993",
    "Ullensstraat",
    "Actief",
]:
    i = text.find(needle)
    if i >= 0:
        print("KBO", needle, "->", text[i : i + 140])
print("NACE", re.findall(r"88\.\d{3}|47\.\d{3}|38\.\d{3}|81\.\d{3}", k)[:12])
