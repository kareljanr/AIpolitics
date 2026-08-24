# -*- coding: utf-8 -*-
"""Race-recover tick2168: find unused YE2025 WZC/MRS with live CW euros."""
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2168")
out.mkdir(parents=True, exist_ok=True)

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
    "docs/doge/data/research_queue.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=28) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:70])
        return None


def parse_cw(t):
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {
            k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
        }
    fte = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed = re.search(r"filed on ([0-9-]{10})", t or "")
    title = re.search(r"<title>([^<]+)", t or "")
    nace = re.findall(r"87\.\d{3}", t or "")[:6]
    nace68 = re.findall(r"68\.\d{3}", t or "")[:4]
    nace55 = re.findall(r"55\.\d{3}", t or "")[:4]
    return (
        yblocks,
        (fte.group(1) if fte else None),
        (filed.group(1) if filed else None),
        (title.group(1) if title else None),
        nace,
        nace68 + nace55,
    )


CANDS = [
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0877556624", "agb_bornem"),
    ("0755822317", "lork_hoeselt"),
    ("0450755634", "residentie_oudenburg"),
    ("0410219433", "f2_dir"),
]

# harvest from tick2164/2126 probe filenames
extra = []
for folder in [
    Path("docs/doge/data/raw/tick2164"),
    Path("docs/doge/data/raw/tick2126"),
    Path("docs/doge/data/raw/tick2125"),
]:
    if not folder.exists():
        continue
    for p in folder.glob("*.html"):
        m = re.search(r"(\d{10})", p.name)
        if m:
            extra.append((m.group(1), p.stem[:40]))

MORE = [
    ("0475123890", "c0475123890"),
    ("0464822341", "c0464822341"),
    ("0453380125", "c0453380125"),
    ("0443249616", "c0443249616"),
    ("0480566704", "c0480566704"),
    ("0598966387", "c0598966387"),
    ("0685516024", "c0685516024"),
    ("0422620585", "c0422620585"),
    ("0441675147", "c0441675147"),
    ("0787300696", "c0787300696"),
    ("0889421308", "c0889421308"),
    ("0410958712", "c0410958712"),
    ("0438687654", "c0438687654"),
    ("0412210456", "c0412210456"),
    ("0425123789", "c0425123789"),
    ("0459770496", "c0459770496"),
    ("0466266429", "c0466266429"),
    ("0845064196", "c0845064196"),
    ("0887690451", "c0887690451"),
    # Anima Care operating entities sometimes separate
    ("0470673890", "zorgsaam_mined"),
    ("0698940725", "anima_vl_mined"),
    ("0446506836", "avond_mined"),
    ("0469969453", "anima_hold_mined"),
]

seen = set()
allc = []
for k, l in CANDS + extra + MORE:
    if k in seen:
        continue
    seen.add(k)
    allc.append((k, l))

strong = []
for kbo, label in allc:
    status = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    title_m = re.search(r"<title>([^<]+)", t or "")
    title0 = title_m.group(1) if title_m else ""
    if not t or "Error 404" in title0:
        print(label, kbo, status, "404/fail")
        continue
    yb, fte, filed, title, nace, nace_other = parse_cw(t)
    y5 = yb.get("2025", {})
    has = any(y5.get(x) for x in ("omzet", "bruto_marge", "winst", "eigen_vermogen"))
    print(
        f"{status} {kbo} {(title or '')[:70]} y5={bool(y5)} fte={fte} filed={filed} "
        f"nace87={nace[:3]} other={nace_other[:2]} omzet={y5.get('omzet')} "
        f"bruto={y5.get('bruto_marge')} winst={y5.get('winst')}"
    )
    if status != "FREE" or not has:
        continue
    if nace_other and not nace:
        print("  SKIP non-care NACE")
        continue
    omzet = (y5.get("omzet") or "").replace(",", "")
    bruto = (y5.get("bruto_marge") or "").replace(",", "")
    winst_s = re.sub(r"[^\d-]", "", (y5.get("winst") or "0") or "0")
    o = int(omzet) if omzet.isdigit() else 0
    b = int(bruto) if bruto.isdigit() else 0
    w = int(winst_s) if winst_s not in ("", "-") else 0
    if o >= 200_000 or b >= 200_000 or abs(w) >= 50_000:
        strong.append((kbo, label, title, y5, fte, filed, nace))
        print("  >>> CANDIDATE")

print("\n=== STRONG FREE ===")
for s in strong:
    print(s[0], s[1], (s[2] or "")[:60], s[3], "fte", s[4], "nace", s[6][:4])
