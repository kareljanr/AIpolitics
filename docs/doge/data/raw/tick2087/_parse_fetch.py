# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2087")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


def parse(path: Path) -> None:
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", path.name)
    title = re.search(r"<title>([^<]+)</title>", t)
    print("TITLE", title.group(1)[:140] if title else "?")
    ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
    print("YE", ye.group(1) if ye else "?")
    for ym in list(
        re.finditer(
            r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
            t,
        )
    )[:3]:
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
    filed = re.search(r"neergelegd op ([0-9\-]+)|filed on ([0-9\-]+)", t, re.I)
    print("FILED", filed.group(0) if filed else "?")
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
    print("FTE", fte.group(1) if fte else "?")
    print("spans", re.findall(r"<span>([\d.,]+)</span>", t)[:6])


for name in [
    "faro_nl.html",
    "aiesh_nl.html",
    "rew_nl.html",
    "cand_0418352387_nl.html",
    "cand_0443072838_nl.html",
    "cand_0410853396_nl.html",
]:
    p = RAW / name
    if p.exists():
        parse(p)

# Take Lindelo first (preference order) — fetch full set
KBO = "0418352387"
slug = "woonzorgcentrum-lindelo"


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
    ("lindelo_nl.html", f"https://www.companyweb.be/nl/{KBO}/{slug}"),
    ("lindelo_en.html", f"https://www.companyweb.be/en/{KBO}/{slug}"),
    ("lindelo_fr.html", f"https://www.companyweb.be/fr/{KBO}/{slug}"),
    ("kbo_lindelo.html", f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}"),
]:
    fetch(name, url)

parse(RAW / "lindelo_nl.html")
kbo = (RAW / "kbo_lindelo.html").read_text(encoding="utf-8", errors="replace")
idx = kbo.find("Adres van de zetel")
print("ADDR", re.sub(r"<[^>]+>", " ", kbo[idx : idx + 400]))
for pat in [
    r"pageactief\">([^<]+)",
    r"Vereniging zonder winstoogmerk",
    r"vestigingseenheden \(VE\):.*?<strong>([^<]+)",
    r"87\.\d+",
    r"aanbested",
    r"Lille|2275",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:140])

for name, url in [
    ("lindelo_site.html", "https://www.lindelo.be/"),
    ("lindelo_site2.html", "https://lindelo.be/"),
    ("lindelo_site3.html", "https://www.woonzorgcentrumlindelo.be/"),
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
