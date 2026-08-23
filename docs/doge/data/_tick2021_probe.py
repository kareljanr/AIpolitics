# ephemeral probe tick2021
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2021")
outdir.mkdir(parents=True, exist_ok=True)

candidates = [
    ("agb_bornem", "https://www.companyweb.be/nl/0877556624/autonoom-gemeentebedrijf-bornem"),
    ("agb_bornem_en", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    ("faro", "https://www.companyweb.be/nl/0893863017/faro"),
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro"),
    ("aiesh", "https://www.companyweb.be/nl/0204530555/association-intercommunale-d-electricite-du-sud-hainaut"),
    ("aiesh_en", "https://www.companyweb.be/en/0204530555/association-intercommunale-d-electricite-du-sud-hainaut"),
    ("rew", "https://www.companyweb.be/nl/0202765933/rew"),
    ("rew_en", "https://www.companyweb.be/en/0202765933/rew"),
    ("vincentius_avelgem", "https://www.companyweb.be/nl/0420504403/woon-en-zorgcentrum-sint-vincentius"),
    ("vincentius_avelgem_en", "https://www.companyweb.be/en/0420504403/woon-en-zorgcentrum-sint-vincentius"),
    ("ppc_pittem", "https://www.companyweb.be/nl/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem"),
    ("ppc_pittem_en", "https://www.companyweb.be/en/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem"),
    ("ppc_pittem_fr", "https://www.companyweb.be/fr/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem"),
    ("marias_rustoord", "https://www.companyweb.be/nl/0411600692/wzc-maria-s-rustoord"),
    ("marias_rustoord_en", "https://www.companyweb.be/en/0411600692/wzc-maria-s-rustoord"),
]

for name, url in candidates:
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-doge/1.0)"}
        )
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        year = None
        for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
            i = html.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 250])
                if m:
                    year = m.group(1)
                    break
        omzet = re.findall(r'omzet:\s*"([^"]+)"', html)
        print(f"{name}: ok bytes={len(html)} year={year} omzet={omzet[:2]}")
    except Exception as e:
        print(f"{name}: FAIL {type(e).__name__}: {e}")
