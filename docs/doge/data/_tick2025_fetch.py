# ephemeral fetch tick2025 Carolus + Zilverbos
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2025")
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
    print(" year", year, "nblocks", len(blocks))
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print(" y0 w/eq/br/om", y0)
        if len(blocks) > 1:
            y1 = tuple(parse_amount(x) for x in blocks[1])
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
    return year == "2025" and bool(blocks)


urls = [
    ("carolus_nl", "https://www.companyweb.be/nl/0409970203/woonzorgcentrum-sint-carolus"),
    ("carolus_en", "https://www.companyweb.be/en/0409970203/woonzorgcentrum-sint-carolus"),
    ("carolus_fr", "https://www.companyweb.be/fr/0409970203/woonzorgcentrum-sint-carolus"),
    ("carolus_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409970203"),
    ("carolus_site", "https://www.sintcarolusternat.be/"),
    ("zilverbos_site", "https://www.wzczilverbos.be/"),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        if "kbo" in name or "site" in name:
            emails = sorted(
                set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
            )
            print(name, "ok", len(html), "emails", emails[:6])
            if "kbo" in name:
                m = re.search(r"Aantal vestigingseenheden.{0,180}", html, re.S)
                print(" VE", re.sub(r"<[^>]+>", " ", m.group(0))[:100] if m else None)
        else:
            analyze(html, name)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)

# discover zilverbos enterprise from site / KBO search text
site = outdir / "zilverbos_site.html"
if site.exists():
    t = site.read_text(encoding="utf-8", errors="replace")
    print("zilver be", re.findall(r"BE\s*0?\d{3}[.\s]?\d{3}[.\s]?\d{3}", t)[:5])
    print("zilver nums", re.findall(r"0\d{3}[.\s]\d{3}[.\s]\d{3}", t)[:5])
