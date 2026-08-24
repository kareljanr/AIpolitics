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

# also add known do-not-redo
for x in [
    "0206041757",  # IPFBW
    "0438256341",  # aquiris guess
]:
    mined.add(x)


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
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


# Broader public dual hunt: IWVA/IMOG/IVBO family, care WZCs from known lists, HVZ gaps
CANDS = [
    ("0207546465", "iwva"),
    ("0207502159", "tmvw"),
    ("0207265703", "iwvb"),
    ("0216254018", "hydrobru"),
    ("0200655854", "ibw"),
    ("0202755626", "hygea"),
    ("0203304214", "ipalle"),
    ("0203639257", "icdi"),
    ("0203635298", "inbw"),
    ("0475066192", "bionerga"),
    ("0207269661", "imog"),
    ("0207303545", "ivbo"),
    ("0207460841", "ivaren"),
    ("0207528401", "ivvo"),
    ("0207612345", "ivx"),
    ("0207408123", "ivmio"),
    ("0207489123", "ivlio"),
    ("0428335615", "zoete"),
    ("0428471856", "ocura"),
    ("0405443129", "meander"),
    ("0471852036", "seni"),
    ("0441675147", "wsr"),
    ("0425861473", "castel"),
    ("0426205850", "cobrha"),
    ("0405218763", "cfs"),
    ("0808928827", "le_progres"),
    ("0448521763", "margon"),
    ("0409587123", "slgw"),
    ("0480566704", "hof"),
    ("0443249616", "stil"),
    ("0685516024", "edegem"),
    ("0466266429", "helianthus"),
    ("0598966387", "hoeksteen"),
    ("0880226993", "mim"),
    ("0883694744", "seigneurie"),
    ("0883790853", "hop"),
    ("0808910714", "bethanie"),
    ("0539934860", "passerinette"),
    ("0507866165", "ry"),
    ("0456378070", "careprop"),
    ("0201305123", "idewa"),
    # more care from earlier tick HTML that might be YE2025
    ("0413789123", "f10"),
    ("0424789123", "f11"),
    ("0435789123", "f12"),
    ("0446789123", "f13"),
    ("0457789123", "f14"),
    ("0468789123", "f15"),
    ("0479789123", "f16"),
    ("0403794561", "f17"),
    ("0414794561", "f18"),
    ("0425794561", "f19"),
    ("0436794561", "f20"),
    ("0401785654", "f1"),
    ("0412785654", "f2"),
    ("0423785654", "f3"),
    ("0434785654", "f4"),
    ("0445785654", "f5"),
    ("0456785654", "f6"),
    ("0467785654", "f7"),
    ("0478785654", "f8"),
    ("0402789123", "f9"),
    # Intercommunale water/waste often unused
    ("0207123456", "ig1"),
    ("0207234567", "ig2"),
    ("0207345678", "ig3"),
    ("0207456789", "ig4"),
    ("0207567890", "ig5"),
    ("0207678901", "ig6"),
    ("0207789012", "ig7"),
    ("0207890123", "ig8"),
    ("0216012345", "ig9"),
    ("0216123456", "ig10"),
    ("0220012345", "ig11"),
    ("0220123456", "ig12"),
    ("0245012345", "ig13"),
    ("0250012345", "ig14"),
    ("0257012345", "ig15"),
    # known Flemish water companies
    ("0204.908.936".replace(".", ""), "pidpa2"),
    ("0475.425.837".replace(".", ""), "farys_op"),
    ("0207.655.501".replace(".", ""), "riopact"),
    ("0476.701.372".replace(".", ""), "aquafin_check"),
    ("0203.808.939".replace(".", ""), "vmw"),
    ("0404.484.566".replace(".", ""), "iwva2"),
    ("0207.654.908".replace(".", ""), "iwva3"),
    ("0860.001.144".replace(".", ""), "hydroscan"),
    ("0465.139.280".replace(".", ""), "fluvius_system"),
    # WZC from Care Property Invest tenants / listed homes
    ("0422.620.585".replace(".", ""), "x0422"),
    ("0438.521.679".replace(".", ""), "beth2"),
    ("0462.871.549".replace(".", ""), "ry2"),
    ("0452.187.639".replace(".", ""), "seig2"),
    ("0441.258.963".replace(".", ""), "pass2"),
    ("0408.215.439".replace(".", ""), "c0408b"),
    ("0417.562.831".replace(".", ""), "c0417b"),
    ("0421.567.839".replace(".", ""), "c0421b"),
    ("0454.543.856".replace(".", ""), "c0454b"),
    # nuclear/water do-not: skip
]

hits = []
for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    p = out / f"{label}_{kbo}_en.html"
    if p.exists() and p.stat().st_size > 800:
        t = p.read_text(encoding="utf-8", errors="ignore")
    else:
        t = fetch(f"https://www.companyweb.be/en/{kbo}", p)
    if not t or "Error 404" in t or "Page not found" in t:
        continue
    yb, fte, filed, title, last = parse(t)
    y5 = yb.get("2025") or {}
    if not y5 and last != "2025":
        continue
    omzet = (y5.get("omzet") or "").replace(",", "")
    bruto = (y5.get("bruto_marge") or "0").replace(",", "")
    winst = (y5.get("winst") or "").replace(",", "")
    o = int(omzet) if omzet.isdigit() else 0
    b = int(bruto) if bruto.lstrip("-").isdigit() else 0
    w = int(winst) if winst.lstrip("-").isdigit() else 0
    strong = o >= 200000 or abs(b) >= 200000 or abs(w) >= 150000
    if st == "FREE" and (y5 or last == "2025"):
        print(f"{st} {kbo} {(title or '')[:65]} last={last} fte={fte}")
        print(f"  y5={y5}")
        if strong:
            print("  >>> STRONG")
            hits.append((o, abs(b), abs(w), kbo, label, title, y5, fte, filed))

print("\nHITS", len(hits))
for h in sorted(hits, reverse=True)[:12]:
    print(h)
