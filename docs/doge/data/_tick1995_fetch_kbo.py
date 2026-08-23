import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick1995")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

urls = [
    ("haute_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0256981407"),
    ("haute_site", "https://www.chrhautesenne.be/"),
    ("cndg_fr", "https://www.companyweb.be/fr/0401690559/clinique-notre-dame-de-grace"),
    ("verviers_fr", "https://www.companyweb.be/fr/0250893369/centre-hospitalier-regional-de-verviers"),
]
for name, url in urls:
    req = urllib.request.Request(url, headers=ua)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            data = r.read()
        (dst / f"{name}.html").write_bytes(data)
        print(name, "OK", len(data))
    except Exception as e:
        print(name, "FAIL", e)

kbo = (dst / "haute_kbo.html").read_text(encoding="utf-8", errors="replace")
clean = re.sub(r"<[^>]+>", " ", kbo)
clean = re.sub(r"\s+", " ", clean)
for needle in [
    "Actief",
    "Rechtsvorm",
    "E-mail",
    "Webadres",
    "Aanbested",
    "Soignies",
    "Haute",
    "VZW",
    "Association",
    "vestiging",
]:
    i = clean.lower().find(needle.lower())
    if i >= 0:
        print("KBO", needle, repr(clean[max(0, i - 40) : i + 140]))

site = (dst / "haute_site.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site)))
print("site emails", emails[:20])
