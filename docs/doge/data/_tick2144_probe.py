# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, ssl, csv
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
dst = Path("docs/doge/data/raw/tick2144")
dst.mkdir(parents=True, exist_ok=True)


def get(url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


blob = (
    Path("docs/doge/data/entities.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/leaderboard.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/commitments.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/research_queue.csv").read_text(encoding="utf-8", errors="replace")
).lower()

# redo block from rq_2144
blocked = [
    "care-ion",
    "seniors care",
    "sint-franciscus",
    "groep van voorzieningen",
    "denderrust",
    "en famille",
    "residence prestige",
    "corolles",
    "esplanade",
    "peupliers",
    "comte d'egmont",
    "cigb",
    "maagd der armen",
    "ten rozen",
    "orchidee",
    "orchidée",
    "care-support",
    "mpc sint",
    "de fakkel",
    "restel flats",
    "chateau vert",
    "château vert",
    "slg wallonie",
    "famifamenne",
    "le castel",
    "r.s.w",
    "sebrechts",
    "jolimont",
    "buurthuis",
    "bosquet",
    "strebo",
    "entraide",
    "charmille",
    "charmilles",
    "sittelles",
    "buissons",
    "residence 3",
    "elisabeth aan zee",
    "xxe aout",
    "zilverlinde",
    "sint-camillus",
    "idelux",
    "intradel",
    "korian",
    "always home",
    "arewal",
    "agb bornem",
    "armonea",
    "emeis",
    "prinsenhof",
    "akapella",
    "familiehof",
    "moisson",
    "zusterhof",
    "den akker",
    "mater dei",
    "vander stokken",
    "huize sion",
    "zusters van berlaar",
    "veilige have",
    "wzc christine",
    "zilverbos",
]

queries = [
    'site:companyweb.be/en "Last balance sheet year 2025" "nursing homes"',
    'site:companyweb.be/en "Last balance sheet year 2025" "maison de repos"',
    'site:companyweb.be/en "Last balance sheet year 2025" rusthuis OR woonzorgcentrum',
]

seen = set()
cands = []
for q in queries:
    try:
        page = get("https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q))
    except Exception as e:
        print("ddg fail", q[:40], e)
        continue
    for l in re.findall(r"uddg=([^&\"]+)", page):
        u = urllib.parse.unquote(l).split("&")[0]
        if "companyweb.be" not in u or "/en/" not in u:
            continue
        if u in seen:
            continue
        seen.add(u)
        cands.append(u)
print("unique cand urls", len(cands))

# also try REW alternate slug
for url in [
    "https://www.companyweb.be/en/0200931936/rew",
    "https://www.companyweb.be/nl/0200931936",
    "https://www.companyweb.be/fr/0200931936",
]:
    try:
        t = get(url)
        years = re.findall(r"\n(202[0-9])\s*:", t)
        m = re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", t, re.I)
        title = re.search(r"<title>([^<]+)", t)
        print("REW", url, title.group(1)[:60] if title else "?", years[:4], "last", m.group(1) if m else None)
    except Exception as e:
        print("REW fail", url, type(e).__name__, e)

picked = []
for u in cands[:40]:
    m = re.search(r"companyweb\.be/en/(\d{10})", u)
    if not m:
        continue
    kbo = m.group(1)
    slug = u.rstrip("/").split("/")[-1].lower()
    # skip if kbo or slug heavily present
    if kbo in blob or slug.replace("-", " ") in blob:
        print("SKIP known", kbo, slug[:50])
        continue
    blocked_hit = [b for b in blocked if b in slug.replace("-", " ") or b in u.lower()]
    if blocked_hit:
        print("SKIP blocked", kbo, slug[:50], blocked_hit[:2])
        continue
    try:
        t = get(u)
    except Exception as e:
        print("FAIL", kbo, e)
        continue
    years = re.findall(r"\n(202[0-9])\s*:", t)
    last = re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", t, re.I)
    title = re.search(r"<title>([^<]+)", t)
    if not last or last.group(1) != "2025":
        print("SKIP no2025", kbo, last.group(1) if last else None)
        continue
    # parse 2025 metrics
    mm = re.search(r"2025\s*:\s*\{([^}]+)\}", t)
    fields = {}
    if mm:
        for k, v in re.findall(r'(\w+):\s*"([^"]*)"', mm.group(1)):
            fields[k] = v
    fte = re.search(r'Employees\s*=\s*"([^"]+)"', t)
    filed = re.search(r"filed on ([0-9\-]+)", t, re.I)
    activity = re.search(r'Principal activity[^"]*"([^"]+)"', t, re.I)
    size = re.search(r'Company size[^"]*"([^"]+)"', t, re.I)
    print(
        "LIVE",
        kbo,
        (title.group(1)[:70] if title else "?"),
        fields,
        "fte",
        fte.group(1) if fte else None,
        "filed",
        filed.group(1) if filed else None,
        "act",
        activity.group(1)[:40] if activity else None,
    )
    (dst / f"cand_{kbo}_en.html").write_text(t, encoding="utf-8")
    picked.append((kbo, u, fields, title.group(1) if title else "", fte.group(1) if fte else "", filed.group(1) if filed else ""))
    if len(picked) >= 8:
        break

print("PICKED", len(picked))
for p in picked:
    print(p[0], p[1], p[2])
