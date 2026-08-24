# -*- coding: utf-8 -*-
import urllib.request, re, ssl
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
dst = Path("docs/doge/data/raw/tick2144")
dst.mkdir(parents=True, exist_ok=True)
blob = (
    Path("docs/doge/data/entities.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/leaderboard.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/commitments.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/research_queue.csv").read_text(encoding="utf-8", errors="replace")
).lower()


def get(url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        return r.read().decode("utf-8", "replace"), r.geturl()


# Candidate KBOs / slugs from public directories + prior deferred notes
cands = [
    ("heysel", "0401968196", "https://www.companyweb.be/en/0401968196/residence-du-heysel"),
    ("kalvermarkt", "0441313178", "https://www.companyweb.be/en/0441313178/kalvermarkt"),
    ("notre_dame", "0401472918", "https://www.companyweb.be/en/0401472918"),
    ("st_joseph_liege", "0403408287", "https://www.companyweb.be/en/0403408287"),
    ("st_roch", "0403370142", "https://www.companyweb.be/en/0403370142"),
    ("hirondelles", "0422614814", "https://www.companyweb.be/en/0422614814"),
    ("tilleuls_ath", "0408302145", "https://www.companyweb.be/en/0408302145"),
    ("val_des_roses", "0426558312", "https://www.companyweb.be/en/0426558312"),
    ("home_du_parc", "0403301468", "https://www.companyweb.be/en/0403301468"),
    ("de_foyer", "0413796456", "https://www.companyweb.be/en/0413796456/woon-en-zorgcentra-de-foyer"),
    # more plausible unused from Walloon MRS lists / prior ticks deferred
    ("les_peupliers_check", "0479984011", "https://www.companyweb.be/en/0479984011"),  # already done Peupliers
    ("prestige_check", "0416528391", "https://www.companyweb.be/en/0416528391"),
    ("rew_alt1", "0200931936", "https://www.companyweb.be/en/0200931936"),
    ("rew_alt2", "0200666456", "https://www.companyweb.be/en/0200666456"),
    ("rew_alt3", "0200456789", "https://www.companyweb.be/en/0200456789"),
    # try companyweb search pages
]

# fetch search pages for more IDs
search_urls = [
    "https://www.companyweb.be/en/search?q=maison+de+repos",
    "https://www.companyweb.be/en/search?q=woonzorgcentrum",
    "https://www.companyweb.be/en/search?q=rusthuis",
    "https://www.companyweb.be/nl/zoeken?q=woonzorgcentrum",
]
extra = []
for su in search_urls:
    try:
        h, furl = get(su)
        print("SEARCH", furl[:90], "len", len(h))
        hrefs = re.findall(r'href="(/en/\d{10}/[^"]+)"', h)
        hrefs += re.findall(r'href="(/nl/\d{10}/[^"]+)"', h)
        print("  hrefs", len(hrefs), hrefs[:8])
        for hh in hrefs[:30]:
            m = re.search(r"/(\d{10})/", hh)
            if m:
                digits = m.group(1)
                url = "https://www.companyweb.be" + hh if hh.startswith("/") else hh
                # normalize to /en/
                url = url.replace("/nl/", "/en/")
                slug = url.rstrip("/").split("/")[-1]
                extra.append((slug[:40], digits, url))
    except Exception as e:
        print("SEARCH ERR", su, type(e).__name__, e)

# Upswitch / pappers style lists
for su in [
    "https://www.northdata.com/?q=maison+de+repos+Belgique&region=Belgique",
]:
    try:
        h, furl = get(su)
        print("NORTH", furl[:90], "len", len(h))
        nums = re.findall(r"BE\s?(0\d{9})", h)
        print("  BE", nums[:20])
        for n in nums[:20]:
            digits = n.replace(" ", "")
            if len(digits) == 10:
                extra.append((digits, digits, f"https://www.companyweb.be/en/{digits}"))
    except Exception as e:
        print("NORTH ERR", type(e).__name__, e)

# also try staatsbladmonitor search for 2026 filings MRS
for su in [
    "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0401968196",
]:
    try:
        h, furl = get(su)
        print("SBM", furl[:90], "len", len(h))
    except Exception as e:
        print("SBM ERR", type(e).__name__, e)

all_cands = cands + extra
seen = set()
live = []
for name, digits, url in all_cands:
    if digits in seen:
        continue
    seen.add(digits)
    dotted = digits[:4] + "." + digits[4:7] + "." + digits[7:]
    mined = digits in blob or dotted in blob
    try:
        h, furl = get(url)
    except Exception as e:
        print("FAIL", name, digits, type(e).__name__, e)
        continue
    title = re.search(r"<title>([^<]+)", h)
    years = re.findall(r"\n(202[0-9])\s*:", h)
    last = re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", h, re.I)
    last_y = last.group(1) if last else None
    tstr = (title.group(1) if title else "")[:90]
    print("===", name, digits, "mined", mined, "last", last_y, "years", years[:4])
    print("   ", tstr)
    if last_y != "2025":
        continue
    mm = re.search(r"2025\s*:\s*\{([^}]+)\}", h)
    fields = {}
    if mm:
        for k, v in re.findall(r'(\w+):\s*"([^"]*)"', mm.group(1)):
            fields[k] = v
    fte = re.search(r'Employees\s*=\s*"([^"]+)"', h)
    filed = re.search(r"filed on ([0-9\-]+)", h, re.I)
    print("    2025", fields, "fte", fte.group(1) if fte else None, "filed", filed.group(1) if filed else None)
    (dst / f"cand_{digits}_en.html").write_text(h, encoding="utf-8")
    if not mined:
        live.append((name, digits, furl, fields, tstr, fte.group(1) if fte else "", filed.group(1) if filed else ""))

print("\nUNUSED LIVE YE2025:", len(live))
for row in live[:15]:
    print(row[0], row[1], row[3], row[4][:70])
