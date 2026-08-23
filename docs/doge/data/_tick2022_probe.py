# ephemeral probe tick2022
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10_000_000)
keys = [
    "maria_ingelmunster",
    "0458458325",
    "ppc_pittem",
    "multiversum",
    "sint_carolus",
    "zilverbos",
    "agb_bornem",
]
with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        blob = (
            r.get("entity_id", "")
            + " "
            + r.get("name_nl", "")
            + " "
            + r.get("name_en", "")
        ).lower()
        if any(k in blob for k in keys) or any(k in str(r.values()) for k in keys):
            print("ENT", r.get("entity_id"), (r.get("name_nl") or "")[:60])

outdir = Path("docs/doge/data/raw/tick2022")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
urls = [
    (
        "agb_bornem_en",
        "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem",
    ),
    (
        "faro_en",
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    ),
    (
        "maria_en",
        "https://www.companyweb.be/en/0458458325/maria-rustoord-ingelmunster-v-z-w-",
    ),
    (
        "maria_nl",
        "https://www.companyweb.be/nl/0458458325/maria-rustoord-ingelmunster-v-z-w-",
    ),
    (
        "maria_fr",
        "https://www.companyweb.be/fr/0458458325/maria-rustoord-ingelmunster-v-z-w-",
    ),
]


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) >= 2 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")
        elif len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    return float(s)


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
        blocks = re.findall(
            r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
            html,
        )
        print(name, "ok", "year", year, "nblocks", len(blocks))
        if blocks:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
            print("  y0 w/eq/br/om", y0)
            if y1:
                print("  y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(f"  {n} {a:.0f} vs {b:.0f} {pct:+.2f}%")
        m2 = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        if m2:
            print("  empjs", m2.group(1))
        m3 = re.search(
            r'Employees<[^>]*>.*?<span>([\d.,]+)</span>', html, re.S | re.I
        )
        if m3:
            print("  empspan", m3.group(1))
        filed = None
        for lab in ["filed on", "neergelegd op", "déposés le"]:
            j = html.lower().find(lab.lower())
            if j >= 0:
                filed = html[j : j + 55]
                break
        print("  filed", filed)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
