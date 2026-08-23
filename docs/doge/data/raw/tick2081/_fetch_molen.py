# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2081")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = resp.read()
        final = resp.geturl()
    (RAW / name).write_bytes(data)
    print("OK", name, len(data), final)


URLS = {
    "molenheide_nl.html": "https://www.companyweb.be/nl/0810616132/molenheide-woonzorgcentrum",
    "molenheide_en.html": "https://www.companyweb.be/en/0810616132/molenheide-woonzorgcentrum",
    "molenheide_fr.html": "https://www.companyweb.be/fr/0810616132/molenheide-woonzorgcentrum",
    "kbo_molen.html": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0810616132",
}
for n, u in URLS.items():
    try:
        fetch(n, u)
    except Exception as e:
        print("FAIL", n, e)

t = (RAW / "molenheide_nl.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)</title>", t).group(1)[:140])
for ym in re.finditer(
    r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
    t,
):
    print("Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
filed = re.search(r"neergelegd op ([0-9\-]+)", t)
print("FILED", filed.group(0) if filed else "?")
print("FTE", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t).group(1))
spans = re.findall(r"<span>(\d+[\.,]\d)</span>", t)
print("spans", spans[:5])

# site candidates
for name, url in [
    ("molen_site.html", "https://www.molenheide.be/"),
    ("molen_site2.html", "https://molenheidewzc.be/"),
    ("molen_site3.html", "https://www.woonzorgcentrummolenheide.be/"),
]:
    try:
        fetch(name, url)
        text = (RAW / name).read_text(encoding="utf-8", errors="replace")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [e for e in emails if not any(x in e for x in ("sentry", "wixpres", "example", "cloudflare"))]
        print("SITE emails", name, emails[:8])
    except Exception as e:
        print("FAIL", name, e)

kbo = (RAW / "kbo_molen.html").read_text(encoding="utf-8", errors="replace")
for pat in [r"Actief", r"Vereniging|Besloten|Naamloze", r"Wijnegem", r"vestigingseenheden \(VE\):.*?<strong>([^<]+)", r"87\.\d+", r"aanbested"]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:100])
