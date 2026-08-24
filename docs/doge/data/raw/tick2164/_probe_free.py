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
            for m in re.findall(r"0\d{9}", blob):
                mined.add(m)


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:80])
        return None


def detail(label, t, kbo):
    title = re.search(r"<title>([^<]+)", t)
    if not title or "Error 404" in title.group(1):
        print(label, kbo, "404")
        return False
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {
            k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
        }
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3})", t)))[:6]
    free = kbo not in mined
    y5 = yblocks.get("2025", {})
    live = any(y5.get(k) for k in ("omzet", "bruto_marge", "winst", "eigen_vermogen"))
    omzet = (y5.get("omzet") or "").replace(",", "")
    print("=" * 50)
    print(
        label,
        kbo,
        "FREE" if free else "MINED",
        "YE2025" if live else "noYE2025",
        "fte",
        fte.group(1) if fte else "-",
        "filed",
        filed.group(1) if filed else "-",
        "nace",
        nace,
    )
    print(" title", title.group(1)[:110])
    for y in sorted(yblocks, reverse=True)[:2]:
        print(" ", y, yblocks[y])
    strong = free and live and bool(omzet) and omzet.isdigit() and int(omzet) >= 1_000_000
    if strong:
        print(" >>> STRONG CANDIDATE")
    return strong


# Known leftover / deferred / adjacent WZC-MRS and some IGS/HVZ guesses
CANDS = [
    ("0408041271", "huize_ter_linde"),
    ("0411515075", "emmaus"),
    ("0470673890", "zorg_saam"),
    ("0475400760", "famifamenne"),
    ("0422540661", "de_meerssen"),
    ("0416934425", "sint_anna_guess"),
    ("0427301819", "olvf_guess"),
    ("0428692191", "de_medemens"),
    ("0435440123", "oase_guess"),
    ("0402212345", "skip"),
    # Common Flemish WZC
    ("0412198765", "skip2"),
    ("0454090355", "deinze_check"),  # mined?
    ("0421903676", "christine_check"),
    ("0433419259", "olv_wez_check"),
    ("0424236725", "antonius_check"),
    ("0479401318", "terburg_check"),
    ("0432401155", "compostela_check"),
    ("0521970559", "vulpia_check"),
    ("0436595020", "olv_bornem_check"),
    ("0410556557", "leiehome_check"),
    ("0409942289", "huize_sj_check"),
    # Possible unused
    ("0412789456", "bad"),
    ("0465123456", "bad2"),
    ("0430123456", "bad3"),
    ("0445123456", "bad4"),
    # From prior probes / sites
    ("0416528391", "cand_0416528391"),  # from tick2144 raw
    ("0413796456", "cand_0413796456"),
    ("0479984011", "cand_0479984011"),
    # Walloon MRS leftovers
    ("0400335678", "bad5"),
    ("0421479153", "le_hanois_check"),  # mined
    ("0448023456", "bad6"),
    # IGS / water-ish
    ("0200123456", "bad7"),
    ("0212123456", "bad8"),
    # Care homes often in 04xx
    ("0456789012", "bad9"),
    ("0467890123", "bad10"),
    ("0419876543", "bad11"),
    ("0423456789", "bad12"),
    ("0434567890", "bad13"),
    ("0445678901", "bad14"),
    ("0456789013", "bad15"),
    # Try specific known unused from web memory
    ("0412345678", "bad16"),
    ("0425678901", "avondvrede_guess"),
    ("0436789012", "witte_meren_guess"),
    ("0447890123", "oase_vzw_guess"),
    ("0458901234", "de_meers_guess"),
    ("0469012345", "zonnige_guess"),
    ("0401122334", "bad17"),
    ("0412233445", "bad18"),
    ("0423344556", "bad19"),
    ("0434455667", "bad20"),
    ("0445566778", "bad21"),
    ("0456677889", "bad22"),
    ("0467788990", "bad23"),
    ("0478899001", "bad24"),
    ("0489900112", "bad25"),
    ("0490011223", "bad26"),
    # Real KBOs from prior tick raw names in git status
    ("0413796456", "tick2144a"),
    ("0416528391", "tick2144b"),
    ("0479984011", "tick2144c"),
]

# Also pull KBOs from tick2144 html filenames if present
extra = [
    ("0413796456", "c2144_a"),
    ("0416528391", "c2144_b"),
    ("0479984011", "c2144_c"),
]

seen = set()
hits = []
for kbo, label in CANDS + extra:
    if kbo in seen or kbo.startswith("bad") or "guess" in label and kbo.endswith(("123456", "234567", "345678", "456789", "567890", "678901", "789012", "890123", "901234", "012345", "112233", "223344", "334455", "445566", "556677", "667788", "778899", "889900", "990011", "001122")):
        continue
    # skip obviously fake sequential
    if re.match(r"0\d{2}(\d)\1{5,}", kbo) or kbo[3:] in {
        "123456",
        "234567",
        "345678",
        "456789",
        "567890",
        "678901",
        "789012",
        "890123",
        "901234",
        "012345",
        "112233",
        "223344",
        "334455",
        "445566",
        "556677",
        "667788",
        "778899",
        "889900",
        "990011",
        "001122",
    }:
        continue
    seen.add(kbo)
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"probe_{label}_en.html")
    if t and detail(label, t, kbo):
        hits.append((label, kbo))

print("HITS", hits)
