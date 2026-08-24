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
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        p.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("ERR", p.name, e)
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
    status = re.search(r"(Actief|Active|Stopgezet|Dissolved)", t or "", re.I)
    ve = re.search(r"(\d+)\s*(?:establishment|vestiging)", t or "", re.I)
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        last.group(1) if last else None,
        status.group(1) if status else None,
        ve.group(1) if ve else None,
    )


# Prefer deferred care + unused public duals with plausible YE2025
CANDS = [
    ("0480566704", "hof_ter_lande"),
    ("0443249616", "stil_geluk"),
    ("0685516024", "wzn_edegem"),
    ("0466266429", "helianthus"),
    ("0598966387", "hoeksteen"),
    ("0880226993", "man_in_motion"),
    ("0883694744", "seigneurie"),
    ("0883790853", "hop"),
    ("0808910714", "bethanie"),
    ("0539934860", "passerinette"),
    ("0507866165", "ry_chevreuil"),
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
    ("0456378070", "care_property"),
    ("0201305123", "idewa"),
    ("0204359994", "idelux_eau"),
    # more WZC / care from Flemish operators often deferred
    ("0416493254", "ben"),
    ("0835884236", "het_dorp"),
    ("0898596122", "vlietoever"),
    ("0433217935", "curaz"),
    ("0445106274", "bernardus"),
    # HVZ leftovers / Walloon zones not in do-not-redo
    ("0500912846", "hvz_try1"),
    ("0500913743", "hvz_try2"),
    ("0500914632", "hvz_try3"),
    ("0500915521", "hvz_try4"),
    ("0500916410", "hvz_try5"),
    ("0500917399", "hvz_try6"),
    ("0500920175", "hvz_try7"),
    ("0500921064", "hvz_try8"),
    ("0500921953", "hvz_try9"),
    ("0500922842", "hvz_try10"),
    # water / sewer leftovers
    ("0204908936", "pidpa"),
    ("0207546465", "iwva"),
    ("0207502159", "tmvw"),
    ("0207265703", "iwvb"),
    ("0216254018", "hydrobru"),
    ("0200938748", "swde_check"),
    ("0477382619", "vivaqua_check"),
    # IGS / intercommunale candidates
    ("0200655854", "ibw"),
    ("0202755626", "hygea"),
    ("0216452673", "ibrid"),
    ("0203304214", "ipalle"),
    ("0203639257", "icdi"),
    ("0267339611", "ibrid2"),
    ("0212214367", "iedea"),
    ("0203615491", "tec"),
    ("0203635298", "inbw"),
    ("0475066192", "bionerga"),
    ("0541770734", "imo_check"),
    ("0207269661", "imog"),
    ("0207303545", "ivbo"),
    ("0207460841", "ivaren"),
    ("0207528401", "ivvo"),
    ("0417562831", "c0417"),
    ("0421567839", "c0421"),
    ("0454543856", "c0454"),
    ("0408215439", "c0408"),
]

print("=== SCAN CANDS ===")
hits = []
for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    p = out / f"{label}_{kbo}_en.html"
    if p.exists() and p.stat().st_size > 500:
        t = p.read_text(encoding="utf-8", errors="ignore")
    else:
        t = fetch(f"https://www.companyweb.be/en/{kbo}", p)
    if not t or "Error 404" in (t or "") or "Page not found" in (t or ""):
        continue
    yb, fte, filed, title, last, status, ve = parse(t)
    y5 = yb.get("2025") or {}
    y4 = yb.get("2024") or {}
    if last != "2025" and not y5:
        continue
    omzet = (y5.get("omzet") or "").replace(",", "")
    bruto = (y5.get("bruto_marge") or "0").replace(",", "")
    winst = (y5.get("winst") or "").replace(",", "")
    o = int(omzet) if omzet.isdigit() else 0
    b = int(bruto) if bruto.lstrip("-").isdigit() else 0
    w = int(winst) if winst.lstrip("-").isdigit() else 0
    strong = o >= 150000 or abs(b) >= 150000 or abs(w) >= 100000
    print(f"{st} {kbo} {(title or '')[:60]} last={last} fte={fte} filed={filed}")
    print(f"  y5={y5}")
    if y4:
        print(f"  y4={y4}")
    if st == "FREE" and (y5 or last == "2025"):
        hits.append((strong, o, abs(b), kbo, label, title, y5, fte, filed, ve, status))
        if strong:
            print("  >>> STRONG FREE")

print("\n=== TOP FREE HITS ===")
hits.sort(key=lambda x: (-int(x[0]), -x[1], -x[2]))
for h in hits[:15]:
    print(h[0], h[3], h[4], (h[5] or "")[:50], h[6], "fte", h[7])
