# ephemeral probe tick2025 Sint-Carolus / Zilverbos
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


for p in [
    Path("docs/doge/data/raw/tick2020/kbo_search_woonzorgcentrum_sint_carolus.html"),
    Path("docs/doge/data/raw/tick2020/kbo_search_wzc_zilverbos.html"),
]:
    t = p.read_text(encoding="utf-8", errors="replace")
    nums = re.findall(r"ondernemingsnummer=(\d{9,10})", t)
    nums2 = re.findall(r"0\d{3}\.\d{3}\.\d{3}", t)
    print(p.name, "nums", nums[:5], "fmt", nums2[:5])
    # also bare 10-digit
    nums3 = re.findall(r">\s*(0\d{9})\s*<", t)
    print("  bare", nums3[:5])

# known from earlier Verif ranking ~WZC Sint-Carolus Ternat; try web-known candidates
candidates = [
    # will fill from KBO searches after parse
]

# fetch KBO search live for enterprise numbers
searches = [
    (
        "carolus_kbo_search",
        "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html?searchWord=Woonzorgcentrum+Sint-Carolus&_memory=true",
    ),
]

# Try companyweb search pages / known slugs
cw_guesses = [
    ("carolus_ternat", "https://www.companyweb.be/nl/search?q=Woonzorgcentrum+Sint-Carolus+Ternat"),
    ("zilverbos", "https://www.companyweb.be/nl/search?q=Woonzorgcentrum+Zilverbos"),
    ("carolus2", "https://www.companyweb.be/nl/search?q=%22Sint-Carolus%22+woonzorgcentrum"),
]

for name, url in cw_guesses:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        links = re.findall(
            r"https://www\.companyweb\.be/nl/(0\d{9})/([a-z0-9\-]+)", html
        )
        print(name, "links", links[:8])
        titles = re.findall(r"<title>([^<]+)</title>", html)
        print(" title", titles[:1])
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)

# also try pappers / open companyweb by common Ternat numbers from prior knowledge
# From earlier session Sint-Carolus failed 0412635099 — try other
for name, url in [
    (
        "carolus_try1",
        "https://www.companyweb.be/nl/0412635099/woonzorgcentrum-sint-carolus",
    ),
    (
        "carolus_try2",
        "https://www.companyweb.be/en/0465548219/woonzorgcentrum-sint-carolus",
    ),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        title = re.search(r"<title>([^<]+)</title>", html)
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
        print(name, "ok", title.group(1)[:80] if title else None, "year", year, "n", len(blocks))
        if blocks and year == "2025":
            y0 = tuple(parse_amount(x) for x in blocks[0])
            y1 = tuple(parse_amount(x) for x in blocks[1]) if len(blocks) > 1 else None
            print("  y0", y0)
            if y1:
                print("  y1", y1)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
