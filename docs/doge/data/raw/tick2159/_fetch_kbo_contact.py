# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path
from urllib.parse import quote

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        print("OK", path.name, len(data), url)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, e)
        return None


urls = {
    "hertog_jan_kbo_nl.html": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0845895824",
    "hertog_jan_fr_full.html": "https://www.companyweb.be/fr/0845895824/hertog-jan",
    "hertog_jan_nl_full.html": "https://www.companyweb.be/nl/0845895824/hertog-jan",
    "hertog_jan_en_full.html": "https://www.companyweb.be/en/0845895824/hertog-jan",
    "hertog_site.html": "https://www.inforegio.be/residentie-hertog-jan-kortenberg",
}

for name, url in urls.items():
    t = fetch(url, out / name)
    if not t:
        continue
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)))
    print(name, "emails", emails[:10])
    phones = re.findall(r"(?:\+32|0)\s?\d[\d\s./-]{6,}", t)
    print(name, "phones", phones[:6])
