# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
KBO = "0412886636"
LABEL = "boterlaarhof"


def fetch(url, name):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    (out / name).write_bytes(data)
    print("OK", name, len(data))
    return data.decode("utf-8", "ignore")


for lang in ["en", "nl", "fr"]:
    t = fetch(f"https://www.companyweb.be/{lang}/{KBO}", f"{LABEL}_{lang}.html")
    if lang == "en":
        for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
            if y >= "2023":

                def g(k, b=body):
                    m = re.search(rf'{k}:\s*"([^"]*)"', b)
                    return m.group(1) if m else None

                print(
                    y,
                    {
                        k: g(k)
                        for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
                    },
                )
        fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
        filed = re.search(r"filed on ([0-9-]{10})", t)
        year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
        print("Y", year.group(1) if year else "-", "FTE", fte.group(1) if fte else "-", "filed", filed.group(1) if filed else "-")
        # commercial / NACE-ish
        for pat in [
            r"Commercial name[^<]{0,200}",
            r"Legal form[^<]{0,120}",
            r"Head office[^<]{0,200}",
            r"Main activity[^<]{0,200}",
            r"VAT number[^<]{0,80}",
        ]:
            m = re.search(pat, t, re.I)
            if m:
                print(re.sub(r"\s+", " ", m.group(0))[:180])

fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=412886636",
    f"{LABEL}_kbo.html",
)
# site / contact probe
for url, name in [
    ("https://www.boterlaarhof.be/", "boterlaarhof_site.html"),
    ("https://www.companyweb.be/nl/0412886636/boterlaarhof", "boterlaarhof_nl_named.html"),
]:
    try:
        fetch(url, name)
    except Exception as e:
        print("site fail", name, e)
