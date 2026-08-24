# -*- coding: utf-8 -*-
from pathlib import Path
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)
kbo = "0469969453"


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


for name, url in [
    ("anima_en.html", f"https://www.companyweb.be/en/{kbo}"),
    ("anima_nl.html", f"https://www.companyweb.be/nl/{kbo}"),
    ("anima_fr.html", f"https://www.companyweb.be/fr/{kbo}"),
    (
        "anima_kbo.html",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={kbo}",
    ),
    ("anima_site.html", "https://animagroup.be/"),
]:
    try:
        t = fetch(url, out / name)
        print("OK", name, len(t))
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:80])

t = (out / "anima_en.html").read_text(encoding="utf-8", errors="ignore")
title = re.search(r"<title>([^<]+)", t)
print("title", title.group(1)[:120] if title else "?")
for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t)[:4]:

    def g(k, b=body):
        m = re.search(rf'{k}:\s*"([^"]*)"', b)
        return m.group(1) if m else None

    print(y, {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]})
fte = re.search(r"([\d.,]+)\s*FTE", t)
print("fte", fte.group(1) if fte else "-")
filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
print("filed", filed.group(1) if filed else "-")

k = (out / "anima_kbo.html").read_text(encoding="utf-8", errors="ignore")
kp = re.sub(r"<[^>]+>", " ", k)
kp = re.sub(r"\s+", " ", kp)
for key in [
    "Status",
    "Actief",
    "Adres",
    "Mechelen",
    "vestigingseenheden",
    "E-mail",
    "NACE",
    "Rechtsvorm",
    "Naam",
    "87.",
    "70.",
    "64.",
    "Zandvoort",
]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", kp[max(0, i - 8) : i + 200])
m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", kp)
print("VE", m.group(1) if m else "?")
site = (out / "anima_site.html").read_text(encoding="utf-8", errors="ignore")
emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", site, re.I)
print("emails", list(dict.fromkeys(emails))[:10])
