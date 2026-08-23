# ephemeral fetch tick2020 extras
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2020")
urls = [
    (
        "sint_vincentius_avelgem_fr",
        "https://www.companyweb.be/fr/0420504403/woon-en-zorgcentrum-sint-vincentius",
    ),
    (
        "avelgem_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420504403",
    ),
    (
        "aiesh_en",
        "https://www.companyweb.be/en/0204530555/association-intercommunale-d-electricite-du-sud-hainaut",
    ),
    ("rew_en", "https://www.companyweb.be/en/0202765933/rew"),
    (
        "agb_bornem_cw",
        "https://www.companyweb.be/nl/0877556624/autonoom-gemeentebedrijf-bornem",
    ),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        year = None
        for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
            i = html.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if m:
                    year = m.group(1)
        blocks = re.findall(r'omzet:\s*"([^"]+)"', html)
        print(name, "ok", len(html), "year", year, "omzet_blocks", blocks[:3])
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)

# FTE from EN avelgem
t = (outdir / "sint_vincentius_avelgem_en.html").read_text(encoding="utf-8")
for pat in [
    r"personeel:\s*\"([^\"]+)\"",
    r"Employees.{0,400}",
    r"FTE.{0,80}",
    r"font-medium[^>]*>\s*([\d.,]+)\s*<",
]:
    ms = re.findall(pat, t, re.I | re.S)
    print("PAT", pat[:40], "n", len(ms), "sample", ms[:6] if ms else None)

# try vue data for employees
ms = re.findall(r"employees?[\"']?\s*[:=]\s*[\"']?([\d.]+)", t, re.I)
print("empassign", ms[:10])
ms = re.findall(r"personeels?cijfer.{0,200}", t, re.I)
print("pers", ms[:3])
# look near Big / company size
i = t.find("company size") if "company size" in t.lower() else t.lower().find("bedrijfsgrootte")
print("size idx", i)
if i > 0:
    print(t[i : i + 300])
