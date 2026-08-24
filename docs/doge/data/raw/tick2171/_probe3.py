# -*- coding: utf-8 -*-
"""Probe high-value FREE YE2025 WZC candidates from Companyweb search."""
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2171")

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
    ("0428659430", "mater_dei_heikruis"),
    ("0409970203", "sint_carolus_ternat"),
    ("0424830108", "home_stuyvenberg"),
    ("0898596122", "vlietoever_bornem"),
    ("0439442761", "prinsenhof_bilzen"),
    ("0410142031", "olv_lourdes"),  # may mined
    ("0424236725", "sint_antonius"),  # may mined
    # more from similar searches
    ("0408215439", "x"),
    ("0417568420", "x2"),
    ("0421903670", "christine_almost"),
    ("0435015700", "lindeboom_almost"),
    ("0446022330", "lork_almost"),
    ("0452865380", "jozef_almost"),
    ("0463758970", "vincent_almost"),
    ("0473694740", "ruggeveld_almost"),
    ("0480566700", "hof_almost"),
    ("0861157380", "eycken_almost"),
    ("0865574640", "fakkel_almost"),
    ("0895366220", "annuntiaten_almost"),
    ("0409232010", "esplanade_almost"),
    ("0411600690", "maria_almost"),
    ("0412886630", "boterlaar_almost"),
    ("0413055980", "jozef_aarschot_almost"),
    ("0413796450", "foyer_almost"),
    ("0414678560", "vander_almost"),
    ("0416337260", "vrijzicht_almost"),
    ("0417958150", "camillus_almost"),
    ("0418234990", "witte_meren_almost"),
    ("0419528740", "x3"),
    ("0422152310", "barbara_almost"),
    ("0423571580", "salvator_almost"),
    ("0432582480", "bernardus_almost"),
    ("0433440340", "olv_kempen_almost"),
    ("0435015702", "lindeboom"),  # mined
    ("0445175260", "zilverlinde_almost"),
    ("0446506830", "avondvrede_almost"),
    ("0448190180", "jozef_rumst_almost"),
    ("0449425540", "wijtshage_almost"),
    ("0453287030", "samen_ouder_almost"),
    ("0454090350", "zusters_almost"),
    ("0459770490", "augustinus_almost"),
    ("0461852340", "x4"),
    ("0470673890", "zorgsaam"),  # mined
    ("0810616130", "molenheide_almost"),
    ("0823488130", "thofke_almost"),
    ("0845895820", "hertog_almost"),
    ("0889421300", "armonea_almost"),
    ("0893863010", "faro_almost"),
]

for kbo, label in CANDS:
    kbo = re.sub(r"\D", "", kbo).zfill(10)[-10:]
    mined = is_mined(kbo)
    if mined and label.endswith("_almost"):
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"p3_{label}_{kbo}_en.html")
    if not t or "Error 404" in t or len(t) < 800:
        print(("MINED" if mined else "404"), kbo, label)
        continue
    yb, fte, filed, title, last, act = parse(t)
    y5 = yb.get("2025", {})
    y4 = yb.get("2024", {})
    om = euro(y5.get("omzet"))
    br = euro(y5.get("bruto_marge"))
    pnl = euro(y5.get("winst"))
    eq = euro(y5.get("eigen_vermogen"))
    print(
        f"{'MINED' if mined else 'FREE'} {kbo} last={last} {(title or '')[:65]} "
        f"fte={fte} filed={filed}"
    )
    print(f"  act={act[:70]}")
    print(f"  2025 omzet={om} bruto={br} pnl={pnl} eq={eq}")
    if y4:
        print(
            f"  2024 omzet={euro(y4.get('omzet'))} bruto={euro(y4.get('bruto_marge'))} "
            f"pnl={euro(y4.get('winst'))} eq={euro(y4.get('eigen_vermogen'))}"
        )
    if not mined and last == "2025" and ((om or 0) + (br or 0) >= 150000):
        print("  >>> STRONG HIT")
