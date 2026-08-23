# ephemeral probe tick2029 — Bethanie / Karus + AGB/FARO stalls
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2029")
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


# extract numbers from prior KBO searches
for p in [
    Path("docs/doge/data/raw/tick2020/kbo_search_psychiatrisch_centrum_bethanie.html"),
    Path("docs/doge/data/raw/tick2020/kbo_search_karus_vzw.html"),
]:
    if not p.exists():
        print("MISS", p)
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    nums = re.findall(r"ondernemingsnummer=(\d{9,10})", t)
    nums2 = re.findall(r"0\d{3}\.\d{3}\.\d{3}", t)
    bare = re.findall(r">\s*(0\d{9})\s*<", t)
    print(p.name, "nums", nums[:5], "fmt", nums2[:5], "bare", bare[:5])

# web-known / guess fetches — fill after search
urls = [
    ("agb_en", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    (
        "faro_en",
        "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    ),
]

# Try common Karus / Bethanie companyweb paths from search knowledge
extra = [
    ("karus_try1", "https://www.companyweb.be/nl/search?q=Karus+VZW"),
    ("bethanie_try1", "https://www.companyweb.be/nl/search?q=Psychiatrisch+Centrum+Bethanie"),
]

for name, url in urls + extra:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        if "search" in name:
            links = re.findall(
                r"https://www\.companyweb\.be/nl/(0\d{9})/([a-z0-9\-]+)", html
            )
            print(name, "links", links[:10])
            continue
        year = None
        for lab in ["Last balance sheet year", "Laatste balansjaar"]:
            i = html.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if m:
                    year = m.group(1)
        print(name, "year", year)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
