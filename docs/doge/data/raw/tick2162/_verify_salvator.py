# -*- coding: utf-8 -*-
from pathlib import Path
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0"}
out = Path(__file__).resolve().parent


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


for label, url in [
    ("salvator_en", "https://www.companyweb.be/en/0423571581"),
    ("salvator_nl", "https://www.companyweb.be/nl/0423571581/salvator-welzijnscentrum"),
    ("salvator_fr", "https://www.companyweb.be/fr/0423571581"),
    ("salvator_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0423571581"),
    ("lorkh_en", "https://www.companyweb.be/en/0755822317"),
    ("lorkh_nl", "https://www.companyweb.be/nl/0755822317"),
    ("lorkh_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0755822317"),
]:
    t = fetch(url, out / f"{label}.html")
    year = re.search(r"Last balance sheet year.{0,100}", t, re.S | re.I)
    if not year:
        year = re.search(r"Laatste balansjaar.{0,100}", t, re.S | re.I)
    plain = re.sub(r"<[^>]+>", " ", year.group(0)) if year else ""
    plain = re.sub(r"\s+", " ", plain)
    print("====", label, plain[:100])
    for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t)[:3]:
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        print(y, {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]})
    filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
    if not filed:
        filed = re.search(r"neergelegd op[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    print("filed", filed.group(1) if filed else "-", "fte", fte.group(1) if fte else "-")
