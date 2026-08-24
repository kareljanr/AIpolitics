# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)

CANDS = [
    ("0771796336", "timanti"),
    ("0470673890", "zorg_saam"),
    ("0411515075", "emmaus"),
    ("0755822317", "lork_hoeselt"),
    ("0823488131", "thofke"),
    ("0450755634", "residentie_oudenburg_re"),  # private RE skip later
    # Avondvrede - try search via known patterns; fetch companyweb search
    ("0400123456", "skip"),
    # Try Avondvrede Mechelen variants from staatsblad
    ("0400556677", "skip2"),
    # Common Care Property / Cofinimmo tenants
    ("0426000000", "skip3"),
    # Walloon leftover MRS from prior ticks
    ("0458352318", "lorchidee_check"),  # mined asbl_lorchidee
    ("0422923859", "care_ion_check"),
    ("0443082637", "xxe_aout_check"),
    ("0442694142", "sebrechts_check"),
    ("0462316153", "le_castel_check"),
    ("0475400760", "famifamenne_check"),
    ("0427821963", "slg_wallonie_check"),
    ("0865574649", "fakkel_check"),
    ("0413550491", "restel_check"),
    # Try more WZC names via KBO guesses from Flemish care list
    ("0410220000", "skip4"),
    ("0435000000", "skip5"),
    # Real: Moervaartheem / Zorg-Saam already
    # Search Avondvrede via companyweb name URL
]

# Resolve Avondvrede / Rusthuis Avondvrede via companyweb slug
NAME_URLS = [
    ("avondvrede", "https://www.companyweb.be/en/search?q=avondvrede"),
    ("avondvrede2", "https://www.companyweb.be/nl/avondvrede"),
]


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:70])
        return None


# First resolve Avondvrede KBO from search/slug pages
for label, url in NAME_URLS:
    t = fetch(url, out / f"{label}_search.html")
    if not t:
        continue
    kbos = re.findall(r"/en/(\d{10})", t) + re.findall(r"/nl/(\d{10})", t)
    kbos += re.findall(r"BE(\d{10})", t)
    print("SEARCH", label, "kbos", list(dict.fromkeys(kbos))[:15])
    for k in list(dict.fromkeys(kbos))[:8]:
        if k not in mined:
            CANDS.append((k, f"avond_{k}"))

# Also try direct companyweb pages for known names
DIRECT = [
    ("avondvrede_nv", "https://www.companyweb.be/nl/zoeken?query=Rusthuis+Avondvrede"),
    ("dezorgfamilie", "https://www.companyweb.be/nl/zoeken?query=De+Zorgfamilie"),
    ("haagwinde2", "https://www.companyweb.be/nl/0410219433"),
]
for label, url in DIRECT:
    t = fetch(url, out / f"{label}.html")
    if t:
        kbos = re.findall(r"/nl/(\d{10})", t) + re.findall(r"/en/(\d{10})", t)
        print("DIRECT", label, list(dict.fromkeys(kbos))[:12])
        for k in list(dict.fromkeys(kbos))[:10]:
            if k not in mined:
                CANDS.append((k, f"dir_{k}"))

seen = set()
strong = []
for kbo, label in CANDS:
    if "skip" in label or kbo in seen:
        continue
    seen.add(kbo)
    status = "MINED" if kbo in mined else "FREE"
    print("---", label, kbo, status)
    if status == "MINED":
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"f2_{label}_en.html")
    if not t:
        continue
    title = re.search(r"<title>([^<]+)", t)
    if not title or "Error 404" in title.group(1):
        print(" 404")
        continue
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {
            k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
        }
    fte = re.search(r"([\d.,]+)\s*FTE", t)
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3})", t)))[:5]
    y5 = yblocks.get("2025", {})
    live = any(y5.get(k) for k in ("omzet", "bruto_marge", "winst", "eigen_vermogen"))
    omzet = (y5.get("omzet") or "").replace(",", "")
    print(" title", title.group(1)[:110])
    print(" YE2025" if live else " noYE", "fte", fte.group(1) if fte else "-", "nace", nace)
    for y in sorted(yblocks, reverse=True)[:2]:
        print(" ", y, yblocks[y])
    care = bool(nace) or any(
        x in title.group(1).lower()
        for x in ("wzc", "woon", "repos", "rust", "zorg", "mrs", "home", "senior")
    )
    if live and care:
        if omzet.isdigit() and int(omzet) >= 1_000_000:
            print(" >>> STRONG OMZET")
            strong.append((label, kbo, omzet, title.group(1)[:70]))
        else:
            bm = (y5.get("bruto_marge") or "0").replace(",", "")
            try:
                if abs(int(bm)) >= 400_000:
                    print(" >>> BRUTO CARE")
                    strong.append((label, kbo, f"b{bm}", title.group(1)[:70]))
            except ValueError:
                pass

print("STRONG", strong)
print("mined_count", len(mined))
