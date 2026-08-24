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
out.mkdir(parents=True, exist_ok=True)

mined = set()
with open(Path(r"docs/doge/data/entities.csv"), newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
        for m in re.findall(r"0\d{9}", blob):
            mined.add(m)


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:60])
        return None


def summarize(label, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
    nums = re.findall(r"/en/(0\d{9})", t) + re.findall(r"BE0(\d{9})", t)
    nums = list(dict.fromkeys([n[-10:] if len(n) >= 10 else n for n in nums]))
    y25 = None
    for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t):
        if y in ("2025", "2026"):

            def g(k, b=body):
                m = re.search(rf'{k}:\s*"([^"]*)"', b)
                return m.group(1) if m else None

            y25 = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
            break
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    free = [n for n in nums if n not in mined]
    y = year.group(1) if year else "-"
    print(
        label,
        (title.group(1)[:50] if title else "?"),
        "Y",
        y,
        y25,
        "fte",
        fte.group(1) if fte else "-",
        "FREE",
        free[:2],
    )
    return y in ("2025", "2026") and bool(free) and y25


# Candidate KBOs from public care directories / likely unused YE2025
CANDS = [
    # FARO/AIESH/REW recheck
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    # Likely unused MRS/WZC from directories (not in do-not-redo)
    ("0428080497", "maison_dieu"),  # YE2024 likely
    ("0468223915", "cand_a"),
    ("0478651204", "cand_b"),
    ("0451762883", "cand_c"),
    ("0439821447", "cand_d"),
    ("0472314869", "cand_e"),
    ("0419556882", "cand_f"),
    ("0445891336", "cand_g"),
    ("0408223719", "cand_h"),
    # From repertorium / news
    ("0500952540", "wznd"),  # YE2024
    ("0446022331", "lork"),  # YE2024
    # Try more Walloon MRS known names via digits from prior open pages
    ("0466114791", "en_famille_already"),
    ("0454712838", "egmont_already"),
    # Disability / creche / hospital-ish
    ("0415850084", "mpc_already"),
    ("0420607638", "zonnelied_already"),
    # Fresh guesses from KBO ranges near mined care
    ("0467123456", "bad"),
    ("0437015123", "try1"),
    ("0442019876", "try2"),
    ("0456012345", "try3"),
    ("0478015678", "try4"),
    ("0482012345", "try5"),
    ("0425018765", "try6"),
    ("0432014567", "try7"),
    ("0463017890", "try8"),
    ("0475012345", "try9"),
]

# Better concrete from web/news: dig specific pages
CONCRETE = [
    "https://www.companyweb.be/en/0428080497",  # Maison Dieu - check year
    "https://www.companyweb.be/en/0453.271.496",  # Rustibus - not care
    "https://www.companyweb.be/nl/0418.something",
]

# Use staatsbladmonitor-style: probe known unused from Hertog do-not-redo siblings
# OLV Lourdes Kortenberg was in Hertog do-not-redo so mined
# Try: Residentie Belle Epoque is emeis - mined path
# Try disability ASBL / creche

MORE = [
    ("https://www.companyweb.be/en/0407533117", "try_a"),  # random
    ("https://www.companyweb.be/en/0412345678", "try_b"),
    ("https://www.companyweb.be/en/0465001122", "try_c"),
    ("https://www.companyweb.be/en/0478003344", "try_d"),
    ("https://www.companyweb.be/en/0429005566", "try_e"),
    ("https://www.companyweb.be/en/0436007788", "try_f"),
    ("https://www.companyweb.be/en/0448009900", "try_g"),
    ("https://www.companyweb.be/en/0451001122", "try_h"),
    ("https://www.companyweb.be/en/0462003344", "try_i"),
    ("https://www.companyweb.be/en/0475005566", "try_j"),
]

# Named care operators from repertorium PDF sample not obviously mined
NAMED = [
    ("https://www.companyweb.be/nl/search?q=Vondelhof+Boutersem", "vondelhof"),  # 404 likely
    ("https://www.companyweb.be/en/0860419296", "wissner"),  # medical rental YE2025 but not dual care public
]

hits = []
for kbo, label in [
    ("0428080497", "maison_dieu"),
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0500952540", "wznd"),
    ("0446022331", "lork"),
    ("0860419296", "wissner"),
    # Ter Meeren / Keyhof parent WZND already YE2024
    # Try Apricusa / Neuve Cour via digits if we can find
    ("0466778899", "skip"),
]:
    if kbo in mined:
        print("MINED", label, kbo)
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if t and summarize(label, t):
        hits.append(label)

print("HITS", hits)

# Probe a batch of care-like KBOs from open data patterns near 045x/046x/047x nursing
batch = [
    "0450123456",
    "0451123456",
    "0452123456",
    "0453123489",
    "0454123456",
    "0455123456",
    "0456123456",
    "0457123456",
    "0458123456",
    "0459123456",
    "0460123456",
    "0461123456",
    "0462123456",
    "0463123456",
    "0464123456",
    "0465123456",
    "0466123456",
    "0467123456",
    "0468123456",
    "0469123456",
]
# Too random. Instead use pages from Hertog raw sibling list in tick2159
for name in [
    "de_linde_en.html",
    "huize_sint_jozef_ieper_en.html",
    "ocura_en.html",
    "sint_jozef_ninove_en.html",
]:
    p = Path(r"docs/doge/data/raw/tick2159") / name
    if p.exists():
        summarize(name, p.read_text(encoding="utf-8", errors="ignore"))
