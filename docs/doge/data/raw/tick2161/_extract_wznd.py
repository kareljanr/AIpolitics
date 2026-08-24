# -*- coding: utf-8 -*-
from pathlib import Path
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


for name, url in [
    ("wznd_en.html", "https://www.companyweb.be/en/0500952540/woonzorgnet-dijleland"),
    ("wznd_nl.html", "https://www.companyweb.be/nl/0500952540/woonzorgnet-dijleland"),
    ("wznd_fr.html", "https://www.companyweb.be/fr/0500952540"),
    ("wznd_kbo.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0500952540"),
    ("wznd_site.html", "https://www.wznd.be/"),
]:
    try:
        t = fetch(url, out / name)
        print("OK", name, len(t))
    except Exception as e:
        print("FAIL", name, e)

t = (out / "wznd_en.html").read_text(encoding="utf-8", errors="ignore")
year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
print("year", year.group(1) if year else "-")
for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t)[:4]:
    def g(k, b=body):
        m = re.search(rf'{k}:\s*"([^"]*)"', b)
        return m.group(1) if m else None

    print(y, {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]})
fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
print("fte", fte.group(1) if fte else "-")
filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
print("filed", filed.group(1) if filed else "-")

k = (out / "wznd_kbo.html").read_text(encoding="utf-8", errors="ignore")
kp = re.sub(r"<[^>]+>", " ", k)
kp = re.sub(r"\s+", " ", kp)
for key in ["Status", "Actief", "Adres", "Wingerd", "vestigingseenheden", "E-mail", "Telefoon", "Aanbestedende", "NACE", "87.", "Rechtsvorm"]:
    i = kp.lower().find(key.lower())
    if i >= 0:
        print("KBO", key, ":", kp[max(0, i - 10) : i + 140])

if (out / "wznd_site.html").exists():
    s = (out / "wznd_site.html").read_text(encoding="utf-8", errors="ignore")
    emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+", s)))
    print("site emails", emails[:20])
