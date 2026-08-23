# -*- coding: utf-8 -*-
from pathlib import Path
import urllib.request

RAW = Path("docs/doge/data/raw/tick2080")
RAW.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

URLS = {
    "den_akker_nl.html": "https://www.companyweb.be/nl/0639973732/woonzorgcentrum-den-akker",
    "den_akker_en.html": "https://www.companyweb.be/en/0639973732/woonzorgcentrum-den-akker",
    "den_akker_fr.html": "https://www.companyweb.be/fr/0639973732/woonzorgcentrum-den-akker",
    "kbo_den.html": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0639973732",
    "faro_nl.html": "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_nl.html": "https://www.companyweb.be/nl/0201712587/aiesh",
    "rew_nl.html": "https://www.companyweb.be/nl/0644638937/rew",
    # also try Heem vzw parent / alternate slug if Den Akker redirects
    "sint_barbara_probe.html": "https://www.companyweb.be/nl/search?q=Den+Akker+Sint-Truiden",
}


def fetch(name: str, url: str) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
            final = resp.geturl()
        (RAW / name).write_bytes(data)
        print(f"OK {name} {len(data)} final={final}")
    except Exception as e:
        print(f"FAIL {name}: {e}")


# Also copy prior tick2078 den_akker if present for comparison
prev = Path("docs/doge/data/raw/tick2078/den_akker_nl.html")
if prev.exists():
    (RAW / "den_akker_from2078_nl.html").write_bytes(prev.read_bytes())
    print("copied tick2078 den_akker", prev.stat().st_size)

for n, u in URLS.items():
    fetch(n, u)
