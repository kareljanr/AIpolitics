# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2169")

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


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        p.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", p.name, type(e).__name__)
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
    # NACE from activity section often appears as 87.101 style near "Main activity"
    main = re.search(r"Main activity</[^>]*>\s*<[^>]+>([^<]+)", t or "", re.I)
    nace = re.findall(r"87\.\d{3}|86\.\d{3}|88\.\d{3}|84\.250|36\.\d{3}|37\.\d{3}|38\.\d{3}", t or "")[:8]
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, last.group(1) if last else None, main.group(1).strip() if main else None, nace


CANDS = [
    ("0685516024", "woonzorgnetwerk_edegem"),
    ("0598966387", "de_hoeksteen"),
    ("0480566704", "hof_ter_lande"),
    ("0400371161", "abdij_affligem"),
    ("0787300696", "melis_home"),
    ("0650907810", "ventu"),
    ("0443249616", "stil_geluk"),
    ("0422620585", "sint_vincentius_erpe"),
    ("0883694744", "seigneurie_du_val"),
    ("0808910714", "bethanie_namur"),
    ("0808928827", "le_progres"),
    ("0507866165", "ry_chevreuil"),
    ("0539934860", "passerinette"),
    ("0880226993", "man_in_motion"),
    ("0883790853", "hop_brugge"),
    # more random WZC from earlier raw filenames that looked FREE-ish
    ("0408123456", "x_bad"),
    ("0410958712", "x_0410"),
    ("0889421308", "x_0889"),
    ("0409587123", "slgw"),
    ("0471865204", "extra1"),
    ("0426701853", "extra2"),
    ("0419528741", "extra3"),
    ("0461852741", "extra4"),
    ("0439528714", "extra5"),
    ("0452187639", "extra6"),
    ("0448521763", "extra7"),
    ("0472185639", "extra8"),
    ("0408521763", "extra9"),
    ("0485217639", "extra10"),
    ("0863215478", "extra11"),
    ("0821563478", "extra12"),
    ("0758216347", "extra13"),
    ("0698215473", "extra14"),
    ("0548216379", "extra15"),
    ("0500958123", "extra16"),
]

for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t:
        print(st, kbo, "404/fail")
        continue
    yb, fte, filed, title, last, main, nace = parse(t)
    y5 = yb.get("2025", {})
    print(st, kbo, (title or "")[:60])
    print("  last", last, "fte", fte, "filed", filed)
    print("  main", main, "nace87", nace[:4])
    print("  2025", y5 if y5 else "-")
    if st == "FREE" and y5:
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.isdigit() else 0
        if o >= 150000 or b >= 150000:
            print("  >>> TAKE?", "care" if nace else "other")
