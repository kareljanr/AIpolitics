# ephemeral tick2009 probe3 — Waregem CW + Pappers/Upswitch parse + Yperman
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2009")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))
    return data


urls = [
    ("waregem_nl", "https://www.companyweb.be/nl/0405460592/onze-lieve-vrouw-van-lourdes-ziekenhuis-waregem"),
    ("waregem_en", "https://www.companyweb.be/en/0405460592/onze-lieve-vrouw-van-lourdes-ziekenhuis-waregem"),
    ("waregem_fr", "https://www.companyweb.be/fr/0405460592/onze-lieve-vrouw-van-lourdes-ziekenhuis-waregem"),
    ("yperman_nl", "https://www.companyweb.be/nl/0462915078/jan-yperman-ziekenhuis"),
    ("yperman_en", "https://www.companyweb.be/en/0462915078/jan-yperman-ziekenhuis"),
    ("yperman_fr", "https://www.companyweb.be/fr/0462915078/jan-yperman-ziekenhuis"),
    ("palfijn_upswitch", "https://upswitch.be/nl/bedrijf/algemeen-ziekenhuis-jan-palfijn-gent/0262926616"),
    ("zottegem_upswitch", "https://upswitch.be/nl/bedrijf/algemeen-ziekenhuis-sint-elisabeth-zottegem/0418558166"),
    ("turnhout_upswitch", "https://upswitch.be/nl/bedrijf/az-turnhout/0897191602"),
    ("waregem_upswitch", "https://upswitch.be/nl/bedrijf/onze-lieve-vrouw-van-lourdes-ziekenhuis-waregem/0405460592"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)


def summarize(name):
    path = dst / f"{name}.html"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:130] if title else None))
    print(" blocks", blocks[:3])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "Laatste balansjaar", "Chiffre d", "Omzet", "Turnover"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 160]))
    # pappers/upswitch number patterns
    nums = re.findall(r"(?:omzet|turnover|chiffre|winst|resultaat|eigen vermogen|equity|bruto)[^€<\d]{0,40}([\d.\s]+)", t, re.I)
    print(" num-ish", nums[:10])
    euros = re.findall(r"€\s*([\d\s.,]+)", t)
    print(" euros", euros[:12])
    # year markers
    i = t.find("Laatste balansjaar")
    if i >= 0:
        print(" Laatste slice", repr(t[i : i + 200]))
    j = t.find("Last balance sheet year")
    if j >= 0:
        print(" Last slice", repr(t[j : j + 200]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2])
    print()


for n, _ in urls:
    summarize(n)

# parse pappers from probe2
p = dst / "palfijn_pappers.html"
if p.exists():
    t = p.read_text(encoding="utf-8", errors="replace")
    print("PAPPERS len", len(t))
    for lab in ["2025", "omzet", "Omzet", "chiffre", "résultat", "Résultat", "capitaux", "EUR"]:
        idxs = [m.start() for m in re.finditer(lab, t)]
        for i in idxs[:2]:
            print(lab, repr(t[i : i + 120]))
