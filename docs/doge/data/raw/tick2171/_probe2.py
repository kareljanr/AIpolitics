# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2171")

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
    ("0416493254", "ben_woonzorgnetwerk"),
    ("0835884236", "woonzorg_het_dorp"),
    ("0410219433", "haagwinde"),
    ("0480566704", "hof_ter_lande"),
    ("0443249616", "stil_geluk"),
    ("0685516024", "wzn_edegem"),
    ("0883694744", "seigneurie"),
    ("0808910714", "bethanie"),
    ("0808928827", "le_progres"),
    ("0507866165", "ry_chevreuil"),
    ("0539934860", "passerinette"),
    ("0466266429", "helianthus"),
    ("0441675147", "wsr"),
    ("0598966387", "hoeksteen"),
    # more WZC networks
    ("0401785654", "cand_a"),
    ("0412785654", "cand_b"),
    ("0423785654", "cand_c"),
    ("0434785654", "cand_d"),
    ("0445785654", "cand_e"),
    ("0456785654", "cand_f"),
    ("0467785654", "cand_g"),
    ("0478785654", "cand_h"),
    ("0489785654", "cand_i"),
    ("0402789123", "cand_j"),
    ("0413789123", "cand_k"),
    ("0424789123", "cand_l"),
    ("0435789123", "cand_m"),
    ("0446789123", "cand_n"),
    ("0457789123", "cand_o"),
    ("0468789123", "cand_p"),
    ("0479789123", "cand_q"),
    ("0403794561", "cand_r"),
    ("0414794561", "cand_s"),
    ("0425794561", "cand_t"),
    ("0436794561", "cand_u"),
    ("0447794561", "cand_v"),
    ("0458794561", "cand_w"),
    ("0469794561", "cand_x"),
    ("0404812345", "cand_y"),
    ("0415812345", "cand_z"),
    # Idewa / water leftovers
    ("0201305123", "idewa_guess"),
    ("0204567890", "water_guess"),
    ("0408226993", "x_hop"),
    ("0880226993", "man_in_motion"),
    ("0883790853", "hop"),
    ("0644497395", "prinsenhof_check"),
    ("0416493254", "ben2"),
    # Novadia group?
    ("0640123456", "nova_guess"),
    ("0830123456", "x0830"),
    ("0840123456", "x0840"),
    ("0850123456", "x0850"),
    ("0860123456", "x0860"),
    ("0870123456", "x0870"),
    ("0880123456", "x0880"),
    ("0890123456", "x0890"),
    # known Flemish WZC from repertorium-style
    ("0400371161", "abdij_mined"),
    ("0420607638", "zonnelied_check"),
    ("0412763704", "groep_sf_check"),
    ("0419333572", "denderrust_check"),
    ("0409698009", "denderrust_dg_check"),
    ("0458352318", "orchidee_check"),
    ("0440737514", "corolles_check"),
    ("0409232013", "esplanade_check"),
    ("0416528391", "prestige_check"),
    ("0479984011", "peupliers_check"),
    ("0454712838", "egmont_check"),
    ("0466114791", "en_famille_check"),
    ("0422923859", "careion_check"),
    ("0413550491", "restel_check"),
    ("0415850084", "mpc_check"),
    ("0827850260", "caresupport_check"),
    ("0446222962", "olv_armen_check"),
    ("0414747056", "cigb_check"),
    ("0475400760", "famifamenne_check"),
    ("0427821963", "slg_wallonie_check"),
    ("0442694142", "sebrechts_check"),
    ("0459540765", "rsw_check"),
    ("0462316153", "castel_check"),
    ("0452587548", "parc_forest_check"),
    ("0421479153", "hanois_check"),
    ("0447771695", "epinette_check"),
    ("0435565236", "buurthuis_check"),
    ("0748968276", "jolimont_check"),
]

for kbo, label in CANDS:
    st = "MINED" if kbo in mined else "FREE"
    if st == "MINED" and label.endswith("_check"):
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t:
        if st == "FREE":
            print(st, kbo, label, "404")
        continue
    yb, fte, filed, title, last = parse(t)
    y5 = yb.get("2025", {})
    if st == "FREE":
        print(st, kbo, (title or "")[:55], "last", last)
        if y5:
            print(" ", y5, "fte", fte, "filed", filed)
            omzet = (y5.get("omzet") or "").replace(",", "")
            bruto = (y5.get("bruto_marge") or "").replace(",", "")
            o = int(omzet) if omzet.isdigit() else 0
            b = int(bruto) if bruto.isdigit() else 0
            if o >= 150000 or b >= 150000:
                print("  >>> STRONG")
