# -*- coding: utf-8 -*-
"""Fetch Langerheide WZC YE2025 mirrors + KBO."""
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2173")
out.mkdir(parents=True, exist_ok=True)
kbo = "0864332554"


def fetch(url, name):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
    (out / name).write_bytes(data)
    print("OK", name, len(data))
    return data.decode("utf-8", "ignore")


def parse(t):
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed = re.search(
        r"(?:filed on|neergelegd op|déposés le)\s*([0-9./-]{8,12})", t or "", re.I
    )
    title = re.search(r"<title>([^<]+)", t or "")
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", t or "", re.I)
    act = re.search(r"(?:Principal activity|Hoofdactiviteit|Activité principale)</[^>]+>\s*([^<]+)", t or "", re.I)
    email = re.search(r"([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})", t or "")
    return yb, fte, filed, title, last, act, email


for lang, name in [
    ("nl", "langerheide_nl.html"),
    ("en", "langerheide_en.html"),
    ("fr", "langerheide_fr.html"),
]:
    t = fetch(f"https://www.companyweb.be/{lang}/{kbo}", name)
    yb, fte, filed, title, last, act, email = parse(t)
    print(lang, (title.group(1) if title else "")[:70])
    print("  last", last.group(1) if last else None, "filed", filed.group(1) if filed else None)
    print("  2025", yb.get("2025"))
    print("  2024", yb.get("2024"))
    print("  fte", fte.group(1) if fte else None, "act", (act.group(1).strip() if act else "")[:80])
    print("  email", email.group(1) if email else None)

kbo_html = fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0864332554",
    "langerheide_kbo.html",
)
print("Actief", "Actief" in kbo_html)
text = re.sub(r"<[^>]+>", " ", kbo_html)
text = re.sub(r"\s+", " ", text)
for pat in [
    "vestigingseenhe",
    "87.",
    "E-mail",
    "email",
    "Rechtsvorm",
    "Adres",
    "Haacht",
    "Langerheide",
    "NACE",
    "RSZ",
    "aanbestedende",
]:
    i = text.lower().find(pat.lower())
    if i >= 0:
        print(text[max(0, i - 30) : i + 120])
        print("---")
