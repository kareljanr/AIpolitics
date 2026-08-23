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
    return data


for name, url in [
    ("wijshage_nl.html", "https://www.companyweb.be/nl/0449425546/rust-en-verzorgingstehuis-de-wijtshage"),
    ("wijshage_en.html", "https://www.companyweb.be/en/0449425546/rust-en-verzorgingstehuis-de-wijtshage"),
    ("wijshage_fr.html", "https://www.companyweb.be/fr/0449425546/rust-en-verzorgingstehuis-de-wijtshage"),
    ("kbo_wij.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0449425546"),
]:
    fetch(name, url)

t = (RAW / "wijshage_nl.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)</title>", t).group(1)[:140])
for ym in re.finditer(
    r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
    t,
):
    print("Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
print("FILED", re.search(r"neergelegd op ([0-9\-]+)", t).group(0))
print("FTE", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t).group(1))
print("spans", re.findall(r"<span>(\d+[\.,]\d)</span>", t)[:5])

# site
for name, url in [
    ("wij_site.html", "https://www.dewjtshage.be/"),
    ("wij_site2.html", "https://www.dewjshage.be/"),
    ("wij_site3.html", "https://www.wijshage.be/"),
    ("wij_site4.html", "https://www.woonzorgcentrumdewjshage.be/"),
    ("wij_site5.html", "https://www.dewjishage.be/"),
]:
    try:
        fetch(name, url)
        text = (RAW / name).read_text(encoding="utf-8", errors="replace")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [e for e in emails if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare", "jquery"))]
        print("SITE", name, emails[:8])
    except Exception as e:
        print("FAIL", name, e)

kbo = (RAW / "kbo_wij.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"pageactief\">([^<]+)",
    r"Vereniging zonder winstoogmerk|Naamloze|Besloten",
    r"Rumst|Schoolstraat|Wijshage|Wijtshage",
    r"vestigingseenheden \(VE\):.*?<strong>([^<]+)",
    r"87\.\d+",
    r"aanbested",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:120])

# address from CW
for m in re.finditer(r"Rumst|Schoolstraat|[^<\n]{0,40}2840[^<\n]{0,40}", t):
    print("ADDR", m.group(0)[:100])
    break
# commercial name
for m in re.finditer(r"Wijshage|Wijtshage|commerciële naam[^<]{0,80}", t, re.I):
    print("NAME", re.sub(r"\s+", " ", m.group(0))[:100])
