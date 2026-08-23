# ephemeral fetch tick2032 OLV Lourdes Kortenberg
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10_000_000)
# free?
with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        blob = (
            r.get("entity_id", "")
            + " "
            + r.get("name_nl", "")
            + " "
            + str(r.values())
        ).lower()
        if "0410142031" in blob or (
            "lourdes" in blob and "kortenberg" in blob
        ) or "olvlourdes" in blob.replace("_", ""):
            print("ENT", r.get("entity_id"), r.get("name_nl"))

outdir = Path("docs/doge/data/raw/tick2032")
outdir.mkdir(parents=True, exist_ok=True)
# reuse EN from tick2030 if present
src_en = Path("docs/doge/data/raw/tick2030/lourdes_en.html")
if src_en.exists():
    (outdir / "lourdes_en.html").write_bytes(src_en.read_bytes())

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


for name, url in [
    (
        "lourdes_nl",
        "https://www.companyweb.be/nl/0410142031/woonzorgcentrum-onze-lieve-vrouw-van-lourdes",
    ),
    (
        "lourdes_en",
        "https://www.companyweb.be/en/0410142031/woonzorgcentrum-onze-lieve-vrouw-van-lourdes",
    ),
    (
        "lourdes_fr",
        "https://www.companyweb.be/fr/0410142031/woonzorgcentrum-onze-lieve-vrouw-van-lourdes",
    ),
    (
        "lourdes_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410142031",
    ),
    ("lourdes_site", "https://www.lourdeskortenberg.be/"),
    ("lourdes_site2", "https://www.wzc-lourdes.be/"),
    ("agb_en", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    (
        "faro_en",
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    ),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        title = re.search(r"<title>([^<]+)</title>", html)
        print("==", name, (title.group(1)[:80] if title else None))
        if "kbo" in name or "site" in name:
            emails = sorted(
                set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
            )
            print(" emails", emails[:8])
            if "kbo" in name:
                m = re.search(r"Aantal vestigingseenheden.{0,160}", html, re.S)
                print(" VE", re.sub(r"<[^>]+>", " ", m.group(0))[:100] if m else None)
                m = re.search(r"Adres van de zetel.{0,200}", html, re.S)
                if m:
                    print(" addr", re.sub(r"<[^>]+>", " ", m.group(0))[:160])
            continue
        if name in ("agb_en", "faro_en"):
            i = html.find("Last balance sheet year")
            m = (
                re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if i >= 0
                else None
            )
            print(" year", m.group(1) if m else None)
            continue
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
        print(" year", year, "n", len(blocks))
        if blocks:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
            print(" y0", y0)
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
                print(" filed", html[j : j + 55])
                break
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
