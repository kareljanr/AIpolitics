# ephemeral — KBO/site/email for OLVT / AZ Sint-Blasius
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2009")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data), resp.geturl()[:100])


for name, url in [
    (
        "blasius_kbo2",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411975133",
    ),
    ("blasius_site2", "https://www.azsintblasius.be/"),
    ("blasius_contact", "https://www.azsintblasius.be/contact"),
]:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name in ["blasius_kbo", "blasius_kbo2", "blasius_home", "blasius_site", "blasius_site2", "blasius_contact", "blasius_olv_nl"]:
    p = dst / f"{name}.html"
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    print("==", name, "==")
    emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", t)))
    print(" emails", [e for e in emails if not any(x in e for x in ("sentry", "wght", "example", "wix")) ][:15])
    for lab in ["Status", "Actief", "vestigingseenheden", "Naam", "E-mail", "OLVT", "Blasius", "0411"]:
        i = t.find(lab)
        if i >= 0:
            print(lab, repr(t[i : i + 160]))
    print()
