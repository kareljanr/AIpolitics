# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2173")

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            data = r.read()
        p.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        return None


def parse(t):
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed = re.search(r"filed on ([0-9-]{10})", t or "")
    title = re.search(r"<title>([^<]+)", t or "")
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", t or "", re.I)
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, last.group(1) if last else None


# Broader care/water/IGS from known Belgian lists + prior deferred
CANDS = [
    # water / DSO leftovers
    ("0201305123", "idewa"),
    ("0204567891", "x"),
    ("0420651980", "spge_check"),
    ("0204359994", "idelux_eau_check"),
    # WZC from Vlaamse list-ish
    ("0401789123", "a"),
    ("0412789123", "b"),
    ("0423789123", "c"),
    ("0434789123", "d"),
    ("0445789123", "e"),
    ("0456789123", "f"),
    ("0467789123", "g"),
    ("0478789123", "h"),
    ("0402794561", "i"),
    ("0413794561", "j"),
    ("0424794561", "k"),
    ("0435794561", "l"),
    ("0446794561", "m"),
    ("0457794561", "n"),
    ("0468794561", "o"),
    ("0479794561", "p"),
    ("0403812345", "q"),
    ("0414812345", "r"),
    ("0425812345", "s"),
    ("0436812345", "t"),
    ("0447812345", "u"),
    ("0458812345", "v"),
    ("0469812345", "w"),
    # known operators / property duals
    ("0456378070", "careprop_check"),
    ("0875556624", "agb_bad"),
    # try WZC names from prior ticks deferred as YE2024 now maybe YE2025
    ("0445106274", "bern_assenede_partial"),
    ("0433217935", "curaz_mined"),
    # more random care
    ("0401123456", "z1"),
    ("0412123456", "z2"),
    ("0423123456", "z3"),
    ("0434123456", "z4"),
    ("0445123456", "z5"),
    ("0456123456", "z6"),
    ("0467123456", "z7"),
    ("0478123456", "z8"),
    ("0489123456", "z9"),
    ("0402134567", "z10"),
    ("0413134567", "z11"),
    ("0424134567", "z12"),
    ("0435134567", "z13"),
    ("0446134567", "z14"),
    ("0457134567", "z15"),
    ("0468134567", "z16"),
    ("0479134567", "z17"),
    # Limburg / Care Property tenants style
    ("0406877485", "dhondt2"),
    ("0410219433", "haagwinde2"),
    ("0480566704", "hof2"),
    ("0443249616", "stil2"),
    ("0685516024", "edegem2"),
    # try Aquafin subsidiaries / Pidpa etc
    ("0207543210", "pidpa_guess"),
    ("0208654321", "tmvw_guess"),
    ("0475123890", "x0475"),
    ("0464822341", "x0464"),
    ("0453380125", "x0453"),
    ("0438687654", "x0438"),
    ("0432829147", "x0432"),
    ("0425123789", "x0425"),
    ("0412210456", "x0412"),
    ("0405406887", "x0405"),
]

for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in (t or ""):
        continue
    yb, fte, filed, title, last = parse(t)
    y5 = yb.get("2025", {})
    if st == "FREE" and y5:
        print(st, kbo, (title or "")[:55])
        print(" ", y5, "fte", fte, "filed", filed, "last", last)
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "0").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.lstrip("-").isdigit() else 0
        if o >= 150000 or abs(b) >= 150000:
            print("  >>> STRONG")
    elif st == "FREE" and last == "2025":
        print(st, kbo, (title or "")[:55], "last2025 no y5json")
