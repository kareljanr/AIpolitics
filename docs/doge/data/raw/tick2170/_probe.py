# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2170")
out.mkdir(parents=True, exist_ok=True)

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
    nace = re.findall(r"87\.\d{3}|86\.\d{3}|88\.\d{3}|84\.250", t or "")[:6]
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, last.group(1) if last else None, nace


CANDS = [
    ("0877556624", "agb_bornem"),
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0787300696", "melis_home"),
    ("0400371161", "abdij_affligem"),
    ("0685516024", "wzn_edegem"),
    ("0480566704", "hof_ter_lande"),
    ("0443249616", "stil_geluk"),
    ("0422620585", "sint_vincentius_parent"),
    ("0598966387", "de_hoeksteen"),
    ("0883694744", "seigneurie_du_val"),
    ("0808910714", "bethanie_namur"),
    ("0808928827", "le_progres"),
    ("0507866165", "ry_chevreuil"),
    ("0539934860", "passerinette"),
    ("0880226993", "man_in_motion"),
    ("0883790853", "hop_brugge"),
    ("0650907810", "ventu"),
    ("0641760611", "numera"),
    # more care guesses
    ("0410219433", "cand_0410"),
    ("0409232013", "esplanade"),
    ("0409583092", "sint_felix_check"),
    ("0412886636", "boterlaar_check"),
    ("0432582485", "bernardus_check"),
    ("0473694748", "ruggeveld_check"),
    ("0450755634", "oudenburg"),
    ("0461852347", "p_0461"),
    ("0465723491", "p_0465"),
    ("0472615953", "p_0472"),
    ("0478350612", "p_0478"),
    ("0482156739", "p_0482"),
    ("0500958123", "p_0500"),
    ("0413796456", "de_foyer_check"),
    ("0426701853", "x_0426"),
    ("0439528714", "x_0439"),
    ("0448521763", "margon"),
    ("0452187639", "x_0452"),
    ("0461852741", "x_0461b"),
    ("0471865204", "x_0471"),
    ("0472185639", "x_0472b"),
    ("0408521763", "x_0408"),
    ("0419528741", "x_0419"),
    ("0758216347", "x_0758"),
    ("0698215473", "x_0698"),
    ("0548216379", "x_0548"),
    ("0863215478", "x_0863"),
    ("0821563478", "x_0821"),
]

for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t:
        print(st, kbo, "404/fail")
        continue
    yb, fte, filed, title, last, nace = parse(t)
    y5 = yb.get("2025", {})
    print(st, kbo, (title or "")[:60])
    print("  last", last, "fte", fte, "filed", filed, "nace", nace[:3])
    print("  2025", y5 if y5 else "-")
    if st == "FREE" and y5:
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.isdigit() else 0
        if o >= 150000 or b >= 150000:
            print("  >>> STRONG", "care" if nace else "other")
