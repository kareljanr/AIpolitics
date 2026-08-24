# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2170")

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


# Broader WZC/MRS/IGS/HVZ candidates from recent deferred + nearby
CANDS = [
    ("0650907810", "ventu"),
    ("0641760611", "numera"),
    ("0400371161", "abdij_affligem"),
    ("0787300696", "melis_skip"),
    # unused Walloon MRS still YE2024? check anyway
    ("0416337262", "vrijzicht_check"),
    ("0414678562", "vander_stokken_check"),
    ("0418234997", "witte_meren_check"),
    ("0449425546", "wijtshage_check"),
    ("0422152314", "sint_barbara_check"),
    ("0413055989", "sint_jozef_aarschot_check"),
    ("0448190181", "sint_jozef_rumst_check"),
    ("0411600692", "maria_check"),
    ("0453287037", "samen_ouder_check"),
    ("0410127084", "sint_lodewijk_check"),
    ("0454090355", "zusters_deinze_check"),
    ("0417958152", "camillus_check"),
    ("0445175263", "zilverlinde_check"),
    ("0452865383", "sint_jozef_ninove_check"),
    ("0459770496", "augustinus_check"),
    ("0448033201", "chateau_vert_check"),
    ("0463758978", "huize_vincent_check"),
    ("0421903676", "christine_check"),
    ("0810616132", "molenheide_check"),
    ("0845064196", "slg_operaties_check"),
    ("0887690451", "emeis_check"),
    ("0633687439", "walfergem_check"),
    ("0500952540", "wznd_check"),
    ("0861157387", "eycken_check"),
    ("0865574649", "fakkel_check"),
    ("0895366220", "annuntiaten_check"),
    ("0845895824", "hertog_jan_check"),
    ("0435015702", "lindeboom_check"),
    ("0446022331", "lork_geel_check"),
    ("0433440342", "olv_kempen_check"),
    ("0423571581", "salvator_check"),
    ("0698940725", "anima_vl_check"),
    ("0446506836", "avondvrede_check"),
    ("0469969453", "anima_hold_check"),
    ("0755822317", "lork_hoeselt_check"),
    ("0470673890", "zorgsaam_check"),
    ("0823488131", "thofke_check"),
    # try more unknown WZC numbers
    ("0405406887", "x_0405"),
    ("0412210456", "x_0412"),
    ("0425123789", "x_0425"),
    ("0432829147", "x_0432"),
    ("0438687654", "x_0438"),
    ("0441675147", "wsr"),
    ("0453380125", "x_0453"),
    ("0464822341", "x_0464"),
    ("0466266429", "helianthus"),
    ("0475123890", "x_0475"),
    ("0480566704", "hof_ter_lande"),
    ("0598966387", "hoeksteen"),
    ("0685516024", "wzn_edegem"),
    ("0408123456", "bad"),
    ("0410958712", "slg_vl"),
    ("0889421308", "armonea"),
    # Zone de secours unused?
    ("0500915820", "zs_guess1"),
    ("0500916310", "zs_guess2"),
    ("0500927108", "zs_guess3"),
    ("0500928000", "zs_guess4"),
    ("0500914821", "zs_liege"),
    ("0500913830", "zs_namur"),
    ("0500912840", "zs_lux"),
]

strong = []
for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t:
        if st == "FREE":
            print(st, kbo, "404")
        continue
    yb, fte, filed, title, last = parse(t)
    y5 = yb.get("2025", {})
    if st != "FREE":
        continue
    print(st, kbo, (title or "")[:55], "last", last, "y5", bool(y5))
    if y5:
        print(" ", y5, "fte", fte, "filed", filed)
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.isdigit() else 0
        if o >= 200000 or b >= 200000:
            strong.append((kbo, title, y5, fte, filed))
            print("  >>> STRONG")

print("\n=== STRONG FREE YE2025 ===")
for s in strong:
    print(s[0], (s[1] or "")[:50], s[2], "fte", s[3])
