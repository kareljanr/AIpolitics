# -*- coding: utf-8 -*-
import re
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2088")


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


for name in ["faro_nl.html", "aiesh_nl.html", "rew_nl.html", "ocura_nl.html", "ocura_en.html"]:
    p = RAW / name
    if p.exists():
        parse(p)

kbo = (RAW / "kbo_ocura.html").read_text(encoding="utf-8", errors="replace")
idx = kbo.find("Adres van de zetel")
print("ADDR", re.sub(r"<[^>]+>", " ", kbo[idx : idx + 450]))
for pat in [
    r"pageactief\">([^<]+)",
    r"Vereniging zonder winstoogmerk",
    r"vestigingseenheden \(VE\):.*?<strong>([^<]+)",
    r"87\.\d+",
    r"aanbested",
    r"Beringen|3582",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBO", re.sub(r"\s+", " ", m.group(0))[:140])

for site in ["site_www.ocura.be_.html", "site_www.ocura.be_beringen_contact.html"]:
    p = RAW / site
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", t)))
    emails = [
        e
        for e in emails
        if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare", "jquery"))
    ]
    print("SITE", site, emails[:12])
