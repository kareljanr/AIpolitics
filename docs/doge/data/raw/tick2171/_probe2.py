# -*- coding: utf-8 -*-
"""Probe named FREE WZC/MRS candidates from web + deferred list."""
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2171")
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
    d = re.sub(r"\D", "", kbo)
    return d in blob


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


def euro(s):
    if not s:
        return None
    s = s.replace("\xa0", "").replace(" ", "").replace(".", "").replace(",", "")
    try:
        return int(s)
    except Exception:
        return None


CANDS = [
    ("0424236725", "sint_antonius_spl"),
    ("0410142031", "olv_lourdes_kortenberg"),
    ("0835884236", "woonzorg_het_dorp"),
    ("0452587548", "parc_de_forest"),
    ("0422620585", "cobrha"),
    ("0787300696", "melis_home"),
    ("0480566704", "hof_ter_lande"),
    ("0410219433", "haagwinde"),
    ("0443249616", "stil_geluk"),
    ("0406877485", "dhondt"),
    ("0539934860", "passerinette"),
    ("0507866165", "ry_chevreuil"),
    ("0883694744", "seigneurie"),
    ("0808910714", "bethanie"),
    ("0808928827", "le_progres"),
    # more from companyweb search patterns / known Flanders WZC
    ("0417568421", "sint_anna_guess"),
    ("0421567890", "bad"),
    ("0436123456", "bad2"),
    ("0405443123", "meander_guess"),
    ("0410142031", "olv_lourdes"),
    ("0428335610", "zoet_guess"),
    ("0412881234", "bad3"),
    ("0453891234", "bad4"),
    ("0464123789", "wingerd_guess"),
    ("0475234567", "bad5"),
    ("0408215430", "bad6"),
    ("0419.528.741".replace(".", ""), "cand"),
    ("0425.123.789".replace(".", ""), "cand2"),
    ("0432.829.147".replace(".", ""), "cand3"),
    ("0438.687.654".replace(".", ""), "cand4"),
    ("0439.528.714".replace(".", ""), "cand5"),
    ("0452.187.639".replace(".", ""), "cand6"),
    ("0453.380.125".replace(".", ""), "cand7"),
    ("0464.822.341".replace(".", ""), "cand8"),
    ("0471.865.204".replace(".", ""), "cand9"),
    ("0472.185.639".replace(".", ""), "cand10"),
    ("0475.123.890".replace(".", ""), "cand11"),
    ("0548.216.379".replace(".", ""), "cand12"),
    # real known WZCs
    ("0405.406.887".replace(".", ""), "x"),
    ("0412.210.456".replace(".", ""), "x2"),
    ("0417.562.831".replace(".", ""), "x3"),
    ("0421.560.839".replace(".", ""), "x4"),
    ("0428.471.856".replace(".", ""), "ocura2"),
    ("0435.357.675".replace(".", ""), "psycho"),
    ("0445.499.422".replace(".", ""), "curando"),
    ("0454.543.856".replace(".", ""), "x5"),
    ("0479.401.318".replace(".", ""), "terburg"),
    ("0845.064.196".replace(".", ""), "slgops"),
    # Walloon / more
    ("0416.116.637".replace(".", ""), "charmille"),  # may be mined
    ("0440.737.514".replace(".", ""), "corolles"),
    ("0458.352.318".replace(".", ""), "orchidee"),
    ("0466.114.791".replace(".", ""), "en_famille"),
    ("0479.984.011".replace(".", ""), "peupliers"),
    ("0416.528.391".replace(".", ""), "prestige"),
    # fresh guesses from common WZC names
    ("0408.123.456".replace(".", ""), "bad7"),
    ("0410.987.654".replace(".", ""), "bad8"),
    ("0415.850.084".replace(".", ""), "mpc_franciscus"),  # likely mined
    ("0420.607.638".replace(".", ""), "zonnelied"),
    ("0419.333.572".replace(".", ""), "denderrust"),
    ("0409.698.009".replace(".", ""), "denderrust_dg"),
    ("0412.763.704".replace(".", ""), "gvo_franciscus"),
    ("0422.923.859".replace(".", ""), "seniors_care_ion"),
    ("0447.771.695".replace(".", ""), "epinette"),
    ("0823.488.131".replace(".", ""), "thofke"),
    ("0470.673.890".replace(".", ""), "zorgsaam"),
    ("0446.506.836".replace(".", ""), "avondvrede"),
    ("0469.969.453".replace(".", ""), "anima"),
    ("0698.940.725".replace(".", ""), "anima_vl"),
    ("0755.822.317".replace(".", ""), "lork_hoeselt"),
    ("0644.843.825".replace(".", ""), "aaigem"),
    ("0400.371.161".replace(".", ""), "affligem"),
    ("0410.127.084".replace(".", ""), "sint_lodewijk"),
    # additional Flanders WZC from public lists
    ("0407.355.940".replace(".", ""), "wzc_a"),
    ("0411.234.567".replace(".", ""), "bad9"),
    ("0413.789.012".replace(".", ""), "bad10"),
    ("0418.456.789".replace(".", ""), "bad11"),
    ("0424.236.725".replace(".", ""), "sint_antonius2"),
    ("0426.789.012".replace(".", ""), "bad12"),
    ("0429.012.345".replace(".", ""), "bad13"),
    ("0431.234.567".replace(".", ""), "bad14"),
    ("0436.789.012".replace(".", ""), "bad15"),
    ("0441.234.567".replace(".", ""), "bad16"),
    ("0444.567.890".replace(".", ""), "bad17"),
    ("0448.901.234".replace(".", ""), "bad18"),
    ("0450.123.456".replace(".", ""), "bad19"),
    ("0455.678.901".replace(".", ""), "bad20"),
    ("0459.012.345".replace(".", ""), "bad21"),
    ("0461.234.567".replace(".", ""), "bad22"),
    ("0465.678.901".replace(".", ""), "bad23"),
    ("0468.901.234".replace(".", ""), "bad24"),
    ("0472.345.678".replace(".", ""), "bad25"),
    ("0476.789.012".replace(".", ""), "bad26"),
    ("0480.123.456".replace(".", ""), "bad27"),
    ("0484.567.890".replace(".", ""), "bad28"),
    ("0488.901.234".replace(".", ""), "bad29"),
    ("0492.345.678".replace(".", ""), "bad30"),
    # known from care directories / sites
    ("0405.311.530".replace(".", ""), "elisabeth_aan_zee"),
    ("0412.640.671".replace(".", ""), "residence_3"),
    ("0443.082.637".replace(".", ""), "xxe_aout"),
    ("0466.961.859".replace(".", ""), "les_buissons"),
    ("0451.031.489".replace(".", ""), "sittelles"),
    ("0457.649.265".replace(".", ""), "charmilles"),
    ("0407.699.017".replace(".", ""), "entraide"),
    ("0899.812.184".replace(".", ""), "strebo"),
    ("0463.961.490".replace(".", ""), "bosquet"),
    ("0748.968.276".replace(".", ""), "unite_jolimont"),
    ("0435.565.236".replace(".", ""), "buurthuis"),
    ("0442.694.142".replace(".", ""), "sebrechts"),
    ("0459.540.765".replace(".", ""), "rsw"),
    ("0462.316.153".replace(".", ""), "le_castel"),
    ("0475.400.760".replace(".", ""), "famifamenne"),
    ("0427.821.963".replace(".", ""), "slg_wallonie"),
    ("0865.574.649".replace(".", ""), "fakkel"),
    ("0448.033.201".replace(".", ""), "chateau_vert"),
    ("0827.850.260".replace(".", ""), "care_support"),
    ("0446.222.962".replace(".", ""), "olv_armen"),
    ("0414.747.056".replace(".", ""), "cigb"),
    ("0454.712.838".replace(".", ""), "comte_egmont"),
]

print("=== PROBE2 ===")
hits = []
seen = set()
for kbo, label in CANDS:
    kbo = re.sub(r"\D", "", kbo).zfill(10)[-10:]
    if kbo in seen:
        continue
    seen.add(kbo)
    if is_mined(kbo):
        print("SKIPMINED", kbo, label)
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"p2_{label}_{kbo}_en.html")
    if not t or "Error 404" in t or len(t) < 800:
        print("404", kbo, label)
        continue
    yb, fte, filed, title, last, act = parse(t)
    y5 = yb.get("2025", {})
    om = euro(y5.get("omzet"))
    br = euro(y5.get("bruto_marge"))
    pnl = euro(y5.get("winst"))
    eq = euro(y5.get("eigen_vermogen"))
    care = any(
        x in ((title or "") + " " + act).lower()
        for x in [
            "woonzorg",
            "wzc",
            "rusthuis",
            "nursing",
            "repos",
            "mrs",
            "residence",
            "zorg",
            "elderly",
            "rest home",
            "maison de repos",
        ]
    )
    print(
        f"FREE {kbo} last={last} {(title or '')[:60]} care={care} fte={fte} filed={filed}"
    )
    print(f"  act={act[:70]}")
    print(f"  2025 omzet={om} bruto={br} pnl={pnl} eq={eq}")
    if last == "2025" and ((om or 0) + (br or 0) >= 150000):
        hits.append((kbo, label, title, act, om, br, pnl, eq, fte, filed, care))
        print("  >>> HIT")

print("\n=== HITS ===")
for h in hits:
    print(h)
