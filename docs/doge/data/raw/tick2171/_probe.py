# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2171")
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
    nace = re.findall(r"(?:87|86|88|84|36|37|38)\.\d{3}", t or "")[:6]
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        last.group(1) if last else None,
        nace,
    )


CANDS = [
    ("0877556624", "agb_bornem"),
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    # known FREE/deferred from prior ticks
    ("0480566704", "hof_ter_lande"),
    ("0685516024", "wzn_edegem"),
    ("0443249616", "stil_geluk"),
    ("0598966387", "de_hoeksteen"),
    ("0883694744", "seigneurie"),
    ("0808910714", "bethanie"),
    ("0808928827", "le_progres"),
    ("0507866165", "ry_chevreuil"),
    ("0539934860", "passerinette"),
    ("0422620585", "sint_vincentius_parent"),
    ("0410219433", "haagwinde"),
    ("0466266429", "helianthus"),
    ("0441675147", "wsr"),
    # more care/IGS guesses near known ranges
    ("0405218763", "cfs"),
    ("0438521679", "bethanie2"),
    ("0425861473", "le_castel"),
    ("0441258963", "passerinette2"),
    ("0452187639", "seigneurie2"),
    ("0462871549", "ry2"),
    ("0471852036", "seniservices"),
    ("0409587123", "slgw"),
    ("0485217639", "x0485"),
    ("0500958123", "x0500"),
    ("0548216379", "x0548"),
    ("0698215473", "x0698"),
    ("0758216347", "x0758"),
    ("0821563478", "x0821"),
    ("0863215478", "x0863"),
    ("0408123456", "x0408"),
    ("0426701853", "x0426"),
    ("0439528714", "x0439"),
    ("0448521763", "margon"),
    ("0461852741", "x0461"),
    ("0471865204", "x0471"),
    ("0472185639", "x0472"),
    ("0408521763", "x0408b"),
    ("0419528741", "x0419"),
    # IGS / HVZ / water leftovers sometimes missed
    ("0214014167", "idm_check"),
    ("0220574436", "ivm_check"),
    ("0205657869", "wvi_check"),
    ("0500928388", "hvz_waasland_check"),
    ("0500928586", "hvz_zuidoost_check"),
    ("0500929081", "hvz_vbw_check"),
    # Novadia / Care-Ion siblings sometimes deferred
    ("0641760611", "numera"),
    ("0650907810", "ventu"),
    ("0787300696", "melis"),
    ("0400371161", "abdij_check"),
    # try more WZC from Flemish lists
    ("0416337262", "vrijzicht_check"),
    ("0414678562", "vander_check"),
    ("0418234997", "witte_check"),
    ("0449425546", "wijtshage_check"),
    ("0422152314", "barbara_check"),
    ("0413055989", "jozef_aarschot_check"),
    ("0448190181", "jozef_rumst_check"),
    ("0411600692", "maria_check"),
    ("0453287037", "samen_check"),
    ("0410127084", "lodewijk_check"),
    ("0454090355", "zusters_check"),
    ("0417958152", "camillus_check"),
    ("0445175263", "zilverlinde_check"),
    ("0452865383", "jozef_ninove_check"),
    ("0459770496", "augustinus_check"),
    ("0448033201", "chateau_check"),
    ("0463758978", "vincent_check"),
    ("0421903676", "christine_check"),
    ("0810616132", "molenheide_check"),
    ("0633687439", "walfergem_check"),
    ("0500952540", "wznd_check"),
    ("0861157387", "eycken_check"),
    ("0865574649", "fakkel_check"),
    ("0895366220", "annuntiaten_check"),
    ("0845895824", "hertog_check"),
    ("0435015702", "lindeboom_check"),
    ("0446022331", "lork_geel_check"),
    ("0433440342", "olv_check"),
    ("0423571581", "salvator_check"),
    ("0698940725", "anima_vl_check"),
    ("0446506836", "avond_check"),
    ("0469969453", "anima_hold_check"),
    ("0755822317", "lorkh_check"),
    ("0470673890", "zorgsaam_check"),
    ("0823488131", "thofke_check"),
    ("0473694748", "ruggeveld_check"),
    ("0412886636", "boterlaar_check"),
    ("0432582485", "bernardus_check"),
    ("0644843825", "aaigem_check"),
    ("0410127084", "lodewijk2"),
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
            "wzn_edegem",
            "haagwinde",
            "stil_geluk",
        ):
            print(st, kbo, "404/fail")
        continue
    yb, fte, filed, title, last, nace = parse(t)
    y5 = yb.get("2025", {})
    if label in ("agb_bornem", "faro", "aiesh", "rew") or (st == "FREE" and (y5 or last == "2025")):
        print(st, kbo, (title or "")[:55])
        print("  last", last, "fte", fte, "filed", filed, "nace", nace[:3])
        print("  2025", y5 if y5 else "-")
    if st == "FREE" and y5:
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.isdigit() else 0
        if o >= 200000 or b >= 200000:
            care = any(x.startswith(("87.", "86.", "88.", "84.", "36.", "37.", "38.")) for x in nace)
            print("  >>> STRONG", "care/igs" if care else "other")
            strong.append((kbo, title, y5, fte, filed, nace, care))

print("\n=== STRONG FREE YE2025 ===")
for s in strong:
    print(s[0], (s[1] or "")[:50], s[2], "fte", s[3], "care", s[6], "nace", s[5][:3])
