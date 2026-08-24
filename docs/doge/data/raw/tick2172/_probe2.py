# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2172")

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
    ("0433217935", "curaz"),
    ("0445106274", "bernardus_assenede"),
    ("0406877485", "dhondt"),
    ("0426205850", "cobrha"),
    ("0405443129", "meander2"),
    ("0428471856", "ocura2"),
    ("0428335615", "zoete"),
    ("0454543856", "c0454"),
    ("0417562831", "c0417"),
    ("0421567839", "c0421"),
    ("0408215439", "c0408"),
    # more from social map / care
    ("0401785654", "x1"),
    ("0412785654", "x2"),
    ("0409587123", "slgw"),
    ("0485217639", "x0485"),
    ("0500958123", "x0500"),
    ("0548216379", "x0548"),
    ("0698215473", "x0698"),
    ("0758216347", "x0758"),
    ("0821563478", "x0821"),
    ("0863215478", "x0863"),
    ("0408123456", "x0408b"),
    ("0426701853", "x0426"),
    ("0439528714", "x0439"),
    ("0448521763", "margon"),
    ("0461852741", "x0461"),
    ("0471865204", "x0471"),
    ("0472185639", "x0472"),
    ("0408521763", "x0408c"),
    ("0419528741", "x0419"),
    ("0438521679", "beth2"),
    ("0425861473", "castel2"),
    ("0441258963", "pass2"),
    ("0452187639", "seig2"),
    ("0462871549", "ry2"),
    ("0471852036", "seni"),
    ("0405218763", "cfs"),
    # Flemish WZC guesses from repertory patterns
    ("0401234567", "bad"),
    ("0412345678", "bad2"),
    ("0423456789", "bad3"),
    ("0434567890", "bad4"),
    ("0445678901", "bad5"),
    ("0456789012", "bad6"),
    ("0467890123", "bad7"),
    ("0478901234", "bad8"),
    ("0489012345", "bad9"),
    ("0402345678", "b10"),
    ("0413456789", "b11"),
    ("0424567890", "b12"),
    ("0435678901", "b13"),
    ("0446789012", "b14"),
    ("0457890123", "b15"),
    ("0468901234", "b16"),
    ("0479012345", "b17"),
    ("0403456789", "b18"),
    ("0414567890", "b19"),
    ("0425678901", "b20"),
    ("0436789012", "b21"),
    ("0447890123", "b22"),
    ("0458901234", "b23"),
    ("0469012345", "b24"),
    ("0404567890", "b25"),
    ("0415678901", "b26"),
    ("0426789012", "b27"),
    ("0437890123", "b28"),
    ("0448901234", "b29"),
    ("0459012345", "b30"),
    # try Zorggroep / network shells
    ("0860500000", "zg"),
    ("0870500000", "zg2"),
    ("0880500000", "zg3"),
    ("0890500000", "zg4"),
    ("0800500000", "zg5"),
    ("0810500000", "zg6"),
    ("0820500000", "zg7"),
    ("0830500000", "zg8"),
    ("0840500000", "zg9"),
    ("0850500000", "zg10"),
]

for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t:
        continue
    yb, fte, filed, title, last = parse(t)
    y5 = yb.get("2025", {})
    if st == "FREE" and (y5 or last == "2025"):
        print(st, kbo, (title or "")[:55], "last", last)
        if y5:
            print(" ", y5, "fte", fte, "filed", filed)
            omzet = (y5.get("omzet") or "").replace(",", "")
            bruto = (y5.get("bruto_marge") or "").replace(",", "")
            equity = (y5.get("eigen_vermogen") or "0").replace(",", "")
            o = int(omzet) if omzet.isdigit() else 0
            b = int(bruto) if bruto.lstrip("-").isdigit() else 0
            e = int(equity) if equity.lstrip("-").isdigit() else 0
            if o >= 150000 or abs(b) >= 150000 or abs(e) >= 1000000:
                print("  >>> STRONG")
