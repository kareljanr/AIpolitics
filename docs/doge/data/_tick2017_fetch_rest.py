import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2017")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

t = Path("docs/doge/data/raw/tick2017/riv_en.html").read_text(encoding="utf-8", errors="replace")
em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
print("FTE", em[:2])

for name, url in [
    ("riv_fr", "https://www.companyweb.be/fr/0416851659"),
    (
        "riv_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416851659",
    ),
    ("riv_site", "https://www.azrivierenland.be/"),
    ("sfz", "https://www.companyweb.be/nl/0469037857/sint-franciscusziekenhuis"),
]:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, len(data))
        if name == "sfz":
            tt = data.decode("utf-8", "replace")
            i = tt.find("Laatste balansjaar")
            m = (
                re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", tt[i : i + 220])
                if i >= 0
                else None
            )
            blocks = re.findall(r'omzet:\s*"([^"]+)"', tt)
            print(" sfz year", m.group(1) if m else None, "omzet", blocks[:2])
    except Exception as e:
        print("FAIL", name, e)

text = re.sub(
    r"<[^>]+>",
    " ",
    Path("docs/doge/data/raw/tick2017/riv_kbo.html").read_text(
        encoding="utf-8", errors="replace"
    ),
)
text = re.sub(r"\s+", " ", text)
for kw in [
    "Status",
    "Actief",
    "0416",
    "Rumst",
    "vestiging",
    "Rechtsvorm",
    "Begin",
    "E-mail",
    "Aanbested",
]:
    i = text.lower().find(kw.lower())
    if i >= 0:
        print(kw, ":", text[max(0, i - 10) : i + 110])
