# ephemeral probe tick2027 — confirm Ternat + AGB/FARO stalls
import re
import shutil
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2027")
outdir.mkdir(parents=True, exist_ok=True)
for name in [
    "carolus_en.html",
    "carolus_nl.html",
    "carolus_fr.html",
    "carolus_kbo.html",
    "carolus_site1.html",
]:
    src = Path("docs/doge/data/raw/tick2025") / name
    if src.exists():
        shutil.copy(src, outdir / name)


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


p = outdir / "carolus_en.html"
t = p.read_text(encoding="utf-8", errors="replace")
year = None
for lab in ["Last balance sheet year", "Laatste balansjaar"]:
    i = t.find(lab)
    if i >= 0:
        m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", t[i : i + 220])
        if m:
            year = m.group(1)
blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    t,
)
print("year", year, "n", len(blocks))
y0 = tuple(parse_amount(x) for x in blocks[0])
y1 = tuple(parse_amount(x) for x in blocks[1])
print("y0 w/eq/br/om", y0)
print("y1", y1)
for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
    a, b = y0[i], y1[i]
    pct = (a - b) / abs(b) * 100 if b else None
    print(f"  {n} {a:.0f} vs {b:.0f} {pct:+.2f}%")
m2 = re.search(r'Employees\s*=\s*"([^"]+)"', t)
print("emp", m2.group(1) if m2 else None)
for lab in ["filed on", "neergelegd op"]:
    j = t.lower().find(lab.lower())
    if j >= 0:
        print("filed", t[j : j + 50])
        break

ctx = ssl.create_default_context()
for name, url in [
    ("agb", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    (
        "faro",
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    ),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, context=ctx, timeout=20).read().decode(
            "utf-8", "replace"
        )
        i = html.find("Last balance sheet year")
        m = (
            re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if i >= 0
            else None
        )
        print(name, m.group(1) if m else None)
    except Exception as e:
        print(name, type(e).__name__, e)
