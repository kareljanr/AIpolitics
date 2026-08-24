# -*- coding: utf-8 -*-
import urllib.request
from pathlib import Path

base = Path("docs/doge/data/raw/tick2137")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-doge/1.0)"}
urls = {
    "corolles_cw_nl.html": "https://www.companyweb.be/nl/0440737514/les-corolles",
    "corolles_cw_fr.html": "https://www.companyweb.be/fr/0440737514/les-corolles",
    "corolles_cw_en.html": "https://www.companyweb.be/en/0440737514/les-corolles",
    "corolles_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0440737514"
    ),
    "faro_cw_en.html": (
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"
    ),
    "aiesh_cw_en.html": (
        "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut"
    ),
    "corolles_site.html": "https://www.lavertefeuille.be/",
}
for name, url in urls.items():
    path = base / name
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=45) as r:
            data = r.read()
        path.write_bytes(data)
        print(f"OK {name} {len(data)}")
    except Exception as e:
        print(f"FAIL {name}: {e}")
