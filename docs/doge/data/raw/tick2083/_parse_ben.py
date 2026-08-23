# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2083")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

hits = []
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        s = str(r).lower()
        if (
            ("ben" in s and "woonzorg" in s)
            or "0416.493.254" in str(r)
            or "0416493254" in str(r)
        ):
            hits.append(("ENT", r.get("entity_id"), r.get("name_nl")))
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        s = str(r).lower()
        if (
            "0416493254" in str(r)
            or "0416.493.254" in str(r)
            or "ben woonzorg" in s
            or "ben_woonzorg" in s
            or "vzw_ben" in s
        ):
            hits.append(("RQ", r["task_id"], r["status"], (r.get("title") or "")[:80]))
print("HITS", hits if hits else "NONE — unused OK")

# fetch full set
for name, url in [
    ("ben_nl.html", "https://www.companyweb.be/nl/0416493254/ben-woonzorgnetwerk"),
    ("ben_en.html", "https://www.companyweb.be/en/0416493254/ben-woonzorgnetwerk"),
    ("ben_fr.html", "https://www.companyweb.be/fr/0416493254/ben-woonzorgnetwerk"),
    ("kbo_ben.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416493254"),
]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = resp.read()
        print("OK", name, len(data), resp.geturl())
    (RAW / name).write_bytes(data)

t = (RAW / "ben_nl.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)</title>", t).group(1)[:140])
for ym in list(
    re.finditer(
        r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
        t,
    )
)[:4]:
    print(
        "Y",
        ym.group(1),
        "winst",
        ym.group(2),
        "equity",
        ym.group(3),
        "bruto",
        ym.group(4),
        "omzet",
        ym.group(5),
    )
print("FILED", re.search(r"neergelegd op ([0-9\-]+)", t).group(0))
print("FTE", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t).group(1))
print("spans", re.findall(r"<span>(\d+[\.,]\d)</span>", t)[:5])

kbo = (RAW / "kbo_ben.html").read_text(encoding="utf-8", errors="replace")
idx = kbo.find("Adres van de zetel")
print("ADDR", re.sub(r"<[^>]+>", " ", kbo[idx : idx + 350]))
for pat in [r"pageactief\">([^<]+)", r"Vereniging zonder winstoogmerk", r"vestigingseenheden \(VE\):.*?<strong>([^<]+)", r"87\.\d+", r"aanbested"]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:120])

# site
for name, url in [
    ("ben_site.html", "https://www.benwoonzorg.be/"),
    ("ben_site2.html", "https://www.ben-woonzorgnetwerk.be/"),
    ("ben_site3.html", "https://benwoonzorgnetwerk.be/"),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
            final = resp.geturl()
        text = data.decode("utf-8", "replace")
        text = re.sub(r"pk\.[A-Za-z0-9._\-]+", "pk.REDACTED", text)
        text = re.sub(r"sk\.[A-Za-z0-9._\-]+", "sk.REDACTED", text)
        (RAW / name).write_text(text, encoding="utf-8")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [e for e in emails if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare", "redacted"))]
        print("SITE", name, final, emails[:8])
    except Exception as e:
        print("FAIL", name, e)
