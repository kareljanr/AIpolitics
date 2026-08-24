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
    ("lork_nl.html", "https://www.companyweb.be/nl/0446022331/foyer-de-lork"),
    ("lork_fr.html", "https://www.companyweb.be/fr/0446022331"),
    ("lork_kbo.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0446022331"),
    ("lork_site.html", "https://www.foyerdelork.be/"),
]:
    try:
        t = fetch(url, out / name)
        print("OK", name, len(t))
    except Exception as e:
        print("FAIL", name, e)

t = (out / "lork_en_full.html").read_text(encoding="utf-8", errors="ignore")
fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
print("fte", fte.group(1) if fte else "-")

k = (out / "lork_kbo.html").read_text(encoding="utf-8", errors="ignore")
kp = re.sub(r"<[^>]+>", " ", k)
kp = re.sub(r"\s+", " ", kp)
for key in ["Status", "Actief", "Adres", "Hazenhout", "vestigingseenheden", "E-mail", "Telefoon", "Aanbestedende", "NACE", "87.", "Rechtsvorm"]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print(key, ":", kp[max(0, i - 15) : i + 140])

s = (out / "lork_site.html").read_text(encoding="utf-8", errors="ignore") if (out / "lork_site.html").exists() else ""
emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+", s)))
print("site emails", emails[:15])
