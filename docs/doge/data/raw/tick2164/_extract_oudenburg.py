# -*- coding: utf-8 -*-
from pathlib import Path
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
kbo = "0450755634"


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


for name, url in [
    ("res_oud_en.html", f"https://www.companyweb.be/en/{kbo}"),
    ("res_oud_nl.html", f"https://www.companyweb.be/nl/{kbo}"),
    ("res_oud_fr.html", f"https://www.companyweb.be/fr/{kbo}"),
    (
        "res_oud_kbo.html",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={kbo}",
    ),
]:
    t = fetch(url, out / name)
    print("OK", name, len(t))

t = (out / "res_oud_en.html").read_text(encoding="utf-8", errors="ignore")
title = re.search(r"<title>([^<]+)", t)
print("title", title.group(1)[:120] if title else "?")
year = re.search(r"Last balance sheet year.{0,100}", t, re.S | re.I)
plain = re.sub(r"<[^>]+>", " ", year.group(0)) if year else ""
print("YEAR", re.sub(r"\s+", " ", plain)[:120])
for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t)[:4]:

    def g(k, b=body):
        m = re.search(rf'{k}:\s*"([^"]*)"', b)
        return m.group(1) if m else None

    print(
        y,
        {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]},
    )
fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
print("fte", fte.group(1) if fte else "-")
filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
print("filed", filed.group(1) if filed else "-")
# activity / sector snippets
for pat in [r"NACE[^<]{0,80}", r"87\.\d{3}", r"68\.\d{3}", r"Care Property", r"Armonea", r"Orpea"]:
    m = re.search(pat, t, re.I)
    if m:
        print("hit", pat, ":", re.sub(r"\s+", " ", m.group(0))[:100])

k = (out / "res_oud_kbo.html").read_text(encoding="utf-8", errors="ignore")
kp = re.sub(r"<[^>]+>", " ", k)
kp = re.sub(r"\s+", " ", kp)
for key in [
    "Status",
    "Actief",
    "Adres",
    "Oudenburg",
    "vestigingseenheden",
    "E-mail",
    "NACE",
    "Rechtsvorm",
    "Naam",
    "Bestuurder",
    "87.",
    "68.",
    "aanbestedende",
]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", kp[max(0, i - 10) : i + 180])

# site probe
for name, url in [
    ("res_oud_site.html", "https://www.residentie-oudenburg.be/"),
    ("res_oud_site2.html", "https://residentieoudenburg.be/"),
]:
    try:
        t2 = fetch(url, out / name)
        print("SITE", name, len(t2), re.search(r"<title>([^<]+)", t2).group(1)[:80] if re.search(r"<title>", t2) else "")
        emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", t2, re.I)
        print(" emails", list(dict.fromkeys(emails))[:8])
    except Exception as e:
        print("SITE FAIL", name, type(e).__name__, str(e)[:80])
