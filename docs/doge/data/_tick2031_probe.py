# ephemeral probe tick2031 leftover dual candidates
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
outdir = Path("docs/doge/data/raw/tick2031")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()


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


def analyze(html, label):
    title = re.search(r"<title>([^<]+)</title>", html)
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
    print("==", label, (title.group(1)[:90] if title else None))
    print(" year", year, "n", len(blocks))
    if blocks and year == "2025":
        y0 = tuple(parse_amount(x) for x in blocks[0])
        y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
        print(" y0 w/eq/br/om", y0)
        if y1:
            print(" y1", y1)
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                print(f"  {n} {a:.0f} vs {b:.0f} {pct:+.2f}%")
        m2 = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        print(" emp", m2.group(1) if m2 else None)
        for lab in ["filed on", "neergelegd op", "déposés le"]:
            j = html.lower().find(lab.lower())
            if j >= 0:
                print(" filed", html[j : j + 55].replace("\n", " "))
                break
        return True
    elif blocks:
        print(" sample0", blocks[0])
    return False


# find REW entity hints
with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join(str(v or "") for v in r.values())
        eid = r.get("entity_id") or ""
        if (
            eid.startswith("rew")
            or " REW " in f" {blob} "
            or "Electricite de Wavre" in blob
            or "Régie de l" in blob
            or "Regie Wavre" in blob
        ):
            print(
                "ENTITY",
                eid,
                (r.get("name_en") or r.get("name_nl") or "")[:70],
            )

urls = [
    (
        "agb_en",
        "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem",
    ),
    (
        "faro_en",
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    ),
    (
        "aiesh_en",
        "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut",
    ),
    (
        "cassiers_en",
        "https://www.companyweb.be/en/0434434393/cassiers-woon-en-zorgcentrum",
    ),
    (
        "bernardus_ass_en",
        "https://www.companyweb.be/en/0445106274/woonzorgcentrum-sint-bernardus",
    ),
    (
        "olv_roosdaal_en",
        "https://www.companyweb.be/en/0421031171/woon-en-zorgcentrum-onze-lieve-vrouw",
    ),
    (
        "vincentius_ant_en",
        "https://www.companyweb.be/en/0418016550/woonzorgcentrum-st-vincentius",
    ),
    (
        "lourdes_en",
        "https://www.companyweb.be/en/0410142031/woonzorgcentrum-onze-lieve-vrouw-van-lourdes",
    ),
    (
        "olva_en",
        "https://www.companyweb.be/en/0430977136/woon-en-zorgcentrum-onze-lieve-vrouw-van-antwerpen",
    ),
    (
        "triest_en",
        "https://www.companyweb.be/en/0410509443/woonzorgcentrum-kanunnik-triest-vzw",
    ),
]

live = []
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        if analyze(html, name):
            live.append(name)
    except Exception as e:
        print("FAIL", name, e)

print("LIVE_YE2025", live)
