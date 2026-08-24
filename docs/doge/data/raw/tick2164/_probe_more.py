# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"0\d{9}", blob):
                mined.add(m)

# Candidates: possible unused WZC/MRS/IGS/HVZ from recent seam + web
CANDS = [
    ("0411515075", "emmaus"),
    ("0470673890", "zorg_saam"),
    ("0408041271", "huize_ter_linde"),
    ("0422540661", "de_meerssen"),
    ("0428692191", "de_medemens"),
    ("0416934425", "sint_anna"),
    ("0427301819", "olvf"),
    ("0446340946", "de_verlosser"),  # mined likely
    ("0810616132", "molenheide"),  # mined likely
    ("0435357675", "psychogeriatrisch"),  # mined
    ("0448190181", "sj_rumst"),  # mined
    ("0458458325", "maria_rustoord_ingel"),
    ("0411600692", "marias_rustoord_moorslede"),
    # De Zorgfamilie siblings / Antwerp belt
    ("0412886636", "boterlaar_check"),  # mined 0412.886.636
    ("0412886636", "bad"),
    ("0473694748", "ruggeveld_check"),  # mined
    ("0425889012", "skip"),
    # try known Antwerp care
    ("0404556789", "skip2"),
    ("0430123987", "skip3"),
    # Walloon MRS
    ("0426001122", "skip4"),
    ("0458123456", "skip5"),
    # From Care Property tenants / listed operators
    ("0460123456", "skip6"),
    ("0475123456", "skip7"),
    # Real KBOs from prior FOI/queue mentions - scan foi for deferred
]

# Pull KBOs mentioned as deferred/unused in last ~100 loop_log lines
log = Path("docs/doge/loop_log.md").read_text(encoding="utf-8", errors="ignore")
tail = log[-80000:]
for m in re.findall(r"KBO\s+\*?\*?(\d{4})\.(\d{3})\.(\d{3})", tail):
    kbo = m[0] + m[1] + m[2]
    if kbo not in mined and kbo not in {c[0] for c in CANDS}:
        CANDS.append((kbo, f"log_{kbo}"))

# Also search entities notes for "deferred" names with KBO
with open("docs/doge/data/entities.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        notes = row.get("notes") or ""
        if "deferred" in notes.lower() or "YE2025 deferred" in notes:
            for m in re.findall(r"(\d{4})\.(\d{3})\.(\d{3})", notes):
                kbo = "".join(m)
                if kbo not in mined:
                    CANDS.append((kbo, f"def_{row['entity_id'][:20]}"))


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:60])
        return None


seen = set()
strong = []
for kbo, label in CANDS:
    if kbo in seen or "skip" in label:
        continue
    seen.add(kbo)
    status = "MINED" if kbo in mined else "FREE"
    if status == "MINED":
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"pm_{label}_en.html")
    if not t:
        continue
    title = re.search(r"<title>([^<]+)", t)
    if not title or "Error 404" in title.group(1):
        print(label, kbo, "404")
        continue
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {
            k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
        }
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3})", t)))[:4]
    y5 = yblocks.get("2025", {})
    live = any(y5.get(k) for k in ("omzet", "bruto_marge", "winst", "eigen_vermogen"))
    omzet = (y5.get("omzet") or "").replace(",", "")
    print("=" * 40)
    print(label, kbo, "FREE", "YE2025" if live else "noYE", "fte", fte.group(1) if fte else "-", "nace", nace)
    print(" ", title.group(1)[:100])
    for y in sorted(yblocks, reverse=True)[:2]:
        print(" ", y, yblocks[y])
    if live and omzet.isdigit() and int(omzet) >= 500_000 and nace:
        print(" >>> STRONG")
        strong.append((label, kbo, omzet, title.group(1)[:60]))
    elif live and (y5.get("bruto_marge") or "").replace(",", "").lstrip("-").isdigit():
        bm = int((y5.get("bruto_marge") or "0").replace(",", ""))
        if abs(bm) >= 500_000:
            print(" >>> BRUTO CANDIDATE")
            strong.append((label, kbo, f"bruto{bm}", title.group(1)[:60]))

print("STRONG LIST", strong)
