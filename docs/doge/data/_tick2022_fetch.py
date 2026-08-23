# ephemeral fetch tick2022 extras
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2022")
urls = [
    (
        "maria_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0458458325",
    ),
    ("maria_site", "https://www.mariasrustoord.be/"),
    ("maria_site2", "https://www.maria-rustoord.be/"),
    (
        "maria_zoek",
        "https://www.google.com/search?q=Maria+Rustoord+Ingelmunster+email+contact",
    ),
]
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
        )
        print(name, "ok", len(html), "emails", emails[:8])
        if "kbo" in name:
            m = re.search(r"Aantal vestigingseenheden.{0,180}", html, re.S)
            print(" VE", re.sub(r"<[^>]+>", " ", m.group(0))[:120] if m else None)
            m = re.search(r"Weststraat.{0,80}|Adres van de zetel.{0,200}", html, re.S)
            if m:
                print(" addr", re.sub(r"<[^>]+>", " ", m.group(0))[:160])
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
