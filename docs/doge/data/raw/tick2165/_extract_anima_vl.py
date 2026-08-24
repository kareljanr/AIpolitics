# -*- coding: utf-8 -*-
from pathlib import Path
import re
import ssl
import urllib.request
import shutil

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)
kbo = "0698940725"

# copy prior probe if present
src = Path(__file__).resolve().parents[1] / "tick2164" / "anima_vl_en.html"
if src.exists():
    shutil.copy(src, out / "anima_vl_en.html")


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


for name, url in [
    ("anima_vl_en.html", f"https://www.companyweb.be/en/{kbo}"),
    ("anima_vl_nl.html", f"https://www.companyweb.be/nl/{kbo}"),
    ("anima_vl_fr.html", f"https://www.companyweb.be/fr/{kbo}"),
    (
        "anima_vl_kbo.html",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={kbo}",
    ),
    ("anima_site.html", "https://animagroup.be/"),
    ("anima_contact.html", "https://animagroup.be/contact/"),
]:
    try:
        t = fetch(url, out / name)
        print("OK", name, len(t))
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:80])

t = (out / "anima_vl_en.html").read_text(encoding="utf-8", errors="ignore")
title = re.search(r"<title>([^<]+)", t)
print("title", title.group(1)[:130] if title else "?")
for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t)[:4]:

    def g(k, b=body):
        m = re.search(rf'{k}:\s*"([^"]*)"', b)
        return m.group(1) if m else None

    print(y, {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]})
fte = re.search(r"([\d.,]+)\s*FTE", t)
print("fte", fte.group(1) if fte else "-")
filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
print("filed", filed.group(1) if filed else "-")

k = (out / "anima_vl_kbo.html").read_text(encoding="utf-8", errors="ignore")
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
    "aanbestedende",
    "Zandvoort",
]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", kp[max(0, i - 8) : i + 220])

# VE count more carefully
m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", kp)
print("VE_COUNT", m.group(1) if m else "?")

for site in ["anima_site.html", "anima_contact.html"]:
    p = out / site
    if p.exists():
        s = p.read_text(encoding="utf-8", errors="ignore")
        emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", s, re.I)
        print(site, "emails", list(dict.fromkeys(emails))[:12])
