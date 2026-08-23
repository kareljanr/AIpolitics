import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2094")
RAW.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0; research)"}
urls = {
    "lucia_nl.html": "https://www.companyweb.be/nl/0410151137/sint-lucia",
    "lucia_en.html": "https://www.companyweb.be/en/0410151137/sint-lucia",
    "lucia_fr.html": "https://www.companyweb.be/fr/0410151137/sint-lucia",
    "kbo_lucia.html": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410151137",
    "faro_nl.html": "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_nl.html": "https://www.companyweb.be/nl/0204524501/association-intercommunale-delectricite-du-sud-du-hainaut",
    "rew_nl.html": "https://www.companyweb.be/nl/0645755923/reseau-denergies-de-wavre",
    "agb_bornem_nl.html": "https://www.companyweb.be/nl/0877556624/agb-bornem",
}
# also try site
urls["lucia_site.html"] = "https://www.sintlucia.be/"
for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
            (RAW / name).write_bytes(data)
            print(name, resp.status, len(data), resp.geturl())
    except Exception as e:
        print(name, "FAIL", type(e).__name__, e)
