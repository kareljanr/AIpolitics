# ephemeral probe PPC Pittem for tick2022
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2022")
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


# try known/search slugs
candidates = [
    ("pittem_search", "https://www.companyweb.be/nl/search?q=PPC+Pittem"),
    ("pittem_search2", "https://www.companyweb.be/nl/search?q=Psychiatrisch+ziekenhuis+Pittem"),
]

# from prior tick2020/2021 raw names if present
prior = list(Path("docs/doge/data/raw/tick2021").glob("*pittem*")) + list(
    Path("docs/doge/data/raw/tick2020").glob("*pittem*")
)
print("prior files", [p.name for p in prior])
for p in prior:
    t = p.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    print(" prior", p.name, title.group(1)[:90] if title else None)
    # extract enterprise number from url-like or title BE
    m = re.search(r"BE\s*0?(\d{3})[.\s]?(\d{3})[.\s]?(\d{3})", t[:2000])
    if m:
        print("  be", "".join(m.groups()))
    m = re.search(r"/(\d{10})/", t[:5000])
    if m:
        print("  pathnum", m.group(1))

# web-known: try common
urls = []
# parse from pittem_nl if exists in tick2020
for base in [
    Path("docs/doge/data/raw/tick2020/pittem_nl.html"),
    Path("docs/doge/data/raw/tick2020/pittem_en.html"),
    Path("docs/doge/data/raw/tick2021/ppc_pittem_en.html"),
    Path("docs/doge/data/raw/tick2021/ppc_pittem.html"),
]:
    if base.exists():
        t = base.read_text(encoding="utf-8", errors="replace")
        # find canonical companyweb links
        links = re.findall(
            r"https://www\.companyweb\.be/(?:nl|en|fr)/(\d{10})/[a-z0-9\-]+", t
        )
        print(base.name, "links", links[:5])
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
        print(" year", year, "nblocks", len(blocks))
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
        m2 = re.search(r'Employees\s*=\s*"([^"]+)"', t)
        print(" emp", m2.group(1) if m2 else None)
        for lab in ["filed on", "neergelegd op"]:
            j = t.lower().find(lab.lower())
            if j >= 0:
                print(" filed", t[j : j + 55])
                break
        # copy to tick2022
        (outdir / base.name).write_text(t, encoding="utf-8")
