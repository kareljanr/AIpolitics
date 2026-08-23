import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2015")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


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


def check(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    t = data.decode("utf-8", "replace")
    title = re.search(r"<title>([^<]+)</title>", t)
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
    filed = None
    for lab in ["filed on", "neergelegd op"]:
        i = t.find(lab)
        if i >= 0:
            filed = t[i : i + 40]
    print("==", name, "==", (title.group(1)[:80] if title else None))
    print(" year", year, "filed", filed, "nblocks", len(blocks))
    if blocks and year == "2025":
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print(" LIVE YE2025", y0)


urls = [
    ("sintlucas_gent", "https://www.companyweb.be/en/0459265997"),
    ("klina", "https://www.companyweb.be/en/0434302850"),
    ("turnhout", "https://www.companyweb.be/en/0897191602"),
    ("monica", "https://www.companyweb.be/en/0410214186"),  # may be middelares wrong
    ("azmonica", "https://www.companyweb.be/en/0409835490"),  # imelda
    ("azstlucasbrugge", "https://www.companyweb.be/en/0408116216"),
    ("azoud", "https://www.companyweb.be/en/0870757023"),
    ("azdiest", "https://www.companyweb.be/en/0434602560"),
    ("azwaregem", "https://www.companyweb.be/en/0405460592"),
    # water/DSO leftover?
    ("pidpa", "https://www.companyweb.be/en/0204505846"),
    ("farys", "https://www.companyweb.be/en/0200539968"),
]
for name, url in urls:
    try:
        check(name, url)
    except Exception as e:
        print("FAIL", name, e)
