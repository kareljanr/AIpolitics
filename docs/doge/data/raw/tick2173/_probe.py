# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2173")
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
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
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
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, last.group(1) if last else None


CANDS = [
    ("0877556624", "agb_bornem"),
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0480566704", "hof_ter_lande"),
    ("0443249616", "stil_geluk"),
    ("0685516024", "wzn_edegem"),
    ("0410219433", "haagwinde"),
    ("0445106274", "bernardus_assenede"),
    ("0598966387", "hoeksteen"),
    ("0883694744", "seigneurie"),
    ("0808910714", "bethanie"),
    ("0808928827", "le_progres"),
    ("0507866165", "ry_chevreuil"),
    ("0539934860", "passerinette"),
    ("0441675147", "wsr"),
    ("0466266429", "helianthus"),
    ("0406877485", "dhondt"),
    ("0880226993", "man_in_motion"),
    ("0883790853", "hop"),
    # skip mined
    ("0433217935", "curaz_check"),
    ("0835884236", "hetdorp_check"),
    ("0416493254", "ben_check"),
    ("0898596122", "vlietoever_check"),
    # more care nets / WZC
    ("0405443129", "meander"),
    ("0428471856", "ocura"),
    ("0428335615", "zoete"),
    ("0454543856", "c0454"),
    ("0417562831", "c0417"),
    ("0421567839", "c0421"),
    ("0408215439", "c0408"),
    ("0426205850", "cobrha"),
    ("0438521679", "beth2"),
    ("0425861473", "castel"),
    ("0441258963", "pass2"),
    ("0452187639", "seig2"),
    ("0462871549", "ry2"),
    ("0471852036", "seni"),
    ("0405218763", "cfs"),
    ("0409587123", "slgw"),
    ("0485217639", "x0485"),
    ("0500958123", "x0500"),
    ("0548216379", "x0548"),
    ("0698215473", "x0698"),
    ("0758216347", "x0758"),
    ("0821563478", "x0821"),
    ("0863215478", "x0863"),
    ("0448521763", "margon"),
    ("0461852741", "x0461"),
    ("0471865204", "x0471"),
    ("0472185639", "x0472"),
    ("0408521763", "x0408c"),
    ("0419528741", "x0419"),
    ("0426701853", "x0426"),
    ("0439528714", "x0439"),
    ("0408123456", "x0408b"),
    # try more Vlaamse WZC from common patterns / prior free probes
    ("0401785654", "f1"),
    ("0412785654", "f2"),
    ("0423785654", "f3"),
    ("0434785654", "f4"),
    ("0445785654", "f5"),
    ("0456785654", "f6"),
    ("0467785654", "f7"),
    ("0478785654", "f8"),
    ("0402789123", "f9"),
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
]

strong = []
for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t:
        if st == "FREE" and label in (
            "agb_bornem",
            "faro",
            "aiesh",
            "rew",
            "hof_ter_lande",
            "stil_geluk",
            "wzn_edegem",
            "haagwinde",
            "bernardus_assenede",
            "dhondt",
        ):
            print(st, kbo, label, "404")
        continue
    yb, fte, filed, title, last = parse(t)
    y5 = yb.get("2025", {})
    show = label in (
        "agb_bornem",
        "faro",
        "aiesh",
        "rew",
        "hof_ter_lande",
        "stil_geluk",
        "wzn_edegem",
        "haagwinde",
        "bernardus_assenede",
        "dhondt",
    ) or (st == "FREE" and (y5 or last == "2025"))
    if show:
        print(st, kbo, (title or "")[:55], "last", last)
        if y5:
            print(" ", y5, "fte", fte, "filed", filed)
    if st == "FREE" and y5:
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "0").replace(",", "")
        equity = (y5.get("eigen_vermogen") or "0").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.lstrip("-").isdigit() else 0
        e = int(equity) if equity.lstrip("-").isdigit() else 0
        if o >= 150000 or abs(b) >= 150000 or abs(e) >= 1000000:
            print("  >>> STRONG")
            strong.append((kbo, title, y5, fte, filed))

print("\nSTRONG FREE:", len(strong))
for s in strong:
    print(s[0], (s[1] or "")[:50], s[2], "fte", s[3])
