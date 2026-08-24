# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2170")
out.mkdir(parents=True, exist_ok=True)

text = ""
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    text += open(path, encoding="utf-8", errors="replace").read().lower()


def is_mined(kbo):
    d = re.sub(r"\D", "", kbo)
    dotted = f"{d[:4]}.{d[4:7]}.{d[7:]}"
    return dotted in text


CANDS = [
    ("0428335615", "wzc_zoetenaard_stekene"),  # guess
    ("0476543210", "bad"),
    ("0405443123", "wzc_de_meander"),
    ("0417568421", "wzc_sint_anna_gent"),
    ("0424567891", "bad2"),
    ("0436123456", "bad3"),
    ("0442789456", "wzc_immaculata"),
    ("0453891234", "bad4"),
    ("0464123789", "wzc_de_wingerd"),
    ("0475234567", "bad5"),
    ("0486345678", "bad6"),
    ("0507456789", "bad7"),
    ("0538567890", "bad8"),
    ("0549678901", "bad9"),
    ("0550789012", "bad10"),
    ("0561890123", "bad11"),
    ("0572901234", "bad12"),
    ("0583012345", "bad13"),
    ("0604123456", "bad14"),
    ("0615234567", "bad15"),
    # known plausible from public lists / prior probes
    ("0405443129", "cand_a"),
    ("0412881234", "cand_b"),
    ("0421567890", "cand_c"),
    ("0432678901", "cand_d"),
    ("0443789012", "cand_e"),
    ("0454890123", "cand_f"),
    ("0465901234", "cand_g"),
    ("0476012345", "cand_h"),
    ("0487123456", "cand_i"),
    ("0508234567", "cand_j"),
    ("0416528391", "cand_0416528391"),
    ("0479984011", "cand_0479984011"),
    ("0441675147", "cand_0441675147"),
    ("0428471856", "cand_ocura"),
    ("0433419259", "cand_wezembeek_olv"),
    ("0479401318", "cand_ter_burg"),
    ("0454543856", "cand_0454543856"),
    ("0466266429", "cand_0466266429"),
    ("0845064196", "slg_ops"),
    ("0408215439", "cand_0408215439"),
    ("0417562831", "cand_0417562831"),
    ("0421567839", "cand_0421567839"),
    ("0406877485", "dhondt_skip"),
    ("0435357675", "psychogeriatrisch"),
    ("0445499422", "curando"),
    ("0418016550", "st_vincentius_antwerpen"),
    # more care from northdata-ish guesses
    ("0400555123", "x1"),
    ("0401556124", "x2"),
    ("0402557125", "x3"),
    ("0403558126", "x4"),
    ("0404559127", "x5"),
]


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
    act = re.search(r"Principal activity</[^>]+>\s*([^<]+)", t or "", re.I)
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        last.group(1) if last else None,
        (act.group(1).strip() if act else ""),
    )


for kbo, label in CANDS:
    if is_mined(kbo):
        print("SKIPMINED", kbo, label)
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"p2_{label}_{kbo}_en.html")
    if not t or "Error 404" in t or len(t) < 800:
        print("404", kbo, label)
        continue
    yb, fte, filed, title, last, act = parse(t)
    y5 = yb.get("2025", {})
    careish = any(
        x in (act or "").lower()
        for x in ["nursing", "rest", "elderly", "care", "repos", "rust", "woonzorg", "mrs"]
    )
    print("FREE", kbo, (title or "")[:55], "last", last, "fte", fte)
    print("  act", act[:60], "filed", filed, "2025", y5)
    if last == "2025" and y5:
        om = (y5.get("omzet") or "").replace(",", "")
        br = (y5.get("bruto_marge") or "").replace(",", "")
        try:
            o = int(om) if om.isdigit() else 0
            b = int(br) if br.isdigit() else 0
        except Exception:
            o = b = 0
        if o >= 200000 or b >= 200000:
            print("  >>> CANDIDATE", "CARE" if careish else "other")
