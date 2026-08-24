# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2169")
out.mkdir(parents=True, exist_ok=True)

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
    nace_all = re.findall(r"(\d{2}\.\d{3})", t or "")[:12]
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        nace_all,
    )


# More WZC / MRS / care / unused IGS guesses + stall checks
CANDS = [
    ("0877556624", "agb_bornem"),
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0400371161", "abdij_affligem"),
    ("0650907810", "ventu"),
    ("0787300696", "melis_home"),
    # additional care probes from nearby number ranges / known lists
    ("0405218763", "cfs"),
    ("0438521679", "bethanie"),
    ("0425861473", "le_castel"),
    ("0441258963", "passerinette"),
    ("0452187639", "seigneurie"),
    ("0440123456", "scan_bad"),
    ("0435218769", "chateau_vert_huy_check"),
    ("0416528391", "prestige_mined_check"),
    ("0479984011", "peupliers_mined_check"),
    ("0480566704", "cand_0480"),
    ("0475123890", "cand_0475"),
    ("0466266429", "cand_0466"),
    ("0464822341", "cand_0464"),
    ("0453380125", "cand_0453"),
    ("0443249616", "cand_0443"),
    ("0438687654", "cand_0438"),
    ("0432829147", "cand_0432"),
    ("0425123789", "cand_0425"),
    ("0422620585", "cand_0422"),
    ("0412210456", "cand_0412"),
    ("0405406887", "cand_0405"),
    ("0598966387", "cand_0598"),
    ("0685516024", "cand_0685"),
    ("0880226993", "cand_0880"),
    ("0883694744", "cand_0883"),
    ("0883790853", "cand_0883b"),
    ("0808910714", "cand_0808"),
    ("0808928827", "cand_0808b"),
    ("0507866165", "cand_0507"),
    ("0539934860", "cand_0539"),
    ("0462871549", "ry_chevreuil2"),
    ("0421479153", "p_0421"),
    ("0422923859", "p_0422b"),
    ("0423571581", "p_0423"),
    ("0430215789", "p_0430"),
    ("0433440342", "p_0433"),
    ("0435015702", "p_0435"),
    ("0440737514", "p_0440"),
    ("0441675147", "p_0441"),
    ("0446022331", "p_0446"),
    ("0446222962", "p_0446b"),
    ("0447771695", "p_0447"),
    ("0452587548", "p_0452"),
    ("0454712838", "p_0454"),
    ("0458352318", "p_0458"),
    ("0461852347", "p_0461"),
    ("0465723491", "p_0465"),
    ("0466114791", "p_0466b"),
    ("0472615953", "p_0472"),
    ("0478350612", "p_0478"),
    ("0500952540", "p_0500"),
    ("0827850260", "p_0827"),
    ("0845895824", "p_0845"),
    ("0861157387", "p_0861"),
    ("0865574649", "p_0865"),
    ("0895366220", "p_0895"),
]

for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t:
        print(st, kbo, "fail")
        continue
    if "Error 404" in t:
        print(st, kbo, "404")
        continue
    yb, fte, filed, title, nace = parse(t)
    y5 = yb.get("2025", {})
    if not y5 and "2025" not in str(yb):
        # only print stalls / free with year
        last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", t or "", re.I)
        yr = last.group(1) if last else "?"
        if st == "FREE" or label in ("agb_bornem", "faro", "aiesh", "rew"):
            print(st, kbo, (title or "")[:60], "last", yr, "nace", nace[:4])
        continue
    print(st, kbo, (title or "")[:65])
    print("  fte", fte, "filed", filed, "nace", nace[:5])
    print("  2025", y5)
    if st == "FREE" and y5:
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.isdigit() else 0
        careish = any(x.startswith(("87.", "86.", "88.")) for x in nace)
        if o >= 200000 or b >= 200000:
            print("  >>> STRONG", "CARE" if careish else "OTHER")
