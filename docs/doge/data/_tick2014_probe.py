# ephemeral tick2014 — claim + prefer AGB/FARO/AIESH/REW else HH Leuven YE2025
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
UTC = "2026-08-24T07:55:00Z"

p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
r = next(x for x in rows if x.get("task_id") == "rq_2014")
st = (r.get("status") or "").lower()
print("before", st)
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + st)
r["status"] = "in_progress"
r["updated_utc"] = UTC
with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2014")

dst = Path("docs/doge/data/raw/tick2014")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data), url)


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) >= 2 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")
        elif len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    return float(s)


def summarize(name):
    path = dst / f"{name}.html"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==", (title.group(1)[:120] if title else None))
    for lab in [
        "Last balance sheet year",
        "filed on",
        "neergelegd op",
        "Laatste balansjaar",
        "Dernier exercice",
    ]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 160]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2], "n_blocks", len(blocks))
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0 winst/equity/bruto/omzet", y0)
            if len(blocks) > 1:
                y1 = tuple(parse_amount(x) for x in blocks[1])
                print(" y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(
                        f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%"
                        if pct is not None
                        else f"  {n} {a} vs {b}"
                    )
        except Exception as e:
            print(" err", e)
    # N/A omzet?
    if "N/A" in t and "omzet" in t.lower():
        print("  note: page mentions N/A/omzet")
    print()


# Prefer leftover duals; known KBOs from prior ticks
urls = [
    ("agb_bornem_en", "https://www.companyweb.be/en/0877556624"),
    ("agb_bornem_nl", "https://www.companyweb.be/nl/0877556624"),
    ("faro_en", "https://www.companyweb.be/en/0893863017"),
    ("faro_nl", "https://www.companyweb.be/nl/0893863017"),
    # AIESH / REW Walloon energy IGS — common KBOs from prior notes
    ("aiesh_en", "https://www.companyweb.be/en/0200976951"),
    ("rew_en", "https://www.companyweb.be/en/0200933262"),
    ("hhleuven_en", "https://www.companyweb.be/en/0412939886"),
    ("hhleuven_nl", "https://www.companyweb.be/nl/0412939886"),
    ("hhleuven_fr", "https://www.companyweb.be/fr/0412939886"),
    ("azzeno_en", "https://www.companyweb.be/en/0405671991"),
    ("vesalius_en", "https://www.companyweb.be/en/0411837540"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name, _ in urls:
    summarize(name)
