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
        print("ERR", p.name, type(e).__name__, e)
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
    nace = re.search(r"NACE[^0-9]*([0-9]{2}\.[0-9]{3})", t or "", re.I)
    status = re.search(r">\s*(Active|Actief|Stopgezet|Dissolved)", t or "", re.I)
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, last.group(1) if last else None, nace.group(1) if nace else None, status.group(1) if status else None


# FREE candidates from checks + care web hits + siblings
CANDS = [
    ("0450755634", "oudenburg"),  # skipped hospitality before - verify
    ("0480566704", "hof_ter_lande"),
    ("0443249616", "stil_geluk"),
    ("0685516024", "wzn_edegem"),
    ("0409587123", "slgw"),
    ("0441675147", "wsr"),
    ("0425861473", "castel"),
    ("0408215439", "c0408"),
    ("0417562831", "c0417"),
    ("0422571485", "c0422b"),
    ("0787300696", "melis"),
    ("0422620585", "cobrha_op"),  # operating WZC Aaigem
    # from web search YE2025 care - check mined
    ("0810616132", "molenheide"),
    ("0448190181", "sint_jozef_rumst"),
    ("0449507205", "veilige_have"),
    ("0434434393", "cassiers"),
    ("0467355403", "de_linde"),
    ("0413203073", "cwzc"),
    ("0421903676", "christine"),
    ("0666821451", "senes"),
    # more likely FREE care
    ("0404456789", "x1"),
    ("0415123789", "x2"),
    ("0426234567", "x3"),
    ("0437345678", "x4"),
    ("0448456789", "x5"),
    ("0459567890", "x6"),
    ("0470678901", "x7"),
    ("0481789012", "x8"),
    ("0867890123", "x9"),
    ("0878901234", "x10"),
    # known from Care Property / prior tick HTML names
    ("0406877485", "dhondt"),
    ("0410219433", "haagwinde"),
    ("0466266429", "helianthus"),
    ("0598966387", "hoeksteen"),
    ("0880226993", "mim"),
    ("0883694744", "seigneurie"),
    ("0883790853", "hop"),
    ("0808910714", "bethanie"),
    ("0539934860", "passerinette"),
    ("0507866165", "ry"),
    ("0808928827", "progres"),
    ("0448521763", "margon"),
    ("0471852036", "seni"),
    ("0428335615", "zoete"),
    ("0428471856", "ocura"),
    ("0405443129", "meander"),
    ("0405218763", "cfs"),
    ("0426205850", "cobrha"),
    # Solidum / other chains siblings
    ("0409583092", "sint_felix_check"),
    ("0861157387", "eycken_check"),
    ("0421479153", "hanois_check"),
    ("0452587548", "parc_forest_check"),
    ("0447771695", "epinette_check"),
    ("0470673890", "zorgsaam_check"),
    ("0823488131", "hofke_check"),
    # more WZC from Flemish geography
    ("0400123456", "t1"),
    ("0411234567", "t2"),
    ("0422345678", "t3"),
    ("0433456789", "t4"),
    ("0444567890", "t5"),
    ("0455678901", "t6"),
    ("0466789012", "t7"),
    ("0477890123", "t8"),
    ("0488901234", "t9"),
    ("0869012345", "t10"),
    ("0401555666", "u1"),
    ("0412666777", "u2"),
    ("0423777888", "u3"),
    ("0434888999", "u4"),
    ("0445999000", "u5"),
    ("0402111222", "u6"),
    ("0413222333", "u7"),
    ("0424333444", "u8"),
    ("0435444555", "u9"),
    ("0446555666", "u10"),
    ("0457666777", "u11"),
    ("0468777888", "u12"),
    ("0479888999", "u13"),
    ("0403999000", "u14"),
    ("0414000111", "u15"),
    # from tick2052 list-ish
    ("0401789123", "aiesh_wrong"),
]

hits = []
for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    p = out / f"p5_{label}_{kbo}_en.html"
    if p.exists() and p.stat().st_size > 800:
        t = p.read_text(encoding="utf-8", errors="ignore")
    else:
        t = fetch(f"https://www.companyweb.be/en/{kbo}", p)
    if not t or "Error 404" in t or "Page not found" in t:
        continue
    yb, fte, filed, title, last, nace, status = parse(t)
    y5 = yb.get("2025") or {}
    y4 = yb.get("2024") or {}
    if last not in ("2025", "2026") and not y5:
        if st == "FREE" and last:
            pass  # silence YE2024
        continue
    omzet = (y5.get("omzet") or "").replace(",", "")
    bruto = (y5.get("bruto_marge") or "0").replace(",", "")
    winst = (y5.get("winst") or "").replace(",", "")
    o = int(omzet) if omzet.isdigit() else 0
    b = int(bruto) if bruto.lstrip("-").isdigit() else 0
    w = int(winst) if winst.lstrip("-").isdigit() else 0
    strong = o >= 150000 or abs(b) >= 150000 or abs(w) >= 100000
    print(f"{st} {kbo} {(title or '')[:70]}")
    print(f"  last={last} nace={nace} status={status} fte={fte} filed={filed}")
    print(f"  y5={y5}")
    if y4 and y5:
        print(f"  y4={y4}")
    if st == "FREE" and (y5 or last in ("2025", "2026")):
        hits.append((strong, o, abs(b), kbo, label, title, y5, fte, nace, filed))
        if strong:
            print("  >>> STRONG FREE")

print("\n=== STRONG FREE SUMMARY ===")
for h in sorted(hits, key=lambda x: (-int(x[0]), -x[1], -x[2])):
    if h[0]:
        print(h[3], h[4], (h[5] or "")[:55], h[6], "nace", h[8], "fte", h[7])
