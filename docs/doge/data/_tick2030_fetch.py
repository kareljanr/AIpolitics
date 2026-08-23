# ephemeral fetch tick2030 St Vincentius Antwerpen
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2030")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()

for name, url in [
    ("vincentius_ant_nl", "https://www.companyweb.be/nl/0418016550/woonzorgcentrum-st-vincentius"),
    ("vincentius_ant_fr", "https://www.companyweb.be/fr/0418016550/woonzorgcentrum-st-vincentius"),
    (
        "vincentius_ant_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418016550",
    ),
    ("vincentius_ant_site", "https://www.vincentiusantwerpen.be/"),
    ("vincentius_ant_site2", "https://www.wzcvincentius.be/"),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
        )
        title = re.search(r"<title>([^<]+)</title>", html)
        print(name, "ok", (title.group(1)[:70] if title else None), "emails", emails[:6])
        if "kbo" in name:
            m = re.search(r"Aantal vestigingseenheden.{0,160}", html, re.S)
            print(" VE", re.sub(r"<[^>]+>", " ", m.group(0))[:100] if m else None)
            m = re.search(r"Adres van de zetel.{0,200}", html, re.S)
            if m:
                print(" addr", re.sub(r"<[^>]+>", " ", m.group(0))[:160])
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
