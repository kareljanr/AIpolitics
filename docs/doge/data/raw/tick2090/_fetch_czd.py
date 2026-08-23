# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2090")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
KBO = "0471475527"


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = resp.read()
        print("OK", name, len(data), resp.geturl())
    text = data.decode("utf-8", "replace")
    text = re.sub(r"pk\.[A-Za-z0-9._\-]+", "pk.REDACTED", text)
    text = re.sub(r"sk\.[A-Za-z0-9._\-]+", "sk.REDACTED", text)
    (RAW / name).write_text(text, encoding="utf-8")
    return text


for name, url in [
    ("czd_nl.html", f"https://www.companyweb.be/nl/{KBO}/zilvervogel"),
    ("czd_en.html", f"https://www.companyweb.be/en/{KBO}/zilvervogel"),
    ("czd_fr.html", f"https://www.companyweb.be/fr/{KBO}/zilvervogel"),
    ("kbo_czd.html", f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}"),
]:
    fetch(name, url)

t = (RAW / "czd_nl.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)</title>", t).group(1)[:140])
for ym in list(
    re.finditer(
        r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
        t,
    )
)[:3]:
    print("Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
print("FILED", re.search(r"neergelegd op ([0-9\-]+)", t).group(0))
print("FTE", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t).group(1))
print("spans", re.findall(r"<span>([\d.,]+)</span>", t)[:6])

kbo = (RAW / "kbo_czd.html").read_text(encoding="utf-8", errors="replace")
idx = kbo.find("Adres van de zetel")
print("ADDR", re.sub(r"<[^>]+>", " ", kbo[idx : idx + 400]))
for pat in [
    r"pageactief\">([^<]+)",
    r"Vereniging zonder winstoogmerk",
    r"vestigingseenheden \(VE\):.*?<strong>([^<]+)",
    r"87\.\d+",
    r"aanbested",
    r"Zilvervogel|CZD|Lo-Reninge|8647",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:140])

for name, url in [
    ("czd_site.html", "https://www.zilvervogel.be/"),
    ("czd_site2.html", "https://zilvervogel.be/"),
    ("czd_site3.html", "https://www.czd.be/"),
]:
    try:
        text = fetch(name, url)
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [
            e
            for e in emails
            if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare", "redacted"))
        ]
        print("SITE", name, emails[:8])
    except Exception as e:
        print("FAIL", name, e)

# also check unused
import csv

csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if "zilvervogel" in str(r).lower() or "0471.475.527" in str(r) or "0471475527" in str(r) or "czd" == (r.get("entity_id") or ""):
            print("ENT HIT", r.get("entity_id"))
