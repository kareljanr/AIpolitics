# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2172")
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
    ("0416493254", "ben_woonzorg"),
    ("0480566704", "hof_ter_lande"),
    ("0443249616", "stil_geluk"),
    ("0685516024", "wzn_edegem"),
    ("0410219433", "haagwinde"),
    ("0598966387", "hoeksteen"),
    ("0883694744", "seigneurie"),
    ("0808910714", "bethanie"),
    ("0808928827", "le_progres"),
    ("0507866165", "ry_chevreuil"),
    ("0539934860", "passerinette"),
    ("0441675147", "wsr"),
    ("0466266429", "helianthus"),
    ("0880226993", "man_in_motion"),
    ("0883790853", "hop"),
    ("0641760611", "numera"),
    ("0650907810", "ventu"),
    # more care from prior free lists / nearby
    ("0406877485", "dhondt"),
    ("0405443129", "meander"),
    ("0428471856", "ocura"),
    ("0428335615", "zoetenaard"),
    ("0454543856", "cand_0454"),
    ("0417562831", "cand_0417"),
    ("0421567839", "cand_0421"),
    ("0408215439", "cand_0408"),
    ("0835884236", "hetdorp_mined"),
    ("0400371161", "abdij_mined"),
    ("0887690451", "emeis_mined"),
    # Ben siblings / care nets
    ("0416500000", "x"),
    ("0420000000", "x2"),
    ("0401789123", "x3"),
    ("0412789123", "x4"),
    ("0423789123", "x5"),
    ("0434789123", "x6"),
    ("0445789123", "x7"),
    ("0456789123", "x8"),
    ("0467789123", "x9"),
    ("0478789123", "x10"),
    ("0489789123", "x11"),
    ("0402794561", "x12"),
    ("0413794561", "x13"),
    ("0424794561", "x14"),
    ("0435794561", "x15"),
    ("0446794561", "x16"),
    ("0457794561", "x17"),
    ("0468794561", "x18"),
    ("0479794561", "x19"),
    ("0403812345", "x20"),
    # Idewa-style water IGS guesses from known Belgian water intercommunales
    ("0201300000", "w"),
    ("0216000000", "w2"),
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
            "ben_woonzorg",
            "hof_ter_lande",
            "stil_geluk",
            "wzn_edegem",
            "haagwinde",
            "dhondt",
            "meander",
            "ocura",
            "zoetenaard",
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
        "ben_woonzorg",
        "hof_ter_lande",
        "stil_geluk",
        "wzn_edegem",
        "haagwinde",
    ) or (st == "FREE" and y5)
    if show:
        print(st, kbo, (title or "")[:55], "last", last)
        if y5:
            print(" ", y5, "fte", fte, "filed", filed)
    if st == "FREE" and y5:
        omzet = (y5.get("omzet") or "").replace(",", "")
        bruto = (y5.get("bruto_marge") or "").replace(",", "")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.isdigit() else 0
        if o >= 150000 or b >= 150000 or abs(int((y5.get("eigen_vermogen") or "0").replace(",", "") or "0")) >= 500000:
            print("  >>> CANDIDATE")
            strong.append((kbo, title, y5, fte, filed))

print("\nSTRONG FREE:", len(strong))
for s in strong:
    print(s[0], (s[1] or "")[:50], s[2], "fte", s[3])
