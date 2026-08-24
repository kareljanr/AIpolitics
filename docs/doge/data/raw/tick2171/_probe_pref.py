# -*- coding: utf-8 -*-
"""Probe preferred leftovers + find FREE YE2025 WZC/MRS/IGS candidates."""
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
    return d in blob or f"{d[:4]}.{d[4:7]}.{d[7:]}" in text


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        p.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", p.name, type(e).__name__, e)
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
    nace = re.findall(
        r"87\.\d{3}|86\.\d{3}|88\.\d{3}|68\.\d{3}|55\.\d{3}|47\.\d{3}|94\.\d{3}|35\.\d{3}",
        t or "",
    )[:6]
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        last.group(1) if last else None,
        (act.group(1).strip() if act else ""),
        nace,
    )


def euro(s):
    if not s:
        return None
    s = s.replace("\xa0", "").replace(" ", "").replace(".", "").replace(",", "")
    try:
        return int(s)
    except Exception:
        return None


PREF = [
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0877556624", "agb_bornem"),
    ("0787300696", "melis"),
]

print("=== PREFERRED ===")
for kbo, label in PREF:
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t:
        print("404", label, kbo)
        continue
    yb, fte, filed, title, last, act, nace = parse(t)
    y5 = yb.get("2025", {})
    print(
        f"{label} mined={is_mined(kbo)} last={last} fte={fte} filed={filed} nace={nace}"
    )
    print(f"  {(title or '')[:70]}")
    print(f"  act={act[:70]}")
    print(
        f"  2025 omzet={y5.get('omzet')} bruto={y5.get('bruto_marge')} "
        f"pnl={y5.get('winst')} eq={y5.get('eigen_vermogen')}"
    )
    if "2024" in yb:
        y4 = yb["2024"]
        print(
            f"  2024 omzet={y4.get('omzet')} bruto={y4.get('bruto_marge')} "
            f"pnl={y4.get('winst')} eq={y4.get('eigen_vermogen')}"
        )

# Candidate WZC / MRS / care VZW-BV from known public lists / prior deferred
CANDS = [
    ("0408215439", "cand_0408215439"),
    ("0417562831", "cand_0417562831"),
    ("0421567839", "cand_0421567839"),
    ("0435357675", "psychogeriatrisch"),
    ("0445499422", "curando"),
    ("0418016550", "st_vincentius_antwerpen"),
    ("0428471856", "ocura"),
    ("0433419259", "wezembeek_olv"),
    ("0479401318", "ter_burg"),
    ("0454543856", "cand_0454543856"),
    ("0466266429", "helianthus"),
    ("0845064196", "slg_ops"),
    ("0410958712", "slg_vl"),
    ("0441675147", "wsr"),
    ("0480566704", "hof_ter_lande"),
    ("0598966387", "hoeksteen"),
    ("0880226993", "man_in_motion"),
    ("0448521763", "margon"),
    ("0411600692", "maria"),
    ("0810616132", "molenheide"),
    ("0641760611", "numera"),
    ("0433440342", "olv_kempen"),
    ("0539934860", "passerinette"),
    ("0507866165", "ry_chevreuil"),
    ("0453287037", "samen_ouder"),
    ("0883694744", "seigneurie"),
    ("0422152314", "sint_barbara"),
    ("0409583092", "sint_felix"),
    ("0413055989", "sint_jozef_aarschot"),
    ("0452865383", "sint_jozef_ninove"),
    ("0448190181", "sint_jozef_rumst"),
    ("0443249616", "stil_geluk"),
    ("0414678562", "vander_stokken"),
    ("0416337262", "vrijzicht"),
    ("0633687439", "walfergem"),
    ("0449425546", "wijtshage"),
    ("0418234997", "witte_meren"),
    ("0685516024", "wzn_edegem"),
    ("0500952540", "wznd"),
    ("0445175263", "zilverlinde"),
    ("0454090355", "zusters_deinze"),
    ("0808910714", "bethanie_namur"),
    ("0808928827", "le_progres"),
    ("0883790853", "hop_brugge"),
    ("0409232013", "esplanade"),
    ("0428335615", "zoetenaard"),
    ("0405443129", "meander"),
    ("0479984011", "cand_0479984011"),
    ("0416528391", "cand_0416528391"),
    # more Flemish WZC from care-sector known KBOs
    ("0406877485", "dhondt"),
    ("0426205850", "cobrha_check"),
    ("0410219433", "cand_0410219433"),
    ("0461852347", "cand_0461852347"),
    ("0465723491", "cand_0465723491"),
    ("0472615953", "cand_0472615953"),
    ("0478350612", "cand_0478350612"),
    ("0482156739", "cand_0482156739"),
    ("0500958123", "cand_0500958123"),
    ("0405406887", "cand_0405406887"),
    ("0408521763", "cand_0408521763"),
    ("0412210456", "cand_0412210456"),
    ("0419528741", "cand_0419528741"),
    ("0425123789", "cand_0425123789"),
    ("0426701853", "cand_0426701853"),
    ("0432829147", "cand_0432829147"),
    ("0438687654", "cand_0438687654"),
    ("0439528714", "cand_0439528714"),
    ("0452187639", "cand_0452187639"),
    ("0453380125", "cand_0453380125"),
    ("0461852741", "cand_0461852741"),
    ("0464822341", "cand_0464822341"),
    ("0471865204", "cand_0471865204"),
    ("0472185639", "cand_0472185639"),
    ("0475123890", "cand_0475123890"),
    ("0548216379", "cand_0548216379"),
    ("0698215473", "cand_0698215473"),
    ("0758216347", "cand_0758216347"),
    ("0821563478", "cand_0821563478"),
    ("0863215478", "cand_0863215478"),
    # Walloon MRS extras
    ("0500914821", "zs_liege"),
    ("0500912840", "zs_lux"),
    ("0500913830", "zs_namur"),
    ("0500915820", "zs_g1"),
    ("0500916310", "zs_g2"),
    ("0500927108", "zs_g3"),
    ("0500928000", "zs_g4"),
]

print("\n=== CANDIDATE HUNT ===")
hits = []
for kbo, label in CANDS:
    if is_mined(kbo):
        print("SKIPMINED", kbo, label)
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    if not t or "Error 404" in t or len(t) < 800:
        print("404", kbo, label)
        continue
    yb, fte, filed, title, last, act, nace = parse(t)
    y5 = yb.get("2025", {})
    careish = any(
        x in (act or "").lower()
        for x in [
            "nursing",
            "rest",
            "elderly",
            "care",
            "repos",
            "rust",
            "woonzorg",
            "mrs",
            "maison de repos",
            "residential care",
        ]
    ) or any(n.startswith("87.") or n.startswith("86.") for n in nace)
    om = euro(y5.get("omzet"))
    br = euro(y5.get("bruto_marge"))
    pnl = euro(y5.get("winst"))
    eq = euro(y5.get("eigen_vermogen"))
    print(
        f"FREE {kbo} last={last} {(title or '')[:55]} care={careish} "
        f"fte={fte} filed={filed}"
    )
    print(f"  act={act[:60]} nace={nace}")
    print(f"  2025 omzet={om} bruto={br} pnl={pnl} eq={eq}")
    if last == "2025" and y5 and (om or 0) + (br or 0) >= 200000:
        hits.append((kbo, label, title, act, nace, om, br, pnl, eq, fte, filed, careish))
        print("  >>> HIT", "CARE" if careish else "other")

print("\n=== HITS ===")
for h in hits:
    print(h[0], h[1], "care", h[11], "om", h[5], "br", h[6], "pnl", h[7], "eq", h[8])
