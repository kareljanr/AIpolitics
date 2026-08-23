# ephemeral fetch tick2034 Sint-Bernardus Assenede
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2034")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()

for name, url in [
    ("bernardus_nl", "https://www.companyweb.be/nl/0445106274/wzc-sint-bernardus"),
    ("bernardus_en", "https://www.companyweb.be/en/0445106274/wzc-sint-bernardus"),
    ("bernardus_fr", "https://www.companyweb.be/fr/0445106274/wzc-sint-bernardus"),
    (
        "bernardus_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445106274",
    ),
    ("bernardus_site", "https://www.wzcsintbernardus.be/"),
    ("bernardus_site2", "https://www.sintbernardusassenede.be/"),
    ("agb_en", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    (
        "faro_en",
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    ),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        title = re.search(r"<title>([^<]+)</title>", html)
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
        )
        print(
            name,
            "ok",
            (title.group(1)[:70] if title else None),
            "emails",
            emails[:6],
        )
        if "kbo" in name:
            m = re.search(r"Aantal vestigingseenheden.{0,160}", html, re.S)
            print(" VE", re.sub(r"<[^>]+>", " ", m.group(0))[:100] if m else None)
            m = re.search(r"Adres van de zetel.{0,200}", html, re.S)
            if m:
                print(" addr", re.sub(r"<[^>]+>", " ", m.group(0))[:160])
        if name in ("agb_en", "faro_en"):
            i = html.find("Last balance sheet year")
            m = (
                re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if i >= 0
                else None
            )
            print(" year", m.group(1) if m else None)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
