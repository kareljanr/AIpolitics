# ephemeral fetch extras tick2021
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2021")
urls = {
    "ppc_pittem_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409956147",
    "ppc_pittem_site": "https://www.ppcpittem.be/contact",
    "aiesh2": "https://www.companyweb.be/en/0204530555",
    "rew2": "https://www.companyweb.be/en/0202765933",
    "agb_bornem_site": "https://www.bornem.be/",
}
for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        m = re.search(
            r"(Last balance sheet year|Laatste balansjaar).{0,120}?(\d{4}|N/A)",
            html,
            re.S | re.I,
        )
        print(name, "ok", len(html), "year", m.group(2) if m else None)
    except Exception as e:
        print(name, "FAIL", type(e).__name__, e)
