# -*- coding: utf-8 -*-
"""Probe unused WZC/MRS candidates for YE2025 live euros."""
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2173")
out.mkdir(parents=True, exist_ok=True)

text = ""
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    text += open(path, encoding="utf-8", errors="replace").read().lower()
blob = re.sub(r"[.\s]", "", text)


def is_mined(kbo):
    d = re.sub(r"\D", "", kbo).zfill(10)[-10:]
    dotted = f"{d[:4]}.{d[4:7]}.{d[7:]}"
    return d in blob or dotted in text


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


# Prefer public-ish / care; skip known mined from entities list comments.
CANDS = [
    # web search hits
    ("0452865383", "jozef_ninove"),  # likely mined
    ("0413055989", "jozef_aarschot"),  # likely mined
    ("0459770496", "augustinus_halle"),  # likely mined
    ("0864332554", "langerheide_haacht"),
    ("0446222962", "olv_armen_aalst"),  # likely mined
    ("0463758978", "huize_vincent"),  # likely mined
    ("0861157387", "eycken_brug"),  # likely mined
    ("0417958152", "camillus_wevelgem"),  # likely mined
    # prior p3 almost/real from tick2171
    ("0424830108", "home_stuyvenberg"),  # likely mined nv_home_stuyvenberg
    ("0439442761", "prinsenhof_bilzen"),
    ("0424236725", "sint_antonius"),
    ("0409970203", "sint_carolus_ternat"),
    ("0410142031", "olv_lourdes"),
    ("0435015702", "lindeboom"),
    ("0428659430", "mater_dei_heikruis"),  # likely mined
    # more unused guesses from recent Flemish WZC lists / CoBRHA siblings / CuraCare
    ("0412218563", "cand_a"),
    ("0423345678", "cand_b"),
    ("0434456789", "cand_c"),
    ("0445567890", "cand_d"),
    ("0456678901", "cand_e"),
    ("0467789012", "cand_f"),
    ("0478890123", "cand_g"),
    ("0489901234", "cand_h"),
    ("0501012345", "cand_i"),
    ("0532123456", "cand_j"),
    # known from Flanders WZC public lists (verify free)
    ("0407355940", "wzc_a"),
    ("0416528391", "cand_0416528391"),
    ("0433419259", "wezembeek_olv"),
    ("0479401318", "ter_burg"),
    ("0435357675", "psychogeriatrisch"),
    ("0445499422", "curando"),
    ("0418016550", "st_vincentius_antwerpen"),
    ("0845064196", "slg_ops"),
    # Walloon MRS / residences often YE2025 on CW
    ("0425861473", "le_castel"),
    ("0448521763", "margon"),
    ("0471852036", "seniservices"),
    ("0409587123", "slgw"),
    ("0462871549", "ry2"),
    ("0438521679", "bethanie2"),
    ("0441258963", "passerinette2"),
    ("0452187639", "seigneurie2"),
    # CuraCare / related unused?
    ("0860500000", "zg_bad"),
    ("0416501234", "x"),
    # more real KBOs from SBM-ish / prior free notes
    ("0405406887", "x0405"),
    ("0412210456", "x0412"),
    ("0432829147", "x0432"),
    ("0438687654", "x0438"),
    ("0453380125", "x0453"),
    ("0464822341", "x0464"),
    ("0465723491", "x0465"),
    ("0472615953", "x0472"),
    ("0478350612", "x0478"),
    ("0482156739", "x0482"),
    # IGS water leftover guesses
    ("0214014167", "idm"),
    ("0220574436", "ivm"),
    ("0205657869", "wvi"),
    ("0500929081", "hvz_vbw"),
    ("0500928388", "hvz_waasland"),
    ("0500928586", "hvz_zuidoost"),
]


for kbo, label in CANDS:
    st = "MINED" if is_mined(kbo) else "FREE"
    if st == "MINED" and label not in (
        "langerheide_haacht",
        "prinsenhof_bilzen",
        "sint_antonius",
        "sint_carolus_ternat",
        "lindeboom",
        "olv_lourdes",
        "idm",
        "ivm",
        "wvi",
    ):
        # still check promising web hits even if mined to confirm
        if label not in (
            "jozef_ninove",
            "jozef_aarschot",
            "augustinus_halle",
            "home_stuyvenberg",
        ):
            continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t or len(t) < 800:
        if st == "FREE":
            print(st, kbo, label, "404")
        continue
    yb, fte, filed, title, last, act = parse(t)
    y5 = yb.get("2025", {})
    careish = any(
        x in ((title or "") + " " + act).lower()
        for x in [
            "woonzorg",
            "wzc",
            "rusthuis",
            "nursing",
            "repos",
            "mrs",
            "residence",
            "elderly",
            "rest home",
            "zorg",
        ]
    )
    show = st == "FREE" or (y5 and last == "2025")
    if show:
        print(st, kbo, (title or "")[:60], "last", last, "fte", fte)
        print("  act", (act or "")[:70], "filed", filed)
        print("  2025", y5)
        if st == "FREE" and last == "2025" and y5 and any(y5.values()):
            print("  >>> CANDIDATE", "CARE" if careish else "other")
