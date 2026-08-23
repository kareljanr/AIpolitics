# ephemeral — fetch AZ Oostende NL/FR/KBO/site for tick2008
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2008")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

urls = [
    ("azo_nl", "https://www.companyweb.be/nl/0800023336/algemeen-ziekenhuis-oostende"),
    ("azo_fr", "https://www.companyweb.be/fr/0800023336/algemeen-ziekenhuis-oostende"),
    (
        "azo_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0800023336",
    ),
    ("azo_site", "https://www.azo.be/"),
]
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, len(data))
    except Exception as e:
        print("FAIL", name, e)
