# -*- coding: utf-8 -*-
"""Find unused WZC with YE2025 live euros; check NACE for Affligem/Ventu/Aaigem dual."""
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2169")

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)

# where is 0644843825 mined?
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), 1):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            if "0644843825" in blob:
                print("MINED_IN", path, "row", i, list(row.values())[:3])


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
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
    fte_m = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed_m = re.search(r"filed on ([0-9-]{10})", t or "")
    title_m = re.search(r"<title>([^<]+)", t or "")
    fte = fte_m.group(1) if fte_m else None
    filed = filed_m.group(1) if filed_m else None
    title = title_m.group(1) if title_m else None
    # richer NACE from activity section
    nace_all = re.findall(r"(\d{2}\.\d{3})", t or "")
    nace_care = [n for n in nace_all if n.startswith(("87.", "86.", "88."))]
    nace_bad = [n for n in nace_all if n.startswith(("68.", "55.", "64.", "70.", "41."))]
    # activity description
    act = re.search(r"Main activity[^<]*</[^>]+>\s*<[^>]+>([^<]+)", t or "", re.I)
    if not act:
        act = re.search(r"Activit[eé] principale[^<]*</[^>]+>\s*<[^>]+>([^<]+)", t or "", re.I)
    return yb, fte, filed, title, nace_care[:5], nace_bad[:5], act.group(1).strip() if act else None


# Dual Aaigem WZC operating entity + Affligem + Ventu + more FREE probes
MORE = [
    ("0422620585", "wzc_sint_vincentius_aaigem_op"),  # operating WZC same address?
    ("0400371161", "abdij_affligem"),
    ("0650907810", "ventu"),
    ("0787300696", "melis_home"),
    # more candidate KBOs often in care space from prior ticks
    ("0405406887", "cand_0405406887"),
    ("0412210456", "cand_0412210456"),
    ("0432829147", "cand_0432829147"),
    ("0438687654", "cand_0438687654"),
    ("0443249616", "cand_0443249616"),
    ("0453380125", "cand_0453380125"),
    ("0464822341", "cand_0464822341"),
    ("0466266429", "cand_0466266429"),
    ("0475123890", "cand_0475123890"),
    ("0480566704", "cand_0480566704"),
    ("0598966387", "cand_0598966387"),
    ("0685516024", "cand_0685516024"),
    ("0408123456", "cand_bad"),  # likely 404
    ("0410958712", "cand_0410958712"),
    ("0889421308", "cand_0889421308"),
    ("0441675147", "cand_0441675147"),
    ("0440123456", "cand_bad2"),
    ("0500937791", "cand_0500937791"),
    ("0507866165", "cand_0507866165"),
    ("0539934860", "cand_0539934860"),
    ("0808910714", "cand_0808910714"),
    ("0808928827", "cand_0808928827"),
    ("0880226993", "cand_0880226993"),
    ("0883694744", "cand_0883694744"),
    ("0883790853", "cand_0883790853"),
    ("0460868477", "cand_0460868477"),
    ("0467222769", "cand_0467222769"),
    ("0450895392", "cand_0450895392"),
    ("0446793678", "cand_0446793678"),
]

print("=== DETAILED ===")
strongs = []
for kbo, label in MORE:
    st = "MINED" if kbo in mined else "FREE"
    p = out / f"{label}_{kbo}_en.html"
    if p.exists() and p.stat().st_size > 2000:
        t = p.read_text(encoding="utf-8", errors="ignore")
    else:
        # also check tick2168
        alt = Path("docs/doge/data/raw/tick2168") / f"h_{kbo}_en.html"
        alt2 = Path("docs/doge/data/raw/tick2168") / f"p_{kbo}_en.html"
        if alt.exists() and alt.stat().st_size > 2000:
            t = alt.read_text(encoding="utf-8", errors="ignore")
            p.write_text(t, encoding="utf-8")
        elif alt2.exists() and alt2.stat().st_size > 2000:
            t = alt2.read_text(encoding="utf-8", errors="ignore")
            p.write_text(t, encoding="utf-8")
        else:
            t = fetch(f"https://www.companyweb.be/en/{kbo}", p)
    if not t or "Error 404" in t:
        print(st, kbo, "404/fail")
        continue
    yb, fte, filed, title, nace, nbad, act = parse(t)
    y5 = yb.get("2025", {})
    y4 = yb.get("2024", {})
    if not y5:
        print(st, kbo, (title or "")[:60], "NO YE2025")
        continue
    omzet = (y5.get("omzet") or "").replace(",", "")
    bruto = (y5.get("bruto_marge") or "").replace(",", "")
    winst = (y5.get("winst") or "").replace(",", "")
    print(st, kbo, (title or "")[:70])
    print("  act:", act)
    print("  nace", nace, "bad", nbad, "fte", fte, "filed", filed)
    print("  2025 omzet", omzet, "bruto", bruto, "winst", winst, "eq", y5.get("eigen_vermogen"))
    print("  2024", y4)
    o = int(omzet) if omzet.lstrip("-").isdigit() else 0
    b = int(bruto.lstrip("-")) if bruto.lstrip("-").isdigit() else 0
    if st == "FREE" and (abs(o) >= 200000 or abs(b) >= 200000):
        print("  >>> STRONG")
        strongs.append((kbo, label, title, o, b, nace, nbad))

print("\nSTRONG FREE:", strongs)
