# -*- coding: utf-8 -*-
from pathlib import Path
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


for name, url in [
    ("lorkh_en.html", "https://www.companyweb.be/en/0755822317"),
    ("lorkh_nl.html", "https://www.companyweb.be/nl/0755822317"),
    ("lorkh_fr.html", "https://www.companyweb.be/fr/0755822317"),
    ("lorkh_kbo.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0755822317"),
]:
    t = fetch(url, out / name)
    print("OK", name, len(t))

t = (out / "lorkh_en.html").read_text(encoding="utf-8", errors="ignore")
year = re.search(r"Last balance sheet year.{0,100}", t, re.S | re.I)
plain = re.sub(r"<[^>]+>", " ", year.group(0)) if year else ""
print("YEAR", re.sub(r"\s+", " ", plain)[:100])
for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t)[:4]:

    def g(k, b=body):
        m = re.search(rf'{k}:\s*"([^"]*)"', b)
        return m.group(1) if m else None

    print(y, {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]})
fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
print("fte", fte.group(1) if fte else "-")
filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
print("filed", filed.group(1) if filed else "-")
title = re.search(r"<title>([^<]+)", t)
print("title", title.group(1)[:90] if title else "?")

k = (out / "lorkh_kbo.html").read_text(encoding="utf-8", errors="ignore")
kp = re.sub(r"<[^>]+>", " ", k)
kp = re.sub(r"\s+", " ", kp)
for key in ["Status", "Actief", "Adres", "Schoten", "Kontich", "Satenrozen", "Hoeselt", "vestigingseenheden", "E-mail", "NACE", "87.", "Rechtsvorm", "Naam"]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", kp[max(0, i - 10) : i + 150])
