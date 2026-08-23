# ephemeral probe tick2024
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10_000_000)
keys = ["multiversum", "evara", "sint_carolus", "zilverbos", "carolus", "agb_bornem", "vzw_faro"]
with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        blob = (
            r.get("entity_id", "")
            + " "
            + r.get("name_nl", "")
            + " "
            + r.get("name_en", "")
        ).lower()
        if any(k in blob for k in keys):
            print("ENT", r.get("entity_id"), (r.get("name_nl") or "")[:70])

outdir = Path("docs/doge/data/raw/tick2024")
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


# reuse prior multiversum if present
for prior in Path("docs/doge/data/raw").rglob("*multiversum*"):
    print("PRIOR", prior)

urls = [
    (
        "multiversum_en",
        "https://www.companyweb.be/en/0412097638/multiversum",
    ),
    (
        "multiversum_nl",
        "https://www.companyweb.be/nl/0412097638/multiversum",
    ),
    (
        "faro_en",
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    ),
    (
        "agb_bornem_en",
        "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem",
    ),
]

# discover carolus/zilverbos via search if needed later
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        year = None
        for lab in ["Last balance sheet year", "Laatste balansjaar"]:
            i = html.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if m:
                    year = m.group(1)
        blocks = re.findall(
            r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
            html,
        )
        print(name, "year", year, "nblocks", len(blocks))
        if blocks and year == "2025":
            y0 = tuple(parse_amount(x) for x in blocks[0])
            y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
            print("  y0 w/eq/br/om", y0)
            if y1:
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(f"  {n} {a:.0f} vs {b:.0f} {pct:+.2f}%")
            m2 = re.search(r'Employees\s*=\s*"([^"]+)"', html)
            print("  emp", m2.group(1) if m2 else None)
            for lab in ["filed on", "neergelegd op"]:
                j = html.lower().find(lab.lower())
                if j >= 0:
                    print("  filed", html[j : j + 50])
                    break
        elif blocks:
            print("  stall y0", blocks[0])
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
